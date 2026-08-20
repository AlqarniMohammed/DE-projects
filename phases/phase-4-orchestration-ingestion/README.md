# Phase 4 — Orchestration & Ingestion

**Duration:** months 7–8 · **Budget:** ~72 hours · **AWS cost:** ≤ $25/mo discipline: Airflow runs **locally**, RDS/DMS/Kinesis labs are short-lived with `make destroy` and per-lab caps below

No exam this phase — you already passed both. Kinesis, DMS, and Redshift arrive as services you've answered exam questions about and now operate for real, with no prep clock running. The platform grows a real orchestrator and three ingestion modes (API, CDC, streaming-lite); this is where it starts reading as production.

## Objectives

1. **Airflow 3.x** production patterns: assets, DAG versioning, sensors, retries, alerts — many small idempotent DAGs, never a mega-DAG.
2. Declarative ingestion with **dlt** (API sources, incremental cursors, merge dispositions).
3. **CDC on AWS** with DMS from a live RDS Postgres into the lakehouse.
4. AWS streaming ingest: **Kinesis Data Streams vs Firehose**, landing into Iceberg — deepening the P2 mini-lab into a real pipeline.
5. Redshift + Spectrum working knowledge (the satellite goes deeper than the P2 taste lab).
6. **Secrets handled like production:** no credential in code or git, ever.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P4]`

Orchestrator vs cron · DAG · Airflow 3 (assets, DAG versioning) · task-based vs asset-based · sensor/trigger · XCom · MWAA · dlt · **CDC** · DMS · Kinesis Streams vs Firehose · Step Functions/EventBridge · Redshift/Spectrum/Serverless · DISTKEY/SORTKEY · secrets backend.

## Learn (~20 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Astronomer Academy Airflow 101](https://academy.astronomer.io/path/airflow-101) + [DAG Authoring path](https://academy.astronomer.io/path/airflow-dag-authoring) (free, Airflow-3-native) | Both paths | 12 | Build step 1 (the small-DAGs migration) + the DAG-integrity test assignment |
| [dlt docs](https://dlthub.com/docs/intro) — REST source tutorial + incremental loading | Working level | 4 | Build step 3: the dlt source + the written dlt-vs-hand-rolled comparison |
| Connector-ELT positioning: skim [Airbyte](https://docs.airbyte.com/) / [Fivetran](https://fivetran.com/docs/getting-started) / [Sling](https://docs.slingdata.io/) landing docs | Where managed connectors beat code, and vice versa | 0.5 | One-paragraph positioning note in `notes/`, written next to the dlt comparison |
| [Glue vs EMR](https://docs.aws.amazon.com/emr/) — when a team picks EMR/EMR Serverless | 1-hour read; Glue stays the hands-on vehicle | 1 | A written Glue-vs-EMR decision note in `notes/` |
| MWAA current state reading | Now runs Airflow 3.x — know the managed trade-offs + cost | 1 | The MWAA lab (build step 7) + its ops-differences note |
| [Airflow secrets backend docs](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/secrets-backends/aws-ssm-parameter-store.html) — SSM Parameter Store | Read before build step 2 | 1 | Build step 2: the SSM-backed connections wiring |

*Before starting, re-verify:* Airflow current minor (3.3.x at research date), MWAA supported versions, Redshift Serverless free-credit terms.

## Build — Platform v2: orchestrated, multi-mode ingestion (~38 h)

Each chargeable lab lists its **cost cap and teardown deadline** — check the AWS billing page mid-phase, not just at the gate.

1. **Airflow 3 locally** (Astro CLI or Docker Compose). Migrate the GitHub-Actions schedule into **small, single-purpose DAGs**: `ingest_taxi`, `dbt_build`, `data_checks` — retries, a **Deadline Alert** (Airflow 3's replacement for the removed SLA feature: a freshness expectation with a callback), Slack (or email) failure alerts, one asset-triggered dependency (dbt runs when ingest's asset updates). Pass one small value (the processed date/path) between `ingest_taxi` and `dbt_build` via **XCom** — and assert it in the DAG-integrity suite below (XCom is for values, never datasets). Keep the Actions workflow as CI only.
2. **Secrets increment (~2–3 h):** wire Airflow's connections to the **AWS SSM Parameter Store secrets backend** — RDS password, Slack webhook, API keys all live there, none in `airflow.cfg`, env files, or git. The P0 `gitleaks` pre-commit hook has guarded the repo since day one; this is where the *runtime* side becomes production-shaped. A question you can now answer cold: "how do your DAGs get credentials?"
3. **dlt increment:** add a second source to the platform — a public REST API (weather for taxi-demand enrichment works nicely) — via **dlt** with incremental cursor + merge disposition, landing in raw and flowing through dbt. Compare: dlt config vs the hand-rolled Phase-1 downloader (line count, schema handling, retries).
4. **CDC increment** *(cap ≤ $8 · teardown ≤ 5 days after first CDC event — the demo records in 2–3 days, and 10 days of RDS+DMS blows the cap)*: seed a small **RDS Postgres** OLTP database → **DMS** full-load + CDC to S3 → MERGE into an Iceberg silver table (Glue job or Athena MERGE) → downstream dbt marts. Prove: an UPDATE in Postgres is visible in Athena in minutes. **Record the demo, then tear down RDS/DMS.**
   **The seeded OLTP spec (P5 reuses this unchanged — build it to spec):** ≥3 related tables (e.g., bookings, customers, listings); a generator emitting a steady transaction mix of roughly **70% inserts / 20% updates / 10% deletes**; one command that adds a column mid-run (the schema-change drill); keep generator + schema in the platform repo. Menu of scenario flavors: the S5 section of [`DATASETS.md`](../../reference/DATASETS.md).
5. **Streaming-lite increment** *(cap ≤ $5 · teardown same day as demo)*: EventBridge-scheduled Lambda polls a live feed (Citi Bike GBFS or similar) → **Kinesis Data Streams → Firehose → Iceberg/S3**, partitioned; Athena queries fresh rows. The P2 mini-lab configured the plumbing once; this time it's a real pipeline with a consumer.
6. **AWS micro-orchestration lab (1 day, ~$1):** one Step Functions state machine + EventBridge rule doing a mini-pipeline — know when this beats Airflow.
7. **MWAA lab** *(cap ~$10–15 · teardown same day)*: spin up the smallest MWAA env, deploy one DAG, note the ops differences.

**AI rule:** your assistant may generate operator boilerplate and setup scripts; hand-write DAG structure, dlt source config, the secrets-backend wiring, and the MERGE logic.

### Prove-it assignment (2–3 h): DAG integrity tests

A pytest suite CI runs on every PR: all DAGs import cleanly (no top-level heavy code), every DAG has retries + owner set, no task is orphaned, the XCom handoff from build step 1 carries the expected value, and one DAG-level unit test with a mocked operator. The standard Airflow testing pattern — and the reason a broken DAG never reaches the scheduler.

## Build — Satellites (~12 h)

**S4a — Redshift + Spectrum hybrid** *(cap = free credits · teardown after demo)*: Redshift **Serverless** + Spectrum external schema over your S3 curated data; dbt-redshift builds one mart joining native + Spectrum tables; `EXPLAIN` screenshot proving the federated plan; cost note vs all-Redshift.

**S4b — Dagster vs Airflow**: [Dagster University Essentials](https://courses.dagster.io/) (free, ~6 h) → rebuild ONE platform pipeline as software-defined assets with `dagster-dbt` → `COMPARISON.md` across **four fixed axes, one concrete code-diff example each**: authoring model (task graph vs asset graph) · backfill story · local dev loop · dbt integration. A senior-level conversation piece.

Unique briefs for either satellite: the `/satellite-brief` skill or [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Competency gate G4

- [ ] **Named artifact:** the orchestrated platform — Airflow UI showing green multi-DAG runs with a deliberate failure + retry + alert demonstrated on video.
- [ ] Secrets demo: a DAG pulls its credentials from SSM Parameter Store; `gitleaks` pre-commit shown catching a planted secret.
- [ ] dlt source live in the platform (weather flowing through dbt) + the written dlt-vs-hand-rolled comparison.
- [ ] CDC demo recorded: Postgres UPDATE → visible in Athena · RDS/DMS torn down on deadline.
- [ ] Kinesis path demo recorded · torn down.
- [ ] DAG-integrity pytest suite green in CI.
- [ ] Both satellites' artifacts published (`EXPLAIN` proof · `COMPARISON.md`).
- [ ] Bill check: the month's AWS spend ≤ $25 despite the labs (evidence in PROGRESS.md) · mid-phase billing check done.
- [ ] **External critique requested:** comparison or CDC artifact posted — request thread linked.
- [ ] `SELF-CHECK.md` updated with this phase's written answers.
- [ ] **Retrieval checkpoint:** all `[P4]` terms + 10 random earlier terms, ≥80%.
- [ ] Comparison post published (see below).

## Publish checkpoint

Post (any public platform): "I built the same pipeline in Airflow and Dagster — task graphs vs asset graphs, honestly compared."

## Check yourself — questions you can now answer

- "Design CDC from an operational Postgres into a lakehouse — managed and open-source options."
- "Kinesis Data Streams vs Firehose vs MSK — when each?"
- "How do you make a DAG safe to re-run?"
- "How do your DAGs get credentials?"
- "Airflow vs Dagster — what's actually different?"
- "When would you keep data in Redshift vs S3 + Spectrum?"

---
← [Phase 3 — Spark & Databricks](../phase-3-spark-databricks/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 5 — Streaming & CDC →](../phase-5-streaming/README.md)**
