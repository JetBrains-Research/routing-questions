# ViBench PRD Adaptation Logic

How we convert ViBench PRDs (https://github.com/ViBench/vibench-public) into
backend-only Python prompts for the solution-quality survey.

## Goal

Reuse the ViBench MVP tasks as greenfield prompts while removing UI
requirements, so that the generated solutions are pure Python backends that a
human can review at code level in 20–30 minutes. The adapted prompt should stay
as close to the original PRD as possible.

The value of using ViBench is that its tasks are grounded in real user behavior,
and the more we rewrite, the less that grounding holds.

## Scope

- **MVP only.** Feature 1/2/3 PRDs are not used.
- One folder per task: `prompts_vibench/<id>-<name>/` containing:
  - `original_prd.md` — the ViBench MVP PRD, verbatim, for traceability
  - `prompt.md` — the adapted prompt
  - `metadata.json` — id, source ViBench app, difficulty, category, stack

## Adaptation Rules

### 1. Preserve the original wording
- Copy sentences verbatim wherever possible. Inly touch sentences that reference the UI.
- Keep the original section structure and headings.
- Keep exact values: credentials, formats (e.g. `YYYY-MM-DD hh:mm`),
  placeholder strings (e.g. "New Note"), limits, sort orders.
- Keep the original's level of ambiguity. If the PRD says "truncated with ellipsis if long",
  do not invent a character count.
  Ambiguity is part of the task.
- Keep **Constraints** blocks verbatim, they define scope boundaries.

### 2. Remove, don't rewrite
- Drop purely UI/browser behaviors entirely: masked input fields, cursor focus,
  autosave-on-navigation, confirmation dialogs, tab/session re-locking,
  page routing, empty-state screens, visual layout.
- Do not replace a removed UI behavior with an invented backend requirement.

### 3. Translate only where necessary
- When a requirement's substance survives without the UI, translate it
  one-to-one to the closest backend equivalent:
  - password gate on page load → password required on every request
  - persists across browser sessions → persists across server restarts
  - "click a note to open it" → individual notes can be retrieved
  - stable note URL → stable note identifier
- Keep translations semantic, not prescriptive: say "requests without the
  password are rejected with an error", not exact header names, routes, or
  HTTP status codes — unless the original specified the error behavior.

### 4. Add no technical requirements
- The original PRDs mandate no framework, ORM, or file layout — the adapted
  prompt must not either.
- The only addition allowed is one sentence in the Overview:
  *"Build this as a Python backend service with no UI; expose the
  functionality below through an HTTP API."*
- No "Deliverables" section, no required file names, no library choices.
  Architecture decisions are part of what survey participants evaluate.

### 5. Keep scope identical
- No requirements added, none dropped beyond UI-only ones.
- If a section becomes empty after removing UI-only content, drop the section.
- If an entire task is inseparable from its UI (e.g. whiteboard, visual
  games), exclude the task instead of forcing an adaptation, and record the
  exclusion and reason in this file.

## Excluded Tasks

(filled in as tasks are reviewed)

| ViBench app | Reason |
|---|---|
