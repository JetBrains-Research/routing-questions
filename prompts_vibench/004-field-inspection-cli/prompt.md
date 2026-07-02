# Field Inspection CLI

## Overview

Build a command-line tool for recording building inspection jobs and checking whether required inspection items have passed.

## Functional Requirements

1. Create a job with builder name, address, and inspection date.
2. Add checklist items to a job with category, description, status (`pass`, `fail`, or `not_checked`), and optional notes.
3. Record blower-door and duct-leakage numeric test results for a job.
4. Show a job summary with counts of passed, failed, and unchecked checklist items.
5. Mark a job as compliant only if all checklist items pass and numeric tests are within configurable thresholds.
6. List all jobs, sorted by inspection date descending.
7. Export a single job report to JSON.

## Technical Constraints

- Language: Python 3.10+
- CLI framework: Click
- Storage: SQLite
- Thresholds should be stored in a small JSON config file.

## Deliverables

- `inspection.py` - CLI entry point and logic
- `config.json` - default thresholds
- `requirements.txt`
