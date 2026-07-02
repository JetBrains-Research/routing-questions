#!/usr/bin/env python3
"""Apply a stricter config to an existing SWE-Chat candidate JSONL file."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from filter_swe_chat_candidates import compiled_pattern_matches, load_config, normalize_text


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-jsonl", required=True, type=Path)
    parser.add_argument("--config", required=True, type=Path)
    parser.add_argument("--out-jsonl", required=True, type=Path)
    parser.add_argument("--out-csv", required=True, type=Path)
    parser.add_argument("--max-candidates", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    rows = []

    with args.input_jsonl.open("r", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            content = normalize_text(row.get("content", ""))
            if not content:
                continue

            required = config.get("_required_patterns_any_compiled", [])
            if required and not compiled_pattern_matches(required, content):
                continue

            positives = compiled_pattern_matches(config["_positive_patterns_compiled"], content)
            negatives = compiled_pattern_matches(config["_negative_patterns_compiled"], content)
            if not positives or negatives:
                continue

            score = 3 * len(positives)
            prompt_intent = str(row.get("prompt_intent") or "").lower()
            if any(intent in prompt_intent for intent in config.get("preferred_prompt_intents", [])):
                score += 8
            if any(intent in prompt_intent for intent in config.get("rejected_prompt_intents", [])):
                score -= 10

            row["strict_score"] = score
            row["strict_positive_matches"] = positives
            row["strict_negative_matches"] = negatives
            rows.append(row)

    rows.sort(key=lambda row: row["strict_score"], reverse=True)
    rows = rows[: args.max_candidates]

    args.out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with args.out_jsonl.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    fieldnames = list(rows[0].keys()) if rows else ["candidate_id"]
    with args.out_csv.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} strict candidates")
    print(f"JSONL: {args.out_jsonl}")
    print(f"CSV:   {args.out_csv}")


if __name__ == "__main__":
    main()
