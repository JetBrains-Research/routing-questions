# File Backup Tool with Versioning

## Overview
A CLI tool that backs up a source directory to a destination directory, keeping multiple timestamped versions and supporting restore operations.

## Functional Requirements
1. Back up a source directory to a destination by copying only changed or new files (`backup` command). Detect changes by comparing file size and modification time.
2. Each backup run creates a versioned snapshot named `backup_YYYYMMDD_HHMMSS/` inside the destination.
3. List all available snapshots with their timestamp, total size, and number of files (`snapshots` command).
4. Restore a snapshot to a target directory (`restore` command); accept snapshot name or `--latest` flag.
5. Delete a snapshot by name (`delete` command) with a confirmation prompt.
6. Support a `--exclude` option in the backup command accepting glob patterns (e.g. `*.pyc`, `.git/`).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- File operations: `pathlib` and `shutil` standard library only
- Snapshot metadata (file list, sizes, timestamps) stored as a `manifest.json` inside each snapshot folder
- No compression required; files are copied as-is

## Deliverables
- `backup.py` — CLI entry point and all logic
- `requirements.txt`
