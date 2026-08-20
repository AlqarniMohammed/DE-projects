# Sources & Evidence

Everything the framework claims traces to the research below. Reports compiled **2026-08-20** by six parallel deep-research passes; the framework was then independently audited and revised twice (v1.1, v1.2) — the what-changed record lives in [`CHANGELOG.md`](../CHANGELOG.md).

## Research reports (in [`sources/research/`](../sources/research/))

| Report | What it established | Key findings that shaped the framework |
|---|---|---|
| [`tool-landscape.md`](../sources/research/tool-landscape.md) | CORE/AWARE/SKIP verdict for ~60 tools, 45+ sources | Iceberg won the format war (v3); S3 Tables matured; Airflow 3 is a different product; Kafka 4 killed ZooKeeper; dbt+Fivetran merged; GX reset; dlt is the breakout ingestion tool; AI-assisted DE is now assumed |
| [`certs.md`](../sources/research/certs.md) | Official blueprints (read from the exam-guide PDFs), prep, timing | Databricks exam rewritten twice (current: May 2026, PySpark/Lakeflow/UC-first); DEA-C01 still v1.0; "dbt Foundational Certificate" doesn't exist; Learning Festival 50% voucher; Free Edition replaced Community Edition |
| [`courses.md`](../sources/research/courses.md) | Best current resources per skill area, verified live | FoDE still canonical (no 2nd ed); DE Zoomcamp Jan 2027 cohort; Astronomer/Dagster/Confluent/Databricks academies all free and current; DDIA 2E published Mar 2026; GX acquired by FICO — quality stack is dbt tests + dbt-expectations (metaplane) + Elementary |
| [`platform-journeys.md`](../sources/research/platform-journeys.md) | Seven real platform-build journeys, deep-read | Consensus build order (ingest→dbt 3 layers→orchestrator→BI→quality); a UK-government platform validates the exact platform stack; serving layer = satellite fed from marts; idempotency+retries is the reliability model; monolith DAGs and 2-layer modeling are the universal regrets |
| [`roadmap-benchmarks.md`](../sources/research/roadmap-benchmarks.md) | How 9 well-known DE roadmaps are structured + their failure modes | Copied: lifecycle-as-skeleton, phase-terminal milestone gates with rubrics, skip-lists, contrast-pair glossary, setup isolated in a pre-phase; added what none have: spaced-retrieval checkpoints |
| [`job-market.md`](../sources/research/job-market.md) | The market signals that set the tool weightings | SQL+Python co-#1 (70–94%); AWS #1 cloud (40.3%); Gulf-region postings pair Databricks+PySpark; Airflow the only orchestrator worth depth; certs in ~4% of postings — the built platform wins; AI-pipeline skills 3%→12% in a year |
| [`de-lifecycle-primer.md`](../sources/research/de-lifecycle-primer.md) | The framework's own primer on the DE lifecycle | Phase 0's pinned reading — the lifecycle in project order, stage by stage |

## Audit trail

The framework has been audited twice and revised both times — first by an independent expert audit (v1.1: 13 findings, all adopted), then by a five-track comprehensive audit covering technical accuracy, the learner journey, consistency, and coverage (v1.2). Decisions and their reasons are recorded in [`CHANGELOG.md`](../CHANGELOG.md); the framework never grades itself alone (external critique is built into every gate from G2).

Case study cited throughout: the [Tweeq data-platform journey](https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904) — an example of the *kind* of end-to-end platform (and public write-up) this framework builds toward, not a stack prescription.

## Known evidence gaps (stated, not hidden)

- Regional market conclusions are directional, assembled from job boards and individual postings — no quantified skills scrape exists for every market. Re-derive weightings for yours ([how](LEARNERS.md)).
- The dbt "61% of postings" figure and the "12% LLM-in-DE" figure each rest on a single, potentially biased source; both were used directionally, not as load-bearing facts.
- Cert blueprints and tool versions churn: each phase README lists what to re-verify before starting it, and a weekly link-check guards the references.

## Optional add-on evaluated but not scheduled

**DataTalksClub DE Zoomcamp** (free, cohort-based) — verdict: **do not run it in parallel** at 6–10 h/wk (it alone is 5–15 h/wk; parallel-running recreates the overwhelm this framework exists to fix). It becomes attractive only if you want its community + peer-reviewed capstone *instead of* this framework's P3–P4 satellites — a conscious swap, decided at the end of Phase 2. Details in [`courses.md`](../sources/research/courses.md).

---
[README](../README.md) · [Why it looks this way](WHY.md) · [Changelog](../CHANGELOG.md)
