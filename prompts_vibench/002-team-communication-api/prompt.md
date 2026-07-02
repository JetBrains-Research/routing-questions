# Team Communication API

## Overview

Build a small backend API for a team communication workspace. Users can create channels, send messages, search messages, and send direct messages to other users.

## Functional Requirements

1. Users can register with a unique username and display name.
2. Users can create public channels and list all channels.
3. Users can post messages to a channel.
4. Users can send direct messages to another user.
5. Messages include sender, body, created timestamp, and edited timestamp if edited.
6. Users can edit and delete only their own messages.
7. Search returns channel and direct messages containing a case-insensitive query.
8. Deleted messages should no longer appear in normal message lists or search results.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic
- No authentication system is required; identify the acting user with an `X-User` header.

## Deliverables

- `main.py` - FastAPI app and routes
- `models.py` - SQLAlchemy models
- `schemas.py` - Pydantic schemas
- `database.py` - database setup
- `requirements.txt`
