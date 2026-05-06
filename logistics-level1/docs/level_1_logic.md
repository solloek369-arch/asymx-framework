# Level 1 Logic

Level 1 is the first safe visibility layer.

## Architecture

- BRON = lokale CSV
- POINTER = locatie/event/tijd
- LIVING FIELD = cluster-markers
- GATE = veilige vervolgstap
- TIJDELIJKE EXPRESSIE = lokale analyse/export

## Explanation

The source is an offline CSV export or mock CSV. The demo does not change that source. It only reads rows, detects deviation events, groups them by location, and checks whether repeated deviations occur within a configurable time window.

The pointer layer is simple: location, event type, and time. If multiple deviation events happen at the same location inside the selected window, the demo marks that as a possible cluster.

The gate is the safe next step: validate the location flow internally. The temporary expression is the local screen output or local export.

SoLuTri can be read here only as an internal architecture rule: source first, pointer second, expression last. No philosophy is required to use the demo.
