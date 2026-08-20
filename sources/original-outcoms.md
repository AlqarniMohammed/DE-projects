# The 30-Project Data Engineering Execution Plan (2026)

## 1. Opening Auditor's Statement

Let me be blunt. These 30 projects will not make you a Principal Data Engineer in 30 weeks — that title takes scar tissue from production incidents you cannot manufacture solo. What they *will* do is close the specific gap diagnosed: you can model data but you cannot operate a Lakehouse. By Week 30 you will have shipped CDC pipelines, tuned Spark jobs, written dbt projects with CI, orchestrated DAGs and software-defined assets, governed an Iceberg lake, and managed it all via Terraform. That is enough to credibly interview as a mid-level Data Engineer at a serious shop and to pass all four target certs (SAA-C03, Databricks DE Associate, DEA-C01, dbt Foundational) with the projects themselves as your study lab. What it will *not* do: replace 5 years of on-call. Do not oversell it. Ship it, then earn the scars in your next role.

## 2. Skill & Tool Coverage Matrix

| Skill / Tool Family       | SAA-C03            | Databricks DE Associate | DEA-C01                   | dbt Foundational |
|---------------------------|--------------------|-------------------------|---------------------------|------------------|
| Advanced SQL              | —                  | 7, 8                    | 13, 14, 16                | 2, 3, 4          |
| Python / PySpark          | —                  | 7, 8, 9, 10, 11, 12     | 17, 18                    | —                |
| dbt (Core + Cloud)        | —                  | 11                      | 14, 16                    | 2, 3, 4, 5, 25   |
| Delta Lake                | —                  | 8, 9, 10, 11, 12        | 18                        | —                |
| Apache Iceberg            | 6                  | —                       | 16, 17, 30                | 5                |
| Parquet / Open Formats    | 1, 6               | 8                       | 13, 17                    | 5                |
| DuckDB / Polars           | —                  | —                       | —                         | 1, 2             |
| AWS S3 / Storage Tiering  | 5, 6, 25, 30       | —                       | 13, 17, 25, 30            | —                |
| AWS Glue (ETL + Catalog)  | 5, 6               | —                       | 13, 14, 17, 18, 30        | —                |
| AWS Athena / Trino        | 5, 6               | —                       | 13, 16, 17, 25, 30        | 5, 25            |
| AWS Redshift / Spectrum   | 15                 | —                       | 15, 25                    | 15               |
| AWS S3 Tables (Iceberg)   | 16                 | —                       | 16, 30                    | —                |
| Lake Formation / IAM      | 5, 6, 16           | —                       | 16, 30                    | —                |
| AWS DMS (CDC)             | —                  | —                       | 18, 30                    | —                |
| AWS Kinesis / Firehose    | 17                 | —                       | 17, 30                    | —                |
| AWS MSK / Kafka           | 21                 | —                       | 21, 22, 30                | —                |
| Debezium (CDC)            | —                  | —                       | 22, 30                    | —                |
| Apache Flink              | —                  | —                       | 23                        | —                |
| EMR Serverless            | 18                 | 18                      | 18                        | —                |
| Databricks Workflows / UC | —                  | 11, 12                  | —                         | —                |
| Delta Live Tables         | —                  | 10, 11                  | —                         | —                |
| Apache Airflow / MWAA     | 19                 | —                       | 19, 30                    | 19               |
| Dagster (SDA)             | —                  | —                       | 20, 30                    | 20               |
| dlt (ingestion)           | —                  | —                       | 24                        | 24               |
| Great Expectations        | —                  | —                       | 24                        | 24               |
| OpenLineage / DataHub     | —                  | —                       | 26                        | 26               |
| Terraform / IaC           | 27, 30             | —                       | 27, 30                    | —                |
| CI/CD for dbt             | —                  | —                       | 28                        | 28               |
| Data Contracts            | —                  | —                       | 28                        | 28               |
| Cost / Observability      | 29                 | 29                      | 29, 30                    | —                |

## 3. Dataset Inventory

| Week | Project Title                                  | Dataset                                  | Source                          | Approx Size | Why this dataset                                              |
|------|------------------------------------------------|------------------------------------------|---------------------------------|-------------|----------------------------------------------------------------|
| 1    | The Laptop Lakehouse                           | NYC TLC Yellow Taxi 2009–2024            | nyc.gov/tlc                     | ~50 GB Parquet | Canonical, partitioned, large enough to feel real on a laptop |
| 2    | dbt from Zero on Hacker News                   | Hacker News full archive (BigQuery dump) | bigquery-public-data            | ~5 GB JSON  | Rich relational structure; ideal for dbt staging→mart layering|
| 3    | The GitHub Archive Mart                        | GHArchive 2024                           | gharchive.org                   | ~150 GB JSON gz | Tests dbt incremental models at real scale on DuckDB         |
| 4    | Testing Reality with dbt + GE                  | Stack Overflow Public Dump               | archive.org/SO dump             | ~80 GB XML  | Messy real-world data exposes weak tests                      |
| 5    | First S3 Lakehouse with Athena                 | NOAA GHCN Daily Weather                  | noaa.gov/ghcn                   | ~30 GB CSV  | Time-series across millions of stations; great for partitioning|
| 6    | Iceberg vs Delta: A Bake-Off on a Laptop       | OpenStreetMap Planet (extract)           | planet.osm.org                  | ~20 GB PBF  | Schema evolution & nested data stress both formats            |
| 7    | PySpark on Databricks Community                | Reddit Pushshift comments (2023)         | files.pushshift.io / academic mirror | ~120 GB ZST | Forces partition tuning and skew handling                |
| 8    | Delta Lake ACID & Time Travel                  | IMDb Datasets (TSV)                      | datasets.imdbws.com             | ~2 GB TSV   | Slowly changing facts (ratings) — perfect for MERGE & travel  |
| 9    | Spark Performance Forensics                    | MovieLens 25M + tags                     | grouplens.org                   | ~1.5 GB CSV | Skewed joins (popular movies) make AQE/broadcast tangible     |
| 10   | Delta Live Tables Medallion                    | Spotify Charts (daily, global)           | kaggle/spotify-charts           | ~3 GB CSV   | Daily cadence ideal for DLT expectations and CDC into silver  |
| 11   | dbt-on-Databricks                              | Steam Game Reviews                       | kaggle/steam-reviews            | ~15 GB JSON | Bridges dbt skill into Databricks SQL warehouse               |
| 12   | Unity Catalog & Lineage                        | FRED Macroeconomic Series                | fred.stlouisfed.org             | ~2 GB CSV   | Many tables, clear domain — perfect for catalog governance    |
| 13   | Glue + Athena Production Pattern               | NYC 311 Service Requests                 | data.cityofnewyork.us           | ~25 GB CSV  | Real categorical, dirty municipal data — Glue jobs shine      |
| 14   | The Cost-Aware Athena Mart                     | SEC EDGAR Financial Statement Datasets   | sec.gov/dera                    | ~40 GB TSV  | Wide tables; cost optimization via partitioning is visible    |
| 15   | Redshift + Spectrum Hybrid Warehouse           | BLS Quarterly Census of Employment       | bls.gov/cew                     | ~10 GB CSV  | Naturally dimensional (NAICS × geography × time)              |
| 16   | S3 Tables: Native Iceberg on AWS               | World Bank Open Data (all indicators)    | data.worldbank.org              | ~5 GB CSV   | Schema evolution across decades = Iceberg's home turf         |
| 17   | Kinesis Firehose to the Lakehouse              | OpenWeather API (live capture)           | openweathermap.org              | ~1 GB/week  | True streaming source; ideal for Firehose → S3 → Iceberg      |
| 18   | EMR Serverless + DMS CDC                       | Chinook + custom RDS Postgres OLTP       | self-seeded on RDS              | ~500 MB     | CDC needs a live OLTP — Chinook seeded into RDS is the standard|
| 19   | Airflow on MWAA: Real DAGs                     | GTFS Static + Realtime (NYC MTA)         | mta.info/developers             | ~5 GB       | Daily static + 30s realtime feeds = perfect orchestration test |
| 20   | Dagster Software-Defined Assets                | eBird Basic Dataset                      | ebird.org/data                  | ~80 GB CSV  | Asset-oriented model fits species/region observations cleanly |
| 21   | Kafka on MSK: Event Backbone                   | Wikipedia EventStream (live)             | stream.wikimedia.org            | ~2 GB/day   | Free public Kafka-like stream; real velocity                  |
| 22   | Debezium CDC: Postgres → Iceberg               | OpenFoodFacts Postgres dump              | openfoodfacts.org               | ~10 GB      | Real schema with frequent updates — Debezium shines           |
| 23   | Flink Streaming Analytics                      | GDELT 2.0 Event Stream                   | gdeltproject.org                | ~1 GB/day   | True real-time geo-political event stream                     |
| 24   | dlt + Great Expectations: Trustworthy Ingest   | World Bank Climate Knowledge Portal API  | climateknowledgeportal.worldbank.org | ~2 GB | API-shaped source; dlt's REST helpers are made for this       |
| 25   | CI/CD for a Lakehouse dbt Project              | USDA Food Data Central                   | fdc.nal.usda.gov                | ~1 GB JSON  | Stable schema lets you focus purely on CI rigor               |
| 26   | OpenLineage End-to-End                         | NHTSA FARS Crash Data                    | nhtsa.gov/fars                  | ~3 GB CSV   | Multi-table joins make lineage diagrams non-trivial           |
| 27   | Terraform the Whole Stack                      | USGS Earthquake Catalog                  | earthquake.usgs.gov             | ~2 GB CSV   | Small enough to redeploy cheaply while testing Terraform      |
| 28   | Data Contracts in CI                           | Common Crawl WAT (single segment)        | commoncrawl.org                 | ~5 GB WARC  | Schema drift is the default — perfect contract testing ground |
| 29   | Cost & Observability Control Plane             | Hacker News Realtime API (live)          | hacker-news.firebaseio.com      | ~500 MB/wk  | Live ingest gives real ops signals to instrument              |
| 30   | The Capstone: A Real-Time Lakehouse Platform   | NYC Citi Bike Trip Data + Live GBFS Feed | citibikenyc.com/system-data     | ~30 GB + live | Combines batch history + live stream into one capstone        |

---

# Phase 1 — Weeks 1–6: SQL, Python, Lakehouse Foundations & dbt Fundamentals

## Week 1 — "The Laptop Lakehouse"

- **Phase:** 1
- **One-line pitch:** Stand up a fully local Lakehouse on your laptop using DuckDB, Parquet, and Iceberg to query 15 years of NYC taxi trips in seconds.
- **Primary new skill gained:** Operating a Lakehouse pattern (object storage + open table format + query engine) end-to-end without any cloud.
- **Secondary skills reinforced:** Parquet partitioning trade-offs, DuckDB tuning, advanced SQL window functions on >1B rows, Docker Compose for local infra.
- **Tool stack (3+ tools):** DuckDB, PyIceberg, MinIO (S3-compatible), Parquet, Docker Compose, Python.
- **Cert exam domains touched:** SAA-C03 — *Design Secure Architectures / Storage* (S3 mental model via MinIO); dbt Foundational — *Sources and Models* (you will register DuckDB as a dbt source next week).
- **Dataset:** NYC TLC Yellow Taxi 2009–2024, ~50 GB Parquet, from nyc.gov/tlc — canonical and partitioned, large enough to feel real.
- **Architecture in 3–5 lines:** Public Parquet on HTTP → ingested into MinIO via Python → registered as Iceberg tables via PyIceberg → queried by DuckDB with the Iceberg extension → results materialized into a local analytical view.
- **Concrete weekly deliverables:**
  1. GitHub repo: `docker-compose.yml` (MinIO + DuckDB CLI), `Makefile` (`make up`, `make ingest`, `make demo`), ingestion script, README with architecture diagram.
  2. `make demo` runs three benchmark queries against Iceberg-backed taxi data and prints timing.
  3. LinkedIn hook: "I just queried 1.7 billion taxi rides on my laptop in under 4 seconds — here's the local Lakehouse stack."
