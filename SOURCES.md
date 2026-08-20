# Sources & Audit Trail

Everything the framework claims traces to one of these. Research compiled **2026-08-20** by six parallel deep-research passes; audits performed the same day.

## Research reports (in [`sources/research/`](sources/research/))

| Report | What it established | Key findings that shaped the framework |
|---|---|---|
| [`tool-landscape.md`](sources/research/tool-landscape.md) | CORE/AWARE/SKIP verdict for ~60 tools, 45+ sources | Iceberg won the format war (v3); S3 Tables matured; Airflow 3 is a different product; Kafka 4 killed ZooKeeper; dbt+Fivetran merged; GX reset; dlt is the breakout ingestion tool; AI-assisted DE is now assumed |
| [`certs.md`](sources/research/certs.md) | Official blueprints (read from the exam-guide PDFs), prep, timing | Databricks exam rewritten twice (current: May 2026, PySpark/Lakeflow/UC-first); DEA-C01 still v1.0; "dbt Foundational Certificate" doesn't exist; Learning Festival 50% voucher; Free Edition replaced Community Edition |
| [`courses.md`](sources/research/courses.md) | Best current resources per skill area, verified live | FoDE still canonical (no 2nd ed); DE Zoomcamp Jan 2027 cohort; Astronomer/Dagster/Confluent/Databricks academies all free and current; DDIA 2E published Mar 2026; GX acquired by FICO — quality stack is dbt tests + dbt-expectations (metaplane) + Elementary |
| [`platform-journeys.md`](sources/research/platform-journeys.md) | Tweeq deep-read + 6 comparable build journeys | Consensus build order (ingest→dbt 3 layers→orchestrator→BI→quality); UK MoJ validates the exact spine stack; serving layer = satellite fed from marts; idempotency+retries is the reliability model; monolith DAGs and 2-layer modeling are the universal regrets |
| [`roadmap-benchmarks.md`](sources/research/roadmap-benchmarks.md) | How 9 well-known DE roadmaps are structured + their failure modes | Copied: lifecycle-as-skeleton, phase-terminal milestone gates with rubrics, skip-lists, contrast-pair glossary, setup isolated in a pre-phase; added what none have: spaced-retrieval checkpoints |
| [`job-market.md`](sources/research/job-market.md) | Global + Saudi/Gulf demand signals | SQL+Python co-#1 (70–94%); AWS #1 cloud (40.3%), in-Kingdom region 2026; Gulf pairs Databricks+PySpark; Airflow only orchestrator worth depth; certs in ~4% of postings — portfolio wins; AI-pipeline skills 3%→12% in a year |

## Audits (in [`sources/`](sources/))

- [`audit-30-projects.md`](sources/audit-30-projects.md) — disposition of every project in the old 30-project plan: 19 absorbed into the spine, 7 survive as satellites, 3 shrink to labs, 1 dropped; plus the six structural faults that made the old plan overwhelming.
- [`audit-guide-and-posts.md`](sources/audit-guide-and-posts.md) — the 2026 master guide's 10-item gap list (no serving layer, no SQLMesh, stale versions, no learning layer, cost blind spots…) and the senior-posts corroboration table with the anti-drift check: **no module exists because a post featured it**; every overlap is independently corroborated by cert blueprints or research.
- [`DE-audit.md`](sources/DE-audit.md) — the independent expert audit of the framework itself (2026-08-20, at commit `c8457cc`): 13 prioritized findings. **Verdict: all 13 adopted in revision v1.1**, with two refinements (external critique gated on *requested + linked*, not received; the P5 sink resolved as PyIceberg → Glue/S3 Tables REST catalog). Its cert-timing assumption was superseded by the resequencing decision (both certs by ≈ month 7 — see [`CERTS.md`](CERTS.md)).
- [`improvements-v1.md`](sources/improvements-v1.md) — the improvement review that triggered revision v1.1. Adopted: cert resequencing (as the month-4–7 compromise), every-resource-pinned-to-an-exercise rule, per-tool source-of-truth links, the multi-learner edition via requirement-generator prompts, dataset menus. Declined with reasons: a third certificate and pre-P1 SQL video courses (see [`CERTS.md`](CERTS.md) audit note).

## Original materials (in [`sources/`](sources/))

- [`context.md`](sources/context.md) — the brief that started this framework (2026-08-20)
- [`original-prompt.md`](sources/original-prompt.md) + [`original-outcomes.md`](sources/original-outcomes.md) — the old 30-project prompt and its full output
- [`de-master-guide-2026.md`](sources/de-master-guide-2026.md) — the earlier tool guide (audited above)
- [`de-lifecycle-reference.md`](sources/de-lifecycle-reference.md) — DEA course Section-1 notes reorganized by project lifecycle (used as Phase 0 reading)
- [`senior-de-posts.md`](sources/senior-de-posts.md) — senior practitioner posts (verification reference only, per the brief)
- Tweeq article (external): <https://engineering.tweeq.sa/tweeq-data-platform-journey-and-lessons-learned-clickhouse-dbt-dagster-and-superset-fa27a4a61904>

## Known evidence gaps (stated, not hidden)

- No quantified skills scrape exists for the Saudi market specifically — KSA conclusions are directional, assembled from job boards and individual postings.
- Saudi fintech (Tamara/Tabby/stc pay/Lean) stack details weren't publicly findable — monitor their career pages directly during the job-search phase.
- The dbt "61% of postings" figure and the "12% LLM-in-DE" figure each rest on a single, potentially biased source; both were used directionally, not as load-bearing facts.
- Cert blueprints and tool versions churn: each phase README lists what to re-verify before starting it.

## Optional add-on evaluated but not scheduled

**DataTalksClub DE Zoomcamp, Jan 2027 cohort** (free) — its window happens to align with Phases 3–4 of a September start. Verdict: **do not run it in parallel** at 6–10 h/wk (it alone is 5–15 h/wk; parallel-running recreates the overwhelm this framework exists to fix). It becomes attractive only if you want its community + peer-reviewed capstone *instead of* this framework's P3–P4 satellites — a conscious swap, decided at the end of Phase 2. Details in [`sources/research/courses.md`](sources/research/courses.md).
