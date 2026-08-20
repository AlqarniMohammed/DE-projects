# Progress Tracker

Gates decide advancement — not the calendar. A phase is done when every box below is checked with **evidence linked** (repo, screenshot, video, score). Slipping weeks costs nothing; skipping gates costs everything.

**Started:** ____ · **Target pace:** 6–10 focused h/week · **Standing rules:** AWS bill ≤ $25/mo (screenshot monthly) · one LinkedIn post per phase · teardown after every chargeable lab.

---

## Phase 0 — Orientation & Setup (~2 weeks)
- [ ] Lifecycle explained aloud, no notes (voice memo done)
- [ ] `[P0]` glossary self-quiz ≥17/20
- [ ] DuckDB-over-Parquet demo + "why fast" explanation
- [ ] AWS budget alarm live · `de-framework` IAM profile works
- [ ] `aws-lakehouse-platform` repo + this framework repo public
- **Gate G0 passed on:** ____

## Phase 1 — Foundations (months 1–2)
- [ ] Spine v0.1: `make demo` works on fresh clone · dbt docs lineage screenshot
- [ ] Iceberg drill: schema evolution + time travel, narrated (2 min)
- [ ] Satellite S1 (first dbt project) public with docs site
- [ ] LeetCode SQL 50: ≥40 solved
- [ ] Retrieval: 10×[P0] + 15×[P1] terms ≥80%
- [ ] Phase post published
- **Gate G1 passed on:** ____

## Phase 2 — AWS Lakehouse Core (months 3–4)
- [ ] Spine v1 on AWS: nightly Actions run green · dbt-athena build green
- [ ] Backfill idempotency demo (run twice, identical counts)
- [ ] S3 Tables schema-evolution drill narrated
- [ ] Satellite S2: model cost leaderboard + one halved cost
- [ ] Bill ≤ $25 (screenshot) · Maarek tranche 1 done
- [ ] Retrieval ≥80% · Phase post published
- **Gate G2 passed on:** ____

## Phase 3 — Spark & Databricks (months 5–6) ⭐
- [ ] All 7 Free Edition labs done (ingestion, medallion, Delta, Jobs, declarative pipeline, UC, Asset Bundle)
- [ ] **Databricks DE Associate PASSED** — date/score: ____ (voucher used? ____)
- [ ] Satellite S3a: `FORENSICS.md` published
- [ ] Satellite S3b: `BAKEOFF.md` published
- [ ] Retrieval ≥80% · Cert post + forensics post published
- **Gate G3 passed on:** ____

## Phase 4 — Orchestration & Ingestion (months 7–8) ⭐
- [ ] Spine v2: Airflow 3 running the platform (small DAGs, retries, alert demo on video)
- [ ] dlt source live in the platform
- [ ] CDC demo recorded (Postgres UPDATE → Athena) · RDS/DMS torn down
- [ ] Kinesis path demo recorded · torn down
- [ ] **AWS DEA-C01 PASSED** — date/score: ____ (Tutorials Dojo timed ≥80% first)
- [ ] Satellite S4a (Redshift hybrid `EXPLAIN` proof) · S4b (`COMPARISON.md` Dagster vs Airflow)
- [ ] Bill ≤ $25 despite labs (screenshot)
- [ ] Retrieval ≥80% · Cert post + comparison post published
- **Gate G4 passed on:** ____

## Phase 5 — Streaming & CDC (months 9–10)
- [ ] Spine v3: local Kafka event path → Iceberg, idempotent-sink proof (duplicates sent, table correct)
- [ ] Consumer-kill rebalance demo explained
- [ ] Satellite S5: `CDC-SHOWDOWN.md` with measured latency histogram
- [ ] Flink SQL lab done (windows + watermark note)
- [ ] Confluent Kafka 101 certificate earned
- [ ] Retrieval ≥80% · Showdown post published
- **Gate G5 passed on:** ____

## Phase 6 — Production, Serving & Capstone (months 11–12)
- [ ] Elementary live: report + deliberately-introduced anomaly caught
- [ ] Contract blocks a breaking PR (evidence PR linked)
- [ ] OpenLineage → Marquez graph screenshot
- [ ] `terraform plan` clean on spine core · tfsec run
- [ ] `PLATFORM-RUNBOOK.md` written
- [ ] Satellite S6a: ClickHouse + Superset dashboard + latency-vs-Athena number
- [ ] Satellite S6b: pgvector pipeline + retrieval check green
- [ ] Capstone rubric self-graded ≥3 avg (table below) · weakest axis fixed
- [ ] Portfolio surface done: rewritten README, 3 demo videos, pinned repos
- [ ] Resume rewritten from evidence · ≥3 mock interviews
- [ ] **Final retrieval: 30 terms across all phases ≥80%**
- [ ] Capstone post published
- **Gate G6 passed on:** ____

### Capstone rubric scores (0–4)

| Axis | Score | Evidence |
|---|---|---|
| Problem & docs | | |
| Ingestion breadth | | |
| Warehouse/lakehouse design | | |
| Orchestration & reliability | | |
| Quality & contracts | | |
| IaC & reproducibility | | |
| Serving & visibility | | |

---

## Spend log

| Month | AWS | Exams/courses | Notes |
|---|---|---|---|
| | | | |

## Retrieval-checkpoint log (spaced repetition)

| Date | Phases sampled | Score | Weak terms to revisit |
|---|---|---|---|
| | | | |
