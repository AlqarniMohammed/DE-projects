# Phase 3 — Spark & Databricks ⭐ Cert Phase 2

**Duration:** months 5–7 (elastic — the gate decides) · **Budget:** ~80 hours (cert prep overlaps the phase — it *is* the phase) · **Cost:** $0 platform (Databricks Free Edition) + exam $200 (→$100 with voucher) + optional course ~$30–40

Distributed compute enters. Everything here runs on **Databricks Free Edition** (Community Edition's successor: serverless-only, Unity Catalog on by default — exactly the environment the current exam assumes). The gate is the **Databricks Certified Data Engineer Associate** exam (≈ month 6–7 — the second and final cert, completing the pair), current version effective **May 4, 2026** — PySpark-first, Lakeflow-branded. Your DEA-C01 pass arrives as a tailwind: Spark-on-AWS, lakehouse storage, and CI/CD concepts are pre-loaded, so the new surface here is genuinely Databricks-specific. Full blueprint: [CERTS.md](../../CERTS.md).

## Objectives

1. PySpark DataFrame fluency + reading the **Spark UI** (the real interview filter for Spark roles).
2. Delta Lake mechanics: transaction log, MERGE, time travel, Liquid Clustering.
3. The Lakeflow trio: Connect (ingestion), Jobs (orchestration), Spark Declarative Pipelines (ex-DLT).
4. Unity Catalog governance: grants, masking, row filters, ABAC.
5. Pass the cert.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P3]`

Spark/PySpark · lazy evaluation, transformations vs actions · shuffle · skew · broadcast join · AQE · Spark UI · Delta Lake · MERGE · Unity Catalog · Lakeflow (Connect/Jobs/SDP) · Auto Loader / COPY INTO · Liquid Clustering · Asset Bundles · serverless vs classic compute.

## Learn (~25 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| **Databricks Academy self-paced DE path (free)** — the exam guide names these: *Data Ingestion with Lakeflow Connect · Deploy Workloads with Lakeflow Jobs · DevOps Essentials for Data Engineering · Data Interoperability with Unity Catalog · Build Data Pipelines with Lakeflow Spark Declarative Pipelines · Get Started with Data Governance* | All six | 15–20 | Labs 1–7 below — they map 1:1 to the courses and the exam sections |
| *Data Analysis with Python and PySpark* (Rioux, Manning, ~$33) — optional but the best PySpark book for your profile | Ch. 1–9 as reference alongside labs | as-needed | The medallion lab's hand-typed notebooks |
| Senior-post corroboration: skew/broadcast-join and lazy-evaluation posts in [`sources/senior-de-posts.md`](../../sources/senior-de-posts.md) | Quick re-read — you now have the context to appreciate them | 0.5 | The skew-detection kata + forensics satellite S3a |

*Before starting, re-verify:* the exam guide PDF (revises every 6–10 months!), Free Edition quotas, and whether a **Learning Festival** window (50% exam voucher) falls in these two months — plan the Academy pathway inside it if so.

## Build — labs on Free Edition (~30 h; maps 1:1 to exam sections)

A fresh dataset keeps it interesting — pick from the P3 menu in [`DATASETS.md`](../../DATASETS.md) (Spotify charts or IMDb are the proven defaults; anything with daily updates for MERGE practice works):

1. **Ingestion lab:** Auto Loader streaming file ingestion with schema evolution + COPY INTO batch equivalent; know when each.
2. **Medallion lab:** bronze→silver→gold in PySpark notebooks; joins (incl. one broadcast), explode, dedup; gold as **materialized view vs view vs streaming table** — build one of each and explain the difference (exam favorite).
3. **Delta mechanics lab:** MERGE an SCD2 dimension; inspect `_delta_log`; time-travel query; Liquid Clustering on the fact table.
4. **Lakeflow Jobs lab:** a multi-task DAG (notebook + SQL tasks), retries/branching, one **file-arrival trigger** and one **table-update trigger**.
5. **Declarative pipeline lab:** rebuild the medallion as a **Lakeflow Spark Declarative Pipeline** with expectations (Free Edition quota: 1 active pipeline — enough).
6. **Governance lab:** UC grants for two personas, one column mask, one row filter; browse the lineage UI.
7. **CI/CD lab:** wrap one job in an **Asset Bundle**, deploy dev→prod via the Databricks CLI from your terminal.

**AI rule:** notebooks are yours to hand-type; Claude Code may quiz you (paste an exam-guide section, ask for hard questions) — it may not write the lab code.

## Build — Satellites (~15 h)

**S3a — Spark Performance Forensics** *(recycled Week 9)*: deliberately slow job (skewed join, tiny files) on MovieLens → measure → apply fixes one at a time (broadcast, AQE, salting, repartition, file sizing) → `FORENSICS.md` with before/after Spark UI screenshots and a ranked impact table. The strongest Spark portfolio artifact that exists.

**S3b — Iceberg vs Delta bake-off** *(recycled Week 6, local)*: same workload through PyIceberg and delta-rs on your laptop; benchmark write/read/schema-evolution/time-travel; publish `BAKEOFF.md` with real numbers and a verdict. Read about **UniForm/format convergence** to frame the conclusion.

### Prove-it assignment (2–3 h): skew-detection kata

Before starting S3a, hand-write a small `detect_skew(df, key)` helper (partition-size distribution + a skew-ratio number) with provided pytest asserts against two synthetic DataFrames — one uniform, one skewed. It becomes the measuring instrument you use inside the forensics satellite.

## Career track (≤1 h/wk)

The week the cert lands: draft **resume v1** from PROGRESS.md's evidence (accomplishments with numbers — don't wait for P6); send your first 2–3 informational-interview / warm-outreach messages to people at `JOB-SEARCH.md` companies; book your **first Exponent mock interview** (free tier) — post-cert is the audit-recommended moment. Optional but high-leverage: one paid or community **mentor checkpoint** reviewing the spine repo — an hour of external eyes at mid-year is worth ten at month 12.

## Competency gate G3 ⭐

- [ ] **Databricks Certified Data Engineer Associate — passed.** (Book only after ≥80% on Derar Alhussein V4 practice exams.)
- [ ] Forensics artifact published (`FORENSICS.md` + screenshots).
- [ ] Bake-off artifact published.
- [ ] 3-minute narrated demo: your declarative pipeline graph with expectations catching bad rows.
- [ ] **External critique requested:** forensics or bake-off artifact posted to a practitioner community — request thread linked in PROGRESS.md.
- [ ] Career: resume v1 drafted · first outreach sent · first mock interview done.
- [ ] `INTERVIEW.md` updated with this phase's written answers.
- [ ] **Retrieval checkpoint:** 10 random earlier-phase terms + 15 `[P3]` terms (≥80%).

## Publish checkpoint

Two posts this phase: (1) the cert announcement with your honest prep notes (what the new exam actually tests); (2) the forensics story — "I made a Spark job 10× faster with six changes; here's each one ranked by impact."

## Interview questions you can now answer

- "A Spark job is slow — walk me through your diagnosis." 
- "What is a shuffle and why is it expensive?"
- "Delta vs Iceberg — how would you choose?" (with *your own* benchmark numbers)
- "Explain the medallion architecture and what lives in each layer."
- "Materialized view vs streaming table — when each?"
