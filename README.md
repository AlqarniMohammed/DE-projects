# The Data Engineer Framework (2026–2027)

A 12-month, competency-gated framework for becoming a properly trained data engineer — combining **courses, certifications, and projects** around one evolving AWS Lakehouse platform. Built from six deep-research reports (tool landscape, cert blueprints, courses, platform case studies, roadmap benchmarks, job market — see [`sources/research/`](sources/research/)) and a full audit of earlier planning materials ([`sources/`](sources/)).

> **Who this is for:** an AWS SAA-certified professional with strong SQL and data-modeling skills, ~6–10 focused hours/week, targeting a data-engineer role transition (Saudi/Gulf-first, remote-global second).

---

## The idea in one paragraph

You build **one platform all year** — the **spine**: an AWS Lakehouse (S3 + Iceberg/S3 Tables + Glue + Athena + dbt + Airflow) that grows a new capability each phase, exactly the way real teams grow theirs (validated against 7 real platform-build case studies, including [Tweeq's](sources/research/platform-journeys.md)). Around it, each phase adds one or two **satellite projects** for tool diversity (Databricks/Delta, Dagster, Debezium, ClickHouse + Superset, an AI/RAG data pipeline). Every phase follows the same rhythm — **Learn → Build → Gate** — and you advance when you pass the **competency gate**, not when the calendar says. Two certification milestones anchor the middle of the year: **Databricks DE Associate** (≈ month 6) and **AWS DEA-C01** (≈ month 8–9).

## Why this framework looks the way it does

| Design choice | Evidence behind it |
|---|---|
| One evolving platform, not 30 disconnected weekly projects | Every roadmap failure-mode study flags the "capstone cliff" and tutorial hell; every real team builds one platform incrementally ([roadmap benchmarks](sources/research/roadmap-benchmarks.md), [platform journeys](sources/research/platform-journeys.md)). The old 30-project plan is audited in [`sources/audit-30-projects.md`](sources/audit-30-projects.md) — the good projects survive as satellites. |
| Competency gates, not deadlines | Calendar-gated plans cascade when life happens. Gates are named artifacts + retrieval checks; slipping 2 weeks costs nothing. |
| A terminology on-ramp in every phase | The #1 reported problem with the old plan was terminology overwhelm. Every phase lists its new terms first, linked to [`GLOSSARY.md`](GLOSSARY.md), taught as contrast pairs. |
| AWS-first, Databricks second, open-source satellites | AWS leads DE job postings globally (40.3%) and in KSA; Gulf postings conspicuously pair Databricks + PySpark; AWS's in-Kingdom region lands 2026 ([job market](sources/research/job-market.md)). |
| Airflow deep, Dagster taste | Airflow is #1 in every demand source; Dagster is the credible challenger worth one satellite ([tools](sources/research/tool-landscape.md)). |
| Streaming late, batch first | "Default to batch, justify streaming" — and every surveyed roadmap puts Kafka/streaming last of the core topics. |
| Portfolio > certs | Certs appear in only ~4% of postings; fewer than 1 in 10 junior candidates show any portfolio. The spine + satellites *are* the differentiator; the two certs are milestones, not the goal. |
| An AI-data module at the end | LLM-pipeline skills jumped ~3% → ~12% of DE postings in one year and compound with Vision-2030 hiring — a differentiator, not the spine. |

## The 12-month map

```
 P0          P1              P2              P3              P4              P5              P6
 Orientation Foundations     AWS Lakehouse   Spark &         Orchestration   Streaming       Production,
 & Setup     SQL·Python·dbt  Core            Databricks      & Ingestion     & CDC           Serving & Capstone
 ~2 wks      Mo 1–2          Mo 3–4          Mo 5–6          Mo 7–8          Mo 9–10         Mo 11–12
 ──────────  ──────────────  ──────────────  ──────────────  ──────────────  ──────────────  ─────────────────
 env setup   SPINE v0.1:     SPINE v1:       Databricks      SPINE v2:       SPINE v3:       SPINE v4: quality,
 lifecycle   local lakehouse S3·Glue·Athena  Free Edition    Airflow 3,      Kafka event     lineage, Terraform,
 glossary    DuckDB·Iceberg  S3 Tables       labs (Lakeflow, dlt, DMS CDC,   path, stream    observability
 bootcamp    dbt 3 layers    dbt-athena      UC, medallion)  Kinesis         → Iceberg       ────────────────
             ─────────────   ─────────────   ─────────────   ─────────────   ─────────────   SATELLITES:
             SATELLITE:      SATELLITE:      SATELLITES:     SATELLITES:     SATELLITE:      ClickHouse+Superset
             first dbt       cost-aware      Spark forensics Redshift hybrid Debezium vs     serving layer ·
             project         Athena mart     Iceberg-vs-     Dagster vs      DMS comparison  AI/RAG data pipeline
                                             Delta bake-off  Airflow                         ────────────────
 GATE:       GATE:           GATE:           GATE: ⭐        GATE: ⭐        GATE:           GATE: capstone
 env demo +  local demo +    AWS spine live  DATABRICKS      AWS DEA-C01     CDC artifact +  rubric + portfolio
 20 terms    dbt docs graph  + cost report   DE ASSOCIATE    (mo 8–9)        stream demo     + mock interviews
                                             (mo 6–7)
```

Each phase's full spec lives in [`phases/`](phases/):
[Phase 0](phases/phase-0-orientation/README.md) · [Phase 1](phases/phase-1-foundations/README.md) · [Phase 2](phases/phase-2-aws-lakehouse-core/README.md) · [Phase 3](phases/phase-3-spark-databricks/README.md) · [Phase 4](phases/phase-4-orchestration-ingestion/README.md) · [Phase 5](phases/phase-5-streaming/README.md) · [Phase 6](phases/phase-6-production-serving/README.md)

## How to use this framework

1. **Work one phase at a time.** Open the phase README. It always has the same sections: *Objectives → New terminology → Learn → Build (spine increment) → Build (satellite) → Competency gate → Cert checkpoint → Publish checkpoint → Interview questions.*
2. **Learn before you build.** Each phase front-loads a small, bounded learning block (courses/readings with hour estimates). Don't start the build before the listed on-ramp — that's the overwhelm trap the old plan fell into.
3. **The gate decides when you move on.** Each gate is a named artifact you can demo plus a short retrieval checkpoint on *earlier* phases' terms (spaced repetition — the mechanism every public roadmap lacks). Track gates in [`PROGRESS.md`](PROGRESS.md).
4. **Publish per phase, not per week.** One LinkedIn post per phase, drafted from the phase's "publish checkpoint" prompt. Build in public without the treadmill.
5. **Use AI deliberately.** Use Claude Code to scaffold, explain errors, and explain terminology — but hand-type the core artifacts of each phase (the dbt models, the DAG, the Spark job). The rule per phase is stated in its Build section. AI-assisted DE is now assumed in job specs; *unexamined* AI output teaches nothing.
6. **Cost posture:** target ≤ **$25/month** AWS. Every spine increment lists its cost posture. Non-negotiables from day one: AWS Budget alert + `make destroy`-style teardown for anything chargeable. Exam fees: Databricks $200 (often $100 via Learning Festival voucher) + AWS $150.

## Repo map

| File | What it is |
|---|---|
| [`GLOSSARY.md`](GLOSSARY.md) | The terminology on-ramp — every term the phases use, taught as contrast pairs, tagged by phase |
| [`TOOLS.md`](TOOLS.md) | The tool universe: CORE / AWARE / SKIP verdict, phase placement, cert mapping, evidence |
| [`CERTS.md`](CERTS.md) | Both cert blueprints mapped to phases, study plans, exam timing, vouchers |
| [`PROGRESS.md`](PROGRESS.md) | Competency-gate tracker + retrieval checkpoints |
| [`SOURCES.md`](SOURCES.md) | Research bibliography + audit verdicts |
| [`phases/`](phases/) | One folder per phase: the executable spec |
| [`sources/`](sources/) | Original materials + the six research reports + audits |

## Principles (read once, re-read when stuck)

1. **SQL and Python are the permanent spine** — they appear in 70–94% of postings; every phase keeps exercising them.
2. **Idempotency + retries is the reliability model.** Re-runnable jobs, MERGE-upsert semantics, orchestrator retries, alerts. The highest lesson-density skill across all seven real-platform case studies.
3. **Many small jobs, never a mega-DAG.** Two teams independently regretted the monolith DAG within a year.
4. **Three modeling layers from day one** (staging → intermediate → marts). Two teams independently regretted two.
5. **Table maintenance is the lakehouse's hidden cost** — compaction, snapshot expiry, schema evolution are first-class learning objectives, not footnotes.
6. **Concepts are the skeleton; tools are replaceable leaves.** When a tool churns (they will), the phase objective survives.
7. **Anything you build must survive weeks of your inattention** — prefer serverless over self-hosted; the framework never asks you to run Kubernetes.
8. **Ship the phase, then improve it.** A gate passed at "good" beats a phase polished forever.

## Explicit skip-list (and why)

You will **not** study these this year — each was evaluated and cut deliberately (full verdicts in [`TOOLS.md`](TOOLS.md)):
- **Hadoop/HDFS ops, Hive-only patterns** — legacy; concepts arrive via Spark/Glue anyway.
- **Prefect, Kestra** — a third Python orchestrator adds no employability over Airflow + Dagster.
- **Apache Hudi** — niche upsert estates; Iceberg + Delta cover the concepts.
- **StarRocks/Doris** — a second OLAP engine adds nothing at entry level; ClickHouse covers the category.
- **Kubernetes administration** — not a DE entry requirement; serverless covers this year.
- **Scala** — PySpark first; revisit only if a target employer demands it.
- **Deep Flink** — one Flink SQL lab (Phase 5); stateful streaming depth is a post-job specialization.
- **A third cloud** — one light Azure-vocabulary lab (Phase 6) hedges the Saudi enterprise market; no Azure builds.

---

*Framework compiled 2026-08-20 from research current to that date. Tool versions and cert blueprints churn — each phase README notes what to re-verify before starting it (cert pages, course editions). The structure is concept-keyed precisely so tool churn doesn't invalidate it.*
