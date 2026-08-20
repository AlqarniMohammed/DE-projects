# Audit: Master Guide Gaps & Senior-Posts Corroboration

## Part 1 — `de-master-guide-2026.md` gap list (preliminary; finalized against research in SOURCES.md)

What the guide gets right: lakehouse-first framing, batch-default/justify-streaming rule, the OSS→AWS service mapping table, the learning priority order ("steps 1–6 make you hireable"), Kimball-first modeling advice.

Gaps and corrections found in the audit:

| # | Gap / issue | Impact on the framework |
|---|-------------|-------------------------|
| 1 | **No serving/BI layer** beyond a one-line viz mention — no ClickHouse/OLAP engines, no Superset/Metabase treatment, despite these being core to real platforms (see Tweeq) | P6 adds a serving-layer satellite; TOOLS.md adds an OLAP/serving category |
| 2 | **No SQLMesh** (dbt's main challenger) and no mention of dbt Labs' recent product changes | Research verifies; TOOLS.md renders a verdict |
| 3 | **No data observability tools** (Elementary, Monte Carlo, Soda) — quality is covered only as GE + dbt tests | P6 scope decision informed by research |
| 4 | **No catalog/metadata platforms** (DataHub, OpenMetadata) beyond Glue/Unity | AWARE-level coverage decision in TOOLS.md |
| 5 | **No semantic layer** discussion | AWARE-level candidate |
| 6 | **"dbt Foundational Certificate" does not exist** — verified: the real credential is the **dbt Analytics Engineering Certification** ($200, updated May 2026); the free "dbt Fundamentals" course confers a badge, not a cert | Corrected; cert itself was dropped from milestones |
| 7 | **No AI-era DE coverage** — vector stores in pipelines, LLM-assisted engineering, whether GenAI skills appear in DE job specs | Research agent reports; framework adds an awareness module if warranted |
| 8 | **Version currency** — Airflow 3.x, Kafka 4.x/KRaft, Spark 4.x, Iceberg v3, GX (Great Expectations rewrite) not reflected | Resource picks in each phase specify current-version material |
| 9 | **No learning-resource layer** — the guide names tools but no courses/books/labs to learn them with | CERTS.md + per-phase "Learn" blocks fill this |
| 10 | **No cost reality-check per service** (e.g., MWAA and MSK baselines are budget-breaking for a solo learner) | Every spine increment carries a cost posture line |

## Part 2 — Senior-posts corroboration notes (verification-only, per context.md)

The posts were checked as a *reference signal*, not a source of framework content:

| Post theme | Corroborates | Notes |
|---|---|---|
| Great Expectations for DQ dimensions, automated via Airflow + dashboard | The *practice* of automated DQ dimension measurement (P6) | **Tool status changed:** GX was acquired by FICO (May 2026), GX Cloud shut down (June 2026), OSS moved to Fivetran stewardship. The framework teaches the same DQ-dimensions practice with dbt tests + dbt-expectations (metaplane fork) + Elementary, keeping GX as interview vocabulary only |
| Validity vs Accuracy; business-rule-driven DQ | P6 quality curriculum framing | Good conceptual framing; matches DAMA-style dimensions in the DEA lifecycle notes |
| Spark data skew + broadcast join; lazy evaluation | P3 Spark performance content (satellite #9) | Matches Databricks cert scope |
| ClickHouse + dbt + Airflow ELT; chDB badge | The Tweeq-style serving satellite in P6 | Two independent Saudi practitioners (posts + Tweeq) using ClickHouse is a meaningful local-market signal — checked against global job-market research before weighting |
| Medallion architecture on Databricks (Riyadh lakehouse project) | P3 medallion labs | Consistent with Databricks exam content |
| Databricks DE cert pass (recommends ~6 months hands-on first) | CERTS.md exam-timing guidance (exam gate at end of P3, ~month 6) | Directly supports the framework's cert placement |
| dbt as the T in ELT; FastAPI for API simulation | P1 dbt satellite; P4 ingestion labs | FastAPI-mock idea adopted as an optional P4 lab exercise |
| DuckDB on partitioned Parquet; Parquet vs Pickle/Feather; Polars/PyArrow | P1 foundations content | Matches the guide and the P1 design |

**Anti-drift check:** no framework module exists *because* a post featured it; every overlapping topic is independently present in the cert blueprints, the master guide, or the research findings. ClickHouse/Superset enter via the Tweeq case study + market research, with the posts as secondary corroboration only.
