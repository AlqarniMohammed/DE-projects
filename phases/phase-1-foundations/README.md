# Phase 1 — Foundations

**Duration:** months 1–2 · **Budget:** ~70 hours · **AWS cost:** $0 — everything runs on your laptop

Two months, a learn-first rhythm, one dataset carried end-to-end. By the gate you will have personally operated every layer of a lakehouse — storage, table format, engine, transformation — small enough to fit in your head.

## Objectives

1. Analytical SQL at interview strength (window functions, CTEs, performance intuition).
2. DE-flavored Python: API extraction, files, DuckDB/Polars transforms, tests.
3. Understand what a **table format does** by operating Iceberg locally.
4. A real 3-layer dbt project with tests, docs, and an SCD2 dimension — the skill you'll reuse in every later phase.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P1]`

Parquet internals (pushdown/pruning) · partitioning · DuckDB · Polars · Arrow · **table format** · ACID · time travel · schema evolution · catalog · dbt (model/source/seed/test/materialization) · staging→intermediate→marts · incremental model · lineage · **and the modeling cluster:** fact vs dimension · grain · SCD1 vs SCD2 · dbt snapshot · conformed dimension · star schema vs One Big Table.

## Learn (~28 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [DataLemur SQL tutorial](https://datalemur.com/sql-tutorial) — start at [window functions](https://datalemur.com/sql-tutorial/sql-aggregate-window-functions) | Windows, CTEs, then the free question bank | 8 | Gate check: ≥40 of LeetCode SQL 50 solved (or ≥40 comparable DataLemur medium questions) |
| [Python Essentials for Data Engineers](https://www.startdataengineering.com/post/python-for-de/) (updated Jul 2026) | Full tutorial + exercises | 8 | The tested-ingester assignment (build step 1) |
| [DuckDB docs](https://duckdb.org/docs/) friendly-SQL + Parquet pages; [Polars getting started](https://docs.pola.rs/) | Working level; Polars = half a day | 4 | `make demo` benchmark queries + the Polars lab |
| [*Apache Iceberg: The Definitive Guide*](https://www.dremio.com/guides/apache-iceberg-the-definitive-guide/) (free) | Ch. 1–4 (architecture, metadata, why it exists) | 4 | The Iceberg drill: schema evolution + time travel, narrated |
| [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) (free, grab the badge) — prefer the [VS Code variant](https://learn.getdbt.com/courses/dbt-fundamentals-vs-code) | Full course | 4 | The platform's 3-layer dbt project + satellite S1 from zero |

**Video lane — optional swap.** Each row below **replaces** the default row it names: same "Pinned by" exercise, hours swap rather than add. Pick one lane per row before starting ([the rule](../../GUIDE.md#the-phase-loop)); prices, details, and the rows with no video twin: [COURSES.md](../../reference/COURSES.md).

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Dremio University: Apache Iceberg courses](https://university.dremio.com/course/apache-iceberg) (free) | Swaps the *Apache Iceberg: The Definitive Guide* ch. 1–4 row — the same architecture/metadata ground in course form | 3–4 | The Iceberg drill: schema evolution + time travel, narrated |
| [calmcode.io Polars series](https://calmcode.io/course/polars/introduction) (free) | Swaps only the **Polars half** of the DuckDB/Polars row; the DuckDB friendly-SQL + Parquet pages stay either way | 1–2 | `make demo` benchmark queries + the Polars lab |

*Before starting, re-verify:* course editions (dbt Learn reorganizes periodically), DuckDB major version (v2.0 was in preview Aug 2026).

## Build — Platform v0.1: the local lakehouse (~25 h)

Repo: `aws-lakehouse-platform` (yes, even while local — the platform story starts here).

1. **Ingest** (Python + uv project, typed, tested): downloader for 6+ months of NYC TLC taxi Parquet + the taxi-zone lookup CSV → lands files in a `data/raw/` zone, partitioned by `year/month`. Idempotent: re-running never duplicates.
2. **Table format:** register the raw data as an **Iceberg** table with [PyIceberg](https://py.iceberg.apache.org/) (SQLite catalog is fine locally). Exercise the format deliberately: add a column (schema evolution), overwrite one month (snapshot), query the previous snapshot (time travel). *This drill is the point of the phase.*
3. **Transform:** a **dbt-duckdb** project with the three layers — `staging` (rename/type), `intermediate` (zone joins, trip enrichment), `marts` (e.g., `fct_trips`, `dim_zones`, `mart_daily_revenue`) — plus ≥25 tests (unique/not_null/relationships/accepted_values) and generated docs. **Note:** dbt's sources read the raw **Parquet** directly; the Iceberg registration in step 2 is the table-format drill, not dbt's input (DuckDB can't attach a PyIceberg SQLite catalog — knowing why is part of the lesson).
4. **Dimensional modeling, shown not assumed:** a **dbt snapshot** making `dim_zones` a documented **SCD2 dimension** (interviews hit this hard, and work never gets credit for an invisible strength), plus a short `MODELING.md` in the platform repo — a grain statement per fact table, a conformed-dimension note, and one honest star-schema-vs-One-Big-Table paragraph. The `[P1]` modeling cluster in the glossary gives you every term this step uses.
5. **Demo:** `make demo` runs ingest → dbt build → prints three benchmark queries with timings; `dbt docs serve` shows the lineage graph.
6. **README** with an architecture diagram (mermaid is fine) and a *decisions* section: why Parquet, why Iceberg, why DuckDB. The written reasoning is what earns credibility.

**Standing rule from here to P6 — work via PRs:** every platform change is branch → PR → self-review checklist → squash-merge, even solo. Zero extra hours; a year of PR history reads as an operated platform, not a tutorial, and P6's contract-blocks-a-breaking-PR demo becomes a natural extension instead of a first.

**Lab (half-day):** rewrite one intermediate transformation in Polars; note where SQL vs DataFrame ergonomics win (`notes/p1-polars-vs-sql.md` in the platform repo). Include one **Arrow drill cell**: hand the same data DuckDB → Arrow → Polars with zero copies, and print the memory addresses that prove it — that's what Arrow *is*. **Reading (1 h):** DuckLake — what it is, why it exists; one-paragraph note in `notes/`.

### Prove-it assignment (folded into build step 1): the tested ingester

"Typed, tested" is a claim — prove it: a pytest suite for the downloader covering the happy path, a corrupted-file retry, and the **idempotency property** (run twice → identical file inventory, no duplicates). This suite is what P2 extends with moto against real S3.

**AI rule:** scaffold the project structure and Makefile with your assistant; **hand-type every dbt model and the PyIceberg drill** — the syntax needs to live in your hands.

## Build — Satellite S1: your first standalone dbt project (~15 h)

Separate repo. Pick a relational public dataset from the S1 menu in [`DATASETS.md`](../../reference/DATASETS.md) (the Hacker News dump is the proven default; anything with 3+ related entities works). Load to DuckDB → 3-layer dbt project → 20+ models, 40+ tests, docs published via GitHub Pages (run `dbt docs generate`, then publish the output — commit `target/` to a `gh-pages` branch or upload it with an Actions artifact step). One custom generic test (e.g., `not_a_future_timestamp`). Want a unique, realistic brief instead? Use the `/satellite-brief` skill or [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

This satellite exists so you experience starting a dbt project *from zero* twice — once guided (platform), once alone.

## Competency gate G1

- [ ] **Named artifact:** `make demo` works on a fresh clone of the platform repo; dbt docs lineage graph screenshot in the README.
- [ ] `MODELING.md` written · SCD2 snapshot demonstrated (change a zone name, show both versions).
- [ ] Ingester pytest suite green (incl. the idempotency property test).
- [ ] Platform history shows the PR workflow (≥3 merged PRs by gate time).
- [ ] Satellite repo public with docs site live.
- [ ] SQL check: ≥40 of [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) solved (or ≥40 comparable DataLemur medium questions).
- [ ] Iceberg drill demo: schema-evolve + time-travel, narrated in 2 minutes.
- [ ] `SELF-CHECK.md` started in the platform repo: 3–5-sentence written answers to this phase's check-yourself questions, evidence linked.
- [ ] **Retrieval checkpoint:** all `[P1]` terms + 10 random `[P0]` terms, ≥80% (the `/quiz` skill runs this).
- [ ] Phase post published (see the publish checkpoint below).

## Publish checkpoint

Post (any public platform): the local lakehouse — "I queried N million taxi trips on my laptop with an open table format; here's what a lakehouse actually is," with the lineage graph image. Draft it from your README's decisions section.

## Check yourself — questions you can now answer

- "What does a table format add on top of Parquet?"
- "Walk me through your dbt project structure and why staging exists."
- "What makes an incremental load idempotent?"
- "SCD1 vs SCD2 — what changes, and when is each right?"
- "DuckDB vs Spark — when is each the right tool?"

---
← [Phase 0 — Orientation & Setup](../phase-0-orientation/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 2 — AWS Lakehouse Core →](../phase-2-aws-lakehouse-core/README.md)**
