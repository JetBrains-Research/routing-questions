# Initial SWE-Chat Filtering Findings

## Data Pulled

Downloaded top-level SWE-Chat parquet tables into `data/raw/`:

- `conversations.parquet` - 1.2 GB
- `sessions.parquet` - 1.9 MB
- `repositories.parquet` - 239 KB

The conversations table contains 2,692,480 rows. Filtering to first-turn user prompts gives 5,764 rows.

## Outputs Generated

Broad first pass:

- `data/candidates/candidates.jsonl`
- `data/candidates/candidates.csv`
- 300 candidates

Strict first-turn pass:

- `data/candidates/candidates_strict.jsonl`
- `data/candidates/candidates_strict.csv`
- 191 candidates

Greenfield/no-starting-files pass:

- `data/candidates/candidates_greenfield.jsonl`
- `data/candidates/candidates_greenfield.csv`
- 0 candidates after hard-rejecting prompts with file paths, filenames, repository/project context, issue/PR references, docs/readme/makefile references, and common existing-work verbs such as add/change/update/fix/refactor.

Strict rescore of broad top 300:

- `data/candidates/candidates_strict_from_top300.jsonl`
- `data/candidates/candidates_strict_from_top300.csv`
- 27 candidates

## Quality Assessment

The extracted candidates are realistic coding-agent requests, but most are not clean zero-shot greenfield prompts. Even after filtering for first-turn user messages and `create new code` intent, many prompts still depend on:

- a specific existing repository
- existing files or docs
- local paths
- issue numbers or PRs
- previous project/domain context
- existing UI/dashboard/application state
- agent-specific commands or workflow wrappers

An additional no-starting-files filter was applied to reject prompts with any explicit starting file, path, repository, issue, PR, docs, README, Makefile, or existing-project language. This reduced the candidate set to zero, suggesting that SWE-Chat does not provide usable standalone greenfield prompts without manual rewriting.

Examples of common near-misses:

- "look at the docs folder..."
- "Building on PR #..."
- "this project..."
- "add a tab to the admin dashboard..."
- "read plans/... and implement..."
- "use the makefile to start the local dev server..."

## Interpretation

SWE-Chat is useful as evidence for real coding-agent interaction style. It shows that real users often write informal, under-specified, context-dependent prompts. However, it is not a strong direct source of ready-to-use zero-shot greenfield Python prompts.

For our study, SWE-Chat should probably be used in one of two ways:

1. As methodological support for prompt realism.
2. As a source of informal prompt ideas that are manually rewritten into self-contained Python greenfield prompts.

It should not be presented as a clean prompt benchmark like ViBench or StaminaBench.

## Practical Recommendation

Keep SWE-Chat as a supporting source, not the primary extraction source.

Suggested paper wording:

> We also reviewed SWE-Chat, a dataset of real coding-agent conversations, to understand the style and specificity of actual user requests. Because SWE-Chat records full agentic coding sessions, even first-turn prompts often depend on repository state, issue context, local files, or previous project assumptions. We therefore used it only as evidence for realistic prompt style and not as a direct source of final zero-shot greenfield tasks.

If we still want to use SWE-Chat prompts directly, the next step should be manual review of `data/candidates/candidates_strict.csv` with labels:

- `keep`: self-contained enough to use
- `rewrite`: realistic idea but requires conversion into a standalone Python prompt
- `reject`: too repo-specific or not greenfield
