#!/usr/bin/env python3
"""Filter SWE-Chat rows into candidate zero-shot greenfield prompts.

The script is intentionally conservative. It is meant to produce a manual
review shortlist, not a final prompt set.
"""

from __future__ import annotations

import argparse
import csv
import heapq
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[1] / "filter_config.json"


@dataclass
class Candidate:
    candidate_id: str
    session_id: str
    turn_id: str
    repo_id: str
    content: str
    word_count: int
    score: int
    positive_matches: list[str]
    negative_matches: list[str]
    prompt_intent: str
    agent: str
    session_success_score: str
    agent_percentage: str


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        config = json.load(fh)
    for key in ("positive_patterns", "negative_patterns", "required_patterns_any", "reject_patterns_any"):
        config[f"_{key}_compiled"] = [
            re.compile(pattern, flags=re.IGNORECASE) for pattern in config.get(key, [])
        ]
    return config


def import_pandas():
    try:
        import pandas as pd  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "This script needs pandas. Install with: python3 -m pip install pandas pyarrow"
        ) from exc
    return pd


def read_table(path: Path):
    pd = import_pandas()
    suffix = path.suffix.lower()
    if suffix == ".parquet":
        return pd.read_parquet(path)
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".jsonl", ".ndjson"}:
        return pd.read_json(path, lines=True)
    if suffix == ".json":
        return pd.read_json(path)
    raise SystemExit(f"Unsupported input format: {path}")


def parquet_columns(path: Path) -> set[str]:
    import pyarrow.parquet as pq

    parquet_file = pq.ParquetFile(path)
    return set(parquet_file.schema.names)


def first_existing(row: Any, names: list[str], default: str = "") -> str:
    for name in names:
        if name in row and row[name] is not None:
            value = row[name]
            if not is_nan(value):
                return str(value)
    return default


def first_bool(row: Any, names: list[str]) -> bool | None:
    for name in names:
        if name in row and row[name] is not None:
            value = row[name]
            if is_nan(value):
                continue
            if isinstance(value, bool):
                return value
            return str(value).strip().lower() in {"true", "1", "yes"}
    return None


def is_nan(value: Any) -> bool:
    return value != value


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def compiled_pattern_matches(patterns: list[re.Pattern[str]], text: str) -> list[str]:
    return [pattern.pattern for pattern in patterns if pattern.search(text)]


def is_user_prompt(row: Any) -> bool:
    role = first_existing(row, ["role", "speaker", "message_role"]).lower()
    turn_type = first_existing(row, ["turn_type", "type", "event_type"]).lower()
    if role and role != "user":
        return False
    if turn_type and "user" not in turn_type and "prompt" not in turn_type and "message" not in turn_type:
        return False
    return True


def is_first_turn(row: Any) -> bool:
    explicit = first_bool(row, ["is_first_turn", "first_turn", "is_initial_prompt"])
    if explicit is not None:
        return explicit

    turn_index = first_existing(row, ["turn_index", "turn_number", "message_index", "step_index"])
    if turn_index:
        try:
            return int(float(turn_index)) in {0, 1}
        except ValueError:
            return False

    return False


def score_row(row: Any, config: dict[str, Any]) -> tuple[int, list[str], list[str]]:
    content = normalize_text(first_existing(row, ["content", "text", "message", "prompt"]))
    positives = compiled_pattern_matches(config["_positive_patterns_compiled"], content)
    negatives = compiled_pattern_matches(config["_negative_patterns_compiled"], content)

    score = 0
    score += 3 * len(positives)
    score -= 4 * len(negatives)

    prompt_intent = first_existing(row, ["prompt_intent", "intent"]).lower()
    if prompt_intent:
        if any(intent in prompt_intent for intent in config.get("preferred_prompt_intents", [])):
            score += 8
        if any(intent in prompt_intent for intent in config.get("rejected_prompt_intents", [])):
            score -= 10

    if is_first_turn(row):
        score += 5
    if is_user_prompt(row):
        score += 5

    return score, positives, negatives


def build_session_lookup(sessions_path: Path | None) -> dict[str, dict[str, Any]]:
    if not sessions_path:
        return {}
    if not sessions_path.exists():
        raise SystemExit(f"Sessions file not found: {sessions_path}")

    sessions = read_table(sessions_path)
    lookup: dict[str, dict[str, Any]] = {}
    for row in sessions.to_dict(orient="records"):
        session_id = first_existing(row, ["session_id", "id"])
        if session_id:
            lookup[session_id] = row
    return lookup


