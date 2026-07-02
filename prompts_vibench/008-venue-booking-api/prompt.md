# Venue Booking API

## Overview

Build a backend API for couples to search wedding venues, request tour slots, and submit booking requests.

## Functional Requirements

1. Venue managers can create venues with name, postcode, capacity, description, and price range.
2. Managers can add available tour slots for a venue.
3. Couples can search venues by postcode, minimum guest capacity, and date.
4. Couples can request a tour slot if it is still available.
5. A requested tour slot becomes unavailable to other couples.
6. Couples can submit a wedding booking request for a venue and date.
7. Managers can approve or decline booking requests.
8. List bookings by status.

## Technical Constraints

- Language: Python 3.10+
- Framework: FastAPI
- Storage: SQLite via SQLAlchemy
- Validation: Pydantic
- No payment processing, calendar integration, or email sending.

## Deliverables

- `main.py` - API routes
- `models.py` - database models
- `schemas.py` - request/response schemas
- `database.py` - database setup
- `requirements.txt`
