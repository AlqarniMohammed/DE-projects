# Phase 4 — Orchestration, Ingestion & AWS-Native Depth ⭐ Cert Phase 2

**Duration:** months 7–8 · **Budget:** ~85 hours (DEA prep overlaps — your builds are the labs) · **AWS cost:** ≤ $25/mo discipline: Airflow runs **locally**, RDS/DMS/Kinesis labs are short-lived with `make destroy`; exam $150 + Tutorials Dojo $15

The spine grows a real orchestrator and three ingestion modes (API, CDC, streaming-lite). The gate is **AWS DEA-C01** at the end of this phase / start of the next — Kinesis is built here deliberately so exam Domain 1 (34%) is hands-on before you sit it. Full blueprint: [CERTS.md](../../CERTS.md).

## Objectives

1. **Airflow 3.x** production patterns: assets, DAG versioning, sensors, retries, alerts — many small idempotent DAGs, never a mega-DAG.
2. Declarative ingestion with **dlt** (API sources, incremental cursors, merge dispositions).
3. **CDC on AWS** with DMS from a live RDS Postgres into the lakehouse.
4. AWS streaming ingest: **Kinesis Data Streams vs Firehose**, landing into Iceberg.
5. Redshift + Spectrum working knowledge (exam-heavy, market-relevant).
6. Pass DEA-C01.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P4]`

Orchestrator vs cron · DAG · Airflow 3 (assets, DAG versioning) · task-based vs asset-based · sensor/trigger · XCom · MWAA · dlt · **CDC** · DMS · Kinesis Streams vs Firehose · Step Functions/EventBridge · Redshift/Spectrum/Serverless · DISTKEY/SORTKEY.

## Learn (~28 h)

| Resource | Scope | Hours |
|---|---|---|
| [Astronomer Academy Airflow 101](https://academy.astronomer.io/path/airflow-101) + [DAG Authoring path](https://academy.astronomer.io/path/airflow-dag-authoring) (free, Airflow-3-native) | Both paths | 12 |
| [dlt docs](https://dlthub.com/docs/intro) — REST source tutorial + incremental loading | Working level | 4 |
| Maarek/Kane DEA course — **tranche 2** | Orchestration, Kinesis/streaming, DMS, Redshift, security, ops sections | 10 |
| [Tutorials Dojo DEA-C01 practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) ($15) | Final 3 weeks; ≥80% timed before booking | (in prep time) |
| MWAA current state reading | Now runs Airflow 3.x — know the managed trade-offs + cost | 1 |

*Before starting, re-verify:* Airflow current minor (3.3.x at research date), MWAA supported versions, Redshift Serverless free-credit terms.

## Build — Spine v2: orchestrated, multi-mode ingestion (~35 h)

1. **Airflow 3 locally** (Astro CLI or Docker Compose). Migrate the GitHub-Actions schedule into **small, single-purpose DAGs**: `ingest_taxi`, `dbt_build`, `data_checks` — retries, SLAs, Slack (or email) failure alerts, one asset-triggered dependency (dbt runs when ingest's asset updates). Keep the Actions workflow as CI only.
2. **dlt increment:** add a second source to the platform — a public REST API (weather for taxi-demand enrichment works nicely) — via **dlt** with incremental cursor + merge disposition, landing in raw and flowing through dbt. Compare: dlt config vs the hand-rolled Phase-1 downloader (line count, schema handling, retries).
3. **CDC increment:** seed a small **RDS Postgres** OLTP database (simulated operational data, e.g., a bookings app with a data generator) → **DMS** full-load + CDC to S3 → MERGE into an Iceberg silver table (Glue job or Athena MERGE) → downstream dbt marts. Prove: an UPDATE in Postgres is visible in Athena in minutes. **Tear down RDS/DMS after the demo recording** (this is a 1–2 week lab, not a permanent resident).
4. **Streaming-lite increment:** EventBridge-scheduled Lambda polls a live feed (Citi Bike GBFS or similar) → **Kinesis Data Streams → Firehose → Iceberg/S3**, partitioned; Athena queries fresh rows. Understand Streams-vs-Firehose *by having configured both ends*. Short-lived; `make destroy` after demo.
5. **AWS micro-orchestration lab (1 day):** one Step Functions state machine + EventBridge rule doing a mini-pipeline — know when this beats Airflow.
6. **MWAA lab (half-day, budgeted):** spin up the smallest MWAA env, deploy one DAG, note the ops differences, **tear it down same day** (~$10–15 total).

**AI rule:** Claude Code may generate operator boilerplate and Terraform-less setup scripts; hand-write DAG structure, dlt source config, and the MERGE logic.

## Build — Satellites (~12 h)

**S4a — Redshift + Spectrum hybrid** *(recycled Week 15)*: Redshift **Serverless** (free-credit posture) + Spectrum external schema over your S3 curated data; dbt-redshift builds one mart joining native + Spectrum tables; `EXPLAIN` screenshot proving the federated plan; cost note vs all-Redshift. Teardown after.

**S4b — Dagster vs Airflow** *(recycled Week 20)*: [Dagster University Essentials](https://courses.dagster.io/) (free, ~6 h) → rebuild ONE spine pipeline as software-defined assets with `dagster-dbt` → a short `COMPARISON.md`: task-graphs vs asset-graphs, where each wins. A senior-level conversation piece.

## Competency gate G4 ⭐

- [ ] **AWS DEA-C01 — passed** (end of month 8 / month 9).
- [ ] **Named artifact:** the orchestrated spine — Airflow UI showing green multi-DAG runs with a deliberate failure + retry + alert demonstrated on video.
- [ ] CDC demo recorded: Postgres UPDATE → visible in Athena.
- [ ] Both satellites' artifacts published.
- [ ] Bill check: the month's AWS spend ≤ $25 despite RDS/DMS/Kinesis labs (evidence in PROGRESS.md).
- [ ] **Retrieval checkpoint:** 10 random earlier terms + 15 `[P4]` terms (≥80%).

## Publish checkpoint

Two posts: (1) DEA-C01 announcement + what actually mattered in prep; (2) "I built the same pipeline in Airflow and Dagster — task graphs vs asset graphs, honestly compared."

## Interview questions you can now answer

- "Design CDC from an operational Postgres into a lakehouse — managed and open-source options."
- "Kinesis Data Streams vs Firehose vs MSK — when each?"
- "How do you make a DAG safe to re-run?" 
- "Airflow vs Dagster — what's actually different?"
- "When would you keep data in Redshift vs S3 + Spectrum?"