- **Wow-factor:** A terminal recording showing a 1.7B-row aggregation finishing in seconds, then a `git diff` showing the entire stack is ~100 lines of YAML and Python.
- **Stretch goal:** Add Polars as a second query engine and benchmark it against DuckDB on the same Iceberg tables.
- **Why this project (90 words):** You already know SQL; this week you learn what a Lakehouse *physically is* by building one with your hands. Most engineers entering DE in 2026 cannot articulate the difference between a warehouse and a Lakehouse — by Friday you will, because you operated one. It closes the "I've never touched object storage or an open table format" gap immediately, costs $0, and produces a `make demo` artifact that recruiters can run. This is the foundation the next 29 weeks build on.

## Week 2 — "dbt from Zero on Hacker News"

- **Phase:** 1
- **One-line pitch:** Build your first production-grade dbt project against DuckDB with staging→intermediate→marts layering and a full test suite on 18 years of Hacker News data.
- **Primary new skill gained:** The dbt project anatomy: sources, models, refs, tests, docs, exposures, and the staging/marts separation that actually scales.
- **Secondary skills reinforced:** Jinja templating, dbt macros, incremental materializations, DAG thinking, documentation-as-code.
- **Tool stack (3+ tools):** dbt-core, dbt-duckdb, DuckDB, Git, dbt-docs, pre-commit (sqlfluff).
- **Cert exam domains touched:** dbt Foundational — *Sources, Models, Tests, Documentation, Materializations* (covers ~60% of the exam blueprint in one project).
- **Dataset:** Hacker News full archive (BigQuery dump), ~5 GB JSON, from bigquery-public-data — rich relational structure (stories/comments/users) ideal for layered modeling.
- **Architecture in 3–5 lines:** HN JSON dump → loaded into DuckDB raw schema → dbt staging models normalize and clean → dbt marts produce `fct_engagement_daily`, `dim_users`, `dim_stories` → dbt docs generate a navigable DAG.
- **Concrete weekly deliverables:**
  1. Repo with `models/staging`, `models/intermediate`, `models/marts`, `dbt_project.yml`, `schema.yml` with 40+ tests, generated docs site committed to `gh-pages`.
  2. `dbt build && dbt docs serve` produces the lineage graph locally.
  3. LinkedIn hook: "I rebuilt 18 years of Hacker News into a dimensional model with 40+ data tests in a single dbt project. Here's what staging→marts actually buys you."
- **Wow-factor:** A screenshot of the dbt docs lineage graph showing 25+ models flowing cleanly from sources to a single mart, with green test results.
- **Stretch goal:** Add a custom generic test (e.g., `not_a_future_timestamp`) and publish it as a package.
- **Why this project (90 words):** dbt is the transformation layer for the next decade and the Foundational cert is the lowest-effort high-signal credential on your list. You can read the dbt docs in an afternoon, but you cannot internalize ref()-driven dependency management without building a non-trivial project. Hacker News is the ideal first dataset: relational enough to model, public enough to share, weird enough (deleted comments, missing parents) to force you to write real tests. By Friday you can defend every choice in a dbt project structure interview.

## Week 3 — "The GitHub Archive Mart"

- **Phase:** 1
- **One-line pitch:** Build an incremental dbt project on GHArchive that processes 150 GB of GitHub events into a developer-activity mart, with backfills and snapshots.
- **Primary new skill gained:** dbt **incremental models** and **snapshots** — the two materializations that separate toy projects from production ones.
- **Secondary skills reinforced:** Late-arriving data handling, surrogate keys with `dbt_utils`, partitioned incremental strategies, idempotent backfills.
- **Tool stack (3+ tools):** dbt-core, dbt-duckdb, dbt_utils, DuckDB, Python loader, GHArchive (gz JSON).
- **Cert exam domains touched:** dbt Foundational — *Incremental Models, Snapshots, Packages, dbt_utils*; DEA-C01 — *Data Store Management* (incremental ingestion patterns).
- **Dataset:** GHArchive 2024, ~150 GB JSON gz, from gharchive.org — hourly partitioned files that test incremental models at real scale.
- **Architecture in 3–5 lines:** Hourly GHArchive `.json.gz` files → Python downloader writes to local Parquet partitioned by date/hour → dbt source over Parquet via DuckDB external tables → incremental `fct_events` model with `unique_key` and `merge` strategy → snapshot table tracks user-repo membership changes.
- **Concrete weekly deliverables:**
  1. Repo with incremental models, snapshot definitions, a backfill script, dbt seeds for event-type lookup tables.
  2. `make backfill DATE_FROM=2024-01-01 DATE_TO=2024-01-07` produces a 7-day mart idempotently.
  3. LinkedIn hook: "150 GB of GitHub events, processed incrementally in dbt with idempotent backfills. Here's the unique_key pattern most tutorials skip."
- **Wow-factor:** Re-running `make backfill` twice and showing the row counts don't change — true idempotency, demonstrated.
- **Stretch goal:** Add a `dbt-osmosis`-style yaml propagation tool to auto-document columns across the project.
- **Why this project (90 words):** Incremental models are the single most-asked dbt interview topic and the most-failed cert question. You cannot fake this — you must build one, break it with a duplicate run, and fix it with `unique_key`. GHArchive at 150 GB is small enough to fit on your laptop but big enough that a full-refresh strategy is visibly wrong, forcing you into the right pattern. Combined with snapshots, this week converts dbt from "templated SQL" into "engineered SQL," which is the actual leap the Foundational cert tests.

## Week 4 — "Testing Reality with dbt + Great Expectations"

- **Phase:** 1
- **One-line pitch:** Stress-test the messiest public dataset you can find against a layered defense of dbt tests and Great Expectations suites — and let the failures teach you what to test.
- **Primary new skill gained:** **Data quality as a discipline** — knowing the difference between schema tests, distributional tests, freshness tests, and contract tests, and where each belongs.
- **Secondary skills reinforced:** Custom dbt generic tests, dbt_expectations package, GE checkpoints, CI integration of test results.
- **Tool stack (3+ tools):** dbt-core, dbt-duckdb, dbt-expectations, Great Expectations, DuckDB, GitHub Actions.
- **Cert exam domains touched:** dbt Foundational — *Tests, Generic Tests, Singular Tests*; DEA-C01 — *Data Quality and Validation*.
- **Dataset:** Stack Overflow Public Dump (Posts, Users, Comments, Votes XML), ~80 GB, from archive.org — gloriously messy with deleted users, orphaned comments, encoding issues.
- **Architecture in 3–5 lines:** SO XML dump → Python parser into Parquet → dbt staging with `unique`, `not_null`, `accepted_values`, `relationships` tests → dbt-expectations for distributional tests → GE checkpoint runs nightly via GitHub Actions on a sampled extract.
- **Concrete weekly deliverables:**
  1. Repo with ~80 tests across dbt and GE, a `tests/` directory of custom singular tests, GE expectations suites in version control, GitHub Actions CI run on every PR.
  2. A `data_quality_report.md` artifact generated on each CI run summarizing pass/fail counts and severity.
  3. LinkedIn hook: "I ran 80 data quality checks against 80 GB of Stack Overflow data. Half of them failed on the first run. Here's what I learned about layered testing."
- **Wow-factor:** A side-by-side comparison: "dbt tests caught 23 issues. GE caught 17 more. Here's where each tool earned its keep."
- **Stretch goal:** Wire failed test results into a Slack webhook via the dbt `on-run-end` hook.
- **Why this project (90 words):** Anyone can write `unique` and `not_null`. Almost nobody builds a *layered* data quality strategy distinguishing what dbt tests well (constraints, referential integrity) from what GE tests well (distributions, schemas, profiles). This week makes you fluent in that distinction — which is the difference between a junior and a mid-level data engineer in any interview loop. The dataset is intentionally messy so that the tests *fail*, forcing you to confront real triage decisions instead of admiring a green CI run on toy data.

## Week 5 — "First S3 Lakehouse with Athena"

- **Phase:** 1
- **One-line pitch:** Promote your laptop Lakehouse to AWS: land 30 GB of weather data in S3, register it in Glue Data Catalog, and query it with Athena — for under $5.
- **Primary new skill gained:** The **AWS S3 + Glue Catalog + Athena trifecta** — the cheapest production Lakehouse pattern on AWS and a DEA-C01 exam centerpiece.
- **Secondary skills reinforced:** S3 partitioning conventions, Glue Crawlers, Athena cost mechanics (data scanned), IAM roles for cross-service access, dbt-athena adapter.
- **Tool stack (3+ tools):** AWS S3, AWS Glue Data Catalog, AWS Glue Crawlers, AWS Athena, dbt-athena, IAM, Parquet.
- **Cert exam domains touched:** SAA-C03 — *Storage, IAM, Cost-Optimized Architectures*; DEA-C01 — *Data Ingestion and Transformation, Data Store Management*; dbt Foundational — *Adapters and Profiles*.
- **Dataset:** NOAA GHCN Daily Weather, ~30 GB CSV, from noaa.gov/ghcn — time-series across millions of stations, excellent partitioning candidate.
- **Architecture in 3–5 lines:** NOAA CSV bulk download → Python conversion to Parquet partitioned by `year/month` → upload to S3 → Glue Crawler infers schema → Athena queries the catalog → dbt-athena materializes a `fct_daily_weather` mart back into S3.
- **Concrete weekly deliverables:**
  1. Repo with IaC-free shell scripts (Terraform comes Week 27), partitioning logic, dbt-athena project, README with a screenshot of an Athena query showing scanned-bytes savings.
  2. `make athena-demo` runs partitioned vs unpartitioned query and prints cost delta.
  3. LinkedIn hook: "Partitioning Parquet correctly cut my Athena scan from 28 GB to 240 MB — a 99% cost drop. Same query, same answer."
- **Wow-factor:** A side-by-side screenshot of two Athena queries: "Bytes scanned: 28 GB" vs "Bytes scanned: 240 MB."
- **Stretch goal:** Add an Athena workgroup with a per-query data-scanned limit and demonstrate it blocking a runaway query.
- **Why this project (90 words):** This is your first real AWS spend and your first taste of what makes the DEA-C01 different from the SAA-C03: the cert obsesses over *how data is laid out in S3*. Until you have personally seen the dollar difference between `WHERE year=2023` against a partitioned and unpartitioned table, you do not understand Athena. dbt-athena is also the cheapest production-grade dbt adapter on AWS, so you are simultaneously skilling up on the transformation layer most AWS shops actually use.

