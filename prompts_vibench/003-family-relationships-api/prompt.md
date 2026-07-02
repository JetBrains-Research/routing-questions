# Family Relationships API

## Overview

Build a private family relationship API where users can form confirmed family relationships and share posts visible only to direct family members.

## Functional Requirements

1. Users can register with email, username, display name, and password.
2. Email and username are unique case-insensitively.
3. Users can send relationship requests to another user as `parent`, `child`, `spouse`, or `sibling`.
4. A relationship becomes active only after the recipient accepts the request.
5. A user cannot have more than one pending or active relationship with the same other user.
6. Either party can end an active relationship.
7. Users can create text posts.
8. A user can list posts from themselves and active direct family relationships only.
9. When a relationship ends, both users immediately lose access to each other's posts.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Passwords may be stored with a simple hash for this exercise.
- No friends-of-friends visibility.

## Deliverables

- `main.py` - API routes
- `models.py` - database models
- `schemas.py` - request/response schemas
- `database.py` - database setup
- `requirements.txt`
