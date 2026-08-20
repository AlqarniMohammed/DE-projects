# Using This Framework — Any Learner, Any Entry Point

The framework has one **default path**: the seven phase specs in [`phases/`](phases/), exactly as written. The default path is complete and self-sufficient — datasets chosen, resources vetted, gates defined; you never need to generate anything to follow it. This file exists for everything around that path: entering midway, running it as one of several learners, and generating unique project requirements so no two learners build from identical briefs.

**The level guarantee.** Different learners can vary the *scenario* — never the *bar*. Competency gates and satellite objectives are fixed; requirements, datasets, and stakeholders vary. Two learners who both hold gate G6 evidence have, by construction, reached the same level: **Associate Data Engineer, role-ready** — regardless of which datasets or scenarios they crossed to get there.

---

## Placement — entering at the right phase

Gates are cumulative, so placement is simple: **you may start at phase N if you can pass gate N−1 today.** To test that:

1. Open `PROGRESS.md` at gate N−1 and read every checkbox.
2. Take the phase's **retrieval checkpoint** (the glossary terms tagged for that phase and all earlier ones — the Anki deck from P0 makes this fast). You need ≥80% cold.
3. For each named artifact in the gate, you must hold an **equivalent from your own past work** (a real dbt project you built ≈ G1's spine; a production Airflow deployment you ran ≈ G4's orchestration artifact). Link your equivalents in your `PROGRESS.md` where the originals would go.
4. Any checkbox you can't cover with evidence: do that item from the phase spec in compressed form before advancing. Don't skip it — the gates are the guarantee, and an unearned checkbox is a gap an interviewer will find later.

When in doubt, enter one phase earlier. The early phases move fast for experienced people, and gates absorb speed just as well as slowness.

## Running your own pass

1. **Fork the repo** (both this framework repo and create your own platform repo per P0).
2. Reset `PROGRESS.md`: clear all checkboxes, dates, and logs — it's your tracker now.
3. **Re-derive the regional assumptions.** The market analysis in [`sources/research/`](sources/research/) (job demand, cert weighting, target-company watchlist) was built for a Saudi/Gulf-first search. If that's not your market, redo those conclusions for yours before trusting the career track's watchlist and the Databricks-vs-Snowflake weighting.
4. Follow the default path phase by phase — or generate unique satellite requirements as below.
5. Keep the standing rules: gates decide advancement, every learn-resource is pinned to an exercise, PR workflow, no secrets in git, cost ceiling, publish per phase.

## Generating unique requirements

For any satellite, [`prompts/generate-satellite-requirements.md`](prompts/generate-satellite-requirements.md) turns an AI assistant into a non-technical stakeholder who hands you realistic business requirements, black-box acceptance tests, and a sealed reference solution — with the satellite's objectives and gate artifact held fixed. Use it when:

- you're a second/third learner and want a brief nobody else has,
- you're re-running a phase and want fresh material,
- you want interview stories that don't start with "so, the NYC taxi dataset…".

Cohorts: have each learner run the generator (it reads your `PROGRESS.md` and avoids repeating scenarios), then compare builds at the gate — same bar, different roads, and reviewing each other's artifacts doubles as the gate's external-critique requirement.

## The bar itself — what each gate certifies

| Gate | Passing it certifies you can… |
|---|---|
| **G0** | Speak the DE lifecycle and core contrast-pairs; operate a guard-railed cloud account and local toolchain |
| **G1** | Write interview-strength analytical SQL; ship tested DE Python; operate a table format (schema evolution, time travel); build a documented 3-layer dbt project with an SCD2 dimension |
| **G2** | Run a production-pattern lakehouse on AWS (S3 · Glue · Athena · S3 Tables); prove idempotent backfills; explain and cut query costs; test pipelines in CI; **AWS DEA-C01** |
| **G3** | Work PySpark at Spark-UI-literacy level; explain and fix skew; operate Delta/Lakeflow/Unity Catalog; **Databricks DE Associate** |
| **G4** | Orchestrate with Airflow 3 (small idempotent DAGs, retries, alerts); ingest via dlt, CDC (DMS), and Kinesis; handle secrets like production |
| **G5** | Reason about Kafka partitions/offsets/delivery guarantees; build an idempotent stream-to-lakehouse sink; compare CDC approaches with measured evidence |
| **G6** | Layer quality checks + anomaly detection; enforce contracts in CI; show lineage; codify infra in Terraform; serve data (dashboard or data product); run an AI-data pipeline; interview on all of it |

**Definition of done — Associate Data Engineer, role-ready:** all seven gates passed with linked evidence. In practice: you can design, build, operate, and explain a batch + streaming lakehouse end-to-end; prove your data is correct; say what it costs; and answer every interview question in this repo from your own artifacts, not from theory.
