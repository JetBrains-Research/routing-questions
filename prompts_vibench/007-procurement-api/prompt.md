# Procurement Request API

## Overview

Build a backend API for tracking purchase requests, suppliers, quotes, and purchase orders for a small procurement team.

## Functional Requirements

1. Create purchase requests with title, description, requester, estimated budget, and status.
2. Statuses are `draft`, `submitted`, `reviewing`, `approved`, `ordered`, and `fulfilled`.
3. Create supplier records with name, contact email, and performance score from 1 to 5.
4. Add quotes from suppliers to an approved purchase request.
5. Select a winning quote and create a purchase order.
6. A purchase order stores supplier, selected quote amount, status, and creation timestamp.
7. List purchase requests filtered by status.
8. Show a request detail view including quotes and linked purchase order.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic
- Do not implement payments or external supplier integrations.

## Deliverables

- `main.py` - API routes
- `models.py` - database models
- `schemas.py` - request/response schemas
- `database.py` - database setup
- `requirements.txt`
