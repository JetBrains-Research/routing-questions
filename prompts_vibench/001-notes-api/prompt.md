# Notes REST API

## Overview
A single-user notes API where all endpoints are protected by a fixed API key. Users can create, edit, search, and delete plain text notes.

**Authentication**: All endpoints require the header `X-API-Key: my-notes-are-mine`. Requests without it or with a wrong key return HTTP 401.

**Persistence**: Notes persist across server restarts (SQLite).

**Constraints**:
- No folders, tags, or pinning
- Plain text only (no rich text or attachments)
- Single-user (no accounts or multi-user support)

## Functional Requirements

1. `POST /notes` — create a new note with a plain text `body`. Returns the created note object.
2. `GET /notes` — list all notes sorted by `last_edited_at` descending. Each note includes: `id`, `title` (first non-empty line of body, or `"New Note"` if body is empty), `preview` (second line of body truncated to 100 chars, or empty string), `last_edited_at` (UTC ISO-8601).
3. `GET /notes/{id}` — return the full note including `id`, `body`, and `last_edited_at`.
4. `PATCH /notes/{id}` — update the body of a note; updates `last_edited_at` to current UTC time. Returns the updated note.
5. `DELETE /notes/{id}` — permanently delete a note. Returns HTTP 204. Deleting a non-existent note returns HTTP 404.
6. `GET /notes?q=<query>` — filter notes by case-insensitive substring match against body. Returns same format as the full list, maintaining sort order.

## Technical Constraints
- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic v2
- Authentication: simple API key header check (no JWT or OAuth)
- All timestamps in UTC ISO-8601

## Deliverables
- `main.py` — FastAPI app and routes
- `models.py` — SQLAlchemy models
- `schemas.py` — Pydantic schemas
- `database.py` — DB session setup
- `requirements.txt`
