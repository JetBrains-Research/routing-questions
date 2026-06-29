# Simple Blog Web Application

## Overview
A Flask web application for a single-author blog. The author can write and manage posts; visitors can read posts and leave comments.

## Functional Requirements
1. Admin area (protected by a hardcoded username/password in config) for creating, editing, and deleting posts.
2. Each post has: title, body (Markdown, rendered to HTML), slug (auto-generated from title), published date, and published/draft status.
3. Home page lists published posts sorted by date descending, showing title, date, and first 200 characters of body.
4. Individual post page renders the full Markdown body and shows approved comments below.
5. Visitors can submit comments (name + body); comments are stored but marked unapproved by default.
6. Admin can approve or delete comments from the post detail page.
7. Posts are paginated at 5 per page on the home page.

## Technical Constraints
- Language: Python 3.10+
- Framework: Flask with Flask-Login for admin session management
- ORM: SQLAlchemy with SQLite
- Markdown rendering: `mistune`
- Templates: Jinja2
- No JavaScript frameworks

## Deliverables
- `app.py` — Flask app, models, and routes
- `templates/` — Jinja2 templates (base, index, post, admin)
- `requirements.txt`
