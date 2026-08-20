# Phase 3 — Spark & Databricks ⭐ Cert Phase 2

**Duration:** months 5–7 (elastic — the gate decides) · **Budget:** ~75 hours (cert prep overlaps the phase — it *is* the phase) · **Cost:** $0 platform (Databricks Free Edition) + exam $200 (→$100 with voucher) + optional course ~$30–40

Distributed compute enters. The exam labs run on **Databricks Free Edition** (serverless, Unity Catalog on by default — exactly the environment the current exam assumes); the Spark-internals work runs on **local PySpark**, where the full Spark UI is available. The gate is the **Databricks Certified Data Engineer Associate** exam — current version effective **May 4, 2026**: PySpark-first, Lakeflow-branded. Full blueprint: [CERTS.md](../../reference/CERTS.md).

## Objectives

1. PySpark DataFrame fluency + reading the **Spark UI** (the real interview filter for Spark roles).
2. Delta Lake mechanics: transaction log, MERGE, time travel, Liquid Clustering.
3. The Lakeflow trio: Connect (ingestion), Jobs (orchestration), Spark Declarative Pipelines (ex-DLT).
4. Unity Catalog governance: grants, masking, row filters, ABAC.
5. Pass the cert.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P3]`

Spark/PySpark · lazy evaluation, transformations vs actions · shuffle · skew · broadcast join · AQE · Spark UI · Delta Lake · MERGE · Unity Catalog · Lakeflow (Connect/Jobs/SDP) · Auto Loader / COPY INTO · Liquid Clustering · Asset Bundles · serverless vs classic compute.

## Learn (~20 h + book as-needed)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [**Databricks Academy** self-paced DE path (free)](https://www.databricks.com/learn/training/home) — the exam guide names these: *Data Ingestion with Lakeflow Connect · Deploy Workloads with Lakeflow Jobs · DevOps Essentials for Data Engineering · Data Interoperability with Unity Catalog · Build Data Pipelines with Lakeflow Spark Declarative Pipelines · Get Started with Data Governance* | All six | 15–20 | Labs 1–7 below — they map 1:1 to the courses and the exam sections |
| *Data Analysis with Python and PySpark* (Rioux, Manning, ~$33) — optional; the strongest current PySpark book | Ch. 1–9 as reference alongside labs | as-needed | The medallion lab's hand-typed notebooks |
| [Spark performance-tuning docs](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — skew, broadcast joins, AQE | Quick read — you now have the context to appreciate it | 0.5 | The skew-detection kata + forensics satellite S3a |

**Video lane — optional swap.** Each row below **replaces** the default row it names: same "Pinned by" exercise, hours swap rather than add. Pick one lane per row before starting ([the rule](../../GUIDE.md#the-phase-loop)); prices, details, and the rows with no video twin: [COURSES.md](../../reference/COURSES.md). *(Most default rows above are already video — this swap changes the provider or the price, not the format.)*

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Derar Alhussein: Databricks DE Associate prep course](https://www.udemy.com/course/databricks-certified-data-engineer-associate/) + [practice exams](https://www.udemy.com/course/practice-exams-databricks-certified-data-engineer-associate/) (~$30–40 on sale; V4, May-2026 syllabus) | Swaps the *Databricks Academy path* row as your primary video, if a single-instructor format sticks better; keep the Academy course list as your syllabus checklist — the exam guide names those courses. (His practice exams are already assumed by gate G3) | 15–20 | Labs 1–7 below — they map 1:1 to the courses and the exam sections |
| [PySpark: Apache Spark Programming for Beginners](https://www.udemy.com/course/apache-spark-programming-in-python-for-beginners/) (Pandey, ~$15–20 on sale; runs in Databricks) | Swaps the *Rioux book* reference row — course-as-reference instead of book-as-reference; watch sections as the labs demand them, not front-to-back | as-needed (14–18 watched through) | The medallion lab's hand-typed notebooks |

*Before starting, re-verify:* the exam guide PDF (revises every 6–10 months!), Free Edition quotas, and whether a **Learning Festival** window (50% exam voucher) falls in these two months — plan the Academy pathway inside it if so.

## Build — labs on Free Edition (~30 h; maps 1:1 to exam sections)

A fresh dataset keeps it interesting — pick from the P3 menu in [`DATASETS.md`](../../reference/DATASETS.md) (Spotify charts or IMDb are the proven defaults; anything with daily updates for MERGE practice works):

1. **Ingestion lab:** Auto Loader streaming file ingestion with schema evolution + COPY INTO batch equivalent; know when each.
2. **Medallion lab:** bronze→silver→gold in PySpark notebooks; joins (incl. one broadcast), explode, dedup; gold as **materialized view vs view vs streaming table** — build one of each and explain the difference (exam favorite).
3. **Delta mechanics lab:** MERGE an SCD2 dimension; inspect `_delta_log`; time-travel query; Liquid Clustering on the fact table.
4. **Lakeflow Jobs lab:** a multi-task DAG (notebook + SQL tasks), retries/branching, one **file-arrival trigger** and one **table-update trigger**.
5. **Declarative pipeline lab:** rebuild the medallion as a **Lakeflow Spark Declarative Pipeline** with expectations (Free Edition quota: 1 active pipeline — enough).
6. **Governance lab:** UC grants for two personas, one column mask, one row filter; browse the lineage UI.
7. **CI/CD lab:** wrap one job in an **Asset Bundle**, deploy dev→prod via the Databricks CLI from your terminal (on one free workspace, dev/prod are two bundle *targets* — that's normal and worth saying out loud).

**AI rule:** notebooks are yours to hand-type; your assistant may quiz you (paste an exam-guide section, ask for hard questions) — it may not write the lab code.

### Prove-it assignment (2–3 h, do it before S3a): skew-detection kata

Hand-write a small `detect_skew(df, key)` helper (partition-size distribution + a skew-ratio number), plus pytest asserts you write yourself against two synthetic DataFrames — one uniform, one ~90/10 skewed. It becomes the measuring instrument you use inside the forensics satellite.

## Build — Satellites (~15 h)

**Environment note first:** S3a runs on **local PySpark** (`uv add pyspark`, single-node — the full Spark UI at `localhost:4040` works there; ~1 h setup). Free Edition's serverless environment can't show the classic Spark UI the artifact needs — it stays the exam-lab home.

**S3a — Spark Performance Forensics:** deliberately slow job (skewed join, tiny files) on MovieLens → measure with your kata → apply fixes one at a time (broadcast, AQE, salting, repartition, file sizing) → `FORENSICS.md` with before/after Spark UI screenshots and a ranked impact table. The strongest Spark showcase artifact that exists.

**S3b — Iceberg vs Delta bake-off** *(local)*: same workload through PyIceberg and delta-rs on your laptop; benchmark write/read/schema-evolution/time-travel; publish `BAKEOFF.md` with real numbers and a verdict. Read about **UniForm/format convergence** to frame the conclusion.

Unique briefs for either satellite: the `/satellite-brief` skill or [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Competency gate G3 ⭐

- [ ] **Databricks Certified Data Engineer Associate — passed.** (Book only after ≥80% on Derar Alhussein V4 practice exams.)
- [ ] All 7 Free Edition labs done (ingestion, medallion, Delta, Jobs, declarative pipeline, UC, Asset Bundle).
- [ ] Skew-detection kata: asserts green, used inside S3a.
- [ ] Forensics artifact published (`FORENSICS.md` + screenshots).
- [ ] Bake-off artifact published (`BAKEOFF.md`).
- [ ] 3-minute narrated demo: your declarative pipeline graph with expectations catching bad rows.
- [ ] **External critique requested:** forensics or bake-off artifact posted to a practitioner community — request thread linked in PROGRESS.md. *(Optional but high-leverage: one community or paid **mentor checkpoint** reviewing the platform repo — an hour of external eyes at mid-year is worth ten at month 12.)*
- [ ] `SELF-CHECK.md` updated with this phase's written answers.
- [ ] **Retrieval checkpoint:** all `[P3]` terms + 10 random earlier terms, ≥80%.
- [ ] Both phase posts published (see below).

## Publish checkpoint

Two posts this phase (any public platform): (1) the cert announcement with your honest prep notes (what the new exam actually tests); (2) the forensics story — "I made a Spark job 10× faster with six changes; here's each one ranked by impact."

## Check yourself — questions you can now answer

- "A Spark job is slow — walk me through your diagnosis."
- "What is a shuffle and why is it expensive?"
- "Delta vs Iceberg — how would you choose?" (with *your own* benchmark numbers)
- "Explain the medallion architecture and what lives in each layer."
- "Materialized view vs streaming table — when each?"

---
← [Phase 2 — AWS Lakehouse Core](../phase-2-aws-lakehouse-core/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 4 — Orchestration & Ingestion →](../phase-4-orchestration-ingestion/README.md)**
