# Extensible CLI with Plugin System

## Overview
A CLI application framework where core functionality is minimal and all features are loaded as plugins from a designated folder at runtime.

## Functional Requirements
1. The core CLI (`main.py`) discovers and loads all `.py` files in a `plugins/` directory at startup.
2. Each plugin registers one or more Click commands by implementing a `register(cli)` function that receives the root Click group.
3. Include three example plugins:
   - `hello.py` — a `hello` command that greets the user by name
   - `time.py` — a `time` command that prints the current date/time in a given timezone (using `pytz`)
   - `hash.py` — a `hash` command that hashes a string with a selectable algorithm (md5, sha1, sha256)
4. Running `python main.py --help` must list all commands from all loaded plugins.
5. If a plugin fails to load (syntax error, missing dependency), print a warning and continue loading the rest.
6. Support a `--plugins-dir` option on the root command to specify a custom plugins directory.

## Technical Constraints
- Language: Python 3.10+
- CLI framework: Click
- Plugin loading: `importlib` standard library
- `pytz` for timezone support in the example plugin only
- No plugin should need to import from `main.py`

## Deliverables
- `main.py` — core CLI and plugin loader
- `plugins/hello.py`, `plugins/time.py`, `plugins/hash.py` — example plugins
- `requirements.txt`