## Week 6 — "Iceberg vs Delta: A Bake-Off on a Laptop"

- **Phase:** 1
- **One-line pitch:** Implement the same workload twice — once on Iceberg, once on Delta — and write the brutal comparison nobody else has.
- **Primary new skill gained:** **Deep mechanics of open table formats** — manifest files, snapshot isolation, hidden partitioning, schema evolution, time travel — and the trade-offs that determine which to choose.
- **Secondary skills reinforced:** PyIceberg, delta-rs, schema evolution patterns, table maintenance (compaction, vacuuming), nested data handling.
- **Tool stack (3+ tools):** PyIceberg, delta-rs (Python), DuckDB, MinIO, Parquet, OpenStreetMap PBF parser.
- **Cert exam domains touched:** DEA-C01 — *Data Store Management (table formats)*; SAA-C03 — *Storage Patterns*; dbt Foundational — *Sources across multiple formats*.
- **Dataset:** OpenStreetMap Planet extract (regional), ~20 GB PBF, from planet.osm.org — schema evolution on nested tags makes both formats sweat.
- **Architecture in 3–5 lines:** OSM PBF → Python parser into two parallel paths → Iceberg table via PyIceberg + Delta table via delta-rs (both on MinIO) → identical query suite via DuckDB → benchmark harness records latency, file count, snapshot size, and behavior under schema change.
- **Concrete weekly deliverables:**
  1. Repo with parallel `iceberg/` and `delta/` directories, a benchmark harness, a `BAKEOFF.md` reporting raw numbers and a verdict.
  2. `make bakeoff` reproduces every benchmark on a fresh machine.
  3. LinkedIn hook: "I ran the same workload through Iceberg and Delta on my laptop and wrote down everything that surprised me. Spoiler: it's not what the vendors say."
- **Wow-factor:** A clean comparison table — write latency, read latency, schema-evolution behavior, time-travel cost — sourced from your own benchmark, not a blog post.
- **Stretch goal:** Add Apache Hudi as a third format and produce a triangular comparison.
- **Why this project (90 words):** Every serious DE interview in 2026 includes "Iceberg or Delta?" If your answer is the vendor talking points, you are exposed. This week forces you to feel the mechanics: write an Iceberg snapshot, evolve a schema, time-travel back, then do the same in Delta. The output — a public BAKEOFF.md — becomes the most-shared artifact of the 30 because nobody else has done it with real numbers. It also closes Phase 1 by graduating you from "I can query a Lakehouse" to "I can choose the right one."

---

# Phase 2 — Weeks 7–12: PySpark, Databricks & Delta Lake Mastery

## Week 7 — "PySpark on Databricks Community"

- **Phase:** 2
- **One-line pitch:** Move from DuckDB single-node to PySpark distributed by ingesting 120 GB of Reddit comments on Databricks Community Edition, learning the DataFrame API the right way.
- **Primary new skill gained:** **PySpark DataFrame API fluency** — select/filter/groupBy/window/joins/UDFs and when to use SQL vs DataFrame syntax.
- **Secondary skills reinforced:** Databricks notebooks and clusters, reading compressed JSON at scale, Spark UI navigation, partition/file sizing intuition.
- **Tool stack (3+ tools):** PySpark, Databricks Community Edition, Delta Lake (default sink), DBFS, Spark UI.
- **Cert exam domains touched:** Databricks DE Associate — *Apache Spark, DataFrame API, Databricks Workspace*.
- **Dataset:** Reddit Pushshift comments 2023 (single month), ~120 GB ZST, from academic Pushshift mirrors — naturally skewed (subreddit popularity) and forces partition tuning.
- **Architecture in 3–5 lines:** ZST comment dumps → uploaded to DBFS → PySpark job decompresses and parses JSON → writes raw Delta table partitioned by subreddit hash bucket → notebook with 8 analytical queries demonstrating DataFrame API patterns.
- **Concrete weekly deliverables:**
  1. Databricks Repos-linked GitHub repo with 4 notebooks (`01_ingest`, `02_dataframe_api`, `03_sql_vs_df`, `04_perf_tour`), README with cluster config screenshot.
  2. A notebook exportable as HTML showing the full workflow runnable on Community Edition.
  3. LinkedIn hook: "I processed 120 GB of Reddit comments on a free Databricks cluster. Here are the five PySpark idioms I wish I'd learned first."
- **Wow-factor:** A Spark UI screenshot of a 200-task job, with stage timings, demonstrating you can read the execution plan.
- **Stretch goal:** Rewrite one notebook in Scala Spark for comparison and document the differences.
- **Why this project (90 words):** Until this week, every project has been single-node. This week breaks that ceiling. Databricks Community Edition is free, which means there is *no* excuse for not knowing PySpark — and PySpark is the single highest-leverage skill on the Databricks DE Associate exam (~30% of questions). Choosing a deliberately skewed dataset (Reddit) means you cannot avoid the partition/skew lessons. By Friday you will have read the Spark UI for a real job, which is the actual interview filter for any Spark role.

## Week 8 — "Delta Lake ACID & Time Travel"

- **Phase:** 2
- **One-line pitch:** Master the four Delta Lake features that make it a real database — ACID transactions, MERGE, time travel, and OPTIMIZE/ZORDER — using slowly changing IMDb ratings.
- **Primary new skill gained:** **Delta Lake transactional semantics** — what a transaction log entry looks like, why MERGE is not an UPSERT shortcut, and how time travel actually works.
- **Secondary skills reinforced:** SCD Type 2 implementation in Delta, OPTIMIZE compaction, ZORDER colocation, VACUUM retention.
- **Tool stack (3+ tools):** Delta Lake, PySpark, Databricks, Delta transaction log reader, IMDb TSV files.
- **Cert exam domains touched:** Databricks DE Associate — *Delta Lake, ACID, MERGE, Time Travel, OPTIMIZE/ZORDER* (this is the densest exam zone).
- **Dataset:** IMDb Datasets (title.basics, title.ratings, name.basics, etc.), ~2 GB TSV, from datasets.imdbws.com — ratings change nightly, perfect for MERGE and time travel.
- **Architecture in 3–5 lines:** Daily IMDb TSV refresh → PySpark loads into bronze Delta → MERGE into silver SCD2 dimension tables → OPTIMIZE + ZORDER on `tconst` → time-travel queries demonstrate "what did the top-10 list look like last Tuesday?"
- **Concrete weekly deliverables:**
  1. Repo with notebooks, a `_delta_log` reader script showing transaction log contents, before/after OPTIMIZE benchmarks.
  2. A reproducible demo: "Here is the top-10 movies as of `VERSION AS OF 3`. Here it is now."
  3. LinkedIn hook: "Delta Lake time travel isn't a gimmick — it's how I reconstructed the IMDb top-10 from any day in the past three months. Here's the MERGE pattern."
- **Wow-factor:** A live query showing `SELECT * FROM ratings VERSION AS OF 5` returning a different result than the current version.
- **Stretch goal:** Implement Change Data Feed (CDF) on the silver tables and stream changes to a third bronze.
- **Why this project (90 words):** Delta Lake is the only topic where the Databricks exam goes into mechanical depth, and time travel is the feature interviewers love to ask about because they know most candidates parrot the marketing without having used it. This week forces you to read the transaction log, run OPTIMIZE on real data, and watch ZORDER change query latency. That mechanical understanding is the difference between passing the cert by guessing and passing it by knowing — and the same gap shows up in interviews.

## Week 9 — "Spark Performance Forensics"

- **Phase:** 2
- **One-line pitch:** Take a deliberately slow Spark job and tune it from 40 minutes to 4 minutes using AQE, broadcast joins, salting, and partition tuning — and document every fix.
- **Primary new skill gained:** **Spark performance debugging** — reading the Spark UI, identifying skew, choosing between broadcast/sort-merge joins, enabling AQE, and salting.
- **Secondary skills reinforced:** Catalyst optimizer behavior, partition pruning, file-size tuning, memory tuning.
- **Tool stack (3+ tools):** PySpark, Databricks, Spark UI, Delta Lake, MovieLens dataset.
- **Cert exam domains touched:** Databricks DE Associate — *Spark Performance Tuning, AQE, Joins*.
- **Dataset:** MovieLens 25M + tags, ~1.5 GB CSV, from grouplens.org — popular movies create heavy skew on `movieId` joins, ideal for tuning.
- **Architecture in 3–5 lines:** MovieLens ratings + tags + movies → intentionally naive PySpark job with skewed joins and tiny files → measure baseline → apply six tuning techniques sequentially → produce a forensics report with before/after Spark UI screenshots and timing.
- **Concrete weekly deliverables:**
  1. Repo with `notebooks/baseline.py`, `notebooks/tuned.py`, and `FORENSICS.md` showing six numbered fixes with metrics.
  2. A reproducible benchmark notebook anyone can run on Community Edition.
  3. LinkedIn hook: "I tuned a Spark job from 40 minutes to 4 minutes with six changes. Here's each one, ranked by impact."
- **Wow-factor:** A waterfall chart showing job duration after each of the six fixes — a visual story of compounding gains.
- **Stretch goal:** Disable AQE entirely and quantify how much of the speedup came purely from it.
- **Why this project (90 words):** Anyone can write a Spark job. The exam — and every real DE interview — tests whether you can *fix* a slow one. Most candidates have only ever seen tuning slides; they have never read a Spark UI on a job they wrote. This week forces you to. The output is a public forensics document that is shareable, citable, and instantly demonstrates you can do the highest-leverage thing a Spark engineer does: cut a job's runtime by 10x without throwing hardware at it.

## Week 10 — "Delta Live Tables Medallion"

- **Phase:** 2
- **One-line pitch:** Build a full bronze→silver→gold medallion pipeline using Delta Live Tables with declarative expectations on daily Spotify chart data.
- **Primary new skill gained:** **Declarative pipelines with DLT** — defining streaming and batch tables in pure SQL/Python with built-in data quality expectations.
- **Secondary skills reinforced:** Medallion architecture, DLT expectations (expect / expect_or_drop / expect_or_fail), CDC apply_changes pattern, pipeline event log.
- **Tool stack (3+ tools):** Delta Live Tables, Databricks, PySpark, Delta Lake, dbutils.
- **Cert exam domains touched:** Databricks DE Associate — *Delta Live Tables, Medallion Architecture, Data Quality Expectations*.
- **Dataset:** Spotify Charts (daily, global), ~3 GB CSV, from kaggle/spotify-charts — daily cadence ideal for streaming-style DLT with CDC into silver.
- **Architecture in 3–5 lines:** Daily Spotify chart CSVs → DLT streaming bronze table → DLT silver dim_artist / dim_track / fct_chart_position with expectations → DLT gold `agg_artist_streams_weekly` → pipeline event log queried via SQL to surface dropped rows.
- **Concrete weekly deliverables:**
  1. Repo with a DLT pipeline definition (SQL + Python), pipeline JSON config, README with screenshot of the DLT graph view.
  2. A demo notebook querying the DLT event log to show how many rows each expectation dropped.
  3. LinkedIn hook: "Delta Live Tables turned my 200-line PySpark pipeline into a 40-line declarative spec — with data quality baked in. Here's the medallion in 40 lines."
