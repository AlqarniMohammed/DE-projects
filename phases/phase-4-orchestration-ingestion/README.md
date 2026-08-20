# Phase 4 — Orchestration, Ingestion & AWS-Native Depth

**Duration:** months 7–8 · **Budget:** ~72 hours · **AWS cost:** ≤ $25/mo discipline: Airflow runs **locally**, RDS/DMS/Kinesis labs are short-lived with `make destroy` and per-lab caps below

The spine grows a real orchestrator and three ingestion modes (API, CDC, streaming-lite). **You sit no exam this phase — the builds are the point.** Both certs are already behind you, which changes the texture: Kinesis, DMS, and Redshift arrive as services you've *answered exam questions about* and now get to operate for real, with no prep clock running. This is where the platform starts reading as production.

## Objectives

1. **Airflow 3.x** production patterns: assets, DAG versioning, sensors, retries, alerts — many small idempotent DAGs, never a mega-DAG.
2. Declarative ingestion with **dlt** (API sources, incremental cursors, merge dispositions).
3. **CDC on AWS** with DMS from a live RDS Postgres into the lakehouse.
4. AWS streaming ingest: **Kinesis Data Streams vs Firehose**, landing into Iceberg — deepening the P2 mini-lab into a real pipeline.
5. Redshift + Spectrum working knowledge (market-relevant; the satellite goes deeper than the P2 taste lab).
6. **Secrets handled like production:** no credential in code or git, ever.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P4]`

Orchestrator vs cron · DAG · Airflow 3 (assets, DAG versioning) · task-based vs asset-based · sensor/trigger · XCom · MWAA · dlt · **CDC** · DMS · Kinesis Streams vs Firehose · Step Functions/EventBridge · Redshift/Spectrum/Serverless · DISTKEY/SORTKEY · secrets backend.

## Learn (~18 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Astronomer Academy Airflow 101](https://academy.astronomer.io/path/airflow-101) + [DAG Authoring path](https://academy.astronomer.io/path/airflow-dag-authoring) (free, Airflow-3-native) | Both paths | 12 | Build step 1 (the small-DAGs migration) + the DAG-integrity test assignment |
| [dlt docs](https://dlthub.com/docs/intro) — REST source tutorial + incremental loading | Working level | 4 | Build step 3: the dlt source + the written dlt-vs-hand-rolled comparison |
| MWAA current state reading | Now runs Airflow 3.x — know the managed trade-offs + cost | 1 | The MWAA lab (build step 7) + its ops-differences note |
| [Airflow secrets backend docs](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-ssm-parameter-store-secrets-backend.html) — SSM Parameter Store | Read before build step 2 | 1 | Build step 2: the SSM-backed connections wiring |

*Before starting, re-verify:* Airflow current minor (3.3.x at research date), MWAA supported versions, Redshift Serverless free-credit terms.

## Build — Spine v2: orchestrated, multi-mode ingestion (~38 h)

Each chargeable lab lists its **cost cap and teardown deadline** — check the AWS billing page mid-phase, not just at the gate.

1. **Airflow 3 locally** (Astro CLI or Docker Compose). Migrate the GitHub-Actions schedule into **small, single-purpose DAGs**: `ingest_taxi`, `dbt_build`, `data_checks` — retries, SLAs, Slack (or email) failure alerts, one asset-triggered dependency (dbt runs when ingest's asset updates). Keep the Actions workflow as CI only.
2. **Secrets increment (~2–3 h):** wire Airflow's connections to the **AWS SSM Parameter Store secrets backend** — RDS password, Slack webhook, API keys all live there, none in `airflow.cfg`, env files, or git. The P0 `gitleaks` pre-commit hook has guarded the repo since day one; this is where the *runtime* side becomes production-shaped. Interview probe you can now answer: "how do your DAGs get credentials?"
3. **dlt increment:** add a second source to the platform — a public REST API (weather for taxi-demand enrichment works nicely) — via **dlt** with incremental cursor + merge disposition, landing in raw and flowing through dbt. Compare: dlt config vs the hand-rolled Phase-1 downloader (line count, schema handling, retries).
4. **CDC increment** *(cap ≤ $8 · teardown ≤ 10 days after first CDC event)*: seed a small **RDS Postgres** OLTP database (simulated operational data, e.g., a bookings app with a data generator) → **DMS** full-load + CDC to S3 → MERGE into an Iceberg silver table (Glue job or Athena MERGE) → downstream dbt marts. Prove: an UPDATE in Postgres is visible in Athena in minutes. **Record the demo, then tear down RDS/DMS.**
5. **Streaming-lite increment** *(cap ≤ $5 · teardown same day as demo)*: EventBridge-scheduled Lambda polls a live feed (Citi Bike GBFS or similar) → **Kinesis Data Streams → Firehose → Iceberg/S3**, partitioned; Athena queries fresh rows. The P2 mini-lab configured the plumbing once; this time it's a real pipeline with a consumer.
6. **AWS micro-orchestration lab (1 day, ~$1):** one Step Functions state machine + EventBridge rule doing a mini-pipeline — know when this beats Airflow.
7. **MWAA lab** *(cap ~$10–15 · teardown same day)*: spin up the smallest MWAA env, deploy one DAG, note the ops differences.

**AI rule:** Claude Code may generate operator boilerplate and setup scripts; hand-write DAG structure, dlt source config, the secrets-backend wiring, and the MERGE logic.

### Prove-it assignment (2–3 h): DAG integrity tests

A pytest suite CI runs on every PR: all DAGs import cleanly (no top-level heavy code), every DAG has retries + owner set, no task is orphaned, and one DAG-level unit test with a mocked operator. The standard Airflow testing pattern — and the reason a broken DAG never reaches the scheduler.

## Build — Satellites (~12 h)

**S4a — Redshift + Spectrum hybrid** *(recycled Week 15; cap = free credits · teardown after demo)*: Redshift **Serverless** + Spectrum external schema over your S3 curated data; dbt-redshift builds one mart joining native + Spectrum tables; `EXPLAIN` screenshot proving the federated plan; cost note vs all-Redshift.

**S4b — Dagster vs Airflow** *(recycled Week 20)*: [Dagster University Essentials](https://courses.dagster.io/) (free, ~6 h) → rebuild ONE spine pipeline as software-defined assets with `dagster-dbt` → a short `COMPARISON.md`: task-graphs vs asset-graphs, where each wins. A senior-level conversation piece.

Generated, unique requirements for either satellite: [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Career track (≤1 h/wk)

Applications begin: **3–5 targeted applications per month** from the `JOB-SEARCH.md` watchlist, tailored from resume v1. Interview feedback is curriculum — log every question you couldn't answer into `INTERVIEW.md` and let it steer the remaining phases.

## Competency gate G4

- [ ] **Named artifact:** the orchestrated spine — Airflow UI showing green multi-DAG runs with a deliberate failure + retry + alert demonstrated on video.
- [ ] Secrets demo: a DAG pulls its credentials from SSM Parameter Store; `gitleaks` pre-commit shown catching a planted secret.
- [ ] CDC demo recorded: Postgres UPDATE → visible in Athena · RDS/DMS torn down on deadline.
- [ ] Kinesis path demo recorded · torn down.
- [ ] DAG-integrity pytest suite green in CI.
- [ ] Both satellites' artifacts published.
- [ ] Bill check: the month's AWS spend ≤ $25 despite the labs (evidence in PROGRESS.md) · mid-phase billing check done.
- [ ] **External critique requested:** comparison or CDC artifact posted — request thread linked.
- [ ] Career: ≥3 applications sent this phase · `INTERVIEW.md` updated.
- [ ] **Retrieval checkpoint:** 10 random earlier terms + 15 `[P4]` terms (≥80%).

## Publish checkpoint

Post: "I built the same pipeline in Airflow and Dagster — task graphs vs asset graphs, honestly compared."

## Interview questions you can now answer

- "Design CDC from an operational Postgres into a lakehouse — managed and open-source options."
- "Kinesis Data Streams vs Firehose vs MSK — when each?"
- "How do you make a DAG safe to re-run?"
- "How do your DAGs get credentials?"
- "Airflow vs Dagster — what's actually different?"
- "When would you keep data in Redshift vs S3 + Spectrum?"
