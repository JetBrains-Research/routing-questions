# Habit Tracker Web Application

## Overview
A Flask web application for tracking daily habits. Users log in, define habits they want to build, and check them off each day. The app visualizes streaks and completion rates.

## Functional Requirements
1. User registration and login with hashed passwords (Flask-Login + `werkzeug.security`).
2. Each user can create habits with a name, description, and target frequency (daily only, for simplicity).
3. A dashboard shows all habits with: current streak (consecutive days checked), longest streak ever, and completion rate over the last 30 days.
4. Users check off a habit for today via a button on the dashboard; checking is idempotent (clicking again does nothing).
5. A calendar view for a single habit shows a 12-week grid where each day is colored green (done) or grey (missed/future).
6. Users can archive habits (hide from dashboard without deleting history) and delete habits permanently.

## Technical Constraints
- Language: Python 3.10+
- Framework: Flask with Flask-Login
- ORM: SQLAlchemy with SQLite
- Templates: Jinja2
- Calendar grid: rendered server-side in HTML using a table, no JavaScript charting libraries
- No external CSS frameworks required

## Deliverables
- `app.py` — Flask app, models, and routes
- `templates/` — Jinja2 templates (base, dashboard, calendar, auth)
- `requirements.txt`