- **Wow-factor:** Screenshot of the DLT lineage graph in the Databricks UI showing bronze→silver→gold with green expectation indicators.
- **Stretch goal:** Convert one of the silver tables to a streaming table and feed it from a generated micro-batch source.
- **Why this project (90 words):** DLT is the Databricks exam's biggest delta from "generic Spark" — and the topic most candidates skip because it requires platform access. Community Edition does not run DLT directly, but you can use a 14-day trial of standard Databricks for under $20. This week earns you genuine fluency with the medallion architecture (which is the answer to every "how would you structure this Lakehouse?" interview question) and with declarative pipelines, which are increasingly the default authoring mode in 2026.

## Week 11 — "dbt-on-Databricks"

- **Phase:** 2
- **One-line pitch:** Bridge the dbt skill from Phase 1 onto the Databricks SQL warehouse, running dbt against Delta tables with Unity Catalog as your metadata store.
- **Primary new skill gained:** **dbt-databricks adapter** in production posture — using SQL warehouses, Unity Catalog three-level namespaces, and Delta-specific incremental strategies.
- **Secondary skills reinforced:** Databricks SQL warehouses, Unity Catalog catalogs/schemas, dbt Delta `merge` strategy, Liquid Clustering.
- **Tool stack (3+ tools):** dbt-core, dbt-databricks, Databricks SQL Warehouse, Unity Catalog, Delta Lake.
- **Cert exam domains touched:** dbt Foundational — *Adapters, Profiles, Materializations*; Databricks DE Associate — *Databricks SQL, Unity Catalog basics*.
- **Dataset:** Steam Game Reviews, ~15 GB JSON, from kaggle/steam-reviews — bridges your dbt practice into Databricks SQL.
- **Architecture in 3–5 lines:** Steam reviews JSON → uploaded to Unity Catalog volume → Auto Loader ingests to bronze Delta → dbt-databricks builds silver and gold marts using `merge` incremental strategy → Liquid Clustering on `app_id` → exposures point to a final review-trends dashboard.
- **Concrete weekly deliverables:**
  1. Repo with full dbt project, `profiles.yml` template, README with a Unity Catalog screenshot.
  2. `dbt build` runs end-to-end against a Databricks SQL warehouse.
  3. LinkedIn hook: "I ran the same dbt project against DuckDB, Athena, and Databricks SQL in three weeks. Here's what the dbt adapter ecosystem actually buys you."
- **Wow-factor:** A three-screen comparison: same dbt project, three different platforms, three identical mart results — proof that dbt portability is real.
- **Stretch goal:** Add a dbt model that uses Databricks SQL AI Functions (`ai_classify`) to categorize review sentiment.
- **Why this project (90 words):** Phase 1 taught dbt fundamentals; this week proves you can deploy dbt against the platform most enterprises use in 2026. The three-platform comparison is the strongest possible signal in interviews — it says "I know dbt as a *layer*, not as a DuckDB toy." It also forces you into Unity Catalog (a Databricks exam topic) without making UC the whole point of the week. Liquid Clustering specifically is the newest Delta feature and asking about it filters for engineers who read release notes.

## Week 12 — "Unity Catalog & Lineage"

- **Phase:** 2
- **One-line pitch:** Govern a multi-domain Lakehouse with Unity Catalog — catalogs, schemas, row/column-level security, lineage, and audit logs — using FRED macroeconomic data.
- **Primary new skill gained:** **Lakehouse governance with Unity Catalog** — the 2026 standard for data governance on Databricks.
- **Secondary skills reinforced:** Three-level namespace, dynamic views for row filtering, column masking, system tables for audit, lineage UI navigation.
- **Tool stack (3+ tools):** Unity Catalog, Databricks, dbt-databricks, Delta Lake, dynamic views.
- **Cert exam domains touched:** Databricks DE Associate — *Unity Catalog, Data Governance, Permissions*.
- **Dataset:** FRED Macroeconomic Series (1000+ series), ~2 GB CSV, from fred.stlouisfed.org — many tables across clear domains, perfect for catalog/schema organization.
- **Architecture in 3–5 lines:** FRED API bulk pull → land into a `raw` catalog → curate into `finance` and `econ` catalogs with separate schemas → dynamic views enforce row-level filtering by user group → system tables surface lineage and access logs.
- **Concrete weekly deliverables:**
  1. Repo with catalog setup scripts, GRANT statements, dynamic view definitions, a README walkthrough of system table queries.
  2. A demo notebook that runs as two different users showing different filtered results from the same view.
  3. LinkedIn hook: "I built a governed Lakehouse where two users running `SELECT *` see different data — without any application code. Unity Catalog dynamic views, explained."
- **Wow-factor:** Side-by-side terminal output showing user A seeing 1000 rows and user B seeing 200 from the same view, with the GRANT/dynamic view code visible.
- **Stretch goal:** Wire Unity Catalog lineage into an OpenLineage receiver and visualize cross-platform lineage.
- **Why this project (90 words):** Governance is the section of the Databricks exam where unprepared candidates lose the most points, because they have never actually configured Unity Catalog. This week fixes that with a low-stakes dataset (FRED) so all your attention goes to the governance constructs. It also produces a remarkably differentiated portfolio piece: row-level security via dynamic views is a topic almost nobody demonstrates publicly. Closes Phase 2 by graduating you from "I can run Spark jobs" to "I can run a Lakehouse other people can be trusted on."

---

# Phase 3 — Weeks 13–18: AWS-Native Data Engineering

## Week 13 — "Glue + Athena Production Pattern"

- **Phase:** 3
- **One-line pitch:** Build the canonical AWS-native ELT pattern — Glue ETL jobs, Glue Data Catalog, S3 partitioned Parquet, Athena queries — on real NYC 311 service request data.
- **Primary new skill gained:** **AWS Glue ETL job authoring** — PySpark scripts in Glue, job bookmarks, Glue triggers, and the difference between Glue ETL and a self-managed Spark job.
- **Secondary skills reinforced:** Glue Crawlers vs static schemas, Athena CTAS, Athena views, partition projection.
- **Tool stack (3+ tools):** AWS Glue (ETL + Catalog + Crawlers), AWS Athena, AWS S3, PySpark, IAM.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion and Transformation* (Glue is ~25% of the exam); SAA-C03 — *Storage, IAM*.
- **Dataset:** NYC 311 Service Requests, ~25 GB CSV, from data.cityofnewyork.us — dirty municipal data with categorical chaos, perfect for Glue ETL.
- **Architecture in 3–5 lines:** 311 CSV → raw S3 zone → Glue Crawler builds initial catalog → Glue ETL job (PySpark) cleans, types, partitions by `created_year/created_month` → writes curated Parquet zone → Athena views for analyst access with partition projection enabled.
- **Concrete weekly deliverables:**
  1. Repo with Glue job script, deployment shell scripts (Terraform later), Athena view DDL, README with cost screenshot.
  2. A reproducible demo: drop a new CSV in raw S3, trigger crawler + job, watch the Athena view update.
  3. LinkedIn hook: "Glue ETL gets a bad rap. Here's the production pattern that makes it the cheapest way to run Spark on AWS — and what I'd avoid."
- **Wow-factor:** A cost report showing the full job ran for under $0.50, with curated Athena queries scanning <100 MB.
- **Stretch goal:** Convert the Glue job to use Glue 4.0 with Iceberg as the target format.
- **Why this project (90 words):** Glue is on the DEA-C01 exam in nearly every section — ingestion, transformation, cataloging, orchestration via Glue Workflows. You cannot study around it. This week makes Glue muscle-memory: writing a job, debugging it in CloudWatch, watching it write back to S3, querying via Athena. NYC 311 is intentionally dirty so you encounter the schema inconsistencies that Glue's DynamicFrame is actually designed for. By Friday you will have an opinion on Glue vs EMR, which is exactly the opinion the exam expects you to have.

## Week 14 — "The Cost-Aware Athena Mart"

- **Phase:** 3
- **One-line pitch:** Engineer a dbt-athena project against SEC EDGAR filings where every query is benchmarked for cost, and every model is optimized to scan the minimum bytes.
- **Primary new skill gained:** **Cost-aware data modeling** — partition design, file size tuning, columnar projection, and the economics of pay-per-scan engines.
- **Secondary skills reinforced:** dbt-athena incremental strategies (`insert_overwrite`, `append`, `merge`), Athena workgroups, partition projection patterns, query result reuse.
- **Tool stack (3+ tools):** dbt-athena, AWS Athena, AWS Glue Catalog, AWS S3, AWS CloudWatch metrics.
- **Cert exam domains touched:** DEA-C01 — *Data Store Management, Cost Optimization*; dbt Foundational — *Materializations, Incremental*.
- **Dataset:** SEC EDGAR Financial Statement Datasets (quarterly), ~40 GB TSV, from sec.gov/dera — wide tables with millions of facts, cost optimization is visible.
- **Architecture in 3–5 lines:** SEC quarterly ZIPs → S3 raw zone → dbt-athena staging models materialize Parquet partitioned by `fiscal_year/quarter` → marts use `insert_overwrite` incremental → workgroup logs every query's scanned bytes → a `cost_report.py` script summarizes weekly cost per model.
- **Concrete weekly deliverables:**
  1. Repo with dbt-athena project, workgroup config, cost report script, and a `MODEL_COST_REPORT.md` showing each model's $-per-build.
  2. `dbt build && python cost_report.py` produces a per-model cost ledger.
  3. LinkedIn hook: "I built a dbt mart on SEC filings and tagged every model with its dollar cost per refresh. Here's the dashboard."
- **Wow-factor:** A leaderboard of dbt models sorted by cost per refresh, with the most expensive one then shown halved by a partitioning fix.
- **Stretch goal:** Implement an Athena query results cache hit-rate dashboard.
- **Why this project (90 words):** Cost is the dimension nobody teaches and every employer cares about. By tagging every dbt model with its dollar cost, you produce an artifact that interviews well: "I can not only build this, I can tell you what it costs to run." SEC EDGAR is the right dataset because financial data is wide enough that columnar projection wins matter, and quarterly enough that incremental matters. By Friday you will have an internal mental model for AWS scan-based pricing that the DEA-C01 exam tests under "cost optimization."

## Week 15 — "Redshift + Spectrum Hybrid Warehouse"

- **Phase:** 3
- **One-line pitch:** Build a hybrid warehouse where hot dimensions live in Redshift, cold facts stay on S3 via Spectrum, and dbt-redshift models seamlessly join across both.
- **Primary new skill gained:** **Redshift architecture mechanics** — RA3 nodes, distribution and sort keys, Redshift Spectrum for S3-resident facts, automatic table optimization.
- **Secondary skills reinforced:** dbt-redshift adapter, Redshift WLM queues, RS COPY from S3, Spectrum external schema.
- **Tool stack (3+ tools):** AWS Redshift Serverless, Redshift Spectrum, AWS S3, dbt-redshift, AWS Glue Catalog.
- **Cert exam domains touched:** DEA-C01 — *Redshift, Spectrum*; SAA-C03 — *Databases, Cost-Optimized Architectures*; dbt Foundational — *Adapters*.
- **Dataset:** BLS Quarterly Census of Employment and Wages, ~10 GB CSV, from bls.gov/cew — naturally dimensional (NAICS code × geography × time).
- **Architecture in 3–5 lines:** BLS quarterly CSVs → S3 raw → Redshift COPY for current 2 years (hot) → older years remain on S3 as Spectrum external tables → dbt-redshift builds dimensions in native Redshift, facts via Spectrum, joined in marts.
- **Concrete weekly deliverables:**
  1. Repo with Redshift Serverless setup, Spectrum external schema DDL, dbt project, README with cost comparison vs all-Redshift.
  2. `dbt build` produces a mart joining native and Spectrum tables; a query plan screenshot proves the federation.
  3. LinkedIn hook: "I cut my Redshift bill 70% by keeping 90% of my data on S3 via Spectrum — and dbt didn't care. Here's the hybrid pattern."
