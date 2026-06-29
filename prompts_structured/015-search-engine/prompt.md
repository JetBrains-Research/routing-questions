# In-Memory Full-Text Search Engine

## Overview
A Python library and CLI tool implementing a basic inverted index for full-text search over a collection of plain text documents.

## Functional Requirements
1. Index a directory of `.txt` files, building an inverted index (term → list of document IDs with positions) (`index` command).
2. Save and load the index to/from a binary file using `pickle` (`--save` / `--load` flags).
3. Query the index with a search string and return ranked results (`search` command):
   - Support multi-word queries (AND semantics by default)
   - Rank results by TF-IDF score
   - Display top N results (default 10) with filename and a snippet showing the match in context
4. Support a `--or` flag to switch to OR semantics for multi-word queries.
5. `stats` command prints: total documents indexed, total unique terms, average document length in tokens, top 10 most frequent terms.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- No external search libraries (`whoosh`, `elasticsearch`, etc.)
- Tokenization: lowercase, strip punctuation, split on whitespace
- No stemming or stopword removal required
- TF-IDF must be computed from scratch using standard math

## Deliverables
- `search.py` — CLI entry point
- `index.py` — inverted index and TF-IDF implementation
- `requirements.txt`
