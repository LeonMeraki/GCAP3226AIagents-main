# Plan for Government Enquiries — Team 1: Flu Vaccination Project

Purpose: Secure the minimum viable datasets to analyze flu vaccination participation, campaign effectiveness, and policy options in Hong Kong, aligned with the team roadmap and meeting notes.

Success criteria:
- Obtain aggregated, de-identified datasets sufficient for regression and/or simulation.
- Coverage for at least 5–8 seasons (e.g., 2017/18–2024/25) to support trend modeling.
- Clear data dictionaries and consistent geographic/time units for linkage.

---

## 1) Inputs reviewed
- Team folder: `Team1_FluShot/`
  - `README.md` (project overview, objectives, data sources)
  - `Project_Roadmap_Team1.md` (timeline, enquiry template draft)
  - `adminFluShot.md` (admin notes)
  - Transcripts: meeting notes discussing causal inference, targeting vulnerable groups, school outreach program, and data gaps

## 2) Core questions the data must answer
- What factors drive vaccination uptake by district/demographic group and over time?
- How does vaccination uptake relate to influenza infection and hospitalization trends?
- Do school-based outreach programs materially increase uptake?
- Which targeting strategies (e.g., chronic-condition groups) are most cost-effective?

## 3) Key data gaps to fill
- Vaccination uptake with consistent denominators (population eligible) by age group and district over time
- Program modality breakdown (e.g., School Outreach vs. private GP vs. GOPC)
- Infection and hospitalization counts for influenza (and ILI) by age group/district over time
- If available, linkage/stratification by vaccination status (de-identified, aggregated)
- School outreach participation rates and coverage (school counts, uptake, grades)
- Population denominators and socio-demographic covariates for modeling (C&SD)
- Operational data for simulation (site locations, capacities, hours, resource allocations)

---

## 4) Agencies and targeted requests (CAI)
Keep each request scoped, aggregated, and machine-readable (CSV/XLSX). Ask for a data dictionary and codebooks.

### A) Department of Health (DH)
Subject: Code on Access to Information request — Flu Vaccination Programme data (2017/18–2024/25)

Request:
- Core tables (aggregated, de-identified):
  1) vaccination_coverage.csv (long format preferred)
    - Required fields: season_label (e.g., 2017/18), time_key (YYYY-Www or YYYY-MM), geo_key (district_code or ha_cluster), age_band_code, sex (M/F/U), eligibility_code, delivery_channel_code, vaccinated_count, eligible_count, coverage_pct
    - Constraints: include zero rows for combinations with 0 counts; add field "suppressed" (TRUE/FALSE) when applying small-cell suppression; provide population denominator definition used for eligible_count
  2) campaign_operations.csv (if available)
    - season_label, campaign_start_date, campaign_end_date, delivery_channel_code, outreach_events_count, materials_distributed_count, media_campaign_flag
  3) site_roster.csv (if available)
    - site_id, site_name, address_line, district_code, lat, lon, delivery_channel_code, capacity_class (S/M/L), opening_weeks (list or start_week/end_week), weekday_hours (e.g., Mon–Sun ranges)

  Definitions and code lists requested:
  - age_band_code target bands: <6, 6–11, 12–17, 18–49, 50–64, 65+ (provide exact bands used in reporting)
  - district_code: 18 District Councils; provide mapping table (district_code, district_name, ha_cluster)
  - eligibility_code (examples): child_school, child_non_school, elderly_65p, chronic_condition, healthcare_worker, pregnant, other — please provide official categories
  - delivery_channel_code (examples): school_outreach, GOPC, private_GP, community_clinic, outreach_mobile — please provide official channels

  Time resolution and period:
  - Weekly (ISO-8601) preferred; monthly acceptable with season_label; seasons 2017/18 to latest available

  Quality and metadata:
  - Provide data dictionary, calculation of coverage_pct, small-cell suppression rule, revision history (last_updated), and contact point for queries
  - If vaccine brand/strain composition by season is reported publicly, include a simple table (season_label, vaccine_type/strain)

Format & period:
- CSV/XLSX; seasons 2017/18 to latest available; aggregated, no personal data

### B) Hospital Authority (HA)
Subject: Code on Access to Information request — Influenza infection and hospitalization statistics (2017–2025)

