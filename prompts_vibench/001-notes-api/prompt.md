# Notes Application (MVP) — Backend API

## Overview

A single-user notes API for quickly creating, editing, and viewing text notes. All notes belong to a single shared space protected by a fixed API key.

**Authentication**: All endpoints require the header `X-API-Key: my-notes-are-mine` (case-sensitive). Requests without it or with a wrong key return HTTP 401.

**Persistence**: Notes persist across server restarts in SQLite.

**Constraints**:
- No organization features (folders, tags, pinning)
- No rich text formatting (only plain text with line breaks)
- No attachments, exports, or imports
- No multi-user accounts or sync

## Notes List

`GET /notes` returns a list of all notes.

**Each note includes**:
- **Title**: First non-empty line of the note body, trimmed of whitespace. If body is empty/whitespace-only, use placeholder `"New Note"`
- **Preview**: Single-line snippet from the body following the title line, truncated to 100 characters
- **last_edited_at**: Last edited time in UTC ISO-8601

**Sorting**: Notes sorted by `last_edited_at` descending (most recent first).

## Create & Edit Note

- `POST /notes` — create a new note with a `body` field. Empty body is valid.
- `PATCH /notes/{id}` — update the body of a note. Updates `last_edited_at` to current UTC time.

**Empty notes**: A note with empty body remains valid (uses placeholder title).

## Search

`GET /notes?q=<query>` filters notes by case-insensitive substring match against the body.

- Filtered results maintain `last_edited_at` sort order
- Empty or missing `q` returns all notes

## Delete Note

`DELETE /notes/{id}` — permanently deletes a note. Returns HTTP 204 on success, HTTP 404 if not found. Deletion is permanent; no trash or recovery.

## Technical Constraints
- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic v2

## Deliverables
- `main.py` — FastAPI app and routes
- `models.py` — SQLAlchemy models
- `schemas.py` — Pydantic schemas
- `database.py` — DB session setup
- `requirements.txt`
