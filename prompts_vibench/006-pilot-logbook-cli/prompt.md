# Pilot Logbook CLI

## Overview

Build a single-user digital pilot logbook as a command-line tool. The user records flights, manages aircraft, and checks recent flight currency.

## Functional Requirements

1. Add aircraft records with tail number, make, model, and category.
2. Log a flight with date, aircraft tail number, route, total time, night time, instrument time, and number of landings.
3. Reject flights for unknown aircraft.
4. List flights with optional date range filters.
5. Show total flight time grouped by aircraft category.
6. Show currency status for day landings, night landings, and instrument time using configurable lookback windows.
7. Export the logbook to CSV.

## Technical Constraints

- Language: Python 3.10+
- CLI framework: Click
- Storage: SQLite
- Dates should use ISO format `YYYY-MM-DD`.

## Deliverables

- `logbook.py` - CLI entry point and logic
- `requirements.txt`
