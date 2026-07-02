# Team Sprint Board (MVP)

## Overview

A collaborative sprint board for small teams. No authentication—users provide a display name and immediately join a single shared board. Board data persists until manually cleared.

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

---

## Identity

- Users must provide a display name before accessing the board.

---

## Board Structure

- Four fixed columns: **Backlog**, **In Progress**, **Review**, **Done**.
- Columns cannot be added, removed, renamed, or reordered.
- Each column contains a list of cards.

---

## Cards

**Card Data**
- Title (required)
- Description (optional)
- Story Points (optional): blank, 1, 2, 3, 5, 8, 13
- Status: determined by which column the card is in

**Creating Cards**
- Cards are created in a specific column with title, description, and story points fields.
- Title is required; submission with empty title returns a validation error.
- A card can be created with only title set.
- New cards appear in the column where they were created.

**Editing Cards**
- A card's title, description, story points, and status are editable.
- Changing status moves the card to the corresponding column immediately.
- A card can be permanently deleted.

**Moving Cards**
- Cards can be moved between columns by changing their status.

---

## Clear Done

- All cards in Done can be permanently deleted in one operation.
- Cards in other columns are unaffected.
