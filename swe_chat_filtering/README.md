# SWE-Chat Filtering

This folder is for extracting candidate zero-shot greenfield prompts from SWE-Chat without mixing that work into the ViBench prompt set.

SWE-Chat is useful because it contains real coding-agent conversations. It is not directly a prompt benchmark: many rows are multi-turn instructions, tool calls, test failures, repository-specific requests, or follow-ups. For our study, we only want first-turn user prompts that ask the agent to create a new tool/project and do not depend on an existing codebase.

## Source

- Dataset: https://huggingface.co/datasets/SALT-NLP/SWE-chat
- Paper: https://arxiv.org/abs/2604.20779

The Hugging Face dataset may require access approval. Download the needed files manually into:

```text
swe_chat_filtering/data/raw/
```

Expected files:

```text
conversations.parquet
sessions.parquet
repositories.parquet   # optional
```

If you have access to the dataset and a Hugging Face token, you can use the helper script:

```bash
HF_TOKEN=... python3 swe_chat_filtering/scripts/download_swe_chat_tables.py
```

The script downloads only:

```text
conversations.parquet
sessions.parquet
repositories.parquet
```

It intentionally does not download `transcripts/`, because the top-level parquet tables are enough for the first filtering pass.

## Filtering Goal

Keep prompts that satisfy all of the following:

- first user prompt in a session
- asks for new code, a new project, a new script, a small app, a CLI, an API, or a tool
- can be understood without reading an existing repository
- does not require previous turns, failing tests, stack traces, open PRs, or repo-specific files
- is small enough for a human evaluator to compare two outputs in about 30 minutes

Reject prompts that mention:

- fixing/debugging existing failures
- modifying a named file/path in an existing repo
- continuing previous work
- issue/PR/branch/commit-specific work
- tests/logs/errors/tracebacks as the main input
- frontend/UI-heavy work unless we decide to keep a web-app category

## Run

From the repository root:

```bash
python3 swe_chat_filtering/scripts/filter_swe_chat_candidates.py \
  --conversations swe_chat_filtering/data/raw/conversations.parquet \
  --sessions swe_chat_filtering/data/raw/sessions.parquet \
  --out-jsonl swe_chat_filtering/data/candidates/candidates.jsonl \
  --out-csv swe_chat_filtering/data/candidates/candidates.csv \
  --max-candidates 300
```

If `pandas` cannot read parquet, install a parquet backend locally:

```bash
python3 -m pip install pandas pyarrow
```

## Outputs

The script writes:

- `data/candidates/candidates.jsonl`: machine-readable candidate rows
- `data/candidates/candidates.csv`: spreadsheet-friendly candidate rows

Each candidate includes:

- session id
- turn id
- repository id if available
- original prompt text
- heuristic score
- matched positive/negative signals
- session metadata when available

For the first extraction run, see `initial_findings.md`.

## Manual Review

After filtering, use `manual_review_template.md` for a human pass. The automatic filter should be treated as a shortlist generator, not final inclusion logic.

Recommended review labels:

- `keep`: usable as a zero-shot greenfield sample with only light cleanup
- `rewrite`: useful idea, but needs rewriting into a self-contained prompt
- `reject`: depends too much on existing code/context or is outside scope

## Method Note

If we use SWE-Chat in the paper, the defensible claim is:

> We used SWE-Chat as a source of real coding-agent request style. Because SWE-Chat consists of complete coding sessions rather than standalone benchmark prompts, we filtered for first-turn user requests with new-code intent and manually removed prompts that depended on repository state, previous conversation context, failures, or existing files.
