# Search Intent Map — AsymX Logistics Level 1

This document maps real search intent to the repository structure.

The repository should be discoverable through the underlying operational reality, not only through the project name.

## Problem-solving intent

People may search:

- herhaalde manco per locatie
- manco scanning magazijn analyse
- ghost pick detecteren CSV
- voorraadverschil WMS vloer
- repeated short pick analysis
- warehouse deviation CSV analyzer
- floor vs WMS mismatch analysis
- short-pick cluster detection

Repository entry points:

- README.md
- index.html
- docs/level_1_logic.md
- samples/mock_manco_data.csv

## Technical / IT review intent

People may search:

- offline CSV warehouse tool
- static ghost pick analyzer
- browser-only CSV analyzer
- no data upload CSV tool
- WMS export schema
- pick-log CSV analyzer
- warehouse event_type location_id timestamp
- local-only warehouse analysis

Repository entry points:

- SECURITY.md
- docs/no_data_policy.md
- schema/asymx_logistics_level1.schema.json
- template/shadow_run_template.csv
- checksums/SHA256SUMS.txt

## Research / operational improvement intent

People may search:

- inventory record inaccuracy
- phantom inventory CSV
- short pick cluster
- repeated deviation cluster
- warehouse visibility gap
- inventory latency
- supply chain visibility shadow run
- floor reality vs WMS data

Repository entry points:

- docs/shadow_run_book.md
- docs/claim_safety.md
- docs/level_1_logic.md
- docs/intentional_alignment.md

## Dutch intent terms

- herhaalde manco
- manco per locatie
- voorraadverschil magazijn
- WMS vloer afwijking
- pick-log analyse
- offline manco analyzer
- schaduwdraai magazijn
- geen data upload
- browser-only analyse

## English intent terms

- repeated manco per location
- ghost pick cluster detection
- warehouse deviation analyzer
- offline inventory inaccuracy tool
- floor vs WMS mismatch
- static CSV analyzer
- no-upload warehouse tool
- WMS export CSV schema
- short-pick cluster detection

## Principle

Who searches broadly sees a tool.
Who searches deeply finds the mechanism.

Head term → depth term → data structure → safety → recognition → testable entry.
