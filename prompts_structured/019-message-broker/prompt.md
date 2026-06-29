# Simple Message Broker

## Overview
A lightweight publish-subscribe message broker implemented as a TCP server. Producers publish messages to named topics; consumers subscribe to topics and receive messages in delivery order.

## Functional Requirements
1. The server accepts TCP connections on a configurable port.
2. Clients send newline-delimited text commands:
   - `SUBSCRIBE <topic>` — subscribe to a topic; server will push new messages as they arrive
   - `PUBLISH <topic> <message>` — publish a message to a topic
   - `UNSUBSCRIBE <topic>` — unsubscribe from a topic
   - `TOPICS` — list all topics with their message counts
3. Messages published to a topic are delivered to all currently connected subscribers of that topic.
4. Messages are persisted to a SQLite database so late-joining subscribers can request history: `HISTORY <topic> <n>` returns the last n messages.
5. The server handles multiple concurrent clients using `threading`.
6. Include a simple Python client class (not a CLI) that wraps the TCP connection and exposes `publish`, `subscribe`, and `get_history` methods.

## Technical Constraints
- Language: Python 3.10+
- Server: `socket` and `threading` standard library
- Storage: SQLite via `sqlite3` standard library
- No external broker libraries
- Message format on the wire: plain UTF-8 text, newline-delimited

## Deliverables
- `broker.py` — server implementation
- `client.py` — Python client class
- `requirements.txt`
