# AsymX Logistics Level 1 — Static Shadow Run Lens

AsymX Logistics Level 1 is a static, local-only demonstration for making repeated logistics deviations visible from mock data or an anonymized CSV export.

AsymX Logistics Level 1 requires no system access. It starts from an offline export or mock CSV and shows how repeated deviations can be grouped into visible friction patterns.

## What This Is

- A single-file static HTML demo.
- No ERP, WMS, SAP, or AS400 connection.
- No backend.
- No data upload.
- No dependencies.
- Runs locally in a browser.
- Uses mock data or an anonymized CSV.

## What This Is Not

This demo is not proof of company-specific impact. It does not claim that a specific organization loses orders, has proven ghost picks, or has a confirmed system fault.

The goal is narrower and safer: make repeated deviations per location visible as possible friction clusters so an organization can decide whether internal validation is useful.

## First Real Step

The first real operational step is an internal shadow run using existing export data. That means reviewing anonymized manco, short-pick, not-found, empty-location, or blocked-location events without changing the operation.

## How To Use

1. Open `index.html` locally.
2. Load the built-in mock CSV or select an anonymized local CSV.
3. Adjust the time window and minimum event count.
4. Review possible repeated deviation clusters.
5. Export local analysis CSV or JSON if needed.

No data is uploaded or transmitted by the demo.

## Search intent / intent routing

This repository is written for people searching for the underlying operational friction, not for marketing reach.

Common intent paths include:

- repeated manco per location
- ghost pick cluster detection
- WMS export CSV schema
- offline warehouse deviation analyzer
- no-upload CSV analysis
- floor vs WMS mismatch
- short-pick cluster review
- shadow-run warehouse analysis

See:

- docs/intentional_alignment.md
- docs/search_intent_map.md
