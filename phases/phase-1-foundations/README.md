# Phase 1 — Foundations: SQL, Python & the Local Lakehouse

**Duration:** months 1–2 · **Budget:** ~70 hours · **AWS cost:** $0 — everything runs on your laptop

The old 30-project plan crammed this phase's content into "Week 1" and it overwhelmed. Here it gets two months, a learn-first rhythm, and one dataset carried end-to-end. By the gate you will have personally operated every layer of a lakehouse — storage, table format, engine, transformation — small enough to fit in your head.

## Objectives

1. Analytical SQL at interview strength (window functions, CTEs, performance intuition).
2. DE-flavored Python: API extraction, files, DuckDB/Polars transforms, tests.
3. Understand what a **table format does** by operating Iceberg locally.
4. A real 3-layer dbt project with tests and docs — the skill you'll reuse in every later phase.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P1]`

Parquet internals (pushdown/pruning) · partitioning · DuckDB · Polars · Arrow · **table format** · ACID · time travel · schema evolution · catalog · dbt (model/source/seed/test/materialization) · staging→intermediate→marts · incremental model · lineage.

## Learn (~28 h)

| Resource | Scope | Hours |
|---|---|---|
| [DataLemur SQL tutorial](https://datalemur.com/sql-tutorial) — start at [window functions](https://datalemur.com/sql-tutorial/sql-aggregate-window-functions) | Windows, CTEs, then free question bank | 8 |
| [Python Essentials for Data Engineers](https://www.startdataengineering.com/post/python-for-de/) (updated Jul 2026) | Full tutorial + exercises | 8 |
| [DuckDB docs](https://duckdb.org/docs/) friendly-SQL + Parquet pages; [Polars getting started](https://docs.pola.rs/) | Working level; Polars = half a day | 4 |
| [*Apache Iceberg: The Definitive Guide*](https://www.dremio.com/guides/apache-iceberg-the-definitive-guide/) (free) | Ch. 1–4 (architecture, metadata, why it exists) | 4 |
| [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) (free, grab the badge) — prefer the [VS Code variant](https://learn.getdbt.com/courses/dbt-fundamentals-vs-code) | Full course | 4 |

*Before starting, re-verify:* course editions (dbt Learn reorganizes periodically), DuckDB major version (v2.0 was in preview Aug 2026).

## Build — Spine v0.1: the local lakehouse (~25 h)

Repo: `aws-lakehouse-platform` (yes, even while local — the platform story starts here).

1. **Ingest** (Python + uv project, typed, tested): downloader for 6+ months of NYC TLC taxi Parquet + the taxi-zone lookup CSV → lands files in a `data/raw/` zone, partitioned by `year/month`. Idempotent: re-running never duplicates.
2. **Table format:** register the raw data as an **Iceberg** table with [PyIceberg](https://py.iceberg.apache.org/) (SQLite catalog is fine locally). Exercise the format deliberately: add a column (schema evolution), overwrite one month (snapshot), query the previous snapshot (time travel). *This drill is the point of the phase.*
3. **Transform:** a **dbt-duckdb** project with the three layers — `staging` (rename/type), `intermediate` (zone joins, trip enrichment), `marts` (e.g., `fct_trips`, `dim_zones`, `mart_daily_revenue`) — plus ≥25 tests (unique/not_null/relationships/accepted_values) and generated docs.
4. **Demo:** `make demo` runs ingest → dbt build → prints three benchmark queries with timings; `dbt docs serve` shows the lineage graph.
5. **README** with an architecture diagram (mermaid is fine) and a *decisions* section: why Parquet, why Iceberg, why DuckDB. The written reasoning is what gets interviews.

**Lab (half-day):** rewrite one intermediate transformation in Polars; note where SQL vs DataFrame ergonomics win. **Reading (1 h):** DuckLake — what it is, why it exists; awareness only.

**AI rule:** scaffold the project structure and Makefile with Claude Code; **hand-type every dbt model and the PyIceberg drill** — the syntax needs to live in your hands for interviews.

## Build — Satellite S1: your first standalone dbt project (~15 h)

*(Recycled from old plan Week 2, re-scoped.)* Separate repo. Pick a relational public dataset you like (Hacker News dump is proven; anything with 3+ related entities works). Load to DuckDB → 3-layer dbt project → 20+ models, 40+ tests, docs published via GitHub Pages. One custom generic test (e.g., `not_a_future_timestamp`).

This satellite exists so you experience starting a dbt project *from zero* twice — once guided (spine), once alone.

## Competency gate G1

- [ ] **Named artifact:** `make demo` works on a fresh clone of the spine; dbt docs lineage graph screenshot in the README.
- [ ] Satellite repo public with docs site live.
- [ ] SQL check: ≥40 of [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) solved (or DataLemur equivalent).
- [ ] Iceberg drill demo: schema-evolve + time-travel, narrated in 2 minutes.
- [ ] **Retrieval checkpoint:** re-quiz 10 random `[P0]` terms + 15 `[P1]` terms (≥80%).

## Publish checkpoint

Post: the local lakehouse — "I queried N million taxi trips on my laptop with an open table format; here's what a lakehouse actually is," with the lineage graph image. Draft it from your README's decisions section.

## Interview questions you can now answer

- "What does a table format add on top of Parquet?"
- "Walk me through your dbt project structure and why staging exists."
- "What makes an incremental load idempotent?"
- "DuckDB vs Spark — when is each the right tool?"
