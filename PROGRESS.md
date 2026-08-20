# Progress Tracker

Gates decide advancement — not the calendar. A phase is done when every box below is checked with **evidence linked** (repo, screenshot, video, score). Slipping weeks costs nothing; skipping gates costs everything.

**Started:** ____ · **Target pace:** 6–10 focused h/week (see the honest hour math in the README — ~9 h/wk lands the 12-month arc) · **Standing rules:** AWS bill ≤ $25/mo (screenshot monthly) · one LinkedIn post per phase · teardown after every chargeable lab · every spine change via PR · no secret ever enters git (gitleaks) · career track ≤1 h/wk from G2.

> **Resume ritual (after any dark stretch — illness, work crunch, Ramadan):** don't restart, re-enter. (1) Re-run your last retrieval checkpoint. (2) Re-read the current phase's Objectives. (3) Do one 30-minute warm-up task (a small PR: fix a link, add a test). Momentum returns in an evening; guilt-driven restarts cost weeks.

---

## Phase 0 — Orientation & Setup (~2 weeks)
- [ ] Lifecycle explained aloud, no notes (voice memo done)
- [ ] `[P0]` glossary self-quiz ≥17/20
- [ ] DuckDB-over-Parquet demo + "why fast" explanation
- [ ] AWS budget alarm live · `de-framework` IAM profile works
- [ ] `aws-lakehouse-platform` repo + this framework repo public · gitleaks pre-commit in both
- [ ] Anki generator built: deck imported, parser test green
- **Gate G0 passed on:** ____

## Phase 1 — Foundations (months 1–2)
- [ ] Spine v0.1: `make demo` works on fresh clone · dbt docs lineage screenshot
- [ ] Iceberg drill: schema evolution + time travel, narrated (2 min)
- [ ] `MODELING.md` written · SCD2 snapshot demo (both versions of a changed zone)
- [ ] Ingester pytest suite green (idempotency property test included)
- [ ] PR workflow live: ≥3 merged PRs in the spine
- [ ] Satellite S1 (first dbt project) public with docs site
- [ ] LeetCode SQL 50: ≥40 solved
- [ ] `INTERVIEW.md` started (this phase's questions answered in writing)
- [ ] Retrieval: 10×[P0] + 15×[P1] terms ≥80%
- [ ] Phase post published
- **Gate G1 passed on:** ____

## Phase 2 — AWS Lakehouse Core (months 3–5) ⭐
- [ ] Spine v1 on AWS: nightly Actions run green (test-gated) · dbt-athena build green
- [ ] Backfill idempotency demo (run twice, identical counts)
- [ ] S3 Tables schema-evolution drill narrated
- [ ] pytest + moto suite green in CI
- [ ] Exam mini-labs done + torn down (Kinesis ≤$3 · Redshift free credits)
- [ ] **AWS DEA-C01 PASSED** — date/score: ____ (Tutorials Dojo timed ≥80% first)
- [ ] Satellite S2: model cost leaderboard + one halved cost
- [ ] Bill ≤ $25 (screenshot) · both Maarek tranches done
- [ ] External critique requested (thread link): ____
- [ ] Career: LinkedIn rewritten · `JOB-SEARCH.md` watchlist started
- [ ] `INTERVIEW.md` updated · Retrieval ≥80% · Cost post + cert post published
- **Gate G2 passed on:** ____

## Phase 3 — Spark & Databricks (months 5–7) ⭐
- [ ] All 7 Free Edition labs done (ingestion, medallion, Delta, Jobs, declarative pipeline, UC, Asset Bundle)
- [ ] Skew-detection kata: asserts green, used inside S3a
- [ ] **Databricks DE Associate PASSED** — date/score: ____ (voucher used? ____)
- [ ] Satellite S3a: `FORENSICS.md` published
- [ ] Satellite S3b: `BAKEOFF.md` published
- [ ] External critique requested (thread link): ____
- [ ] Career: resume v1 drafted · first outreach sent · first mock interview done
- [ ] `INTERVIEW.md` updated · Retrieval ≥80% · Cert post + forensics post published
- **Gate G3 passed on:** ____

## Phase 4 — Orchestration & Ingestion (months 7–8)
- [ ] Spine v2: Airflow 3 running the platform (small DAGs, retries, alert demo on video)
- [ ] Secrets demo: DAG credentials from SSM Parameter Store · gitleaks catches a planted secret
- [ ] dlt source live in the platform
- [ ] CDC demo recorded (Postgres UPDATE → Athena) · RDS/DMS torn down on deadline (≤10 days, ≤$8)
- [ ] Kinesis path demo recorded · torn down same day (≤$5)
- [ ] DAG-integrity pytest suite green in CI
- [ ] Satellite S4a (Redshift hybrid `EXPLAIN` proof) · S4b (`COMPARISON.md` Dagster vs Airflow)
- [ ] Bill ≤ $25 despite labs (screenshot) · mid-phase billing check done
- [ ] External critique requested (thread link): ____
- [ ] Career: ≥3 applications sent this phase
- [ ] `INTERVIEW.md` updated · Retrieval ≥80% · Comparison post published
- **Gate G4 passed on:** ____

## Phase 5 — Streaming & CDC (months 9–10)
- [ ] Spine v3: local Kafka event path → AWS Iceberg via PyIceberg/REST catalog, idempotent-sink proof (duplicates sent, table correct)
- [ ] Consumer-kill rebalance demo explained
- [ ] Satellite S5: `CDC-SHOWDOWN.md` with measured latency histogram
- [ ] Flink SQL lab done (windows + watermark note)
- [ ] Confluent Kafka 101 certificate earned
- [ ] External critique requested (thread link): ____
- [ ] Career: ≥3 applications sent this phase
- [ ] `INTERVIEW.md` updated · Retrieval ≥80% · Showdown post published
- **Gate G5 passed on:** ____

## Phase 6 — Production, Serving & Capstone (months 11–12)
- [ ] Elementary live: report + deliberately-introduced anomaly caught
- [ ] Contract blocks a breaking PR (evidence PR linked)
- [ ] OpenLineage → Marquez graph screenshot
- [ ] `terraform plan` clean on spine core · tfsec run
- [ ] `PLATFORM-RUNBOOK.md` written (incl. the PDPL note)
- [ ] Satellite S6a: ClickHouse + Superset dashboard + latency-vs-Athena number (or the full-stack data-product variant)
- [ ] Satellite S6b: pgvector pipeline + retrieval check green
- [ ] Capstone rubric self-graded ≥3 avg (table below) · weakest axis fixed
- [ ] Portfolio surface done: rewritten README, 3 demo videos, pinned repos
- [ ] Resume v2 rewritten from evidence · ≥3 mock interviews
- [ ] External critique requested on the capstone (thread link): ____
- [ ] `INTERVIEW.md` complete across all phases
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

## Career log (≤1 h/wk from G2)

| Month | Applications sent | Outreach/interviews | Notes / questions I couldn't answer (→ INTERVIEW.md) |
|---|---|---|---|
| | | | |

## Weekly hours log (ISO weeks — a year of honest hours is itself a portfolio artifact)

| Week | Hours | Focus |
|---|---|---|
| 2026-W__ | | |

## Spend log

| Month | AWS | Exams/courses | Notes |
|---|---|---|---|
| | | | |

## Retrieval-checkpoint log (spaced repetition)

| Date | Phases sampled | Score | Weak terms to revisit |
|---|---|---|---|
| | | | |
