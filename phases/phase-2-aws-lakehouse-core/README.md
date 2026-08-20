# Phase 2 — The AWS Lakehouse Core

**Duration:** months 3–4 · **Budget:** ~70 hours · **AWS cost:** target ≤ $25/mo (S3 pennies, Athena $5/TB scanned, Glue job minutes; teardown discipline for everything else)

The spine moves to AWS — the same lakehouse, now on the services the DEA-C01 tests and the pattern the UK Ministry of Justice runs in production (S3 + Iceberg + Athena + dbt — see [`sources/research/platform-journeys.md`](../../sources/research/platform-journeys.md) for their potholes, which you will hit too).

## Objectives

1. Operate the **S3 + Glue Catalog + Athena** trifecta — the cheapest production lakehouse on AWS.
2. Adopt **S3 Tables** (managed Iceberg) as the curated layer and understand what maintenance it automates.
3. Feel Athena's **cost mechanics** in dollars (partitioning, Parquet, scanned bytes).
4. Ship **incremental dbt models with idempotent backfills** against a cloud engine.
5. Start DEA-C01 prep in stride (course tranche 1).

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P2]`

Object storage semantics · S3 Tables · Glue's three faces · Athena · dbt adapters · partition projection · CTAS · Lake Formation · data zones · compaction/small files · snapshot expiration · backfill.

## Learn (~22 h)

| Resource | Scope | Hours |
|---|---|---|
| Maarek/Kane DEA-C01 course (owned) — **tranche 1** | Storage, Glue, Athena, Lake Formation, migration/S3 sections; 1.5× on SAA overlap | 10 |
| [AWS Glue Immersion Day](https://catalog.workshops.aws/glue-immersion-day/en-US) | Crawlers + one ETL job lab (~$5–10 spend) | 4 |
| [S3 Tables / SageMaker Lakehouse walkthrough](https://builder.aws.com/content/2voduyQmGbAaMbTC0O5pieY5CkK/getting-started-with-amazon-sagemaker-lakehouse) + [Iceberg-on-AWS prescriptive guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html) | Read + follow along | 4 |
| [dbt-athena adapter docs](https://docs.getdbt.com/reference/resource-configs/athena-configs) | Incremental strategies (`insert_overwrite`, `merge`), workgroups | 2 |
| SageMaker Lakehouse rebrand reading | Know the umbrella diagram — Glue/Athena/Redshift/EMR as engines over one Iceberg lakehouse | 1 |
| dbt Fusion engine — what/why reading | Awareness (Athena adapter support was "planned" as of research date — verify) | 1 |

*Before starting, re-verify:* S3 Tables regional availability & pricing; dbt-athena current incremental strategy support; Athena Iceberg-version support (v3 was unsupported as of research date).

## Build — Spine v1: the lakehouse on AWS (~30 h)

1. **Zones:** `raw` and `curated` S3 buckets (versioning, lifecycle rules, SSE). Migrate the Phase-1 ingest to land in `raw/` (same idempotent partitioned layout).
2. **Catalog:** Glue Crawler builds the raw tables; then *replace* the crawler with explicit DDL and understand why teams often do (drift control). Register everything in the Glue Data Catalog.
3. **Curated layer on S3 Tables:** create a table bucket; write the cleaned taxi data as managed Iceberg via a small **Glue ETL job** (PySpark — your first cloud Spark, gently). Observe what S3 Tables automates: compaction, snapshot expiry. Repeat the Phase-1 schema-evolution drill *on the managed table*.
4. **Transform:** point the **same dbt project** at Athena (dbt-athena target). Convert `fct_trips` to an **incremental** model; implement `make backfill START=... END=...` and prove idempotency by running it twice and diffing row counts.
5. **Cost telemetry:** Athena workgroup with per-query scanned-bytes limit + query metrics; a `cost_report.py` that prints scanned-bytes per dbt model. Screenshot the partitioned-vs-unpartitioned query cost delta for the README (the classic 28 GB → 240 MB moment).
6. **Governance (scoped):** Lake Formation grants for a read-only "analyst" principal on curated tables only.
7. **Interim scheduling:** a GitHub Actions workflow runs ingest + `dbt build` nightly (the MoJ pattern) — real orchestration arrives in Phase 4; feel the *absence* first.
8. **Ops guardrails:** `make destroy` for anything chargeable; budget alarm verified monthly.

**AI rule:** let Claude Code write boilerplate (IAM policy JSON, workflow YAML); hand-write the Glue job's transform logic and every dbt incremental config.

## Build — Satellite S2: the cost-aware Athena mart (~12 h)

*(Recycled from old plan Week 14, re-scoped smaller.)* Separate repo, fresh dataset (SEC EDGAR financial statements or NYC 311 both work; pick ~5–10 GB). Build a small dbt-athena mart where **every model is tagged with its dollar cost per build** — a `MODEL_COST_REPORT.md` leaderboard, then one partitioning fix shown halving the top model's cost. This artifact interviews extremely well ("I can tell you what my pipeline costs to run").

## Competency gate G2

- [ ] **Named artifact:** spine on AWS — nightly GitHub Actions run green; `dbt build` against Athena; README updated with AWS architecture diagram + cost section.
- [ ] Backfill idempotency demo (run twice, counts identical).
- [ ] Schema-evolution drill on S3 Tables narrated in 2 minutes.
- [ ] Satellite cost leaderboard published.
- [ ] Monthly AWS bill ≤ $25 with evidence (billing screenshot in PROGRESS.md).
- [ ] **Retrieval checkpoint:** 10 random `[P0]`+`[P1]` terms + 15 `[P2]` terms (≥80%).
- [ ] DEA course tranche 1 finished.

## Publish checkpoint

Post: the cost story — "Partitioning cut this query's scan by 99%. Same query, same answer, 1% of the cost," with the two Athena screenshots.

## Interview questions you can now answer

- "Design a cheap analytics platform on AWS for ~100 GB/day." 
- "Glue Crawler vs explicit DDL — trade-offs?"
- "How does Athena pricing work and how do you control it?"
- "What table maintenance does a lakehouse need and who does it in your design?"
