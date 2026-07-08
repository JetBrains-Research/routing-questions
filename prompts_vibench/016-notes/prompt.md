# Notes Application (MVP)

## Overview

A single-user notes application for quickly creating, editing, and viewing text notes. All notes belong to a single shared space protected by a fixed password.

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

**Credentials**: Password is exactly `my-notes-are-mine` (case-sensitive, not changeable).

**Persistence**: Notes persist across server restarts.

**Constraints**:
- No organization features (folders, tags, pinning)
- No rich text formatting (only plain text with line breaks)
- No attachments, exports, or imports
- No multi-user accounts or sync

## Password Protection

Every request must include the password.

**Behavior**:
- Missing password is rejected with an error ("Password is required" or similar)
- Wrong password is rejected with an error ("Incorrect password" or similar)
- No note data (titles, previews, counts, timestamps) is accessible without the correct password

## Notes List

All notes can be listed.

**Each note in the list includes**:
- **Title**: First non-empty line of the note body, trimmed of whitespace. If body is empty/whitespace-only, show placeholder like "New Note"
- **Preview**: Single-line snippet from the body following the title line, truncated with ellipsis if long
- **Timestamp**: Last edited time in exact format `YYYY-MM-DD hh:mm` (24-hour, UTC)

**Sorting**: Notes sorted by last edited timestamp, descending (most recent first).

## Create & Edit Note

**Creating**: Creating a note starts it with an empty body.

**Editing**: A note's body can be updated. Line breaks preserved.

- The last edited timestamp updates on each save

**Empty notes**: A note with empty body remains valid and listed (uses placeholder title).

## Search

Notes can be filtered by a search query.

**Matching**: Case-insensitive substring match against title OR body.

**Behavior**:
- Filtered results maintain last-edited-time sort order
- Empty query shows all notes

## Delete Note

Notes can be deleted.

**Behavior**:
- Deletion immediately removes the note from all listings and search results
- Deletion is permanent; no trash, undo, or recovery

## Note Identity

Each note has a stable identifier that returns the same note when requested again. Access to individual notes respects the password protection.
