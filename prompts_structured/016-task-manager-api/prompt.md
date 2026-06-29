# Multi-User Task Manager API

## Overview
A REST API for a collaborative task manager where multiple users can manage shared project boards, lists, and tasks.

## Functional Requirements
1. User registration (`POST /users`) and JWT-based login (`POST /auth/token`); all other endpoints require a valid token.
2. Users can create projects and invite other registered users by email (`POST /projects/{id}/members`).
3. Each project contains lists (e.g. "To Do", "In Progress", "Done"); lists can be created, renamed, and deleted.
4. Tasks belong to a list and have: title, description, assignee (project member), due date, and priority (low / medium / high).
5. Tasks can be moved between lists via `PATCH /tasks/{id}` (update `list_id`).
6. `GET /projects/{id}/tasks` returns all tasks in the project with optional filtering by assignee, priority, and due date range.
7. Only project members can view or modify a project's data; return HTTP 403 otherwise.

## Technical Constraints
- Language: Python 3.10+
- Framework: FastAPI
- Auth: `python-jose` for JWT, `passlib[bcrypt]` for password hashing
- ORM: SQLAlchemy with SQLite
- Validation: Pydantic v2

## Deliverables
- `main.py` — FastAPI app
- `models.py` — SQLAlchemy models
- `schemas.py` — Pydantic schemas
- `auth.py` — JWT logic and dependency
- `database.py` — DB session setup
- `requirements.txt`