- **Wow-factor:** An `EXPLAIN` output showing a single query reading from both Redshift-native and S3-Spectrum tables in one plan.
- **Stretch goal:** Add Redshift data sharing to expose marts to a second (consumer) Redshift workgroup.
- **Why this project (90 words):** Redshift is the AWS warehouse most large enterprises actually run, and Spectrum is the feature that keeps Redshift relevant in a Lakehouse world. The DEA-C01 tests both heavily, and most candidates only know Athena. This week makes you bilingual. The hybrid pattern (hot in RS, cold in S3) is also one of the most economically rational designs you can show in an interview — it signals you understand the cost curve, not just the architecture diagram.

## Week 16 — "S3 Tables: Native Iceberg on AWS"

- **Phase:** 3
- **One-line pitch:** Run a production-style Iceberg Lakehouse on **AWS S3 Tables** — the managed Iceberg service that changes the AWS Lakehouse calculus in 2026.
- **Primary new skill gained:** **AWS S3 Tables operations** — table buckets, automatic maintenance (compaction, snapshot expiration), integration with Athena, Glue, EMR, and Lake Formation.
- **Secondary skills reinforced:** Iceberg in production, Lake Formation permissions on table buckets, schema evolution managed by AWS, cross-engine Iceberg access.
- **Tool stack (3+ tools):** AWS S3 Tables, Apache Iceberg, AWS Athena, AWS Lake Formation, dbt-athena.
- **Cert exam domains touched:** DEA-C01 — *Data Store Management (Iceberg, S3 Tables)*; SAA-C03 — *Storage, Security*.
- **Dataset:** World Bank Open Data — all indicators across all countries since 1960, ~5 GB CSV, from data.worldbank.org — schema evolves over decades, Iceberg's home turf.
- **Architecture in 3–5 lines:** World Bank annual CSV refresh → S3 raw → ingestion script writes to S3 Tables Iceberg table → schema evolves over time as new indicators appear → Athena queries via the S3 Tables catalog integration → Lake Formation governs analyst access.
- **Concrete weekly deliverables:**
  1. Repo with S3 Tables setup, ingestion script demonstrating schema evolution, Lake Formation grants, dbt-athena mart, README with screenshots.
  2. `make demo` adds three new columns to the Iceberg table and shows Athena reading old + new data seamlessly.
  3. LinkedIn hook: "AWS S3 Tables turn Iceberg into a managed service. Here's the 2026 AWS Lakehouse architecture you should be drawing on whiteboards."
- **Wow-factor:** A live schema-evolution demo: add a column, drop a column, rename a column, query historical snapshots — all on managed Iceberg.
- **Stretch goal:** Read the same S3 Tables table from a Databricks Spark cluster via the Iceberg REST catalog.
- **Why this project (90 words):** S3 Tables is the newest meaningful AWS data service and the DEA-C01 has already absorbed it into the blueprint. Most candidates have not touched it. Writing this project in 2026 puts you ahead of 95% of the labor market on this specific topic. Combined with the Phase 1 Iceberg fundamentals, this week makes you fluent in the format that is replacing Hive-style tables across the AWS ecosystem, while giving you the Lake Formation experience the SAA-C03 security domain expects.

## Week 17 — "Kinesis Firehose to the Lakehouse"

- **Phase:** 3
- **One-line pitch:** Capture live weather telemetry into your Lakehouse via Kinesis Data Streams → Firehose → S3 Iceberg, the AWS-native streaming ingest pattern.
- **Primary new skill gained:** **AWS streaming ingest** — Kinesis Data Streams shards, Firehose delivery streams with dynamic partitioning, and direct-to-Iceberg sinks.
- **Secondary skills reinforced:** Lambda producers, Firehose data transformation, S3 partitioning for streaming data, Glue Catalog auto-registration.
- **Tool stack (3+ tools):** AWS Kinesis Data Streams, AWS Kinesis Firehose, AWS Lambda, AWS S3, Apache Iceberg, AWS Glue Catalog.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion and Transformation (streaming)*; SAA-C03 — *Event-driven Architectures*.
- **Dataset:** OpenWeather API live capture (~1 GB/week), from openweathermap.org — true streaming source ideal for Firehose.
- **Architecture in 3–5 lines:** EventBridge schedule triggers Lambda every 5 minutes → Lambda calls OpenWeather API for 50 cities and pushes records to Kinesis Data Streams → Firehose buffers and writes to S3 in Iceberg format with dynamic partitioning by `city/date` → Athena queries the table live.
- **Concrete weekly deliverables:**
  1. Repo with Lambda code, Firehose config, IAM, README with architecture diagram, Athena queries against live data.
  2. A live dashboard (Streamlit) showing temperatures updating as Firehose flushes.
  3. LinkedIn hook: "Live weather for 50 cities, streamed into an Iceberg Lakehouse on AWS. Zero servers managed. Here's the wiring diagram."
- **Wow-factor:** A 30-second screen recording: terminal showing Lambda invocations, dashboard updating in real time, Athena returning fresh rows.
- **Stretch goal:** Add a Kinesis Data Analytics (Managed Service for Flink) consumer producing 5-minute aggregations.
- **Why this project (90 words):** Streaming is on the DEA-C01 and the SAA-C03 in different flavors; both reward candidates who have actually wired up Kinesis. This week is the cheapest possible way to build that muscle, and OpenWeather is the cleanest free streaming source (better than synthetic generators because it has natural variance). The dashboard makes it instantly demoable. Most AWS data engineers know Kinesis from slides, not from a project they shipped end-to-end — by Friday you will be in the smaller group.

## Week 18 — "EMR Serverless + DMS CDC"

- **Phase:** 3
- **One-line pitch:** Replicate a live OLTP Postgres database into a Lakehouse using AWS DMS CDC, with EMR Serverless processing the change log into Delta tables.
- **Primary new skill gained:** **CDC ingestion on AWS** — DMS source/target endpoints, replication tasks, full-load + ongoing-replication mode, and reconciling change events into a target table.
- **Secondary skills reinforced:** EMR Serverless job submission, Spark on EMR vs Databricks, S3 raw zones for CDC events, Delta MERGE for change application.
- **Tool stack (3+ tools):** AWS DMS, AWS RDS Postgres, AWS EMR Serverless, PySpark, Delta Lake (via delta-spark on EMR), AWS S3.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion (CDC), EMR*; SAA-C03 — *Migration Services, EMR architecture*; Databricks DE Associate — *Spark fundamentals (transferable)*.
- **Dataset:** Chinook OLTP schema, seeded into RDS Postgres (~500 MB seeded, ~2 GB after a week of synthetic transactions), from chinookdatabase.codeplex.com.
- **Architecture in 3–5 lines:** RDS Postgres with Chinook + a `transaction_generator.py` script producing inserts/updates/deletes → DMS replication task in CDC mode writes Parquet change events to S3 → EMR Serverless job reads change events and applies MERGE into Delta target tables → Athena queries the silver Delta layer.
- **Concrete weekly deliverables:**
  1. Repo with RDS seed script, transaction generator, DMS task config, EMR Serverless job script, README with CDC architecture diagram.
  2. `make cdc-demo` runs a transaction in Postgres and surfaces the change in Athena within 60 seconds.
  3. LinkedIn hook: "I replicated a live Postgres database into my Lakehouse via AWS DMS CDC and EMR Serverless. End-to-end latency under a minute. Here's the wiring."
- **Wow-factor:** A side-by-side terminal: Postgres `UPDATE` on the left, Athena row reflecting the change on the right within seconds.
- **Stretch goal:** Add deletion handling with soft-delete tombstones in the silver Delta table.
- **Why this project (90 words):** CDC is the single most-asked architecture question in DE interviews and the topic the DEA-C01 covers most asymmetrically — heavy on DMS, light on alternatives. This week makes you fluent in both DMS *and* EMR Serverless, which is the lighter-weight Spark runtime AWS is pushing in 2026. Closes Phase 3 by tying together every AWS service: RDS, DMS, S3, EMR, Athena, IAM. You finish Phase 3 with a complete mental map of the AWS data stack — exactly what the exam tests.

---

# Phase 4 — Weeks 19–24: Orchestration, Streaming, CDC & Open Source Stack

## Week 19 — "Airflow on MWAA: Real DAGs"

- **Phase:** 4
- **One-line pitch:** Orchestrate a real transit data pipeline with Apache Airflow on MWAA — daily GTFS static refreshes plus 30-second realtime feeds — using sensors, XComs, and TaskGroups.
- **Primary new skill gained:** **Production Airflow patterns** — sensors, XComs, TaskGroups, dynamic task mapping, backfills, and the difference between MWAA and self-hosted.
- **Secondary skills reinforced:** Airflow operators (S3, Glue, Athena), DAG retries and SLA, MWAA cost posture, Airflow CLI.
- **Tool stack (3+ tools):** Apache Airflow, AWS MWAA, AWS S3, AWS Glue, GTFS-realtime protobufs, Python.
- **Cert exam domains touched:** DEA-C01 — *Orchestration (MWAA)*; SAA-C03 — *Application Integration*; dbt Foundational — *Production deployment via orchestrator*.
- **Dataset:** GTFS Static + GTFS Realtime (NYC MTA), ~5 GB total, from mta.info/developers — daily static schedules + 30-second realtime feeds.
- **Architecture in 3–5 lines:** MWAA DAG 1 (daily) downloads GTFS static ZIP → unzips to S3 → Glue job → curated Parquet; MWAA DAG 2 (every 5 min) polls GTFS-realtime → writes protobufs to S3 → small Glue job produces a `realtime_vehicle_positions` table → Athena views join static and realtime.
- **Concrete weekly deliverables:**
  1. Repo with two DAGs (using `@dag` decorator), `requirements.txt`, MWAA environment config, README with screenshot of the Airflow Grid view showing successful runs.
  2. A `make smoke-test` that runs both DAGs locally on Airflow standalone before MWAA deploy.
  3. LinkedIn hook: "MWAA orchestrating a real-time transit pipeline. Two DAGs, ten tasks, full sensor + XCom + TaskGroup patterns. Here's the repo."
- **Wow-factor:** Airflow Grid view screenshot showing both DAGs running on schedule, with a TaskGroup expanded showing 20+ dynamically mapped tasks.
- **Stretch goal:** Add a Slack notification operator that alerts on SLA misses.
- **Why this project (90 words):** Airflow is still the most-deployed orchestrator in production data engineering, and MWAA is the AWS-managed flavor the DEA-C01 specifically tests. Most candidates have only run Airflow tutorials with `BashOperator hello-world`. This week forces you into real patterns: sensors waiting on S3, XComs passing partition dates, TaskGroups organizing parallel work. It also gives you experience with a live realtime feed (GTFS-RT protobufs), which is rarer in portfolios than batch — a differentiating signal.

