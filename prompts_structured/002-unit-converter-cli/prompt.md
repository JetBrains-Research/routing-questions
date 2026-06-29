# Unit Converter CLI

## Overview
A command-line tool for converting between common units of measurement across multiple categories. Conversions are defined in a data file so new units can be added without changing code.

## Functional Requirements
1. Convert a value from one unit to another given a numeric value, source unit, and target unit (`convert` command).
2. Support at least four categories: length, weight, temperature, and data storage.
3. List all available units grouped by category (`list` command).
4. Accept input in the form `python converter.py convert 100 km miles`.
5. Handle temperature conversions correctly (non-linear: Celsius, Fahrenheit, Kelvin).
6. Print a clear error message when an unsupported unit or incompatible category pair is requested.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Unit definitions stored in a `units.json` file, not hardcoded in Python
- No external conversion libraries (implement conversion logic manually)
- Output rounded to 4 decimal places

## Deliverables
- `converter.py` — CLI entry point and conversion logic
- `units.json` — unit definitions and conversion factors
- `requirements.txt`
