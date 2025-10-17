# Team 2 — Bus Route Coordination: Key Policy Issues and Recommendations

Purpose: Analyze the bus route coordination project materials and identify the most pressing policy issues, data needs, and actionable recommendations for the Transport Department (TD) and operators.

---

## Executive summary
- Priority issues: opaque criteria for frequency changes, limited real-time coordination across routes/operators, uneven service equity by district/time, and insufficient publication of route-level KPIs.
- What to fix: institutionalize demand forecasting + multi-route coordination simulation; publish decision criteria and KPIs; enable data-sharing (Octopus/GPS) with privacy safeguards; pilot dynamic headways on transfer corridors.
- Expected impact: 15–25% lower average wait time, 10–20% higher utilization, improved reliability, better resilience to disruptions.

---

## Policy problem framing
1) Demand–supply mismatch
- Static timetables don’t adapt to peaks, events, and weather.
- Frequency reviews are periodic, not continuous.

2) Fragmented coordination
- Overlapping routes (and MTR feeders) lack synchronized headways, causing bus bunching and inefficient transfers.

3) Transparency and accountability
- Public lacks visibility into TD’s criteria for frequency/route adjustments and post-change evaluation.

4) Equity and accessibility
- Off-peak, peri-urban, and elderly-heavy areas face longer waits and poorer transfer alignment.

5) Resilience and incident response
- Limited playbooks for rapid reallocation during MTR disruptions or major events.

---

## Data and governance gaps
- Octopus OD samples and GPS traces are not consistently accessible for academic or civic analysis.
- Route-level KPIs (wait time percentiles, load factor distributions, on-time performance) not systematically published.
- Event/weather enrichments are ad hoc; no standard linkage to service decisions.

Minimal data package to address gaps
- Demand: boardings by stop × 5–15 min, headway observations, load by segment.
- Supply: scheduled departures, actual departures/arrivals, dwell times, capacity.
- Context: weather, special events, incidents, and MTR status.
- Geometry: stop coordinates, route paths, transfer nodes.

---

## Analytical approach (from project materials)
- Regression: predict stop- and time-specific demand and travel time; drivers include hour, day type, weather, events, demographics.
- Simulation: extend Route 56 framework to multi-route corridors; optimize headways, synchronize transfers, and test dynamic dispatch rules.
- KPIs: average and 95th percentile wait, load factor distribution, on-time reliability, transfer success rate, cost per passenger-km.

Design of experiments (DoE)
- Headway grid search (±30%) × synchronization windows (±2–6 min) × dispatch triggers (queue length, predicted demand).
- Incident scenarios: MTR partial outage, heavy rain, major event release windows.

---

## Key policy issues (detailed)
1) Decision criteria and review cadence
- Issue: Frequency changes rely on legacy thresholds; unclear thresholds for transfer synchronization.
- Remedy: Publish a KPI-based rulebook; move to rolling monthly micro-adjustments backed by forecasts.

2) Multi-operator coordination
- Issue: Different operators/routes optimize locally.
- Remedy: TD mandates corridor-level targets and synchronization at shared nodes; shared timetable API.

3) Equity-aware headways
- Issue: Off-peak and peripheral districts under-served.
- Remedy: Equity index (elderly share, income, accessibility) as constraint in optimization; minimum service guarantees by time band.

4) Real-time adjustment
- Issue: Bunching and missed transfers persist.
- Remedy: Implement control logic: hold-for-transfer, gap-based headway correction, short-turn when warranted.

5) Evaluation and public reporting
- Issue: Limited ex-post evaluation of changes.
- Remedy: Publish quarterly corridor scorecards (wait P50/P95, load factor, transfers, reliability) and change logs.

---

## Recommendations (actionable)
1) Adopt a two-tier planning cycle: quarterly planning + weekly micro-tuning from forecasts.
2) Pilot dynamic headways on two transfer corridors; synchronize with MTR event feeds.
3) Publish route/corridor KPIs and decision criteria; add a public change-log dashboard.
4) Establish a secure data-sharing protocol (Octopus OD samples, anonymized; GPS traces) with clear retention and privacy rules.
5) Introduce an equity constraint in optimization to protect off-peak and peri-urban service.
6) Define incident playbooks: auto-boost frequency, short-turn, and hold-for-transfer triggers during disruptions.
7) Create TD–operator API for timetable and control messages; standardize GTFS-RT extensions for headway control.

---

## Implementation roadmap
- Month 0–1: Data access agreements; define KPIs and corridor list; instrument baseline measurement.
- Month 2–3: Build demand model and multi-route simulator; select pilot corridors; pre-pilot tests.
- Month 4–5: Pilot dynamic headways and synchronization; monitor KPIs; weekly tuning.
- Month 6: Evaluate impact; publish report; expand to more corridors.

---

## Risks and mitigations
- Data privacy/compliance: use aggregated/anonymized OD samples; DPIA and governance.
- Operator alignment: joint KPI contracts; shared savings or incentive mechanisms.
- Model drift: monthly re-training and drift monitoring.
- Public perception: proactive comms; publish scorecards and rationale for changes.

---

## Appendices
A) Core KPIs
- Wait time (P50, P95), load factor distribution, transfer success rate, on-time reliability, cost/passenger-km.

B) Minimal schemas
- demand_by_stop(time_5min, stop_id, route_id, boardings)
- operations(time_5min, trip_id, actual_dep, actual_arr, dwell_s, load)
- context(time_5min, weather_code, event_flag, mtr_status)
- geometry(stop_id, lat, lon, corridor_id, transfer_node_id)

C) Suggested CAI request bullets (TD)
- Route-level headway observations, stop-level boardings (aggregated), load distributions, punctuality metrics; last 24 months; 5–15 min bins; CSV/XLSX; codebook.
