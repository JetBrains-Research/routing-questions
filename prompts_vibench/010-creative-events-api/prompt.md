# Creative Events API

## Overview

Build a backend API for a small invite-only creative community where members can discover events and RSVP while admins manage capacity and attendance.

## Functional Requirements

1. Admins can create invite codes.
2. A user can register only with a valid unused invite code.
3. Admins can create events with title, category, location, start time, capacity, and optional price.
4. Members can RSVP to an event if capacity is available.
5. If an event is full, members can join a waitlist.
6. Canceling an RSVP promotes the first waitlisted member automatically.
7. Admins can mark attendance for an event.
8. Admins can list event attendees and waitlisted members in waitlist order.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic
- No payment processing or email sending.

## Deliverables

- `main.py` - API routes
- `models.py` - database models
- `schemas.py` - request/response schemas
- `database.py` - database setup
- `requirements.txt`
