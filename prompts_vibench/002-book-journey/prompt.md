# Book Journey (MVP)

## Overview

A multi-user reading journal where users add short "journey checkpoints" to pre-seeded books. Each book publicly exposes its details and all readers' checkpoints.

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

Books are loaded from `assets/books.json` (users cannot add or edit books). Each book contains: `id`, `title`, `author`, `year_published`, `synopsis`, `total_chapters`, `genre`.

---

## Authentication (Username Only)

- Users log in with a username only.
- Username rules: required, 3–20 characters, letters/numbers/underscores only, case-sensitive, unique.
- If validation fails: return an error.
- On valid submit:
  - If username does not exist: create account and log in.
  - If username already exists: log that user in.

---

## Browse Books

- Returns a list of all books with: title, author, year published, genre, and a synopsis preview.
- Search filters by substring match on title or author (case-insensitive).

---

## My Journey

- Lists all books where the logged-in user has at least one checkpoint.
- Shows: title, author, year published for each book.

---

## Book Details

**Book Details**:
- Title, author, year published, genre, full synopsis
- Total chapters

**Your Journey**:
- Whether the requesting user has checkpoints for this book, and their count.

**Reader Checkpoints**:
- All checkpoints from all users for this book.
- Each shows: username, chapter number, note text, mood (if present).
- Ordered by chapter number ascending.
- The requesting user's own checkpoints are identifiable as such.

---

## Checkpoints (Add Only)

Each checkpoint contains: chapter number, note text, mood (optional).

**Validation**:
- Chapter: integer between 1 and `total_chapters` (inclusive).
- Note: required, 1–280 characters after trimming leading/trailing whitespace.
- Mood options: Curious, Confused, Excited, Calm, Sad, Delighted (or none).

**On save**:
- If validation fails: return errors, do not save.
- If valid: save checkpoint. The checkpoint appears in Reader Checkpoints sorted by chapter. If first checkpoint for this book, the book appears in My Journey.

Users cannot edit or delete checkpoints.
