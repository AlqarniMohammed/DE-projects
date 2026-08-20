# Research Report — Real-World Data Platform Build Journeys
*Research date: 2026-08-20. For: design of a 12-month personal data-platform build (AWS Lakehouse spine: S3 + Iceberg + Glue/Athena + dbt + orchestrator, plus open-source satellites). The primary Medium article was Cloudflare-blocked to direct fetch; full text retrieved via a reader proxy (published 2024-05-16, author Atheer Alabdullatif, Tweeq Engineering).*

---

## Section 1 — Primary Source: Tweeq Data Platform (Saudi fintech)

**Source:** [Tweeq Data Platform: Journey and Lessons Learned — ClickHouse, dbt, Dagster, and Superset](https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904) (May 16, 2024)

### 1.1 Requirements that drove the design (verbatim from the article)

Tweeq (a Saudi spend-management fintech) started from explicit constraints, not tools:

- "hosted within the region to comply with regulatory requirements" (Saudi data residency)
- "cloud agnostic for future cloud provider migration"
- "optimised for analytical usage, including: customer-facing/in-app analytics and Business intelligence (BI)/Data analytics"
- "utilise open-source tools"
- "highly available and support data replication by storing data in multiple nodes"
- "achieve some level of observability"

Key architectural driver: Tweeq runs microservices, so "data is distributed across service-level databases, which make joining the tables for any customer-facing features an expensive operation, thus the choice to relay in the data warehouse for any feature that requires data join/aggregation." Their warehouse is not just BI — it is a **production backend for in-app features**.

### 1.2 The stack and why each piece was chosen

| Layer | Tool | Why |
|---|---|---|
| Warehouse/storage | **ClickHouse** (self-hosted on K8s via Altinity Operator) | Column store needed for customer-facing analytics; "AWS & GCP tools such as Redshift & BigQuery were out of question" due to regional residency + cloud-agnosticism; Altinity K8s Operator made it "a cloud agnostic data warehouse" |
| Ingestion | **CockroachDB CDC changefeeds → Kafka → ClickHouse Kafka Engine tables** | CDC is "out of the box" in CockroachDB; Kafka acts as "a buffer layer"; ClickHouse Kafka Engine tables "helped us avoid using any third-party sink tools" |
| Load philosophy | **EtLT** | "we ship the raw data without any manipulation except for discarding some PII data" — small "t" is PII-stripping only, real transformation happens post-load |
| Modeling | **dbt** — dimensional modeling (facts, dimensions, data marts) | Incremental models for freshness; seeds "to create a local mock for testing"; analysts "have the freedom to create their own data marts" |
| Orchestration | **Dagster** | "developed specifically for data pipelines, integrates super smoothly with dbt, can be deployed on top of K8s, has a data lineage feature, and an easy to use UI." Tags separate freshness tiers; sensors push failures to Slack |
| BI | **Superset** (+ **PostHog** for product analytics) | Open source, K8s-deployable, GoogleAuth integration |

Two freshness tiers: customer-facing models refresh **every 5 minutes**; warehouse/BI models **at least daily** — separated with Dagster tags.

### 1.3 What they tried/considered and abandoned

- **Redshift and BigQuery**: rejected up front (residency + lock-in), not abandoned mid-flight.
- **Multi-node dbt→ClickHouse writes**: "we faced issues with having dbt write to a ClickHouse cluster. We had to make some compromises by storing the data in one node, which was later fixed in newer dbt versions" — they temporarily sacrificed their own HA requirement because of adapter immaturity.
- **Third-party sink tools** (Kafka Connect-style sinks): deliberately avoided via ClickHouse Kafka Engine — but this bought a new problem (below).

### 1.4 Explicit lessons learned (all of them)

