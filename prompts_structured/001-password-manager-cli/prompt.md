# Password Manager CLI

## Overview
A command-line password manager that stores credentials locally in an encrypted SQLite database. The master password is used to derive an encryption key; all stored passwords are encrypted at rest.

## Functional Requirements
1. Initialize a new vault with a master password (`init` command).
2. Add a credential entry with a service name, username, and password (`add` command).
3. Retrieve a credential by service name and copy the password to the clipboard (`get` command).
4. List all stored service names and usernames without revealing passwords (`list` command).
5. Delete a credential entry by service name (`delete` command).
6. Generate a random password of configurable length and character set and optionally store it immediately (`generate` command).

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Encryption: `cryptography` library (Fernet), key derived from master password using PBKDF2HMAC
- Storage: SQLite via the `sqlite3` standard library
- Clipboard: `pyperclip`
- The master password must never be stored; only the derived key salt is persisted

## Deliverables
- `main.py` — CLI entry point
- `vault.py` — encryption and database logic
- `requirements.txt`
