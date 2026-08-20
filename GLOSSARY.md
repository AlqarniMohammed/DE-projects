# Glossary — The Terminology On-Ramp

Every term the framework uses, defined in plain language, **taught as contrast pairs** where possible (the fastest way to make a term stick), and tagged with the phase where you first need it. Read a phase's terms *before* starting its build. When a build instruction uses a word you can't explain, come back here — if it's missing, add it (this file is yours to grow).

> Format: **Term** `[P#]` — definition. *Contrast:* what it is **not**.

---

## Phase 0 — The Big Picture

- **Data engineering lifecycle** `[P0]` — the stages every data system passes through: generation → ingestion → storage → transformation → serving (with security, orchestration, DataOps as undercurrents). The skeleton this whole framework hangs on. (Your `sources/de-lifecycle-reference.md` walks it in project order.)
- **OLTP vs OLAP** `[P0]` — *OLTP* (online transaction processing): many small reads/writes of single rows — the app's database. *OLAP* (online analytical processing): few large scans aggregating millions of rows — the analytics side. Data engineering largely exists to move and reshape data from OLTP-shaped systems into OLAP-shaped ones.
- **ETL vs ELT** `[P0]` — both move data. *ETL*: transform **before** loading (classic warehouses, schema-on-write). *ELT*: load raw first, transform **inside** the platform (modern default — storage is cheap, and raw data retained = reprocessable).
- **Batch vs streaming** `[P0]` — *batch*: process data in scheduled chunks (hourly/daily) — simpler, cheaper, the workhorse. *Streaming*: process events continuously within seconds — needed only when a consumer genuinely needs fresh data. Rule: default to batch, justify streaming.
- **Data warehouse vs data lake vs lakehouse** `[P0]` — *warehouse*: structured, schema-on-write, SQL-optimized (Redshift, Snowflake). *Lake*: raw files in object storage, schema-on-read, flexible but ungoverned. *Lakehouse*: lake storage + a **table format** that adds warehouse guarantees (ACID, schema evolution) — the 2026 default architecture.
- **Schema-on-write vs schema-on-read** `[P0]` — enforce structure when data is **written** (warehouse) vs when it is **queried** (lake). Determines where your transformation effort goes.
- **Row-oriented vs column-oriented storage** `[P0]` — rows: fast to write/fetch one record (OLTP). Columns: fast to scan one field across millions of records, compresses far better (OLAP). Why Parquet/ClickHouse/Redshift are columnar.
- **Data pipeline** `[P0]` — any automated path data takes from source to consumer. *Contrast:* a script you run by hand is not a pipeline until it's scheduled, retried, and monitored.
- **Medallion architecture (bronze/silver/gold)** `[P0]` — layering convention: *bronze* = raw as-landed, *silver* = cleaned/typed/deduplicated, *gold* = business-ready marts. Same idea as dbt's staging → intermediate → marts.
- **Idempotency** `[P0]` — a job you can safely run twice and get the same result (no duplicates, no double-counting). The single most important pipeline property; every spine job must have it.

## Phase 1 — Files, Local Engines, dbt