1. **Kafka Engine schema-change pain:** "one of the main limitations of Kafka Engine tables is managing schema changes, dropping and recreating the tables manually without down time can be a hectic process." (The no-third-party-sink shortcut has an operational tax.)
2. **dbt-ClickHouse adapter maturity:** early cluster-write issues forced a single-node compromise; fixed in later versions. Lesson: adapter maturity is a real selection criterion, not a footnote.
3. **Dagster on K8s setup friction:** "The only downside of Dagster is the initial set up part on k8s, however the community is super helpful and responsive."
4. **Superset UX:** "The UI can be intimidating at first glance"; visualization options are "good enough" but they still **added PostHog** because a BI tool does not cover product analytics.
5. Implicit but clear: constraints-first design (residency, open source, cloud-agnostic) made every tool decision almost mechanical.

### 1.5 Build sequence, team, timeline

The article does **not** state team size or timeline (the author is a data engineer; the platform reads as a 1–3 person build typical of a Series-A fintech). Implied sequence: (1) CDC ingestion path (CockroachDB → Kafka → ClickHouse), (2) dbt dimensional models, (3) Dagster orchestration with freshness tiers + Slack alerting, (4) Superset/PostHog consumption layer.

---

## Section 2 — Comparable Case Studies (2023–2025)

### 2.1 Summary table

