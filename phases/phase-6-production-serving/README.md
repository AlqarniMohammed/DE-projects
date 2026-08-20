# Phase 6 — Production Hardening, Serving & the Capstone

**Duration:** months 11–12 · **Budget:** ~80 hours · **AWS cost:** ≤ $25/mo (quality/lineage/serving all run locally or inside dbt; Terraform manages what already exists)

The year's final move: turn the platform you've built into something that *reads* like production — quality gates, lineage, IaC, observability — add the two portfolio differentiators (a Tweeq-style serving layer and an AI-data pipeline), and package everything for hiring managers. **The spine is the capstone** — it was built all year instead of assembled in week 30.

## Objectives

1. A layered **data-quality + observability** stack on the spine (dbt tests → dbt-expectations → Elementary anomaly detection + alerts).
2. **Lineage** demonstrated with the OpenLineage standard; **contracts** enforced in CI.
3. Core spine infrastructure in **Terraform**.
4. The **serving-layer pattern**: ClickHouse + Superset fed from gold marts.
5. The **AI-data differentiator**: documents → embeddings → pgvector, orchestrated like any pipeline.
6. Interview-ready portfolio + interview reps.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P6]`

DQ dimensions (validity vs accuracy) · dbt tests vs dbt-expectations vs Elementary · observability vs testing · data contract · OpenLineage/Marquez · IaC/Terraform · state/drift · ClickHouse · serving layer vs lakehouse · Superset · embeddings/vector DB/RAG · semantic layer · SLA/SLO.

## Learn (~20 h)

| Resource | Scope | Hours |
|---|---|---|
| Quality compact path: [dbt tests docs](https://docs.getdbt.com/docs/build/data-tests) + [dbt-expectations (metaplane fork)](https://hub.getdbt.com/metaplane/dbt_expectations/latest/) + [Elementary quickstart](https://docs.elementary-data.com/oss/quickstart/quickstart-cli-package) | Working level | 6 |
| [Terraform AWS get-started](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) | Full track | 5 |
| [OpenLineage getting started](https://openlineage.io/getting-started/) + [Marquez tutorial](https://www.astronomer.io/docs/learn/marquez) | 1-hour demo level | 2 |
| *DDIA 2nd edition* (Kleppmann & Riccomini, **March 2026** — buy the 2E) | Targeted: storage engines, replication, batch/stream chapters | 8 (spread) |
| Vocabulary passes (half-day each): GX/Soda/Monte Carlo story · SQLMesh 2-hr taste · semantic layers · Snowflake positioning · Azure stack (ADF/Synapse/Fabric terms) | Interview hedges — reading only | 4 |

## Build — Spine v4: production hardening (~25 h)

1. **Quality:** dbt-expectations distributional tests on the marts (row-count anomalies, value ranges — port the DQ-dimensions thinking from the senior posts: completeness, uniqueness, validity); **Elementary** on top: anomaly detection, test history, the observability report, Slack alerts on failure. Quarantine pattern: bad rows to a holding table, not silently dropped.
2. **Contracts:** dbt **model contracts** (enforced columns/types) on the two most-consumed marts; a CI check that fails the PR on a breaking change — demo with a deliberately breaking PR left open as evidence.
3. **Lineage:** OpenLineage events from Airflow (built-in provider) → Marquez (Docker) → screenshot the cross-DAG lineage graph. Demo-level; note DataHub/OpenMetadata as the productionized versions.
4. **IaC:** Terraform-ize the spine's core AWS resources (S3 buckets, Glue catalog/job, Athena workgroup, IAM, budgets) — import what exists, `plan` clean, one `destroy`/`apply` cycle on a non-data resource to trust it. Modules kept simple; tfsec scan.
5. **Observability:** CloudWatch dashboard (Glue job metrics, Lambda errors, Athena scanned bytes) + the AWS Budgets story; a `PLATFORM-RUNBOOK.md` — what runs when, what alerts exist, how to recover each failure.

**AI rule:** Terraform boilerplate is fair game for Claude Code; hand-write the contract definitions and the runbook (the runbook *is* the interview prep).

## Build — Satellite S6a: ClickHouse + Superset serving layer (~15 h)

*(The Tweeq pattern — new; the old plan lacked a serving layer entirely.)* Docker Compose: **ClickHouse** + **Superset**. A small Airflow DAG replicates two gold marts from the lakehouse into ClickHouse MergeTree tables on a schedule (the "hot copy" pattern — lakehouse stays the source of truth). Superset dashboard with a live, filterable "customer-facing" view; measure the latency difference vs Athena for the same query and put the number in the README. Read the [Tweeq article](https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904) *after* building — their lessons (Kafka Engine schema pain, adapter maturity) will now read as war stories you understand.

## Build — Satellite S6b: the AI-data pipeline (~12 h)

*(New — the market moved: LLM-pipeline skills in ~12% of DE postings and climbing.)* An Airflow-orchestrated pipeline: a corpus of documents (e.g., AWS whats-new posts or arXiv abstracts) → cleaned + chunked → embeddings (any cheap/local embedding model) → **pgvector** (Postgres in Docker) with dedup/idempotent upserts → a small retrieval-quality check (top-k sanity queries) as the pipeline's "dbt test." Frame in the README: *this is a normal data pipeline with a new sink* — freshness, dedup, and lineage are the DE's job in every RAG system.

## Capstone packaging & interview layer (~10 h)

1. **The capstone review:** self-grade the spine against the rubric below; fix the weakest axis.
2. **Portfolio surface:** spine README rewritten for a hiring manager (problem → architecture diagram → decisions-with-reasons → 3 demo videos ≤3 min: batch + backfill, CDC/streaming, quality+serving); pin the spine + best 3 satellites on your GitHub profile.
3. **Resume + narrative:** rewrite the resume bullets from PROGRESS.md's evidence (accomplishments with numbers); aim at the 2–4-year band story: "database specialist who built and operates a production-grade lakehouse."
4. **Interview reps:** LeetCode SQL 50 finished · [Exponent](https://www.tryexponent.com/practice) peer mocks (5 free/month — do ≥3) · one system-design self-run: "design Tweeq's platform" using everything you know · DDIA targeted chapters as the theory backstop.

### Capstone rubric (self-grade 0–4 each; gate needs ≥3 average, no zero)

| Axis | 4 looks like |
|---|---|
| Problem & docs | A stranger understands what/why in 5 minutes; decisions have reasons |
| Ingestion breadth | Batch + API + CDC + stream, all idempotent |
| Warehouse/lakehouse design | 3-layer models, sensible partitioning, maintained tables |
| Orchestration & reliability | Small DAGs, retries, alerts, demonstrated failure recovery |
| Quality & contracts | Layered tests + anomaly detection + a contract that blocks a breaking PR |
| IaC & reproducibility | Terraform core + a fresh-clone demo path |
| Serving & visibility | A dashboard a non-engineer can use; latency story told |

## Competency gate G6 — the final gate

- [ ] Capstone rubric ≥3 average, self-graded honestly, weakest axis fixed once.
- [ ] Elementary report + a caught anomaly (introduce one on purpose) demonstrated.
- [ ] Breaking-PR-blocked-by-contract evidence linked.
- [ ] Serving-layer latency number published; AI-pipeline retrieval check green.
- [ ] `terraform plan` clean on the spine's core.
- [ ] ≥3 mock interviews done; resume rewritten.
- [ ] **Final retrieval checkpoint:** 30 terms sampled across ALL phases (≥80%).

## Publish checkpoint

The capstone post: the full platform tour — architecture diagram, the year's arc, the three videos, and what you'd do differently. This is the post you pin.

## Interview questions you can now answer

- "Walk me through a data platform you've built end-to-end." *(the money question — you now have a real answer)*
- "How do you know your data is correct?" 
- "A dashboard number looks wrong — trace it."
- "Where does a vector database fit in a data platform?"
- "What does this platform cost to run, and where would you cut?"