- **Parquet** `[P1]` — the universal columnar file format for analytics: column pruning (read only needed columns), predicate pushdown (skip irrelevant chunks), heavy compression. *Contrast:* CSV/JSON are row-oriented text — fine for interchange, terrible for analytics at scale.
- **Predicate pushdown / column pruning** `[P1]` — query engines skipping data *before* reading it: pushdown skips row-groups/partitions failing the WHERE clause; pruning reads only referenced columns. Why Parquet + partitioning = 99% cost cuts.
- **Partitioning (storage)** `[P1]` — physically splitting data by a column's value (e.g., `year=2026/month=08/` folders) so queries touching one slice read one slice. *Contrast with (Spark) partitions* `[P3]`: chunks of data distributed across workers during computation.
- **DuckDB** `[P1]` — an in-process analytical SQL engine ("SQLite for analytics"): queries Parquet/CSV files directly, no server. Your local development warehouse.
- **Polars** `[P1]` — a fast Rust-based DataFrame library (pandas replacement) built on Apache Arrow. Use when Python-native transforms beat SQL.
- **Apache Arrow** `[P1]` — the in-memory columnar format tools use to share data without conversion; the reason DuckDB/Polars/pandas interoperate cheaply.
- **Table format (Iceberg / Delta Lake)** `[P1]` — a metadata layer on top of Parquet files that turns "a folder of files" into "a table" with ACID transactions, schema evolution, time travel, and hidden partitioning. *Iceberg* won the open-format war; *Delta* dominates inside Databricks. *Contrast:* a file format (Parquet) says how bytes are laid out in one file; a table format says which files form a table and what changed when.
- **ACID transactions** `[P1]` — atomic/consistent/isolated/durable writes: readers never see a half-written table. What table formats add to object storage.
- **Time travel** `[P1]` — querying a table *as of* an earlier snapshot/version. Free with Iceberg/Delta; used for debugging, audits, and validating incremental loads.
- **Schema evolution** `[P1]` — adding/renaming/dropping columns without rewriting data or breaking readers. Design for it on day one; retrofitting is painful.
- **Catalog (data catalog / metastore)** `[P1]` — the registry that maps table names → schemas → file locations, so engines can find tables. Local: Iceberg REST catalog / SQLite. AWS: Glue Data Catalog. Databricks: Unity Catalog.
- **dbt** `[P1]` — the transformation framework: SQL SELECT statements as version-controlled, testable, documented **models** with dependencies via `ref()`. Brings software-engineering discipline to SQL.
- **dbt model / source / seed / test / materialization** `[P1]` — *model*: one SELECT → one table/view. *Source*: declared raw input. *Seed*: small CSV loaded as a table. *Test*: assertion (unique, not_null, relationships, accepted_values). *Materialization*: how a model persists — view, table, **incremental**, ephemeral.
- **Staging → intermediate → marts** `[P1]` — dbt's three layers: staging (1:1 with sources, rename/type only) → intermediate (reusable joins/logic) → marts (business-ready facts/dims). Two layers are never enough — every real team added the third within a year.
- **Incremental model** `[P1→P2]` — a dbt model that processes only new/changed rows on each run, using a `unique_key` + strategy (append / merge / insert_overwrite). The most-asked dbt interview topic.
- **Lineage (data lineage)** `[P1]` — the traceable graph of where data came from and what transformed it. dbt docs give it within the dbt project; OpenLineage `[P6]` standardizes it across tools.

## Phase 2 — AWS Lakehouse Core

- **Object storage (S3)** `[P2]` — durable, cheap, schemaless byte buckets. The lakehouse's physical layer. *Contrast:* a filesystem has directories and append; object stores have keys and whole-object writes — why table formats exist.
- **S3 Tables** `[P2]` — AWS's *managed Iceberg* service: table buckets with automatic compaction, snapshot expiry, and an Iceberg REST catalog endpoint. The spine's curated layer.
- **AWS Glue (three faces)** `[P2]` — one brand, three tools: **Glue Data Catalog** (the metastore Athena/EMR/Redshift Spectrum all read), **Glue Crawlers** (schema inference over S3), **Glue ETL** (serverless Spark jobs).
- **Athena** `[P2]` — serverless SQL over S3 (Trino-based), billed **per TB scanned** ($5/TB). Partitioning + Parquet directly cut your bill. The spine's query engine.
- **dbt adapter (dbt-duckdb / dbt-athena / dbt-databricks)** `[P2]` — the plugin that runs the same dbt project against a different engine. Same models, different warehouse — dbt's portability superpower.
- **Partition projection** `[P2]` — Athena feature: compute partition values from a pattern instead of enumerating them in the catalog — avoids slow/stale partition metadata.
- **CTAS** `[P2]` — `CREATE TABLE AS SELECT`: materialize query results as a new (Parquet/Iceberg) table. Athena's workhorse for building curated tables.
- **Lake Formation** `[P2]` — AWS's fine-grained permission layer (database/table/column/row grants) over the Glue Catalog + S3. How a lake becomes *governed*.
- **Data zones (raw/curated)** `[P2]` — S3 bucket/prefix separation mirroring bronze/silver/gold. Raw is immutable; everything downstream is reproducible from it.
- **Compaction / small-files problem** `[P2]` — streaming and incremental writes create thousands of tiny files; engines slow to a crawl listing/opening them. Fix: periodic rewrite into larger files (S3 Tables does it automatically; know why).
- **Snapshot expiration** `[P2]` — deleting old table-format snapshots (and orphaned files) so storage doesn't grow forever. The other half of table maintenance.
- **Backfill** `[P2]` — re-running a pipeline over a historical range. Must be idempotent — running a backfill twice must not duplicate data.

