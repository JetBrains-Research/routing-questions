# RSS Feed Aggregator CLI

## Overview
A CLI tool that manages a list of RSS feed subscriptions, fetches new articles, and stores them locally for offline reading.

## Functional Requirements
1. Add a feed by URL and assign it an optional label (`add` command).
2. Remove a feed by URL or label (`remove` command).
3. List all subscribed feeds with their label, URL, and number of unread articles (`feeds` command).
4. Fetch and store new articles from all subscribed feeds (`fetch` command); skip already-stored articles using the article GUID.
5. List unread articles across all feeds sorted by publication date descending (`articles` command); support `--feed` flag to filter by label.
6. Mark an article as read by its ID and print its full content to the terminal (`read` command).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- RSS parsing: `feedparser` library
- Storage: SQLite via `sqlite3` standard library
- Article content stored as plain text (strip HTML tags using `html.parser`)
- No external HTTP library needed; `feedparser` handles fetching

## Deliverables
- `rss.py` — CLI entry point
- `db.py` — database schema and queries
- `requirements.txt`
