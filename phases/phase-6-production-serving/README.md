# Phase 6 — Production, Serving & Capstone

**Duration:** months 11–12 · **Budget:** ~88 hours · **AWS cost:** ≤ $25/mo (quality/lineage/serving all run locally or inside dbt; Terraform manages what already exists)

The year's final move: turn the platform you've built into something that *reads* like production — quality gates, lineage, IaC, observability — add the two differentiators (a serving layer and an AI-data pipeline), and tell the whole story the way real data teams do: as a **platform journey** write-up. **The platform is the capstone** — it was built all year instead of assembled in week 30. By the end you have what the framework promised on page one: a full data stack, end to end, of the kind engineering teams publish journey posts about.

## Objectives

1. A layered **data-quality + observability** stack on the platform (dbt tests → dbt-expectations → Elementary anomaly detection + alerts).
2. **Lineage** demonstrated with the OpenLineage standard; **contracts** enforced in CI.
3. Core platform infrastructure in **Terraform**.
4. The **serving-layer pattern**: ClickHouse + Superset fed from gold marts.
5. The **AI-data differentiator**: documents → embeddings → pgvector, orchestrated like any pipeline.
6. A showcase-ready platform + the platform-journey write-up.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P6]`

DQ dimensions (validity vs accuracy) · dbt tests vs dbt-expectations vs Elementary · observability vs testing · data contract · OpenLineage/Marquez · IaC/Terraform · state/drift · ClickHouse · serving layer vs lakehouse · Superset · embeddings/vector DB/RAG · semantic layer · SLA/SLO.

## Learn (~26 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| Quality compact path: [dbt tests docs](https://docs.getdbt.com/docs/build/data-tests) + [dbt-expectations (metaplane fork)](https://hub.getdbt.com/metaplane/dbt_expectations/latest/) + [Elementary quickstart](https://docs.elementary-data.com/oss/quickstart/quickstart-cli-package) | Working level | 6 | Build step 1: the layered quality stack + the caught-anomaly demo |
| [Terraform AWS get-started](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) | Full track | 5 | Build step 4: Terraform-izing the platform core, `plan` clean |
| [OpenLineage getting started](https://openlineage.io/getting-started/) + [Marquez tutorial](https://www.astronomer.io/docs/learn/marquez) | 1-hour demo level | 2 | Build step 3: the cross-DAG lineage graph screenshot |
| *DDIA 2nd edition* (Kleppmann & Riccomini, **March 2026** — buy the 2E) | Targeted: storage engines, replication, batch/stream chapters | 8 (spread) | `SELF-CHECK.md` answers + the architecture self-test (packaging step 3) |
| Vocabulary passes (half-day each): GX/Soda/Monte Carlo story · SQLMesh 2-hr taste · Pandera positioning · semantic layers · Snowflake positioning · Azure stack (ADF/Synapse/Fabric terms) | Reading + one written paragraph each | 4 | One written contrast paragraph per pass, filed in `SELF-CHECK.md` |
| **PDPL (Saudi Personal Data Protection Law) primer** — official SDAIA summary/guidelines | 1-hour governance read; pairs with the Lake Formation work | 1 | A short "PDPL implications for this platform" note in `PLATFORM-RUNBOOK.md` — governance-aware engineers are rare |

**Video lane — optional swap.** Each row below **replaces** the default row it names: same "Pinned by" exercise, hours swap rather than add. Pick one lane per row before starting ([the rule](../../GUIDE.md#the-phase-loop)); prices, details, and the rows with no video twin: [COURSES.md](../../reference/COURSES.md).

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [freeCodeCamp: Terraform + AWS dev environment](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) (free video course) | Swaps the *Terraform AWS get-started* row — build-along video instead of the HashiCorp text track; then Terraform the platform's own resources either way | 4–6 (vs 5) | Build step 4: Terraform-izing the platform core, `plan` clean |

*Before starting, re-verify:* Elementary + dbt-expectations package versions (the quality stack churns), Terraform AWS provider major, DDIA 2E availability in your region.

## Build — Platform v4: production hardening (~25 h)

1. **Quality:** dbt-expectations distributional tests on the marts (row-count anomalies, value ranges — completeness, uniqueness, validity thinking made concrete); **Elementary** on top: anomaly detection, test history, the observability report, Slack alerts on failure. **Quarantine pattern as its own task:** bad rows go to a holding table, not silently dropped — build it, don't just read it.
2. **Contracts:** dbt **model contracts** (enforced columns/types) on the two most-consumed marts; a CI check that fails the PR on a breaking change.
3. **Lineage:** OpenLineage events from Airflow (built-in provider) → Marquez (Docker) → screenshot the cross-DAG lineage graph. Demo-level; note DataHub/OpenMetadata as the productionized versions.
4. **IaC:** Terraform-ize the platform's core AWS resources (S3 buckets, Glue catalog/job, Athena workgroup, IAM, budgets) — import what exists, `plan` clean, one `destroy`/`apply` cycle on a non-data resource to trust it. Modules kept simple; tfsec scan.
5. **Observability:** CloudWatch dashboard (Glue job metrics, Lambda errors, Athena scanned bytes) + the AWS Budgets story; a `PLATFORM-RUNBOOK.md` — what runs when, what alerts exist, how to recover each failure.

**AI rule:** Terraform boilerplate is fair game for your assistant; hand-write the contract definitions and the runbook (the runbook *is* how you'll explain the platform to anyone).

### Prove-it assignment (inside build step 2): the contract that blocks a PR

Open a deliberately breaking PR (rename a contracted column) and let CI reject it. Leave the blocked PR open as permanent evidence. One screenshot, one link — the strongest "I run this like production" proof there is.

## Build — Satellite S6a: ClickHouse + Superset serving layer (~15 h)

Docker Compose: **ClickHouse** + **Superset**. A small Airflow DAG replicates two gold marts from the lakehouse into ClickHouse MergeTree tables on a schedule (the "hot copy" pattern — lakehouse stays the source of truth). Superset dashboard with a live, filterable "customer-facing" view; measure the latency difference vs Athena for the same query and put the number in the README. Read the [Tweeq platform-journey article](https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904) *after* building — their lessons (Kafka Engine schema pain, adapter maturity) will now read as war stories you understand. Their write-up is also the model for your own journey post below.

**Optional full-stack variant** (for builders with app-development skills): replace or augment Superset with a small **data product** — a FastAPI read API over the gold marts (or ClickHouse) plus a minimal frontend. The latency story is still required, and the framing writes itself: "I built the pipeline *and* the product it feeds." Very few builders can show this end-to-end. A regional dataset from the S6a menu in [`DATASETS.md`](../../reference/DATASETS.md) compounds the effect.

## Build — Satellite S6b: the AI-data pipeline (~12 h)

An Airflow-orchestrated pipeline: a corpus of documents (e.g., AWS whats-new posts or arXiv abstracts) → cleaned + chunked → embeddings (any cheap/local embedding model) → **pgvector** (Postgres in Docker) with dedup/idempotent upserts → a small retrieval-quality check (top-k sanity queries) as the pipeline's "dbt test." Frame in the README: *this is a normal data pipeline with a new sink* — freshness, dedup, and lineage are the DE's job in every RAG system.

## Capstone packaging (~10 h)

1. **The capstone review:** self-grade the platform against the rubric below; fix the weakest axis.
2. **Showcase surface:** platform README rewritten so a stranger understands it in 5 minutes (problem → architecture diagram → decisions-with-reasons → 3 demo videos ≤3 min: batch + backfill, CDC/streaming, quality+serving); pin the platform + best 3 satellites on your GitHub profile.
3. **The architecture self-test:** one system-design self-run — "design a fintech data platform like the ones in public journey posts" — using everything you know, on paper, timed at 45 minutes. DDIA's targeted chapters are the theory backstop. Finish LeetCode SQL 50 while you're at it — full SQL fluency is a capstone skill, not an extra.
4. **The platform-journey write-up:** `JOURNEY.md` in the platform repo — the full story in the shape real engineering teams publish: the problem → the architecture (diagram) → decisions with reasons → the numbers (cost/month, serving latency, data volumes, test counts) → lessons and what you'd do differently. This is the capstone post; Tweeq's article is the register to aim for.
5. **AI-usage record:** `AI-USAGE.md` — per phase, what you delegated to AI vs hand-typed, plus one MCP tool you tried. Deliberate AI use is a 2026 skill; documenting yours proves it.

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
- [ ] Breaking-PR-blocked-by-contract evidence linked (the prove-it).
- [ ] OpenLineage → Marquez cross-DAG graph screenshot.
- [ ] Serving-layer latency number published; AI-pipeline retrieval check green.
- [ ] `terraform plan` clean on the platform's core · tfsec run.
- [ ] `PLATFORM-RUNBOOK.md` written (incl. the PDPL note).
- [ ] Showcase surface done: rewritten README, 3 demo videos, pinned repos.
- [ ] `JOURNEY.md` written · `AI-USAGE.md` written.
- [ ] **External critique requested:** capstone repo posted for community review — request thread linked.
- [ ] `SELF-CHECK.md` complete: every phase's questions answered in writing, evidence linked.
- [ ] **Final retrieval checkpoint:** 30 terms sampled across ALL phases (≥80%).
- [ ] Capstone journey post published (see below).

## Publish checkpoint

The capstone post *is* your `JOURNEY.md`: the full platform tour — architecture diagram, the year's arc, the numbers, the three videos, and what you'd do differently. This is the post you pin.

## Check yourself — questions you can now answer

- "Walk me through a data platform you've built end-to-end." *(the money question — you now have a real answer)*
- "How do you know your data is correct?"
- "A dashboard number looks wrong — trace it."
- "Where does a vector database fit in a data platform?"
- "What does this platform cost to run, and where would you cut?"

---
← [Phase 5 — Streaming & CDC](../phase-5-streaming/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Finish: [the final gate checklist →](../../PROGRESS.md)**
