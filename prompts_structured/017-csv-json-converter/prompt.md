# CSV ↔ JSON Converter with Schema Inference

## Overview
A CLI tool that converts between CSV and JSON formats and infers column types automatically to produce correctly-typed output.

## Functional Requirements
1. Convert a CSV file to JSON (`to-json` command). Output is a JSON array of objects.
2. Convert a JSON array-of-objects file to CSV (`to-csv` command).
3. During CSV → JSON conversion, infer column types from values: integer, float, boolean (`true`/`false`, `yes`/`no`), ISO date, or string. Apply the inferred type to all values in the column.
4. Support a `--schema` flag on `to-json` to output a separate `schema.json` file describing inferred column names and types.
5. Support a `--delimiter` option for CSV (default `,`).
6. Handle missing values: empty strings become `null` in JSON; `null` JSON values become empty strings in CSV.
7. Print a summary after conversion: row count, column count, and inferred types per column.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Use only Python standard library (`csv`, `json`, `datetime`) — no pandas or external libraries
- Type inference must be deterministic: try int → float → bool → date → string in that order

## Deliverables
- `convert.py` — CLI entry point and all conversion logic
- `requirements.txt`
