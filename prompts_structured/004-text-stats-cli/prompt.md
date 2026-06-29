# Text Statistics Analyzer

## Overview
A CLI tool that reads a plain text file and produces a detailed statistical report about its content.

## Functional Requirements
1. Accept a file path as argument; also accept piped stdin if no file is given.
2. Report the following statistics:
   - Total character count (with and without whitespace)
   - Word count and unique word count
   - Sentence count and average sentence length in words
   - Paragraph count
   - Top 10 most frequent words (excluding common stopwords)
   - Estimated reading time (assume 200 words per minute)
3. Support a `--format` option: `text` (default, human-readable) or `json`.
4. Support a `--stopwords` option to provide a custom stopwords file (one word per line) that overrides the built-in list.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- No NLP libraries; implement all analysis with standard string operations and `re`
- Built-in stopwords list must cover at least 50 common English words

## Deliverables
- `stats.py` — CLI entry point and all analysis logic
- `stopwords.txt` — default stopwords list
- `requirements.txt`
