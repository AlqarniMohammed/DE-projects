# Prompt — Generate Unique Satellite Requirements

Paste this whole file (plus the one satellite block you're running, from the catalog below) into your AI assistant when you want a **unique, realistic set of requirements** for a satellite project instead of the default spec in the phase README. The default specs are complete on their own — this prompt exists so different learners (or a second pass through a phase) get *different data, different stakeholders, different constraints* while provably training the **same competencies**: the satellite's objectives and gate artifact are fixed and non-negotiable.

Pattern credit: the requirements-generation workflow from [`solutions-architecture-projects`](https://github.com/AlqarniMohammed/solutions-architecture-projects).

---

# Role

For Outputs 1 and 2, you are a stakeholder at a fictional company that needs a data capability. In that persona you are NOT an engineer: you do not know the names of data tools or cloud services. Output 3 is written outside this persona — see the role switch marked there.

# Task

Generate business requirements for one data-engineering satellite project, for the satellite block pasted below this prompt.

# Step 0 — Select the scenario yourself (the learner never chooses, to avoid bias)

- Read the learner's `PROGRESS.md` and any previous satellites' `requirements.md` files in their fork — do not reuse industries, scenario shapes, or data domains they've already had.
- Pick **one dataset from the block's Dataset menu** (or a same-shaped equivalent the learner can actually download) and build the company around it.
- Calibrate difficulty to the block's phase: early phases get cleaner scope, later phases get messier operational reality.
- State your selection and reasoning at the top of `requirements.md`.

# Output 1 — `requirements/requirements.md`

1. **Company & Context** — a realistic, imperfect company: small or unevenly skilled team, legacy habits (spreadsheets, a nightly CSV email, one overloaded analyst), existing vendor commitments. Include size, region, and current setup.
2. **The Problem** — purely in business terms: decisions made late, numbers nobody trusts, a regulator or partner asking for data, costs nobody can explain. No technical framing.
3. **The Data** — described as a business person experiences it: what arrives, from where, roughly how much, how often, and what's known to be wrong with it. **Mandatory: include the data warts the block's Fixed objectives train against** (e.g., duplicates and re-sends for an idempotency objective; late or out-of-order records for a streaming objective; renamed columns for a schema-evolution objective) — but describe them as complaints ("sometimes the same day's file shows up twice"), never as engineering terms.
4. **Functional Requirements** — what the stakeholders must be able to see/ask/do.
5. **Non-Functional Requirements** — concrete numbers: freshness expectations, volumes, growth, who consumes what and when.
6. **Constraints** — a realistic budget posture (this framework's hard ceiling: the cloud bill stays under ~$25/month — phrase it as the company being cost-averse), compliance sensitivities if the region implies them (e.g., Saudi PDPL for Gulf scenarios), and any timeline pressure.
7. **Success Criteria** — measurable, testable statements a non-engineer would sign off on.

# Quality rules

- In Outputs 1 and 2, never name a data tool, cloud service, file format, or architecture — you are a client, not an engineer. The learner maps the scenario onto the phase's fixed toolset; choosing tools is not the exercise, using them well is.
- Design the scenario so at least two reasonable pipeline/modeling designs exist and choosing involves real trade-offs. If the requirements imply one obvious build, rewrite until they don't.
- Deliberately leave 2–3 points ambiguous or underspecified — points that materially affect the build (grain, dedup window, what "up to date" means) so the learner must surface and resolve them in writing.
- The scenario must be satisfiable by the block's Dataset menu — don't invent data the learner can't get.

# Output 2 — `requirements/acceptance-tests.md` (BLACK-BOX)

A validation plan derived from the Success Criteria AND the block's fixed gate artifact. For each: what must be proven, how to measure it, and the pass/fail condition with a number wherever possible. Include at least one operational-failure scenario in business terms ("if a day's file arrives twice, the totals must not change"). Strict rule: never name a tool or assume an architecture — this file ships with the requirements and must not leak the solution.

# Output 3 — `requirements/.reference-solution.md` (SEALED)

Drop the client persona and switch roles: as a principal data engineer working within this framework's toolset for the block's phase, write the reference build: the pipeline/modeling design with justifications and at least one rejected alternative, how each acceptance test is satisfied, an estimated cost posture, and your resolution of each deliberate ambiguity. This file is SEALED: the learner does not read it until self-evaluation after the build. Do not quote or reference it in later turns.

---

# Satellite catalog — Fixed blocks

Copy exactly one block below the prompt when you run it. **Fixed = the same-level guarantee; the generator may never alter it.**

## S1 — First standalone dbt project (Phase 1)
- **Fixed objectives:** 3-layer dbt project from zero; 20+ models, 40+ tests, one custom generic test; published docs site. Gate artifact: public repo + live docs.
- **Dataset menu:** Hacker News dump (default) · MovieLens 25M · a data.gov.sa dataset with 3+ related entities (e.g., commercial registrations by region + activity).
- **Variable:** industry framing, which entities matter to stakeholders, the custom data-quality complaint.

## S2 — Cost-aware Athena mart (Phase 2)
- **Fixed objectives:** dbt-athena mart; per-model dollar-cost report (`MODEL_COST_REPORT.md` leaderboard); one partitioning fix demonstrably halving the top model's cost. ~5–10 GB.
- **Dataset menu:** SEC EDGAR financial statements (default) · NYC 311 · a large data.gov.sa extract (e.g., tourism or traffic).
- **Variable:** who's asking about costs and why, query patterns, freshness needs.

## S3a — Spark performance forensics (Phase 3)
- **Fixed objectives:** deliberately slow job (skew, tiny files) → measure → fix one change at a time → `FORENSICS.md` with before/after Spark UI evidence and a ranked impact table.
- **Dataset menu:** MovieLens (default) · IMDb datasets.
- **Variable:** the business job that's "too slow," its SLA, which joins matter.

## S3b — Iceberg vs Delta bake-off (Phase 3, local)
- **Fixed objectives:** same workload via PyIceberg and delta-rs; benchmark write/read/schema-evolution/time-travel; `BAKEOFF.md` with real numbers and a verdict.
- **Dataset menu:** NYC taxi months (default) · Spotify charts history.
- **Variable:** the evaluation's business trigger (vendor choice, migration debate) and which operations the company cares about most.

## S4a — Redshift + Spectrum hybrid (Phase 4)
- **Fixed objectives:** Redshift Serverless + Spectrum external schema over the learner's curated S3 data; one dbt mart joining native + external; `EXPLAIN` proof of the federated plan; cost note. Free-credit posture, teardown after.
- **Dataset menu:** the learner's own spine curated data (fixed by nature) + one small native table from any menu above.
- **Variable:** which consumer "needs the warehouse," their query shapes and cadence.

## S4b — Dagster vs Airflow comparison (Phase 4)
- **Fixed objectives:** rebuild ONE spine pipeline as Dagster software-defined assets with `dagster-dbt`; `COMPARISON.md` on task-graphs vs asset-graphs.
- **Dataset menu:** the learner's own spine pipeline (fixed).
- **Variable:** the organizational framing (who's proposing the switch and what they claim).

## S5 — CDC showdown: Debezium vs DMS (Phase 5)
- **Fixed objectives:** identical workloads through both CDC paths; `CDC-SHOWDOWN.md` with measured latency histogram, schema-change behavior, delete handling, ops/cost verdict.
- **Dataset menu (as the seeded OLTP domain):** bookings app (default) · e-commerce orders/returns · clinic appointments — any domain with updates AND deletes.
- **Variable:** the operational database's business story, table shapes, transaction mix, freshness demand.

## S6a — Serving layer (Phase 6)
- **Fixed objectives:** scheduled hot-copy of two gold marts into ClickHouse; a consumer-facing Superset dashboard **or** the full-stack data-product variant (API + minimal UI); measured latency-vs-Athena number.
- **Dataset menu:** the learner's own gold marts (default) · a regional swap: Tadawul market summaries · Umrah/Hajj seasonal statistics (data.gov.sa).
- **Variable:** who the "customer" is, the dashboard's/product's three key questions, load expectations.

## S6b — AI-data pipeline (Phase 6)
- **Fixed objectives:** documents → clean/chunk → embeddings → pgvector with idempotent upserts; a retrieval-quality check as the pipeline's test; framed as "a normal pipeline with a new sink."
- **Dataset menu:** AWS what's-new posts (default) · arXiv abstracts · a Saudi regulations/open-documents corpus.
- **Variable:** who needs retrieval and for what, corpus size, update cadence, what "a good answer" means.
