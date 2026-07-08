Furniture Delivery Pricing Calculator (MVP)

## Overview

Deterministic calculator for furniture delivery quotes. No payments, no accounts. Application starts empty; Admin configures all data.

Build this as a Python backend service with no UI; expose the functionality below through an HTTP API.

## Data Model

- **Settings:** Rural Rate per km, Assembly Rate per 15-min interval, Rubbish Flat Rate
- **Locations:** type (store/warehouse/supplier), name, address, city, suburb
- **Rate Cards:** serviceType (B2B/B2C), fromCity, toCity, toSuburb, ratePerM3
- **Furniture Catalog:** SKU, name, cubic metres, category

## Quote Calculation

### Inputs

- Delivery Type: B2C or B2B
- Origin: select from locations
- Destination: B2C = enter City (required) + Suburb (optional); B2B = select from locations
- Items: from catalog (quantity 1-10, optional m³ override) or custom (name, m³, quantity 1-10)
- Services: Assembly intervals (0-99), Rubbish quantity (0-99), Rural km (B2C only, ≥0)

Required: Delivery Type, Origin, Destination, at least one item. Calculation is rejected until all required inputs are present.

### Rate Matching

Filter rate cards by serviceType = Delivery Type AND fromCity = Origin's city.

- Destination city/suburb: B2C uses entered values; B2B uses selected location's city/suburb.
- **Exact Match:** toCity AND toSuburb both match destination (empty matches empty). Select lowest ratePerM3. Result labeled "Exact Match".
- **City Match (fallback):** toCity matches but toSuburb doesn't. Select highest ratePerM3. Result labeled "City Match" with "N suburbs available for this city." where N = count of unique non-empty toSuburb values for matching toCity.
- **Unavailable:** no toCity match. Result: "No rate card for selected route and delivery type."

### Pricing Formulas

- Volume Charged = MAX(1.00, Total Cubic Metres)
- Base Delivery = ratePerM3 × Volume Charged
- Assembly Cost = Assembly Rate × intervals
- Rubbish Cost = Rubbish Flat Rate × quantity
- Rural Cost = Rural Rate × km (B2C only; B2B = 0)
- Total = Base Delivery + Assembly + Rubbish + Rural

### Output

- Currency and volumes to two decimals
- When volume < 1.00, indicate "X.XX m³ (charged as 1.00 m³)"
- Rural km is not accepted for B2B

## Quotes Management

- A quote can be saved after any calculation result (including Unavailable)
- Save captures immutable snapshot (inputs, rates, costs)
- Saved quotes preserve original rates unchanged by later Admin edits
- Quotes list shows: timestamp, delivery type, origin city, destination "City (Suburb)", match tier, total (or "Unavailable")
- Quote detail shows: items, services, matched ratePerM3, volume charged, cost breakdown
- Quotes can be deleted

## Admin

- Manage Settings, Locations, Rate Cards, and Furniture Catalog (add/edit/delete)
- Reset Data: clears all locations, rate cards, catalog, quotes; resets settings to zero

## Empty Data Behavior

- **No Locations:** quote calculation is not possible
- **No Rate Cards:** calculation returns Unavailable
- **No Catalog:** user can still add custom items
