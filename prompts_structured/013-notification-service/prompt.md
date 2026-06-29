# Event-Driven Notification Service

## Overview
A Python service where producers publish typed events to named channels and consumers subscribe to channels and receive events in real time via long-polling HTTP endpoints.

## Functional Requirements
1. `POST /publish/{channel}` — publish a JSON event to a named channel; return the event ID.
2. `GET /subscribe/{channel}` — long-poll endpoint: hold the connection open until a new event arrives on that channel (or a 30-second timeout), then return the event.
3. `GET /channels` — list all active channels with the count of events published to each.
4. `GET /history/{channel}?limit=N` — return the last N events for a channel (default 50, max 200).
5. Events have: `id` (UUID), `channel`, `payload` (arbitrary JSON), `published_at` (UTC ISO-8601).
6. Events are stored in SQLite for history but delivered to waiting subscribers from an in-memory queue.

## Technical Constraints
- Language: Python 3.10+
- Framework: FastAPI with `asyncio` for the long-poll mechanism (use `asyncio.Queue` per channel)
- Storage: SQLite via `aiosqlite` for async DB access
- No external message broker (Redis, RabbitMQ, etc.)
- No WebSockets; long-polling only

## Deliverables
- `main.py` — FastAPI app and routes
- `store.py` — in-memory channel/queue management and SQLite persistence
- `requirements.txt`
