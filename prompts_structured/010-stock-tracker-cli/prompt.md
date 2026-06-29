# Stock Price Tracker CLI

## Overview
A CLI tool that tracks a personal watchlist of stock tickers, fetches current prices, and stores historical data locally for trend analysis.

## Functional Requirements
1. Add or remove ticker symbols to/from the watchlist (`watch` / `unwatch` commands).
2. Fetch the latest price for all watchlist tickers and store them with a timestamp (`fetch` command). Use the Yahoo Finance unofficial API via the `yfinance` library.
3. Display current prices for all watchlist tickers in a formatted table with day change and percent change (`prices` command).
4. Show a 7-day price history for a given ticker as an ASCII line chart in the terminal (`chart` command). Use `plotext` for terminal plotting.
5. Alert if any ticker has moved more than a configurable threshold (default 5%) since the last fetch (`alerts` command).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Data fetching: `yfinance`
- Terminal chart: `plotext`
- Storage: SQLite via `sqlite3` standard library
- All prices stored with UTC timestamp

## Deliverables
- `stocks.py` — CLI entry point
- `db.py` — database schema and queries
- `requirements.txt`