## Phase 3 — Spark & Databricks

- **Apache Spark / PySpark** `[P3]` — the dominant distributed compute engine: a driver plans work, executors process **partitions** of data in parallel. PySpark is its Python API.
- **Lazy evaluation / transformations vs actions** `[P3]` — Spark records transformations (select, filter, join) into a plan and executes nothing until an **action** (count, write, show) forces it. Lets the optimizer see the whole plan first.
- **Shuffle** `[P3]` — redistributing rows across executors so matching keys co-locate (joins, groupBys). The most expensive thing Spark does; most tuning is shuffle avoidance.
- **Data skew** `[P3]` — some keys are vastly more frequent, so one partition/worker gets most of the data and everyone waits for it. Fixes: broadcast join, salting, AQE.
- **Broadcast join** `[P3]` — copy the small table to every executor so the big table never shuffles. First tool against skewed joins.
- **AQE (Adaptive Query Execution)** `[P3]` — Spark re-optimizing mid-job using real statistics (coalescing partitions, switching join strategies, splitting skewed partitions).
- **Spark UI** `[P3]` — the web console showing jobs → stages → tasks, shuffle sizes, spill, skew. Reading it is the interview filter for Spark roles.
- **Delta Lake** `[P3]` — Databricks' table format (transaction log `_delta_log`, MERGE, time travel, OPTIMIZE). Conceptually ≈ Iceberg; UniForm makes Delta readable *as* Iceberg.
- **MERGE (upsert)** `[P3]` — one statement that updates matching rows and inserts new ones. The mechanism behind CDC application and SCD dimensions in the lakehouse.
- **Unity Catalog (UC)** `[P3]` — Databricks' governance layer: three-level namespace (catalog.schema.table), grants, row/column security, lineage. The current exam assumes UC everywhere.
- **Lakeflow** `[P3]` — Databricks' 2025+ umbrella brand: **Lakeflow Connect** (ingestion connectors), **Lakeflow Jobs** (orchestration, ex-Workflows), **Lakeflow Spark Declarative Pipelines** (ex-Delta Live Tables: declare tables + expectations, the engine handles the how).
- **Auto Loader / COPY INTO** `[P3]` — Databricks incremental file ingestion: Auto Loader streams new files with schema inference/evolution; COPY INTO is its batch SQL cousin.
- **Liquid Clustering** `[P3]` — Delta's replacement for fixed partitioning/ZORDER: the engine incrementally re-clusters data by chosen keys.
- **Asset Bundles (Databricks)** `[P3]` — YAML-defined deployable units (jobs, pipelines, code) promoted dev → prod via the Databricks CLI: CI/CD for Databricks.
- **Serverless vs classic compute** `[P3]` — Databricks-managed instant compute vs self-configured clusters. Free Edition is serverless-only; the exam still asks classic-cluster questions — learn the concepts.

## Phase 4 — Orchestration & Ingestion

