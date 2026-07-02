# Furniture Freight Quote CLI

## Overview

Build a deterministic CLI for calculating furniture delivery quotes. An admin maintains locations, furniture items, and rate cards. A user asks for a quote by selecting origin, destination, items, and extra services.

## Functional Requirements

1. Import locations from a CSV file.
2. Import furniture catalog items from a CSV file with item name, category, and base handling fee.
3. Import rate cards from a CSV file with origin city, destination city, and base delivery price.
4. Calculate a quote from origin, destination, item quantities, and optional services such as `assembly` or `stairs`.
5. Use exact city matching for rate cards.
6. If no rate card matches, print a clear error instead of guessing.
7. Save each generated quote with timestamp and line-item breakdown.
8. List previous quotes and show a specific quote by ID.

## Technical Constraints

- Language: Python 3.10+
- CLI framework: Click
- Use pandas for CSV import.
- Persist quote history in SQLite.

## Deliverables

- `freight.py` - CLI entry point and quote logic
- `sample_locations.csv`
- `sample_catalog.csv`
- `sample_rates.csv`
- `requirements.txt`
