# Configurable Web Crawler

## Overview
A Python web crawler that starts from a seed URL, follows internal links up to a configurable depth, and extracts structured data from each visited page.

## Functional Requirements
1. Accept a seed URL, max depth, and max pages as CLI arguments.
2. Crawl only URLs within the same domain as the seed (no external links).
3. For each visited page, extract and store: URL, page title, meta description, all internal links found, HTTP status code, and crawl timestamp.
4. Respect `robots.txt`; skip disallowed URLs.
5. Add a configurable delay between requests (default 1 second) to avoid overloading servers.
6. Export the collected data to a JSON file at the end of the crawl.
7. Print a live progress summary to the terminal (pages visited, pages queued, errors).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- HTTP: `requests`
- HTML parsing: `BeautifulSoup4`
- `robots.txt` parsing: `urllib.robotparser` standard library
- Storage: in-memory during crawl, exported to JSON at the end
- Crawl must be single-threaded (no concurrency required)

## Deliverables
- `crawler.py` — CLI entry point and crawler logic
- `requirements.txt`