| # | Company / context | Stack | Team size | Standout numbers | Source(s) |
|---|---|---|---|---|---|
| 1 | **ClickHouse Inc.** — internal DWH for their own cloud business (2023, +1yr update 2024) | ClickHouse Cloud, Airflow, S3 raw staging, Superset, dbt (added yr 2), Docker | **3 people** (1 FT DE, 1 analyst, 1 lead at ~30%) | ~$1,500/mo infra; 40k queries/day; 70+ MAU; yr 2: 19 sources, 6B rows/day, 470TB compressed | [Part 1](https://clickhouse.com/blog/building-a-data-warehouse-with-clickhouse), [Part 2](https://clickhouse.com/blog/building-a-data-warehouse-with-clickhouse-part-2) |
| 2 | **Zippi** — Brazilian YC fintech | Hevo → S3 → Redshift, dbt Core, Dagster, Hex/Metabase, Metaplane | Startup-scale, small data team | Adopted Dagster for ML first, then pulled dbt + ingestion under it | [Dagster case study](https://dagster.io/blog/zippi-case-study) (vendor) |
| 3 | **UK Ministry of Justice** — government analytical platform (Oct 2024) | **S3 + Parquet + Iceberg + Athena + Glue Catalog + dbt-core (dbt-athena)**, GitHub Actions orchestration, medallion layers | Public-sector DE team (small) | "99% reduction in individual query costs" vs Glue PySpark; longest jobs −75%; tables ≤200GB/~3B rows | [MoJ blog](https://ministryofjustice.github.io/data-and-analytics-engineering/blog/posts/building-a-transaction-data-lake-using-amazon-athena-apache-iceberg-and-dbt/) |
| 4 | **Halodoc** — Indonesian healthtech (2021–22; closest real AWS-lakehouse journey with explicit lessons) | DMS CDC → S3 raw → EMR/PySpark + **Hudi** → S3 processed → Glue/Athena → Redshift marts; MWAA | Mid-size DE team | Framework-driven onboarding replaced per-pipeline builds; detailed Hudi tuning lessons | [Data Platform 2.0](https://blogs.halodoc.io/lake-house-architecture-halodoc-data-platform-2-0/), [Hudi learnings](https://blogs.halodoc.io/key-learnings-on-using-apache-hudi-in-building-lakehouse-architecture-halodoc/) |
| 5 | **jchandra (Indian SME-lending fintech)** — "modern data stack from scratch, bill −70%" (Mar 2025) | Debezium CDC → Kafka/Confluent → S3 + Parquet, Glue catalog, **Trino** + **DuckDB**, dbt, Great Expectations, Airflow, Metabase, medallion | ~2 people | $2,200/mo → ~$460/mo (~79% reduction) | [Article](https://jchandra.com/posts/data-infra/), [HN thread](https://news.ycombinator.com/item?id=43312199) |
| 6 | **UDisc** — bootstrapped disc-golf app | MongoDB (OLTP) → MotherDuck (DuckDB), Dagster, dbt, Hex | Small bootstrapped team | dbt job 6h → 30min; typical query 2min+ → 5s | [MotherDuck case study](https://motherduck.com/case-studies/udisc-motherduck-sports-management/) (vendor) |

### 2.2 Per-case notes

**Case 1 — ClickHouse internal DWH (the best "team of 3" benchmark).**
Built because their VP Product was analyzing cloud usage in Excel. Deliberate simplicity: **rejected CDC as "much more expensive"** than hourly batch extract-to-S3-then-load; 1-hour granularity ("real-time wasn't necessary at our stage"); ~$1,500/month total. Abandoned along the way: (a) a two-layer architecture — recursive mart dependencies forced an intermediate detail layer; (b) sophisticated Airflow DAG graphs — collapsed to per-source extract DAGs + one main DAG; (c) a year later, **the monolithic hourly DAG itself** — refactored into 9 processes managed with **dbt**, which they had originally deferred. Other lessons: idempotency via ReplacingMergeTree + re-runnable jobs as the foundation; `insert_quorum=3` (consistency over availability) with orchestrator retries; GDPR via masked row versions rather than deletes; users unexpectedly loved **raw, less-structured real-time logs**.

**Case 2 — Zippi (vendor case study; treat framing skeptically).**
Managed ingestion (Hevo) + Redshift + dbt Cloud first; hit a wall when ML scoring needed pipelines that "both write tables and then dynamically read back from those same tables." Adopted Dagster **incrementally**: ML jobs first, then dbt orchestration (gaining lineage), then replaced scattered cron/Python scripts. Pain that motivated it: "dbt Cloud alerts were very limited, with no context on the error." The *sequence* (managed EL + warehouse + dbt first, orchestrator when complexity demands it) is credible and matches non-vendor accounts.

**Case 3 — UK Ministry of Justice (the closest match to the AWS spine).**
Migrated from Glue PySpark jobs to **Athena + Iceberg + dbt-athena**, orchestrated by GitHub Workflows. Why: Athena is serverless and SQL-first; at their scale (≤500GB datasets) $5/TB-scanned is cheap; Iceberg gives ACID writes, row-level updates for SCD2, `RENAME TABLE` for write-audit-publish, time travel for validating incrementals. Results: "99% reduction in individual query costs," 75% faster longest jobs, weekly → daily refreshes. Honest caveats: they **started with full-refresh materializations, not incrementals**; dbt's one-model-per-table philosophy forced a Python model-generator for repeated logic; Athena per-query resource caps forced a custom `insert_by_chunk` materialization; native observability weak. Meta-lesson: a unified SQL stack "fosters a culture of collaboration"; cost advantage "may diminish… at the petabyte-scale."

**Case 4 — Halodoc (AWS lakehouse, hard-won table-format ops lessons).**
Platform 1.0 (timestamp-based batch replication) failed on cost and correctness. Platform 2.0: DMS CDC → S3 raw → EMR/PySpark writing **Hudi** → Glue catalog → Athena + Redshift marts, MWAA, Terraform. Biggest structural lesson: moving **from hand-built per-source pipelines to a config/framework-driven platform**. Hudi lessons that transfer to Iceberg: cleaner/retention policies or storage "would increase exponentially"; small-file compaction must be planned; CoW vs MoR effectively irreversible; millisecond-safe ordering needed DMS `ar_h_change_seq` as precombine key; enable the metadata table to avoid file-listing bottlenecks.

**Case 5 — jchandra fintech + the HN counter-narrative (the most instructive pairing).**
Two people replaced Hevo + BigQuery (~$2,200/mo) with Debezium/Kafka CDC → S3 Parquet (medallion) → Glue → Trino + DuckDB → dbt → Great Expectations → Airflow → Metabase. ~$460/mo after. Lessons: reuse infra you already pay for; cheap object storage makes ELT-with-raw-retention the default; early pragmatic choices must be re-architected at scale. **The HN thread is the required skepticism**: "$20k/year savings… doesn't seem like a good use of time"; "engineers who work on projects like these inevitably get bored and move on, and then the company is stuck"; and the sharpest — after making a pipeline work, "keeping it working, keeping it accurate and keeping it cheap comes next."

**Case 6 — UDisc (vendor case study; DuckDB-class engine as the whole warehouse).**
Analytics off MongoDB; dashboards capped at 30 days of data to protect the OLTP DB. Evaluated ClickHouse, Snowflake, Databricks, BigQuery, Postgres — "too expensive and too complex for our use case." Landed on MotherDuck + Dagster + dbt + Hex: dbt run 6h → 30min, queries 2min+ → 5s. Pattern corroborated by MoJ's Athena-over-Spark finding: at small-to-mid volumes a single-node vectorized engine beats distributed warehouses on cost *and* simplicity.

---

## Section 3 — Synthesis

### (a) Recurring build-order pattern

1. **Pain first, platform second.** Every build started from a concrete failing workload. Nobody built a platform speculatively.
2. **Ingestion + raw storage** (cheap durable storage — S3 in 5 of 7 cases; CDC only where the product needs it; ClickHouse Inc. explicitly rejected CDC as premature complexity).
3. **SQL transformation layer with layered modeling** (dbt in 6 of 7; medallion or facts/dims/marts in all). Both ClickHouse Inc. and MoJ learned the same lesson: **two layers are never enough** — an intermediate layer appears within a year whether planned or not.
4. **Orchestration** comes *after* transforms exist — typically after cron/one-DAG pain. Dagster where dbt-integration and lineage were the draw; Airflow where the team knew it; MoJ got away with GitHub Actions.
5. **BI/serving layer** (Superset, Metabase, Hex) once models are trustworthy.
6. **Only then**: observability, quality frameworks, lineage, self-service — universally "future work," rarely done in year one.

### (b) Most common mistakes and regrets

1. **The monolith DAG / linear pipeline** — decomposed within a year in two cases. Design for many small idempotent jobs from the start.
2. **Deferring dbt** — ClickHouse Inc. retrofitted it in year two for lineage, docs, decomposition. Everyone who had it early kept it.
3. **Underestimating table-format/streaming operations** — Tweeq's Kafka Engine schema pain, Halodoc's compaction learning curve, MoJ's Athena caps. The lakehouse's hidden cost is table maintenance, not queries.
4. **Trusting adapter/tool maturity claims** — Tweeq's dbt-ClickHouse compromise. Budget for immaturity in any adapter less mainstream than the big ones.
5. **Two-layer modeling** — independently regretted; preempted by medallion users.
6. **Over-engineering vs TCO blindness (the HN lesson)** — self-built stacks carry a maintenance annuity and bus-factor risk small teams rarely price in; the counter-mistake is staying on a mispriced managed service past the crossover point.
7. **Skipping data quality/observability until incidents force it** — dbt tests and Slack failure alerts were the cheap early wins.

### (c) The "minimum viable data platform" consensus

> **Batch extract (CDC only if the product demands it) → object storage/warehouse with raw data retained → dbt with three layers (staging → intermediate → marts) → one orchestrator with retries + Slack alerting → one open-source BI tool → idempotency everywhere.**

Corroborating parameters: 3 people and ~$1,500/mo ran a 40k-queries/day warehouse; 2 people ran a full CDC lakehouse for ~$460/mo; hourly (not real-time) freshness was "enough for our stage"; MoJ served a national justice system on Athena full refreshes before bothering with incrementals. **Idempotent, re-runnable jobs plus orchestrator retries substitute for most reliability engineering** at this scale.

### (d) Where ClickHouse/Superset-style serving layers fit relative to a lakehouse

- **The lakehouse (S3 + Iceberg + Athena/Trino + dbt) is the system of record and transformation substrate** — cheap, durable, engine-agnostic; latency seconds-to-minutes, fine for BI.
- **ClickHouse/DuckDB-class engines are the low-latency *serving* tier** — when queries face customers (Tweeq's 5-minute in-app analytics; UDisc's dashboards). Tweeq ran ClickHouse as *both* warehouse and serving — forced by residency/cloud-agnostic constraints, and it cost them Kafka Engine schema pain and adapter compromises.
- **Superset/Metabase/Hex sit on top of either**; every team found one BI tool insufficient for product analytics (Tweeq added PostHog).
- Pattern to copy: **lakehouse spine as truth, serving engine as a satellite fed from the marts** — added only when a latency-sensitive consumer exists.

### (e) Implications for a solo 12-month personal platform build

1. **The spine is validated at this scale by the closest comparable.** MoJ runs essentially the same stack in production and found it dramatically cheaper and simpler than Spark. Expect their potholes: Athena per-query limits, dbt one-model-per-table friction, weak default observability.
2. **Sequence like the consensus:** Months 1–3 batch EL into S3 + Glue catalog + Athena end-to-end on one real dataset (skip CDC early). Months 3–6 dbt with three layers from day one, full-refresh first, tests + docs as you go. Months 5–8 orchestrator with idempotent, retryable, alerting jobs — many small jobs, never one mega-DAG. Months 8–12 satellites — BI (Superset), then one of: serving layer, CDC/streaming path, or quality/lineage tooling.
3. **Iceberg maintenance is a first-class learning objective, not an afterthought** — compaction, snapshot expiry, small files, schema evolution drills. This is where lakehouse builds actually hurt.
4. **Add the serving satellite only against a concrete "customer-facing" use case** — e.g., a live dashboard hitting ClickHouse or DuckDB fed from gold marts. That demonstrates the lakehouse-vs-serving distinction better than making ClickHouse the warehouse (Tweeq only did that because residency ruled out managed warehouses).
5. **Practice the pattern everyone converged on: idempotency + retries as the reliability model.** MERGE-upsert semantics, re-runnable partitioned loads, orchestrator retries, failure alerts. Highest lesson-density skill in all seven case studies.
6. **Internalize the HN critique as a design constraint:** anything built must survive weeks of inattention. Prefer serverless (Athena, GitHub Actions early scheduling) over K8s self-hosting — Tweeq's Dagster-on-K8s setup pain and Superset ops are exactly the yak-shaves that stall a solo plan.
7. **Plan the year-2 refactors in year 1**: an intermediate modeling layer, decomposed jobs, and naming conventions — the three things ClickHouse Inc. wished they'd done earlier.

### All sources

- Tweeq: https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904
- ClickHouse internal DWH pt 1: https://clickhouse.com/blog/building-a-data-warehouse-with-clickhouse · pt 2: https://clickhouse.com/blog/building-a-data-warehouse-with-clickhouse-part-2
- Zippi (Dagster, vendor): https://dagster.io/blog/zippi-case-study
- UK MoJ Athena+Iceberg+dbt: https://ministryofjustice.github.io/data-and-analytics-engineering/blog/posts/building-a-transaction-data-lake-using-amazon-athena-apache-iceberg-and-dbt/
- Halodoc Data Platform 2.0: https://blogs.halodoc.io/lake-house-architecture-halodoc-data-platform-2-0/ · Hudi learnings: https://blogs.halodoc.io/key-learnings-on-using-apache-hudi-in-building-lakehouse-architecture-halodoc/
- jchandra fintech stack: https://jchandra.com/posts/data-infra/ · HN discussion: https://news.ycombinator.com/item?id=43312199
- UDisc (MotherDuck, vendor): https://motherduck.com/case-studies/udisc-motherduck-sports-management/

Caveats: Zippi and UDisc are vendor-published (flagged inline); Halodoc's posts predate the 2023 window slightly (2021–22) but are the most detailed real-world AWS open-table-format journey; Tweeq's article omits team size and timeline — those gaps are stated, not inferred.