def iter_candidates(conversations_path: Path, sessions_path: Path | None, config: dict[str, Any]):
    session_lookup = build_session_lookup(sessions_path)
    columns = [
        "turn_id",
        "session_id",
        "repo_id",
        "turn_number",
        "role",
        "turn_type",
        "content",
        "is_first_turn",
        "prompt_intent",
        "agent",
        "model",
    ]

    if conversations_path.suffix.lower() == ".parquet":
        pd = import_pandas()
        available = parquet_columns(conversations_path)
        selected = [column for column in columns if column in available]
        filters = []
        if "is_first_turn" in available:
            filters.append(("is_first_turn", "=", True))
        if "role" in available:
            filters.append(("role", "=", "user"))
        conversations = pd.read_parquet(
            conversations_path,
            columns=selected,
            filters=filters or None,
        )
        rows = conversations.to_dict(orient="records")
    else:
        conversations = read_table(conversations_path)
        rows = conversations.to_dict(orient="records")

    for row in rows:
        content = normalize_text(first_existing(row, ["content", "text", "message", "prompt"]))
        if not content:
            continue
        required_patterns = config.get("_required_patterns_any_compiled", [])
        if required_patterns and not compiled_pattern_matches(required_patterns, content):
            continue
        reject_patterns = config.get("_reject_patterns_any_compiled", [])
        if reject_patterns and compiled_pattern_matches(reject_patterns, content):
            continue
        if not is_user_prompt(row):
            continue
        if not is_first_turn(row):
            continue

        words = word_count(content)
        if words < int(config["min_words"]) or words > int(config["max_words"]):
            continue

        score, positives, negatives = score_row(row, config)
        if not positives:
            continue
        if score <= 0:
            continue

        session_id = first_existing(row, ["session_id", "conversation_id"])
        turn_id = first_existing(row, ["turn_id", "message_id", "id"])
        repo_id = first_existing(row, ["repo_id", "repository", "repository_id"])
        prompt_intent = first_existing(row, ["prompt_intent", "intent"])
        agent = first_existing(row, ["agent", "agent_name", "model"])

        session = session_lookup.get(session_id, {})
        if not repo_id:
            repo_id = first_existing(session, ["repo_id", "repository", "repository_id"])
        if not agent:
            agent = first_existing(session, ["agent", "agent_name", "model"])

        yield Candidate(
            candidate_id=f"swe-chat-{session_id or 'unknown'}-{turn_id or 'turn'}",
            session_id=session_id,
            turn_id=turn_id,
            repo_id=repo_id,
            content=content,
            word_count=words,
            score=score,
            positive_matches=positives,
            negative_matches=negatives,
            prompt_intent=prompt_intent,
            agent=agent,
            session_success_score=first_existing(session, ["success_score", "score"]),
            agent_percentage=first_existing(session, ["agent_percentage", "agent_percent"]),
        )


def write_outputs(candidates: list[Candidate], out_jsonl: Path, out_csv: Path) -> None:
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for candidate in candidates:
        row = {
            "candidate_id": candidate.candidate_id,
            "session_id": candidate.session_id,
            "turn_id": candidate.turn_id,
            "repo_id": candidate.repo_id,
            "content": candidate.content,
            "word_count": candidate.word_count,
            "score": candidate.score,
            "positive_matches": candidate.positive_matches,
            "negative_matches": candidate.negative_matches,
            "prompt_intent": candidate.prompt_intent,
            "agent": candidate.agent,
            "session_success_score": candidate.session_success_score,
            "agent_percentage": candidate.agent_percentage,
        }
        rows.append(row)

    with out_jsonl.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    with out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["candidate_id"])
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--conversations", required=True, type=Path)
    parser.add_argument("--sessions", type=Path)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH)
    parser.add_argument("--out-jsonl", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--max-candidates", type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.conversations.exists():
        raise SystemExit(f"Conversations file not found: {args.conversations}")

    config = load_config(args.config)
    max_candidates = args.max_candidates or int(config["max_candidates"])

    heap: list[tuple[int, int, Candidate]] = []
    for index, candidate in enumerate(iter_candidates(args.conversations, args.sessions, config)):
        item = (candidate.score, index, candidate)
        if len(heap) < max_candidates:
            heapq.heappush(heap, item)
        elif item[0] > heap[0][0]:
            heapq.heapreplace(heap, item)

    candidates = [item[2] for item in heap]
    candidates.sort(key=lambda candidate: candidate.score, reverse=True)

    write_outputs(candidates, args.out_jsonl, args.out_csv)
    print(f"Wrote {len(candidates)} candidates")
    print(f"JSONL: {args.out_jsonl}")
    print(f"CSV:   {args.out_csv}")


if __name__ == "__main__":
    main()
