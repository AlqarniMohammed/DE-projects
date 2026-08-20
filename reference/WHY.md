# Why the Framework Looks the Way It Does

Nothing in this file is required to follow the framework. This is where the reasoning lives, so the learner-facing files can stay short.

Jump: [The destination](#the-destination-a-full-data-stack) · [Hour math](#where-the-12-months-go--the-honest-hour-math) · [Design decisions](#why-one-platform-not-30-projects--the-design-decisions) · [Principles](#the-nine-principles) · [Skip-list](#what-we-deliberately-skip-and-why) · [Certs](#why-both-certs-land-by-month-7) · [Phase rationale](#why-each-phase-opens-the-way-it-does) · [Build in public](#why-build-in-public) · [Evidence](#where-the-evidence-comes-from)

## The destination: a full data stack

The framework ends with something big: a **complete data platform** covering the whole lifecycle — ingestion (batch, API, CDC, streaming), lakehouse storage, transformation, orchestration, quality and contracts, IaC, and a serving layer — plus a written **platform journey** telling its story. That is the kind of system real data teams publish engineering posts about; [Tweeq's journey](https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904) is one example of the *scale and completeness* being aimed at — not a stack to copy. No tool combination is "the right one"; the default path's choices are defaults, each with reasons below.

## Where the 12 months go — the honest hour math

The phase budgets sum to **~483 hours** (18 + 70 + 95 + 75 + 72 + 65 + 88). Practice-exam time and labs are counted, not hidden. Against the stated pace:

| Weekly pace | Total duration | Verdict |
|---|---|---|
| 9–10 h/week | ~12 months | The 12-month arc, with modest slack |
| 8 h/week | ~15 months | Fine — gates don't care about calendars |
| 6 h/week | ~20 months | Also a win — same destination, later arrival |

The title says 12 months; the gates say "when you're ready." Two **buffer weeks per half-year** are planned in (slack is scheduled, not stolen).

**The pre-authorized trim path.** If time runs short, cut in this order, nothing else: ① satellite S4a (Redshift hybrid — the P2 taste lab + exam theory already cover it), ② the Polars and Flink labs, ③ satellite S1 (the platform already teaches dbt from zero). **Trimming an item also strikes its line from the gate** — record it in `PROGRESS.md` as "(trimmed per the pre-authorized path)" so the evidence trail stays honest. **The platform and both certs are never trimmed.**

## Why one platform, not 30 projects — the design decisions

| Design choice | Evidence behind it |
|---|---|
| One evolving platform, not 30 disconnected weekly projects | Every roadmap failure-mode study flags the "capstone cliff" and tutorial hell; every real team builds one platform incrementally ([roadmap benchmarks](../sources/research/roadmap-benchmarks.md), [platform journeys](../sources/research/platform-journeys.md)). |
| Competency gates, not deadlines | Calendar-gated plans cascade when life happens. Gates are named artifacts + retrieval checks; slipping 2 weeks costs nothing. |
| Both certs in the first half of the year | Each exam's core surface is exactly what its phase builds (P2 = DEA's S3/Glue/Athena/Lake Formation; P3 = the Databricks environment itself), so prep and build align instead of competing. Sitting early also shrinks the blueprint-revision risk window. Full reasoning: [CERTS.md](CERTS.md). |
| A terminology on-ramp in every phase | The #1 reported problem with tool-dense plans is terminology overwhelm. Every phase lists its new terms first, linked to the glossary, taught as contrast pairs. |
| Every learn-resource pinned to an exercise | Passive watching is the other half of tutorial hell. Each Learn row names the drill, assignment, or written artifact that exercises it. |
| AWS-first, Databricks second, open-source satellites | AWS leads DE tool demand globally (40.3% of postings) and regionally; many regional postings pair Databricks + PySpark ([job market](../sources/research/job-market.md)). |
| Airflow deep, Dagster taste | Airflow is #1 in every demand source; Dagster is the credible challenger worth one satellite ([tools](../sources/research/tool-landscape.md)). |
| Streaming late, batch first | "Default to batch, justify streaming" — and every surveyed roadmap puts Kafka/streaming last of the core topics. |
| Platform > certs | Certs appear in only ~4% of postings; a built, explained, measured platform is the differentiator. The two certs are milestones, not the goal — which is also why there are 2, not 4. |
| External feedback built into the gates | Solo learners systematically miss their own gaps. From G2 every gate requires requesting community critique — the framework never grades itself alone. |
| An AI-data module at the end | LLM-pipeline skills jumped ~3% → ~12% of DE postings in one year — a differentiator, not the core. |

## The nine principles

1. **SQL and Python are the permanent spine** — they appear in 70–94% of postings; every phase keeps exercising them.
2. **Idempotency + retries is the reliability model.** Re-runnable jobs, MERGE-upsert semantics, orchestrator retries, alerts. The highest lesson-density skill across all seven real-platform case studies.
3. **Many small jobs, never a mega-DAG.** Two teams independently regretted the monolith DAG within a year.
4. **Three modeling layers from day one** (staging → intermediate → marts). Two teams independently regretted two.
5. **Table maintenance is the lakehouse's hidden cost** — compaction, snapshot expiry, schema evolution are first-class learning objectives, not footnotes.
6. **Concepts are the skeleton; tools are replaceable leaves.** When a tool churns (they will), the phase objective survives.
7. **Anything you build must survive weeks of your inattention** — prefer serverless over self-hosted; the framework never asks you to run Kubernetes.
8. **Nothing is learn-only.** Every piece of information is pinned to an exercise, assignment, or written artifact — unexercised knowledge evaporates.
9. **Ship the phase, then improve it.** A gate passed at "good" beats a phase polished forever.

## What we deliberately skip, and why

Full verdicts in [TOOLS.md](TOOLS.md):
- **Hadoop/HDFS ops, Hive-only patterns** — legacy; concepts arrive via Spark/Glue anyway.
- **Prefect, Kestra** — a third Python orchestrator adds nothing over Airflow + Dagster.
- **Apache Hudi** — niche upsert estates; Iceberg + Delta cover the concepts.
- **StarRocks/Doris** — a second OLAP engine adds nothing at this level; ClickHouse covers the category.
- **Kubernetes administration** — not a DE entry requirement; serverless covers this year.
- **Scala** — PySpark first; revisit only if a specific need demands it.
- **Deep Flink** — one Flink SQL lab (Phase 5); stateful streaming depth is a later specialization.
- **A third cloud** — one light Azure-vocabulary pass (Phase 6) as a regional-enterprise hedge; no Azure builds.
- Also skipped as credentials: a third certificate and pre-P1 SQL video courses — reasoning in [CERTS.md](CERTS.md).

## Why both certs land by month 7

Sitting DEA-C01 at gate G2 means the exam lands while the P2 build (its exact hands-on surface) is freshest; the Databricks exam at G3 works the same way — the phase *is* the prep. Doing both in the first half leaves the second half free for the platform's hardest engineering (orchestration, streaming, production hardening) with no prep clock running. The exams' hands-on gaps (Kinesis/DMS/Redshift depth) are bought down with P2 mini-labs, then genuinely closed in P4 — after the exam, when operating them is pure learning. Full blueprints and prep plans: [CERTS.md](CERTS.md).

## Why each phase opens the way it does

- **P0 is only setup** because the single most-reported failure mode of public DE courses is the "week-1 setup wall" — Docker + cloud + IaC landing on top of new concepts. Isolating setup means Phase 1 starts with everything working.
- **P1 gets two full months** for what many plans cram into a week: foundations deserve a learn-first rhythm and one dataset carried end-to-end.
- **P2's stack (S3 + Iceberg + Athena + dbt)** is a production pattern — the same stack a UK-government data platform runs ([platform journeys](../sources/research/platform-journeys.md)), not a teaching toy.
- **P4 is deliberately exam-free**: Kinesis, DMS, and Redshift arrive as services already studied, now operated for real — theory first, then practice with no pressure, is the cheap order.
- **P5 goes open-source** because Kafka's mechanics transfer everywhere; the AWS way was already learned in P4.
- **P6 packages instead of building from scratch** — the platform *is* the capstone, built all year instead of assembled in week 30.

## Why build in public

One post per phase, drafted from that phase's publish checkpoint — the year's arc in ~9 posts, from the local lakehouse to the platform-journey finale. Writing about a build sharpens the understanding of it, creates a public record of steady progress, and each post pairs with one interactive act (answer a community question, comment substantively) so it's participation, not broadcasting. Platform choice is yours — a blog, dev.to, LinkedIn, anywhere public.

## Where the evidence comes from

The framework was compiled 2026-08-20 from six parallel deep-research reports (tool landscape, cert blueprints, courses, platform case studies, roadmap benchmarks, market signals — indexed in [SOURCES.md](SOURCES.md)), then independently audited and revised twice ([CHANGELOG.md](../CHANGELOG.md)). Tool versions and cert blueprints churn — each phase README lists what to re-verify before starting it, a weekly link-check Action guards the references, and the structure is concept-keyed precisely so tool churn doesn't invalidate it.

---
[README](../README.md) · [Guide](../GUIDE.md) · [Sources](SOURCES.md)