## Week 20 — "Dagster Software-Defined Assets"

- **Phase:** 4
- **One-line pitch:** Reimplement an Airflow-style pipeline as Dagster Software-Defined Assets and feel — viscerally — why asset-based orchestration is winning mindshare in 2026.
- **Primary new skill gained:** **Asset-based orchestration with Dagster** — SDAs, asset materializations, asset checks, partitioned assets, asset sensors.
- **Secondary skills reinforced:** Dagster + dbt integration (`load_assets_from_dbt_project`), IO managers, Dagster UI navigation, comparison with task-based Airflow.
- **Tool stack (3+ tools):** Dagster, dbt-duckdb, DuckDB, S3 (boto3 IO manager), Pandas, eBird dataset.
- **Cert exam domains touched:** DEA-C01 — *Orchestration (modern alternatives)*; dbt Foundational — *dbt orchestration patterns*.
- **Dataset:** eBird Basic Dataset, ~80 GB CSV (filtered to a region for the week), from ebird.org/data — asset-oriented model (species × region × month) fits SDAs beautifully.
- **Architecture in 3–5 lines:** eBird regional CSV → Dagster ingestion asset partitioned by month → dbt models loaded as Dagster assets → asset checks enforce data quality → daily schedule materializes new partitions → Dagster UI shows the asset lineage graph.
- **Concrete weekly deliverables:**
  1. Repo with Dagster definitions, dbt project, asset checks, README with screenshot of the Dagster asset graph.
  2. `dagster dev` brings up the local UI; `dagster asset materialize --select '*'` rebuilds end-to-end.
  3. LinkedIn hook: "I rebuilt my Airflow pipeline in Dagster. Same logic, 40% less code, and the asset graph tells you *what* exists — not just *what ran*. Here's the side-by-side."
- **Wow-factor:** Dagster asset graph screenshot with assets, partitions, materialization status, and freshness policies visible — visibly richer than an Airflow DAG view.
- **Stretch goal:** Add an asset sensor that triggers downstream rebuilds when an upstream Iceberg snapshot changes.
- **Why this project (90 words):** Dagster is not on any of your four certs, but it is the orchestrator most modern data platforms are migrating toward and the one that interview panels in 2026 increasingly ask about. Building the same pipeline in both Airflow (Week 19) and Dagster (Week 20) gives you the rare ability to discuss orchestration philosophy with conviction — task graphs versus asset graphs — which is a senior-level conversation. The week pays dividends in interviews even though it does not directly hit an exam blueprint.

## Week 21 — "Kafka on MSK: Event Backbone"

- **Phase:** 4
- **One-line pitch:** Stand up Apache Kafka on AWS MSK Serverless and stream Wikipedia edit events into your Lakehouse — the canonical event-backbone pattern.
- **Primary new skill gained:** **Kafka operational fundamentals** — topics, partitions, consumer groups, offsets, MSK Serverless authentication (IAM), and the producer/consumer API.
- **Secondary skills reinforced:** Kafka Connect S3 sink, schema registry basics, MSK Connect, comparing Kafka and Kinesis trade-offs.
- **Tool stack (3+ tools):** Apache Kafka, AWS MSK Serverless, Kafka Connect, AWS S3, Python (confluent-kafka), Wikipedia EventStream.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion (streaming alternatives)*; SAA-C03 — *Application Integration*.
- **Dataset:** Wikipedia EventStream (live), ~2 GB/day, from stream.wikimedia.org — free public stream of every Wikipedia edit globally.
- **Architecture in 3–5 lines:** Python consumer of Wikipedia EventStream → produces to MSK Serverless topic `wiki.edits` partitioned by language → Kafka Connect S3 sink writes Parquet to S3 → Glue Crawler builds catalog → Athena queries live edit data with ~1 minute end-to-end latency.
- **Concrete weekly deliverables:**
  1. Repo with producer code, MSK config, Kafka Connect connector definition, README with topic/partition design notes.
  2. `make stream` starts the producer and consumer; Athena query refreshes every minute.
  3. LinkedIn hook: "Every Wikipedia edit in the world, streamed into my AWS Lakehouse via MSK and Kafka Connect. Here's what MSK Serverless changes about the Kafka cost equation."
- **Wow-factor:** A live tail of `kafka-console-consumer` next to an Athena query showing the same edits appearing in S3.
- **Stretch goal:** Add a second consumer group running a different transformation, demonstrating Kafka's multi-subscriber strength over Kinesis.
- **Why this project (90 words):** Kafka is the streaming standard outside AWS and increasingly inside it via MSK. The DEA-C01 specifically tests MSK vs Kinesis trade-offs, which you cannot answer credibly without having operated both. Wikipedia EventStream is the highest-quality free streaming source on the internet — high enough velocity to feel real, structured enough to actually query, and free forever. This week is the natural setup for Week 22 (Debezium), because Debezium produces *to Kafka*, and you need to be comfortable with Kafka before adding CDC on top.

## Week 22 — "Debezium CDC: Postgres → Iceberg"

- **Phase:** 4
- **One-line pitch:** Build a fully open-source CDC pipeline — Postgres logical replication → Debezium → Kafka → Iceberg — and benchmark it against the DMS pipeline from Week 18.
- **Primary new skill gained:** **Debezium and logical CDC** — connectors, the outbox pattern, schema changes mid-stream, and tombstones for deletions.
- **Secondary skills reinforced:** Kafka Connect connectors, Postgres logical replication slots, Iceberg writes from a streaming consumer, CDC reconciliation logic.
- **Tool stack (3+ tools):** Debezium, Apache Kafka (MSK), Postgres logical replication, Apache Iceberg, Kafka Connect, Python.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion (CDC)*; SAA-C03 — *Database Architectures*.
- **Dataset:** OpenFoodFacts Postgres dump, ~10 GB, from openfoodfacts.org — real schema with frequent updates from the public.
- **Architecture in 3–5 lines:** OpenFoodFacts Postgres dump loaded into RDS → Debezium Postgres connector publishes change events to MSK topics → Python consumer using PyIceberg appends to Iceberg tables with insert/update/delete semantics → Athena queries the Iceberg target → a benchmark notebook compares latency vs Week 18's DMS pipeline.
- **Concrete weekly deliverables:**
  1. Repo with Debezium connector config, RDS setup with `wal_level=logical`, Iceberg writer, README with comparison table vs DMS.
  2. `make cdc-demo` runs an UPDATE on Postgres and shows it landing in Iceberg via Athena within 30 seconds.
  3. LinkedIn hook: "I built the same CDC pipeline twice: once with AWS DMS, once with Debezium. Here's the honest trade-off matrix nobody publishes."
- **Wow-factor:** A latency histogram comparing DMS and Debezium end-to-end latency over a 1-hour test, showing real numbers.
- **Stretch goal:** Add the outbox pattern to demonstrate transactional consistency between OLTP writes and event publishing.
- **Why this project (90 words):** Debezium is the open-source CDC standard the certs don't test directly, but every senior DE interview asks about. By building it once and comparing it to DMS, you become the candidate who can answer "DMS or Debezium?" with data instead of vibes. The OpenFoodFacts dataset is intentionally large enough that initial snapshotting takes real time, which exposes the operational realities of CDC startup that most tutorials skip. This is the deepest streaming project in your sequence and the one most likely to come up in actual interview whiteboarding.

## Week 23 — "Flink Streaming Analytics"

- **Phase:** 4
- **One-line pitch:** Compute real-time analytics — windowed counts, sessionization, anomaly detection — on the GDELT global event stream using Apache Flink on AWS Managed Service for Apache Flink.
- **Primary new skill gained:** **Stateful stream processing with Flink** — event-time windows, watermarks, state backends, and exactly-once processing.
- **Secondary skills reinforced:** Flink SQL, KDA application deployment, comparing Flink to Spark Structured Streaming.
- **Tool stack (3+ tools):** Apache Flink, AWS Managed Service for Apache Flink, Flink SQL, Kafka (MSK), AWS S3, GDELT.
- **Cert exam domains touched:** DEA-C01 — *Streaming Analytics*; SAA-C03 — *Event-driven Architectures*.
- **Dataset:** GDELT 2.0 Event Stream (live, every 15 min), ~1 GB/day, from gdeltproject.org — real-time global geo-political events.
- **Architecture in 3–5 lines:** GDELT 15-minute archives polled by Lambda → published to MSK topic `gdelt.events` → Flink application consumes the stream with event-time watermarks → computes tumbling and sliding windows + a simple z-score anomaly detector → outputs to S3 Iceberg sink and a CloudWatch metric for "anomaly events per country."
- **Concrete weekly deliverables:**
  1. Repo with Flink Python (PyFlink) and Flink SQL versions of the same job, KDA deployment config, README explaining watermark choice.
  2. A live CloudWatch dashboard showing windowed counts and anomaly metrics updating.
  3. LinkedIn hook: "Real-time anomaly detection on global news events using Apache Flink. Tumbling windows, watermarks, exactly-once — here's the Flink SQL that does it in 30 lines."
- **Wow-factor:** CloudWatch dashboard ticking forward in real time, with a synthetic spike injected to show the anomaly detector firing.
- **Stretch goal:** Reimplement the same logic in Spark Structured Streaming and compare watermark semantics.
- **Why this project (90 words):** Flink is the streaming engine the DEA-C01 names by name and most candidates avoid. Watermarks specifically are the topic that separates engineers who have read about streaming from engineers who have shipped streaming. GDELT is a rare dataset because it is genuinely real-time and genuinely interesting — global events with sentiment and geography. By Friday you will be one of a small number of engineers who can credibly discuss event-time vs processing-time on a whiteboard, which is a senior-level differentiator.

## Week 24 — "dlt + Great Expectations: Trustworthy Ingest"

- **Phase:** 4
- **One-line pitch:** Replace 200 lines of hand-rolled ingestion Python with 30 lines of `dlt` and wrap every load with Great Expectations checks — the modern open-source ingest stack.
- **Primary new skill gained:** **dlt (data load tool)** — declarative ingestion pipelines, schema inference, incremental loads, and merge dispositions.
- **Secondary skills reinforced:** REST API ingestion patterns, Great Expectations integration into ingestion (not just transformation), credentials management.
- **Tool stack (3+ tools):** dlt, Great Expectations, DuckDB, dbt-duckdb, Python REST clients.
- **Cert exam domains touched:** DEA-C01 — *Data Ingestion (modern tools)*; dbt Foundational — *Sources and seeds*.
- **Dataset:** World Bank Climate Knowledge Portal API, ~2 GB, from climateknowledgeportal.worldbank.org — API-shaped source, perfect for dlt's REST helpers.
- **Architecture in 3–5 lines:** Climate Knowledge Portal API → dlt REST source with pagination + incremental cursor → DuckDB destination → Great Expectations checkpoint runs before dbt → dbt-duckdb builds country-climate marts → fail fast on data quality issues.
- **Concrete weekly deliverables:**
  1. Repo with dlt pipeline (~30 lines), GE checkpoint config, dbt project, README showing line-count comparison vs hand-rolled.
  2. `make ingest && make validate && make build` runs the full pipeline with explicit gates.
  3. LinkedIn hook: "I replaced 200 lines of ingestion Python with 30 lines of dlt — and wrapped it with Great Expectations. Here's the modern ingest stack, end-to-end."
