# Contact Book CLI

## Overview
A command-line contact book that stores personal contacts locally and supports import/export.

## Functional Requirements
1. Add a contact with: first name, last name, email (validated format), phone (optional), and one or more tags (`add` command).
2. List all contacts in a formatted table sorted by last name (`list` command).
3. Search contacts by any field (name, email, phone, or tag) with case-insensitive partial matching (`search` command).
4. Edit any field of an existing contact by ID (`edit` command).
5. Delete a contact by ID with confirmation (`delete` command).
6. Export all contacts to a CSV file (`export` command).
7. Import contacts from a CSV file, skipping rows with duplicate emails (`import` command).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Storage: SQLite via `sqlite3` standard library
- CSV handling: `csv` standard library
- Email validation: simple regex, no external library
- Table output: `tabulate` library

## Deliverables
- `contacts.py` — CLI entry point and logic
- `db.py` — database schema and queries
- `requirements.txt`
