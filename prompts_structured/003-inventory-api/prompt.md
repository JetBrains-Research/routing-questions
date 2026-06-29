# Inventory Management REST API

## Overview
A REST API for managing product inventory in a small warehouse. Supports product CRUD, stock adjustments, and low-stock alerts.

## Functional Requirements
1. Create, read, update, and delete products. Each product has: `id`, `name`, `sku` (unique), `quantity`, `reorder_threshold`, `unit_price`.
2. Record stock movements: restock (increase quantity) and sale (decrease quantity), each with an optional note.
3. Reject a sale if it would bring quantity below zero; return HTTP 409 with a descriptive message.
4. `GET /products/low-stock` returns all products where `quantity <= reorder_threshold`.
5. `GET /products/{id}/history` returns the full movement history for a product ordered by timestamp descending.
6. Paginate all list endpoints with `page` and `page_size` query parameters (default page_size: 20).

## Technical Constraints
- Language: Python 3.10+
- Framework: FastAPI
- ORM: SQLAlchemy with SQLite
- Validation: Pydantic v2
- All timestamps stored and returned as UTC ISO-8601
- No authentication required

## Deliverables
- `main.py` — FastAPI app and route definitions
- `models.py` — SQLAlchemy models
- `schemas.py` — Pydantic schemas
- `database.py` — DB session setup
- `requirements.txt`