- **Wow-factor:** A `git diff` showing 200 lines of old Python deleted and replaced with 30 lines of dlt config.
- **Stretch goal:** Configure dlt to write directly to S3 with Iceberg as the destination format.
- **Why this project (90 words):** dlt is the rising star of the open-source ingest layer in 2026 and is starting to appear in DEA-C01 question pools as a representative of "code-first ingestion frameworks." More importantly, this is the project that closes the loop on data quality: you have GE wrapping ingestion (this week), dbt tests on transformation (Phase 1), and you will see them combined under contracts in Week 28. Closes Phase 4 by giving you the open-source counterpart to every AWS-native ingest service you learned in Phase 3.

---

# Phase 5 — Weeks 25–30: Production Concerns, IaC, Observability & Capstone

## Week 25 — "CI/CD for a Lakehouse dbt Project"

- **Phase:** 5
- **One-line pitch:** Build a production-grade CI/CD pipeline for a dbt-on-Athena project with slim CI, state-based test selection, PR previews, and automatic promotion.
- **Primary new skill gained:** **dbt CI/CD in anger** — `dbt build --select state:modified+`, slim CI with manifest comparison, GitHub Actions matrices, environment promotion.
- **Secondary skills reinforced:** dbt environments and targets, secret management in CI, blue/green schema patterns, dbt Cloud-equivalent workflows in pure GHA.
- **Tool stack (3+ tools):** dbt-athena, GitHub Actions, AWS Athena, AWS S3, dbt artifacts (manifest.json), sqlfluff.
- **Cert exam domains touched:** dbt Foundational — *Deployment, Environments, State, Slim CI*; DEA-C01 — *Operations and Monitoring*.
- **Dataset:** USDA Food Data Central, ~1 GB JSON, from fdc.nal.usda.gov — stable schema lets you focus purely on CI rigor.
- **Architecture in 3–5 lines:** Food Data Central JSON → S3 raw → dbt-athena builds nutrition marts → PR opens → GHA runs sqlfluff + `dbt build --select state:modified+` against a PR-specific Athena workgroup → on merge, promotion job builds against prod target.
- **Concrete weekly deliverables:**
  1. Repo with `.github/workflows/` containing 3 workflows (PR check, prod deploy, scheduled rebuild), branch protection rules documented, README with diagram.
  2. A test PR that demonstrates Slim CI building only changed models in <2 minutes.
  3. LinkedIn hook: "I cut my dbt CI from 14 minutes to 90 seconds with Slim CI and state-based selection. Here's the GitHub Actions setup."
- **Wow-factor:** Two GHA run screenshots: a "full build" (14m) and a "slim CI" (90s) on the same PR, with the second highlighted.
- **Stretch goal:** Add automatic dbt docs deployment to GitHub Pages on every prod merge.
- **Why this project (90 words):** CI/CD is the dbt Foundational topic most candidates fake by memorizing terms. This week makes you fluent: you will have an actual GHA workflow file you wrote, with actual state comparison logic, against an actual cloud warehouse. It is also the project that makes every subsequent week's repo better, because you can paste this workflow file into Weeks 26–30 and instantly have professional repo hygiene. High leverage per hour.

## Week 26 — "OpenLineage End-to-End"

- **Phase:** 5
- **One-line pitch:** Instrument every layer of your pipeline — dbt, Airflow, Spark — with OpenLineage and visualize a single cross-platform lineage graph in DataHub or Marquez.
- **Primary new skill gained:** **OpenLineage as a cross-tool standard** — event emission from dbt, Airflow, Spark, and Iceberg, unified in one lineage backend.
- **Secondary skills reinforced:** DataHub or Marquez setup, lineage event schema, column-level lineage, integration debugging.
- **Tool stack (3+ tools):** OpenLineage, DataHub (or Marquez), dbt, Apache Airflow, PySpark, Docker Compose.
- **Cert exam domains touched:** DEA-C01 — *Data Governance and Lineage*; dbt Foundational — *Documentation and lineage*.
- **Dataset:** NHTSA FARS Crash Data, ~3 GB CSV, from nhtsa.gov/fars — multi-table joins make the lineage graph genuinely interesting.
- **Architecture in 3–5 lines:** FARS CSV → Airflow DAG ingests to S3 → Spark job stages to Iceberg → dbt builds marts → all three emit OpenLineage events → DataHub aggregates into a unified lineage graph with column-level edges.
- **Concrete weekly deliverables:**
  1. Repo with OL configuration for each tool, DataHub `docker-compose.yml`, a screenshot of the unified lineage graph showing all three tools.
  2. `make lineage-demo` brings up the stack and produces a working DataHub UI on localhost.
  3. LinkedIn hook: "One pipeline, three tools (Airflow, Spark, dbt), one unified lineage graph via OpenLineage. Here's why this is the only governance pattern that actually scales."
- **Wow-factor:** DataHub UI screenshot showing column-level lineage from a raw CSV column all the way to a final mart metric.
- **Stretch goal:** Add a Great Expectations OL integration so data quality results show up on the lineage edges.
- **Why this project (90 words):** Lineage is a quiet but recurring DEA-C01 topic and a senior-DE interview filter. Most engineers can name "lineage" but have never instrumented a stack. This week makes you the engineer who has. OpenLineage specifically is the open standard winning adoption in 2026 — knowing it transfers across DataHub, Marquez, OpenMetadata, and most commercial catalogs. The column-level demo is the single most impressive visual artifact in your entire portfolio.

## Week 27 — "Terraform the Whole Stack"

- **Phase:** 5
- **One-line pitch:** Replace every click-ops AWS setup from Weeks 5–18 with a single Terraform monorepo that deploys S3, Glue, Athena, Redshift, Kinesis, MSK, MWAA, and Lake Formation — reproducibly, in under 15 minutes.
- **Primary new skill gained:** **Production Terraform for data infrastructure** — modules, remote state, workspaces, drift detection, and the Lake Formation IaC patterns most tutorials skip.
- **Secondary skills reinforced:** AWS provider depth, IAM-as-code, S3 bucket policies, MSK module composition, cost guardrails.
- **Tool stack (3+ tools):** Terraform, AWS (full stack), terraform-aws-modules, tfsec, Atlantis (optional), USGS Earthquake API.
- **Cert exam domains touched:** SAA-C03 — *IaC, Resilient and Cost-Optimized Architectures*; DEA-C01 — *Operations and Deployment*.
- **Dataset:** USGS Earthquake Catalog, ~2 GB CSV, from earthquake.usgs.gov — small enough to redeploy cheaply while iterating on Terraform.
- **Architecture in 3–5 lines:** Terraform monorepo with `modules/lakehouse`, `modules/streaming`, `modules/orchestration` → `terraform apply` deploys the whole stack → a small pipeline ingests USGS earthquake data through the deployed infrastructure → `terraform destroy` tears it down.
- **Concrete weekly deliverables:**
  1. Repo with modular Terraform, `terraform plan` output screenshotted in README, tfsec scan results, an architecture diagram auto-generated from Terraform state.
  2. `make tf-up && make tf-down` is a complete demo cycle costing under $5.
  3. LinkedIn hook: "My entire data Lakehouse — S3, Glue, Athena, Redshift, MSK, MWAA — in 800 lines of Terraform. `apply` to `destroy` in 18 minutes."
- **Wow-factor:** A screen recording of `terraform apply` deploying the full stack in 15 minutes, ending with a successful Athena query against the live infrastructure.
- **Stretch goal:** Add a GitHub Actions Atlantis-style workflow for plan/apply on PRs.
- **Why this project (90 words):** IaC is on both the SAA-C03 and DEA-C01, and it is the single skill that separates "I built a thing in the console" from "I run production." This week takes everything you have already built and re-codifies it — which is the right learning order, because you understand the services first, then the IaC. The Lake Formation IaC pattern especially is poorly documented online; producing a working public example is genuinely useful and instantly shareable.

## Week 28 — "Data Contracts in CI"

- **Phase:** 5
- **One-line pitch:** Enforce data contracts between producers and consumers in CI so that a breaking schema change is caught before merge — not by an analyst at 3am.
- **Primary new skill gained:** **Data contracts as code** — defining schemas with `dbt-contracts` and `datacontract-cli`, enforcing them in PRs, and handling versioning.
- **Secondary skills reinforced:** Schema evolution policies, semver for data, consumer-driven contract testing, sample data fixtures.
- **Tool stack (3+ tools):** datacontract-cli, dbt-core (with contracts), Great Expectations, GitHub Actions, DuckDB, Common Crawl WARC.
- **Cert exam domains touched:** DEA-C01 — *Data Quality and Governance*; dbt Foundational — *Model Contracts (a newer exam topic)*.
- **Dataset:** Common Crawl WAT (single segment), ~5 GB WARC, from commoncrawl.org — schema drift is the default, perfect contract testing ground.
- **Architecture in 3–5 lines:** Common Crawl WAT segment → parser produces a `crawl_metadata` table → a `datacontract.yaml` declares the consumer contract → dbt model contracts enforce the schema → CI runs the contract test on PR and blocks merge on breaking changes.
- **Concrete weekly deliverables:**
  1. Repo with `datacontract.yaml`, dbt model contracts, GHA workflow, a deliberately breaking PR demo branch showing the block.
  2. `make demo-break` opens a draft PR where CI fails with a clear contract violation message.
  3. LinkedIn hook: "I broke my own pipeline on purpose. The data contract caught it before merge. Here's how data contracts work in 2026."
- **Wow-factor:** GHA run screenshot showing a red ❌ contract-violation step with a human-readable diff of the schema change.
- **Stretch goal:** Wire contract metadata into the OpenLineage events from Week 26 so contract violations surface on the lineage graph.
- **Why this project (90 words):** Data contracts are the topic where the industry is moving faster than the certifications — but the smart hiring managers test for it anyway. Building a working contract enforcement pipeline puts you ahead of the curve and gives you an interview answer most candidates literally cannot give. Combined with Week 26 (lineage) and Week 25 (CI/CD), this week completes the "production discipline" triangle that converts you from someone who *builds* pipelines into someone who *operates* them.

## Week 29 — "Cost & Observability Control Plane"

