# Family-Friendly Yinzer Venue Finder (MVP)

## Overview

Service for discovering family-friendly venues in Pittsburgh. No login required. Read-only data from `assets/data.md` (22 venues).

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

**Core Rules:**
- Status: "Open" or "Closed". Any non-Open value in data → Closed.
- Preferences persist until changed or cleared.
- Location fallback: 40.4406° N, 79.9959° W. Indicate when the default location is being used.
- Callers may supply their own coordinates instead of the fallback.

**Distance Formula:**
```
Distance (miles) = √((Δlat × 69)² + (Δlng × 54.6)²)
```

**Distance Display:** < 0.6 mi → feet rounded to nearest 50 ft; ≥ 0.6 mi → miles with 1 decimal.

**Travel Times:** Driving at 22 mph, walking at 3 mph. Both rounded up to whole minutes.

---

## Categories

Two groups: "Food & Dining" | "Places to Visit".

| Food & Dining | Places to Visit |
|---------------|-----------------|
| General Restaurants | Playgrounds & Parks |
| Western Restaurants | Museums & Experience Centers |
| Cafes | Festivals & Events |
| Kids Cafes | Indoor Playgrounds |

Selecting a category → search results for that category.

---

## Preferences

Four sections (multi-select, none selected by default):

| Section | Options |
|---------|---------|
| Cuisine Types | Italian, Mexican, Asian, American, Mediterranean, Steakhouse, Seafood, Vegetarian, Bakery/Dessert |
| Dietary Options | Vegetarian options, Vegan options, Gluten-free, Dairy-free, Nut-free, Organic, Healthy options, Kids menu |
| Facilities | Parking, Play area, High chairs, Kids utensils, Nursing room, Changing station, Spacious seating, Outdoor space |
| Keywords | Highly rated, Good value, Great atmosphere, Romantic, Group friendly, Full bar, Scenic view, Quiet, Clean, Upscale, Casual, Family gathering, Child-friendly, Kids welcome, Entertainment, Activities |

**Keyword Matching Rules:**

| Preference | Matches If |
|------------|------------|
| Highly rated | rating ≥ 4.5 |
| Good value | keyword "good-value" OR price $ or $$ |
| Great atmosphere | keyword in {lively, cozy, beautiful, vibrant, welcoming, elegant, sophisticated, fun} |
| Romantic | keyword "romantic" |
| Group friendly | facility "Spacious seating" OR keyword "family-gatherings" |
| Full bar | facility "Full bar" |
| Scenic view | facility "Scenic view" |
| Quiet | keyword "quiet" |
| Clean | keyword "clean" |
| Upscale | price $$$ or $$$$ OR keyword "upscale" or "elegant" |
| Casual | price $ or $$ OR keyword "casual" |
| Family gathering | keyword "family-gatherings" |
| Child-friendly / Kids welcome | keyword "family-friendly" OR facility in {Play area, High chairs, Kids utensils, Changing station} |
| Entertainment | facility "Entertainment" OR keyword "entertaining" |
| Activities | facility "Play area" OR keyword in {activities, interactive, hands-on} |

Matching is case-insensitive. Hyphens and spaces equivalent (e.g., "good value" matches "good-value").

**Save:** Persists preferences. Preferences can also be cleared (reset all).

---

## Search Results

**Filtering Logic:**
- Venue must match selected category.
- For each preference section with ≥1 selection: venue must match ≥1 selected value from that section.
- Sections with no selections don't filter.

**Sorting:** Distance ascending. Ties: name A–Z.

**Each result includes:** Name, category, address, distance, rating + review count, price range, driving time, walking time, phone, status.

---

## Venue Detail

Individual venues can be retrieved with all venue info plus:

**Keywords:** "What people say" — up to 8 hashtag badges from venue's Keywords field. Format: lowercase with "#" prefix (e.g., "#family-friendly"). Omitted if no keywords.
