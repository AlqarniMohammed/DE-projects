# Audit: Disposition of the Original 30-Project Plan

> Verdict key:
> **ABSORB** — the material becomes part of a spine phase increment (re-scoped, with a learning on-ramp).
> **SATELLITE** — survives as a standalone portfolio project inside a phase (re-scoped).
> **LAB** — shrinks to a guided exercise inside a phase (not a standalone repo).
> **DROP** — removed; reason given.
>
> Phases refer to the new framework: P0 Orientation · P1 Foundations · P2 AWS Lakehouse Core · P3 Spark & Databricks · P4 Orchestration & Ingestion · P5 Streaming · P6 Production & Serving.

| # | Original project | Verdict | Where | Reason |
|---|------------------|---------|-------|--------|
| 1 | The Laptop Lakehouse (DuckDB/PyIceberg/MinIO) | **ABSORB** | P1 spine v0 | This *is* the local lakehouse start — but it was the project that overwhelmed. Re-scoped into 3 smaller steps with a terminology on-ramp (Parquet → DuckDB → Iceberg), MinIO deferred. |
| 2 | dbt from Zero on Hacker News | **SATELLITE** | P1 | Excellent first dbt project; survives nearly intact with a lighter dataset option and a dbt-concepts primer first. |
| 3 | GitHub Archive Mart (incremental dbt) | **ABSORB** | P2 spine | Incremental models + idempotent backfills matter, but as a spine increment on the AWS lakehouse, not a separate 150 GB project. |
| 4 | Testing Reality with dbt + GE | **ABSORB** | P6 spine | Layered data-quality strategy belongs in the production phase, applied to the spine's own tables — not an 80 GB one-off. |
| 5 | First S3 Lakehouse with Athena | **ABSORB** | P2 spine | This is literally the spine's move to AWS (S3 + Glue Catalog + Athena + dbt-athena). |
| 6 | Iceberg vs Delta Bake-Off | **SATELLITE** | P3 | One of the strongest originals: differentiated, benchmark-driven, interview gold. Re-scoped to a smaller dataset. |
| 7 | PySpark on Databricks Community | **ABSORB** | P3 learn/build | PySpark fundamentals are P3's core learning block (on Databricks Free Edition); doesn't need to be a separate repo. |
| 8 | Delta Lake ACID & Time Travel | **ABSORB** | P3 labs | Exactly the Databricks cert's densest zone — becomes structured cert-prep labs. |
| 9 | Spark Performance Forensics | **SATELLITE** | P3 | Strong survivor: before/after tuning forensics is a rare, high-signal portfolio piece. |
| 10 | Delta Live Tables Medallion | **ABSORB** | P3 labs | DLT has been rebranded **Lakeflow Spark Declarative Pipelines** and is heavily tested on the current (May 2026) Databricks exam; Databricks **Free Edition** (Community Edition's successor) supports 1 active declarative pipeline — enough for the labs. |
| 11 | dbt-on-Databricks | **DROP** | — | dbt cert was cut from the milestones; adapter portability is a stretch note in P3, not a week of life. |
| 12 | Unity Catalog & Lineage | **ABSORB** | P3 labs | Cert topic; scaled down to governance labs on the Databricks environment. |
| 13 | Glue + Athena Production Pattern | **ABSORB** | P2 spine | Core spine increment: first real Glue ETL job feeding the lakehouse. |
| 14 | Cost-Aware Athena Mart | **SATELLITE** | P2 | Survivor: per-model cost accounting is a standout artifact and deeply DEA-relevant. Re-scoped dataset. |
| 15 | Redshift + Spectrum Hybrid | **SATELLITE** | P4 | DEA needs Redshift hands-on; scoped to Redshift Serverless free-trial posture + Spectrum join demo. |
| 16 | S3 Tables: Native Iceberg | **ABSORB** | P2 spine | The spine's table layer decision (S3 Tables vs self-managed Iceberg) — evaluated and adopted in-place. |
| 17 | Kinesis Firehose to Lakehouse | **ABSORB** | P5 spine | The spine's first streaming path. |
| 18 | EMR Serverless + DMS CDC | **ABSORB** | P4 spine | CDC ingestion increment on the spine (DMS + RDS); EMR piece scoped to one job. |
| 19 | Airflow on MWAA | **ABSORB** | P4 spine | Orchestration increment — but run Airflow locally/Docker (MWAA's ~$350+/mo baseline breaks the budget); MWAA stays exam-theory + short-lived lab. |
| 20 | Dagster Software-Defined Assets | **SATELLITE** | P4 | Survivor: Airflow-vs-Dagster comparison on the same pipeline is a senior-level conversation piece and feeds the spine's orchestrator decision. |
| 21 | Kafka on MSK | **ABSORB** | P5 spine/labs | Kafka fundamentals locally (Docker/Redpanda); MSK as exam theory + costed short lab. |
| 22 | Debezium CDC: Postgres → Iceberg | **SATELLITE** | P5 | Survivor: the DMS-vs-Debezium comparison (with #18) is the strongest interview artifact in the streaming phase. |
| 23 | Flink Streaming Analytics | **LAB** | P5 | Flink at AWARE depth: a guided Flink SQL lab. A full stateful-streaming project overshoots the 12-month, employability-weighted scope. |
| 24 | dlt + Great Expectations Ingest | **ABSORB** | P4 spine | dlt becomes the spine's API-ingestion increment; the GE half moves to P6. |
| 25 | CI/CD for a Lakehouse dbt Project | **ABSORB** | P6 spine | CI/CD applied to the spine's own dbt project — higher value than a fresh dataset. |
| 26 | OpenLineage End-to-End | **LAB** | P6 | Lineage demonstrated with a lightweight backend (e.g., Marquez quickstart) on spine pipelines; full DataHub deployment is overkill solo. |
| 27 | Terraform the Whole Stack | **ABSORB** | P6 spine | IaC increment: codify the spine's core AWS resources (scoped, not "everything"). |
| 28 | Data Contracts in CI | **LAB** | P6 | Contracts enforced on one spine mart in CI; a full Common Crawl project is unnecessary to learn the pattern. |
| 29 | Cost & Observability Control Plane | **ABSORB** | P6 spine | Observability increment on the spine (CloudWatch + budget alarms + a small dashboard). |
| 30 | Capstone: Real-Time Lakehouse | **ABSORB** | P6 capstone | The spine **is** the capstone — built all year instead of assembled in week 30. P6 finishes with integration polish + demo video + portfolio README. |

## Summary

- **Absorbed into spine:** 1, 3, 4, 5, 7, 8, 10, 12, 13, 16, 17, 18, 19, 21, 24, 25, 27, 29, 30
- **Survive as satellites (7):** 2 (first dbt project), 6 (Iceberg vs Delta), 9 (Spark forensics), 14 (cost-aware mart), 15 (Redshift hybrid), 20 (Dagster vs Airflow), 22 (Debezium vs DMS) — plus one **new** satellite the old plan lacked: the Tweeq-style ClickHouse + Superset serving layer (P6).
- **Labs:** 23 (Flink), 26 (lineage), 28 (contracts)
- **Dropped:** 11 (dbt-on-Databricks)

## Structural faults of the original plan (why it wasn't kept as-is)

1. **No learning layer.** Every week budgeted 6–10 h of pure build; zero hours for courses, reading, or terminology — the direct cause of the Week-1 overwhelm.
2. **Calendar-gated, not competency-gated.** Falling behind one week cascaded; there was no "advance when ready."
3. **30 unique datasets** was a vanity constraint that added setup cost every single week without learning value.
4. **Cert coverage was asserted, not planned** — no study blocks, no exam timing, and it targeted a dbt cert by a name that needed verification.
5. **Cost blind spots** — e.g., weekly MWAA/MSK usage doesn't fit a ~$20/week posture without aggressive teardown discipline the plan only mentioned in passing.
6. **LinkedIn-post-per-week** turned publishing into pressure; per-phase publishing keeps the build-in-public benefit without the treadmill.