Request:
- Core tables (aggregated, de-identified):
  1) influenza_burden.csv
    - Required fields: time_key (YYYY-Www or YYYY-MM), geo_key (ha_cluster or district_code), age_band_code, ili_attendances, lab_confirmed_influenza, admissions_influenza, admissions_influenza_icu
    - Optional fields: all_cause_admissions, respiratory_admissions, influenza_deaths (if coded), occupancy_rate_medical (if routinely reported)
  2) testing_activity.csv (if available)
    - time_key, lab_tests_total, lab_tests_influenza_positive, positivity_rate
  3) vaccination_status_split.csv (if feasible)
    - time_key, geo_key, age_band_code, admissions_influenza_vaccinated, admissions_influenza_unvaccinated_or_unknown

  Specifications and codes:
  - ICD-10 codes used for influenza (e.g., J09–J11); provide exact coding and whether primary/any diagnosis
  - ILI definition used in A&E/OPD and sentinel systems; provide link to HA/WHO definition
  - age_band_code: provide bands used; align to DH bands if possible
  - geo_key mapping: provide table for cluster -> districts

  Quality and metadata:
  - Include zeros for absent weeks; note small-cell suppression approach; provide last_updated and any known breaks in series (e.g., coding changes)

Format & period:
- CSV/XLSX; 2017–latest available; aggregated

### C) Education Bureau (EDB) — School Outreach Vaccination Programme
Subject: Code on Access to Information request — School Outreach Vaccination Programme statistics (2017/18–2024/25)

Request:
- Core tables (aggregated, no school identifiers required):
  1) outreach_coverage.csv
    - Required fields: season_label, district_code, school_type (Govt/Aided/DSS/Private/Special), pupils_eligible, pupils_vaccinated, coverage_pct
  2) grade_breakdown.csv (if available)
    - season_label, district_code, grade_code (P1–P6; S1–S6 if applicable), pupils_eligible, pupils_vaccinated
  3) consent_flow.csv (if available)
    - season_label, district_code, consent_forms_distributed, consent_forms_returned, refusal_count (with categorization if collected)
  4) program_calendar.csv (if available)
    - season_label, district_code, outreach_start_week, outreach_end_week, sessions_held

  Quality and metadata:
  - Provide definitions of school_type categories and whether special schools are included
  - Provide any evaluation metrics used by EDB for program success

Format & period:
- CSV/XLSX; aggregated by district/season; no school identifiers required (district-level is sufficient if school-level is sensitive)

### D) Census & Statistics Department (C&SD)
Subject: Data request — Population denominators and socio-demographic covariates for modeling

Request:
- Core tables:
  1) population_denoms.csv
    - Required fields: year, district_code, age_band_code, sex (M/F), pop_count
  2) socio_demographics.csv
    - year, district_code, median_household_income, median_age, hh_size_avg, education_share_secondary, education_share_tertiary, poverty_rate (if available)
  3) geospatial_support (if available or point to public):
    - District boundary shapefile/GeoJSON (with vintage noted) and district_code list for mapping and joins

  Metadata:
  - Document definitions, vintages (e.g., mid-year population), and any boundary changes across years

Format & period:
- CSV/XLSX; district-level; 2017–latest

### E) OGCIO / data.gov.hk (self-serve public datasets)
- Search and collect:
  - Sentinel ILI surveillance reports
  - Weekly influenza situation updates
  - Vaccination programme press releases/annual summaries
  - District-level demographic tables
- Log dataset titles, publishers, update frequency, and direct URLs in the source log

---

## 5) Minimal variable set and schema examples
Aim for consistent time and geography keys to join across tables.

Common keys:
- time_key: ISO week (YYYY-Www) or month (YYYY-MM); season label (e.g., 2019/20)
- geo_key: district (18 DCs) and/or HA cluster
- age_band: standard age group codes

Example — vaccination_coverage.csv
- season, time_key, geo_key, age_band, eligibility, channel, vaccinated_count, eligible_count, coverage_pct

Example — influenza_burden.csv
- time_key, geo_key, age_band, ili_attendances, lab_confirmed_flu, flu_admissions, flu_icu

