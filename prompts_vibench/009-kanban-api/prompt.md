# Collaborative Kanban API

## Overview

Build a backend API for a small team's Kanban board. The board has fixed columns and supports cards that can be created, edited, moved, assigned, and deleted.

## Functional Requirements

1. Create users with display names.
2. The board has four fixed columns: `backlog`, `in_progress`, `review`, and `done`.
3. Create cards with title, description, column, optional assignee, and story points.
4. Move a card from one column to another.
5. Edit card title, description, assignee, and story points.
6. Delete a card.
7. List cards grouped by column.
8. List cards assigned to a specific user.
9. Keep an audit log for card creation, edits, moves, and deletion.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic
- Real-time synchronization is not required.

## Deliverables

- `main.py` - API routes
- `models.py` - database models
- `schemas.py` - request/response schemas
- `database.py` - database setup
- `requirements.txt`
