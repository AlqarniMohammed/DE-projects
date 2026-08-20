# Phase 2 — AWS Lakehouse Core ⭐ Cert Phase 1

**Duration:** months 3–5 (elastic — the gate decides) · **Budget:** ~95 hours (DEA prep is woven through the phase — the build *is* most of the prep, and practice-exam time is counted honestly below) · **AWS cost:** target ≤ $25/mo (S3 pennies, Athena $5/TB scanned, Glue job minutes; teardown discipline for everything else) + exam $150 + Tutorials Dojo $15

Your lakehouse moves to AWS. Same project, real cloud — the exact services the DEA-C01 exam tests. The phase ends with the **AWS DEA-C01** exam; blueprint and timing rationale: [CERTS.md](../../reference/CERTS.md).

## Objectives

1. Operate the **S3 + Glue Catalog + Athena** trifecta — the cheapest production lakehouse on AWS.
2. Adopt **S3 Tables** (managed Iceberg) as the curated layer and understand what maintenance it automates.
3. Feel Athena's **cost mechanics** in dollars (partitioning, Parquet, scanned bytes).
4. Ship **incremental dbt models with idempotent backfills** against a cloud engine.
5. Test pipelines like a software engineer: pytest + moto, CI-gated.
6. **Pass AWS DEA-C01** at the gate.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P2]`

Object storage semantics · S3 Tables · Glue's three faces · Athena · dbt adapters · partition projection · CTAS · Lake Formation · data zones · compaction/small files · snapshot expiration · backfill.

## Learn (~43 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Maarek/Kane DEA-C01 Udemy course](https://www.udemy.com/course/aws-data-engineer/) (~$15–20 on sale) — **tranche 1** | Storage, Glue, Athena, Lake Formation, migration/S3 sections; skim familiar sections at 1.5× | 10 | Platform build steps 1–6: you operate every service you just watched |
| Maarek/Kane course — **tranche 2** | Orchestration, Kinesis/streaming, DMS, Redshift, security, ops sections (theory now; hands-on depth arrives in P4, post-exam) | 10 | The two exam mini-labs + Tutorials Dojo domain sets |
| **PySpark DataFrame basics** — [official quickstart](https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_df.html) | select/filter/withColumn/write — exactly what the Glue job needs, nothing more (real Spark depth is P3) | 2 | Build step 3: you hand-write the Glue job's transform |
| [AWS Glue Immersion Day](https://catalog.workshops.aws/glue-immersion-day/en-US) | Crawlers + one ETL job lab (~$5–10 spend) | 4 | Build steps 2–3 (crawler→DDL swap, the Glue ETL job) |
| [S3 Tables / SageMaker Lakehouse walkthrough](https://builder.aws.com/content/2voduyQmGbAaMbTC0O5pieY5CkK/getting-started-with-amazon-sagemaker-lakehouse) + [Iceberg-on-AWS prescriptive guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html) | Read + follow along | 4 | Build step 3 + the schema-evolution drill on the managed table |
| [dbt-athena adapter docs](https://docs.getdbt.com/reference/resource-configs/athena-configs) | Incremental strategies (`merge` is Iceberg-only; `insert_overwrite` is for Hive tables), workgroups | 2 | Build step 4: the incremental model + `make backfill` idempotency proof |
| [Apache Polaris](https://polaris.apache.org/) — what an Iceberg REST catalog is | 1-hour read; Glue/S3 Tables covers the doing | 1 | One-paragraph note in `notes/` (the REST-catalog concept returns in P5) |
| SageMaker Lakehouse rebrand reading · dbt Fusion engine what/why | Umbrella diagram + awareness (verify Athena adapter status) | 2 | Half-page note in `notes/` + one written `SELF-CHECK.md` answer |
| [Tutorials Dojo DEA-C01 practice exams](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) ($15) | Final 3 weeks of the phase; ≥80% on timed sets before booking | 8 | The exam itself — book only at ≥80% timed |

*Before starting, re-verify:* S3 Tables regional availability & pricing; dbt-athena current incremental-strategy and S3 Tables catalog support (see build step 4); Athena Iceberg-version support; the DEA-C01 exam guide (~6 weeks before your target booking date).

## Build — Platform v1: the lakehouse on AWS (~30 h)

1. **Zones:** `raw` and `curated` S3 buckets (versioning, lifecycle rules, SSE). Migrate the Phase-1 ingest to land in `raw/` (same idempotent partitioned layout).
2. **Catalog:** Glue Crawler builds the raw tables; then *replace* the crawler with explicit DDL and understand why teams often do (drift control). Register everything in the Glue Data Catalog.
3. **Curated layer on S3 Tables:** create a table bucket; write the cleaned taxi data as managed Iceberg via a small **Glue ETL job** (hand-written PySpark, scoped small: read raw Parquet, cast types, dedupe, write Iceberg — ~40 lines; the basics row above covers every call you need). Observe what S3 Tables automates: compaction, snapshot expiry. Repeat the Phase-1 schema-evolution drill *on the managed table*.
4. **Transform:** point the **same dbt project** at Athena (dbt-athena target). **The catalog pattern, stated plainly:** dbt *reads* the S3 Tables curated layer through Athena's federated `s3tablescatalog` (a one-time integration with AWS analytics services), and *materializes* marts as **Iceberg tables in the regular Glue catalog**. (Materializing directly *into* S3 Tables needs dbt-athena ≥ the July 2026 release via `catalog_type: s3_tables` + catalogs.yml — an advanced variant; pin the adapter version if you try it.) Convert `fct_trips` to an **incremental** model; implement `make backfill START=... END=...` and prove idempotency by running it twice and diffing row counts. Carry the P1 snapshot (SCD2 `dim_zones`) over and note in `MODELING.md` what changed on AWS.
5. **Cost telemetry:** Athena workgroup with per-query scanned-bytes limit + query metrics; a `cost_report.py` that prints scanned-bytes per dbt model *(hint: `GetQueryExecution` statistics expose `data_scanned_in_bytes`; tag each model's queries via dbt's `query_comment` to attribute bytes to models)*. Two micro-drills inside this step, both feeding the cost story: run one explicit **CTAS** in Athena and read its cost; convert one table to **partition projection** and show the metadata-lookup difference. Screenshot the partitioned-vs-unpartitioned query cost delta for the README — expect a 10–100× scan reduction on the platform's data (the S2 satellite's 5–10 GB dataset is where the dollars get visible).
6. **Governance (scoped):** Lake Formation grants for a read-only "analyst" principal on curated tables only.
7. **Interim scheduling:** a GitHub Actions workflow runs ingest + `dbt build` nightly — real orchestration arrives in Phase 4; feel the *absence* first. CI is **test-gated**: the pytest suite (below) must pass before the nightly build runs. **Authenticate via GitHub's OIDC federation to a scoped IAM role** (`aws-actions/configure-aws-credentials`) — never long-lived keys, not even in repo secrets.
8. **Ops guardrails:** `make destroy` for anything chargeable; budget alarm verified monthly.

**AI rule:** let your assistant write boilerplate (IAM policy JSON, workflow YAML); hand-write the Glue job's transform logic, every dbt incremental config, and the tests below.

### Prove-it assignment (half-day): pipeline testing with pytest + moto

The phase's software-engineering proof — job specs increasingly filter on this: unit tests for the ingester with **moto** mocking S3 (upload path, idempotent re-run, partition layout), plus one integration test that runs the dbt project against a DuckDB fixture. Wire both into the GitHub Actions workflow so a red test blocks the nightly run. Done = `pytest` green in CI, badge in the README.

### Exam mini-labs (~6 h, same-day teardown) — Domain 1 & 2 anchors

These exist so DEA Domain 1/2 answers come from muscle memory, not flashcards. The *deep* builds stay in Phase 4, after the exam.

- **Kinesis mini-lab (~3 h, ≤$3):** one Data Stream + one Firehose delivery stream to S3; put records with the CLI; watch buffering hints work; note where Streams ends and Firehose begins. `make destroy` the same day.
- **Redshift Serverless taste (~3 h, free credits):** create a workgroup, load one small table, `CREATE EXTERNAL SCHEMA` over your curated S3 data (Spectrum), run one federated query, read its `EXPLAIN`; note DISTKEY/SORTKEY concepts against your cloud-storage knowledge. Teardown after.

## Build — Satellite S2: the cost-aware Athena mart (~12 h)

Separate repo, fresh dataset — pick from the S2 menu in [`DATASETS.md`](../../reference/DATASETS.md) (SEC EDGAR, NYC 311, or a Saudi Open Data portal dataset; ~5–10 GB). Build a small dbt-athena mart where **every model is tagged with its dollar cost per build** — a `MODEL_COST_REPORT.md` leaderboard, then one partitioning fix shown halving the top model's cost. Few builders can say "I know what my pipeline costs to run" — after this, you can. Want a unique, realistic brief instead? Use the `/satellite-brief` skill or [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Competency gate G2 ⭐

- [ ] **AWS DEA-C01 — passed.** (Book only after ≥80% on Tutorials Dojo timed sets; both Maarek tranches done.)
- [ ] **Named artifact:** platform on AWS — nightly GitHub Actions run green (test-gated); `dbt build` against Athena; README updated with AWS architecture diagram + cost section.
- [ ] Backfill idempotency demo (run twice, counts identical).
- [ ] Schema-evolution drill on S3 Tables narrated in 2 minutes.
- [ ] pytest + moto suite green in CI.
- [ ] Exam mini-labs done **and torn down** (Kinesis ≤$3 · Redshift free credits).
- [ ] Satellite cost leaderboard (`MODEL_COST_REPORT.md`) published.
- [ ] Monthly AWS bill ≤ $25 with evidence (billing screenshot linked in PROGRESS.md).
- [ ] **External critique requested:** phase artifact posted to r/dataengineering, dbt Slack, or DataTalksClub Slack — request thread linked in PROGRESS.md (the ask is the gate; responses are a bonus).
- [ ] `SELF-CHECK.md` updated: 3–5-sentence written answers to this phase's check-yourself questions, evidence linked.
- [ ] **Retrieval checkpoint:** all `[P2]` terms + 10 random earlier terms, ≥80% (the `/quiz` skill runs this).
- [ ] Both phase posts published (see below).

## Publish checkpoint

Two posts this phase (any public platform): (1) the cost story — "Partitioning cut this query's scan by 99%. Same query, same answer, 1% of the cost," with the two Athena screenshots; (2) the DEA-C01 announcement with honest prep notes (what the build taught vs what needed the course).

## Check yourself — questions you can now answer

- "Design a cheap analytics platform on AWS for ~100 GB/day."
- "Glue Crawler vs explicit DDL — trade-offs?"
- "How does Athena pricing work and how do you control it?"
- "What table maintenance does a lakehouse need and who does it in your design?"
- "Kinesis Data Streams vs Firehose — where does each fit?"
- "How do you test a pipeline before it ships?"

---
← [Phase 1 — Foundations](../phase-1-foundations/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 3 — Spark & Databricks →](../phase-3-spark-databricks/README.md)**