Example — outreach_program.csv
- season, geo_key, schools_participating, pupils_eligible, pupils_vaccinated, coverage_pct

Denominators — population_denoms.csv
- year, geo_key, age_band, pop_count, income_median, education_share_secondary, education_share_tertiary

---

## 6) Email templates (concise, CAI-aligned)

Template header
- Subject: Request under the Code on Access to Information — [Dataset name] (2017–[latest])
- To: Access to Information Officer, [Agency]

Body
- We are undergraduate students (HKBU GCAP3226) analyzing flu vaccination campaigns. We request aggregated, de-identified data to support academic research. We prefer CSV/XLSX and can accept existing report layouts.
- Requested items: [bullet list tailored per agency above]
- Timeframe: [season/year range]; Time unit: weekly or monthly if feasible
- Geographic unit: district or HA cluster (no personal data)
- Please include data dictionaries/definitions and any caveats
- If some items are not available, kindly advise nearest available fields or public reports
- We understand CAI target response timelines (~10 days acknowledgement; ~21 days substantive reply) and are happy to refine scope to reduce burden/cost
- Contact: [names/emails]; Deadline: [date ~3 weeks out]
- Thank you for your assistance

---

## 7) Timeline and follow-up
- Week 1 (today): Finalize requests; QA for clarity and minimal burden
- Week 1 Day 2: Send DH and HA requests; log timestamps; set calendar reminders for Day 10 and Day 21
- Week 1 Day 3: Send EDB and C&SD requests; log
- Week 2: Harvest public datasets from data.gov.hk; start source log; begin preliminary EDA
- Week 2–3: Respond to agency clarifications; adjust scope if fees/time are high; accept partial deliveries
- Week 3: Integrate first data drops; draft model choice justification; confirm time/geography harmonization
- Week 4+: Request refinements if necessary (e.g., add age bands or shift to cluster-level if district rejected)

Follow-up rules:
- Polite reminder on Day 12 if no interim reply; formal follow-up on Day 21 if no substantive reply
- Record every correspondence in the source log

---

## 8) Data quality, privacy, and constraints
- Request aggregated counts and rates only; no personal data
- Accept coarser geography (HA cluster) if district-level is restricted
- If vaccination-status stratification is unavailable, request proxies (e.g., sentinel cohorts) and note limitations in analysis
- Ask for clear ICD and definition references to ensure comparability

---

## 9) Modeling alignment
- Regression: Dependent variable = vaccination coverage by district/age; predictors = demographics, outreach availability, time effects, prior season burden
- Simulation: Inputs = site capacity, outreach coverage, demand elasticity by group; Scenarios = targeted outreach to vulnerable groups, timing strategies, resource allocation
- Output link: Recommendations on precision targeting and resource allocation

---

## 10) Source logging (create a shared sheet)
Columns: agency | request title | date sent | contact | expected by | status | link/file | schema notes | caveats | next action

---

## 11) Risks and fallback
- If school-level data not provided: use district-level outreach coverage
- If vaccination-status not available in HA data: use regression with instrumental/lagged proxies; document limitation
- If fees or workload are high: narrow to fewer seasons or coarser geography; accept existing published report tables

---

## 12) Next actions (immediate)
- Paste tailored email text into four requests and send
- Start the source log document
- Begin a lightweight EDA notebook to validate joins once first dataset arrives

Appendix — agency-specific bullets to paste

DH bullets:
- Seasonal vaccination counts/rates by age band, sex (if available), district, eligibility, and delivery channel; weekly/monthly time
- Site list (if available); data dictionary; 2017/18–latest; CSV/XLSX

HA bullets:
- Weekly/monthly ILI, lab-confirmed influenza, admissions, ICU; by age band and cluster/district; 2017–latest; CSV/XLSX; definitions (ICD, ILI)

EDB bullets:
- Schools participating, eligible pupils, vaccinated pupils, coverage by district and season; grade-level if available; 2017/18–latest; CSV/XLSX; definitions

C&SD bullets:
- District population by age/sex annually; median income; education attainment shares; 2017–latest; CSV/XLSX; variable definitions

Notes:
- A meeting transcript contains merge conflict markers; consider cleaning to maintain a single authoritative version before quoting.