- **Phase:** 5
- **One-line pitch:** Build a unified cost and observability dashboard that watches your entire Lakehouse — Athena scans, Glue DPUs, Redshift queries, MSK throughput, MWAA tasks — with alarms.
- **Primary new skill gained:** **Cost and observability instrumentation** — CloudWatch custom metrics, AWS Cost Explorer API, Athena query history, and turning telemetry into actionable alarms.
- **Secondary skills reinforced:** CloudWatch dashboards, EventBridge alarm rules, Athena `system.query_history`, anomaly detection on cost metrics.
- **Tool stack (3+ tools):** AWS CloudWatch, AWS Cost Explorer API, AWS Athena, AWS Lambda, Grafana Cloud (free tier), Python.
- **Cert exam domains touched:** SAA-C03 — *Cost-Optimized and Performance-Efficient Architectures*; DEA-C01 — *Operations and Monitoring*.
- **Dataset:** Hacker News Realtime API (live), ~500 MB/week, from hacker-news.firebaseio.com — live ingest gives real ops signals to instrument.
- **Architecture in 3–5 lines:** A small HN ingest pipeline runs continuously → CloudWatch collects native metrics from every service touched (Lambda, Glue, Athena) → custom Lambda publishes Cost Explorer queries as CloudWatch metrics → Grafana Cloud dashboards visualize cost-per-pipeline → EventBridge alarms fire on cost anomalies.
- **Concrete weekly deliverables:**
  1. Repo with metric-publishing Lambda code, Grafana dashboard JSON, CloudWatch alarm definitions, README with screenshot of the live dashboard.
  2. `make alarm-demo` triggers a synthetic cost spike and shows the alarm firing within 5 minutes.
  3. LinkedIn hook: "I built a single dashboard that tracks the cost of every component in my Lakehouse — down to dollars per pipeline run. Here's the wiring."
- **Wow-factor:** A live Grafana dashboard with cost-per-pipeline panels, query latency p99, and an alarm history panel.
- **Stretch goal:** Add forecasted spend using CloudWatch anomaly detection on a 30-day baseline.
- **Why this project (90 words):** Observability is the topic the certs cover lightly and that real jobs care about heavily. Hiring managers do not promote engineers who cannot answer "what does this cost to run?" By Friday you can. This week is also the warm-up for Week 30 — the capstone needs all of this telemetry to be genuinely demoable. Skipping this would leave the capstone visually flat. Treat this as the polish layer.

## Week 30 — "The Capstone: A Real-Time Lakehouse Platform"

- **Phase:** 5
- **One-line pitch:** Tie 29 weeks of skills into one capstone: a real-time Citi Bike Lakehouse platform with CDC + streaming ingest, Iceberg storage, dbt transformations, Dagster orchestration, OpenLineage lineage, data contracts, Terraform IaC, and a live cost dashboard.
- **Primary new skill gained:** **End-to-end Lakehouse platform integration** — the ability to design, build, and operate a complete modern data platform.
- **Secondary skills reinforced:** Every skill from Weeks 1–29.
- **Tool stack (3+ tools):** AWS S3 Tables (Iceberg), AWS DMS, AWS Kinesis Firehose, AWS Glue, AWS Athena, dbt-athena, Dagster, OpenLineage, DataHub, Terraform, GitHub Actions, datacontract-cli, Great Expectations.
- **Cert exam domains touched:** **All four** — SAA-C03 (architecture, IAM, cost), Databricks DE Associate (Spark/Delta principles transferred), DEA-C01 (every service domain), dbt Foundational (CI/CD, contracts, models).
- **Dataset:** NYC Citi Bike Trip Data (~30 GB historical) + Citi Bike GBFS Live Feed (live), from citibikenyc.com/system-data — combines deep batch history with a true live stream.
- **Architecture in 3–5 lines:** Batch path: historical Citi Bike CSVs → S3 raw → Glue ETL → S3 Tables (Iceberg); Streaming path: GBFS live feed → Lambda → Kinesis Firehose → S3 Tables (Iceberg); CDC path: a synthetic membership Postgres → DMS → Iceberg; dbt-athena builds gold marts across all three; Dagster orchestrates; OpenLineage emits to DataHub; data contracts gate the consumer marts; Terraform deploys everything; CloudWatch + Grafana observe.
- **Concrete weekly deliverables:**
  1. The portfolio centerpiece repo: monorepo with `infra/` (Terraform), `pipelines/` (Dagster + dbt), `streaming/` (Kinesis + Lambda), `cdc/` (DMS), `governance/` (contracts + lineage), `ops/` (dashboards), comprehensive README, architecture diagram, walkthrough video.
  2. `make capstone-up` deploys, ingests, transforms, and exposes a live Citi Bike analytics dashboard within 30 minutes.
  3. LinkedIn hook: "30 weeks. 30 projects. 1 capstone: a real-time Citi Bike Lakehouse with CDC, streaming, Iceberg, dbt, Dagster, OpenLineage, data contracts, Terraform — all under $20/month. Here's everything."
- **Wow-factor:** A 5-minute screen recording: `terraform apply`, pipelines starting, dashboard filling with live data, OpenLineage graph populating, a contract-violating PR being blocked, cost dashboard updating — the whole platform alive.
- **Stretch goal:** Add a public read-only dashboard URL fronted by CloudFront so anyone (recruiters) can interact with the live platform.
- **Why this project (90 words):** The capstone is the only project that proves all the others were real. It forces you to integrate, not just demonstrate. Citi Bike is the right anchor dataset because it has *all three* ingestion shapes — batch history, real-time stream, and a reasonable CDC story for membership — letting you exercise every Phase 3–4 skill in one repo. A working capstone is the single artifact that converts your 30 LinkedIn posts into one career-credible portfolio piece — the one you put at the top of every CV for the next three years.

---

## 5. Cross-Project Skill Compounding Map

The sequence is engineered to compound, not scatter. Phase 1 establishes the *language* — SQL on a Lakehouse (W1), dbt mechanics (W2), incremental patterns (W3), data quality (W4), AWS ergonomics (W5), and open-table-format depth (W6). Every one of those reappears: dbt mechanics from W2 are extended in W3 (incremental), reused in W11 (Databricks), W14 (cost-aware), W25 (CI/CD), W28 (contracts), and W30 (capstone). The Iceberg fluency from W6 directly enables W16 (S3 Tables), W17 (Firehose to Iceberg), W22 (Debezium to Iceberg), and W30. The data quality discipline from W4 compounds into W10 (DLT expectations), W24 (dlt + GE in ingest), W28 (contracts), and W30. Spark from W7 underpins W8–W12 (Delta mastery) and reappears in W18 (EMR Serverless) and W26 (Spark lineage). AWS Glue/Athena from W5 reappears in W13–W17, W25, W26, W27, and W30. Airflow (W19) and Dagster (W20) are deliberately adjacent so you internalize task vs asset thinking; both feed W30. CDC fundamentals from W18 (DMS) are deliberately revisited in W22 (Debezium) so you can compare. Terraform (W27) re-codifies every AWS service you have already operated. The result: by W30, you are not learning new things — you are integrating things you already know. That is the definition of capstone discipline.

## 6. The Capstone Architecture Diagram (Week 30)

```
                              CAPSTONE: REAL-TIME CITI BIKE LAKEHOUSE
                                        (TRACES TO WEEKS 1–29)

  ┌─────────────────────────────────────────────────────────────────────────────────────┐
  │                                INGESTION PLANE                                       │
  │                                                                                      │
  │   BATCH (W1, W5, W13)          STREAM (W17, W21)            CDC (W18, W22)           │
  │   Citi Bike Historical CSVs     Citi Bike GBFS Live Feed     Membership Postgres     │
  │           │                              │                          │                │
  │           ▼                              ▼                          ▼                │
  │   ┌──────────────┐              ┌──────────────┐           ┌──────────────┐          │
  │   │  Glue ETL    │              │ Lambda + KDS │           │   AWS DMS    │          │
  │   │   (W13)      │              │ + Firehose   │           │   (W18)      │          │
  │   └──────┬───────┘              │   (W17)      │           └──────┬───────┘          │
  │          │                      └──────┬───────┘                  │                  │
  └──────────┼─────────────────────────────┼──────────────────────────┼──────────────────┘
             │                             │                          │
             ▼                             ▼                          ▼
   ┌────────────────────────────────────────────────────────────────────────────┐
   │                  STORAGE PLANE  —  S3 TABLES / ICEBERG  (W6, W16)          │
   │     bronze.trips_historical | bronze.gbfs_status | bronze.members_cdc      │
   └─────────────────────────────┬──────────────────────────────────────────────┘
                                 │
                                 ▼
   ┌────────────────────────────────────────────────────────────────────────────┐
   │              TRANSFORMATION PLANE  —  dbt-athena  (W2, W3, W11, W14)       │
   │      silver.fct_trip | silver.dim_station | silver.dim_member              │
   │      gold.agg_demand_by_hour | gold.station_utilization | gold.churn       │
   └─────────────────────────────┬──────────────────────────────────────────────┘
                                 │
                                 ▼
   ┌────────────────────────────────────────────────────────────────────────────┐
   │                   SERVING PLANE  —  Athena  +  Grafana  (W5, W29)          │
   │              Live demand map | Station heatmap | Churn KPIs                │
   └────────────────────────────────────────────────────────────────────────────┘

                                CROSS-CUTTING PLANES
   ┌────────────────────────────────────────────────────────────────────────────┐
   │  ORCHESTRATION:  Dagster software-defined assets  (W20)                    │
   │  QUALITY:        Great Expectations + dbt tests   (W4, W24)                │
   │  CONTRACTS:      datacontract-cli in CI           (W28)                    │
   │  LINEAGE:        OpenLineage → DataHub            (W26)                    │
   │  CI/CD:          GitHub Actions + Slim CI          (W25)                    │
   │  IaC:            Terraform monorepo               (W27)                    │
   │  OBSERVABILITY:  CloudWatch → Grafana + alarms    (W29)                    │
   │  GOVERNANCE:     Lake Formation row/column policy (W12, W16)               │
   └────────────────────────────────────────────────────────────────────────────┘
```

## 7. The Honest Failure Modes

**Failure Mode 1 — Scope creep within a week.** You will be tempted to "just add one more thing" and miss Friday shipping. *Countermeasure:* Hard rule — Sunday night the repo ships with whatever exists, README acknowledges the stretch goal as unfinished, LinkedIn post goes up. Shipping discipline beats perfection.

**Failure Mode 2 — Skipping the LinkedIn post because it feels self-promotional.** You will rationalize that the repo is "not ready yet." *Countermeasure:* Treat the LinkedIn post as part of the build, not after it. Draft the post Monday with the planned hook. If the post cannot be written, the scope is wrong. Anyone in consulting who does not publicly compound their work in 2026 is leaving an obvious lever unused.

**Failure Mode 3 — AWS cost spikes from a forgotten resource.** A misconfigured Kinesis stream or running EMR cluster will silently burn $200 in a weekend. *Countermeasure:* Every week's repo includes a `make destroy` target. AWS Budget alert configured at $50/month with email + SMS. Sunday teardown is non-negotiable. Treat AWS like a campsite: leave no trace.

## 8. The Year-End Resume Statement

> Designed and shipped 30 production-grade data engineering projects in 30 weeks against the 2026 modern data stack, including a real-time Lakehouse platform integrating CDC (AWS DMS + Debezium), streaming ingest (Kinesis Firehose, MSK, Flink), Apache Iceberg storage on AWS S3 Tables, dbt-driven transformation across DuckDB / Athena / Redshift / Databricks adapters, Dagster and Airflow orchestration, and full IaC via Terraform — all governed by OpenLineage, data contracts, and Great Expectations, observed through a custom CloudWatch + Grafana cost dashboard, and operated for under $20/month per project. Earned the AWS Solutions Architect Associate, AWS Data Engineer Associate, Databricks Data Engineer Associate, and dbt Foundational certifications, with every project mapped to specific exam domains and published as an open-source GitHub repository with reproducible `make demo` artifacts.