- **Orchestrator** `[P4]` — the system that runs pipelines on schedule/events with dependencies, retries, backfills, and alerting. *Contrast:* cron runs commands; an orchestrator manages a **graph** with state.
- **DAG** `[P4]` — directed acyclic graph: tasks + dependencies, no cycles. Airflow's unit of scheduling.
- **Airflow 3.x** `[P4]` — the industry-standard orchestrator, heavily modernized in 2025: new UI, **DAG versioning**, **assets** (data-aware, event-driven scheduling), Task SDK. Learn 3.x; 2.x-only tutorials mislead.
- **Task-based vs asset-based orchestration** `[P4]` — Airflow classically models *what runs* (tasks); Dagster models *what exists* (assets — tables/files with freshness and lineage). Airflow 3's assets close part of the gap. Knowing both philosophies is a senior-level conversation.
- **Sensor / trigger** `[P4]` — a task that waits for a condition (file lands, table updates) instead of a clock. The bridge from scheduled to event-driven pipelines.
- **XCom** `[P4]` — Airflow's small-value message-passing between tasks (pass a date or path, never a dataset).
- **MWAA** `[P4]` — Managed Workflows for Apache Airflow: AWS-hosted Airflow (now 3.x). Costly to leave running (~$350+/mo baseline) — learn Airflow locally; know MWAA for the exam.
- **dlt (data load tool)** `[P4]` — declarative Python ingestion library: REST/database sources with pagination, incremental cursors, schema inference, merge dispositions — replaces hand-rolled extract scripts. The breakout ingestion tool of this cycle.
- **CDC (change data capture)** `[P4]` — replicating a database by tailing its transaction log (inserts/updates/deletes as events) instead of re-querying tables. *Contrast:* batch extract re-reads state; CDC streams **changes**.
- **AWS DMS** `[P4]` — AWS's managed migration/CDC service: full-load + ongoing replication from a source DB to S3/targets. The AWS-native CDC answer (Debezium `[P5]` is the open-source one).
- **Kinesis Data Streams vs Firehose** `[P4]` — *Streams*: the durable shard-based event stream you write consumers against. *Firehose*: the zero-admin delivery hose that buffers and lands events into S3/Iceberg/Redshift. Exam favorite distinction.
- **Step Functions / EventBridge** `[P4]` — AWS serverless micro-orchestration: EventBridge routes events/schedules; Step Functions runs state machines. When a full Airflow is overkill.
- **Redshift / Redshift Spectrum / Serverless** `[P4]` — AWS's warehouse; Spectrum queries S3 data from Redshift (hot-in-warehouse, cold-on-S3 pattern); Serverless bills per-use. Heavy on the DEA exam.
- **Distribution key / sort key** `[P4]` — Redshift table design: DISTKEY controls which node holds a row (bad key = built-in skew); SORTKEY orders data for range-scan pruning.

## Phase 5 — Streaming & CDC (Open Source)

- **Kafka** `[P5]` — the distributed event log: producers append to **topics** split into **partitions**; **consumer groups** read with tracked **offsets**. The backbone of event streaming. 4.x is **KRaft-only** (ZooKeeper is gone — pre-2025 ops tutorials are obsolete).
- **Topic / partition / offset / consumer group** `[P5]` — topic: named stream. Partition: ordered shard (parallelism unit). Offset: a consumer's position. Consumer group: consumers sharing work, each partition owned by one member.
- **Redpanda** `[P5]` — Kafka-API-compatible single-binary broker; the friction-free local Kafka for development.
- **Kafka Connect** `[P5]` — Kafka's connector runtime: source connectors (e.g., Debezium) pull data in; sink connectors write out (e.g., to S3/Iceberg) — no custom code.
- **Debezium** `[P5]` — the open-source CDC engine: tails Postgres WAL / MySQL binlog and emits row-change events to Kafka. *Contrast with DMS:* transferable mechanics + full control vs managed convenience.
- **Delivery guarantees (at-least-once / exactly-once)** `[P5]` — whether duplicates can appear downstream. Practical answer everywhere: at-least-once delivery + **idempotent writes** = effectively exactly-once results.
- **Event time vs processing time & watermarks** `[P5]` — when the event *happened* vs when the system *saw* it. A **watermark** is the engine's moving claim "all events up to T have arrived," which lets time-windows close despite late data. The concept that separates streaming engineers from batch engineers.
- **Flink** `[P5]` — the reference engine for *stateful* stream processing (event-time windows, exactly-once state). This framework: one Flink SQL lab — semantics, not operations.
- **Tombstone** `[P5]` — a null-value record marking a key as deleted; how CDC streams communicate deletions.
- **Outbox pattern** `[P5]` — app writes business row + event row in one DB transaction; CDC ships the event table — solving dual-write inconsistency.
- **Diskless/object-storage streaming (WarpStream-style)** `[P5]` — brokers that persist directly to S3, trading latency for 10x cost cuts. Concept to know; the direction high-volume streaming is moving.

