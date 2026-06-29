# Recipe Manager Web App

## Overview
A Flask web application for storing and browsing personal recipes. Users can create, edit, and delete recipes and search by ingredient or tag.

## Functional Requirements
1. Create a recipe with: title, description, ingredients (list of name + quantity), steps (ordered list), tags (comma-separated), and prep/cook time in minutes.
2. List all recipes on a home page with title, tags, and total time shown.
3. View a single recipe on its own page with full details.
4. Edit and delete recipes from the detail page.
5. Search recipes by ingredient name or tag via a search bar (case-insensitive, partial match).
6. Tag pages: clicking a tag shows all recipes with that tag.

## Technical Constraints
- Language: Python 3.10+
- Framework: Flask
- ORM: SQLAlchemy with SQLite
- Templates: Jinja2 (included with Flask)
- No JavaScript frameworks; plain HTML forms only
- CSS: minimal inline or single stylesheet, no external CSS frameworks required

## Deliverables
- `app.py` — Flask app, routes, and DB models
- `templates/` — Jinja2 HTML templates
- `static/style.css` — basic stylesheet
- `requirements.txt`
