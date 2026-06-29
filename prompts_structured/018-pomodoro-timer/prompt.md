# Pomodoro Timer CLI

## Overview
A terminal Pomodoro timer that runs work and break intervals, tracks completed sessions, and shows productivity statistics.

## Functional Requirements
1. Start a Pomodoro session with configurable work duration (default 25 min), short break (default 5 min), and long break (default 15 min, taken after every 4 work intervals) (`start` command).
2. Display a live countdown in the terminal using `\r` to update in place; show current phase (Work / Short Break / Long Break) and interval number.
3. Play a terminal bell (`\a`) when a phase ends.
4. Log each completed work interval to a SQLite database with start time, end time, and an optional task label (passed as `--task` flag).
5. `stats` command shows: total completed Pomodoros today, this week, and all time; and the 5 most-used task labels.
6. Allow interrupting a session with Ctrl+C; log the partial interval as incomplete (do not count toward stats).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Storage: SQLite via `sqlite3` standard library
- No external timer or display libraries; use `time.sleep` and `\r` escape codes
- Must run on macOS and Linux terminals

## Deliverables
- `pomodoro.py` — CLI entry point and timer logic
- `db.py` — session logging and stats queries
- `requirements.txt`