## Phase 6 — Production, Serving & Quality

- **Data quality dimensions** `[P6]` — completeness, uniqueness, validity, accuracy, consistency, timeliness. Note *validity* (conforms to rules) ≠ *accuracy* (matches reality).
- **dbt tests vs dbt-expectations vs Elementary** `[P6]` — dbt tests: schema/constraint assertions in the project. dbt-expectations (metaplane fork): distributional/statistical tests as dbt macros. Elementary: a dbt package adding anomaly detection, test history, and an observability report + Slack alerts. Together: the 2026 lakehouse quality stack. (Great Expectations: know the vocabulary; the product was acquired/reset in 2026.)
- **Data observability** `[P6]` — monitoring data health (freshness, volume, schema, distribution anomalies) the way DevOps monitors services. *Contrast:* testing asserts what you predicted; observability catches what you didn't.
- **Data contract** `[P6]` — an explicit, versioned schema+semantics agreement between producer and consumer, enforced in CI so breaking changes fail the PR, not the 3am dashboard. dbt **model contracts** enforce column names/types on build.
- **OpenLineage / Marquez** `[P6]` — the open standard for emitting lineage events (job/run/dataset) across tools (Airflow provider, Spark, dbt); Marquez is its reference server/UI.
- **Infrastructure as Code / Terraform** `[P6]` — declaring cloud resources in versioned files; `plan` shows the diff, `apply` converges reality. *Contrast:* console click-ops is unreproducible. (OpenTofu = the compatible open fork; skills transfer 1:1.)
- **Terraform state / drift** `[P6]` — the recorded mapping of config → real resources; *drift* is reality diverging from it (someone clicked in the console).
- **ClickHouse** `[P6]` — the dominant open-source real-time OLAP engine (MergeTree storage): sub-second aggregations over billions of rows. Role in this framework: the **serving/speed layer** fed *from* the lakehouse gold marts — not a warehouse replacement.
- **Serving layer vs lakehouse** `[P6]` — lakehouse: system of record + transformation substrate (seconds-to-minutes latency, cheap). Serving layer: a copy of hot marts in a low-latency engine for customer-facing dashboards. Add it only when a latency-sensitive consumer exists (the Tweeq lesson).
- **Apache Superset** `[P6]` — the standard open-source BI tool (SQL IDE + dashboards) — the visible front-end that makes portfolio pipelines demoable.
- **Embeddings / vector database / RAG** `[P6]` — *embedding*: text → numeric vector capturing meaning. *Vector DB* (pgvector = Postgres extension): stores vectors for similarity search. *RAG*: retrieve relevant chunks → feed the LLM as context. The DE's role: the **pipeline** that turns raw documents into fresh, deduplicated, chunked, embedded rows — a normal pipeline with a new sink.
- **Semantic layer** `[P6]` — governed metric definitions ("revenue means *this*") exposed to BI/AI tools so every consumer computes numbers the same way (dbt MetricFlow, Cube). Awareness level.
- **SLA / SLO (for data)** `[P6]` — the promise ("gold marts fresh by 07:00") and the measured objective behind it; what your alerts should actually track.

---

*Missing a term you hit during a build? Add it here in the same format, tagged with the phase — maintaining this glossary is itself Phase-0-gate behavior.*
