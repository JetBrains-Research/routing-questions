# Configurable Data Transformation Pipeline

## Overview
A CLI tool that reads tabular data, applies a user-defined sequence of transformation steps, and writes the result to an output file. Transformations are specified in a YAML config file.

## Functional Requirements
1. Read input data from a CSV or JSON file (auto-detected by extension).
2. Apply a pipeline of transformations defined in a YAML config. Supported transformations:
   - `filter`: keep rows where a column matches a condition (`eq`, `gt`, `lt`, `contains`)
   - `rename`: rename one or more columns
   - `drop`: remove specified columns
   - `add_column`: add a new column as a Python expression over existing columns (e.g. `price * quantity`)
   - `sort`: sort by one or more columns with asc/desc direction
3. Write the output to a CSV or JSON file (specified in config or as a CLI flag).
4. A `--dry-run` flag prints the first 5 rows of the result without writing to disk.
5. Report row counts before and after each transformation step when `--verbose` is set.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Data processing: `pandas`
- Config parsing: `PyYAML`
- Expression evaluation for `add_column`: use `pandas.eval` (not Python `eval`)

## Deliverables
- `pipeline.py` — CLI entry point and transformation logic
- `example_config.yaml` — a working example config demonstrating all transformation types
- `requirements.txt`
