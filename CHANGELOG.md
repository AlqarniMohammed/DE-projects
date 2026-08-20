# Changelog

## v1.2 — 2026-08-20 · Comprehensive audit + repositioning

A five-track audit (principal-engineer technical review with external verification against official docs · a full learner-journey walkthrough · usability/navigation design · internal-consistency sweep · a "nothing is learn-only" coverage matrix) produced ~55 findings; every decision below was reconciled explicitly.

**Repositioned as a pure upskilling framework.** Career/job-search content removed throughout; end-of-phase question sections kept as "Check yourself" knowledge checks, and `INTERVIEW.md` became `SELF-CHECK.md`. The destination is stated plainly: a full end-to-end data stack of the kind engineering teams publish journey posts about, with the learner's own `JOURNEY.md` as the capstone write-up.

**Made easy to use.**
- New **GUIDE.md** — a literal do-this-then-this operating manual (Day 0, the phase loop, the comeback ritual); README rewritten as a short plain-language front door; rationale moved to **reference/WHY.md**.
- Six **Claude Code skills** ship in-repo: `/start-phase`, `/quiz`, `/gate-check`, `/satellite-brief`, `/explain`, `/resume` (with manual fallbacks for every flow).
- Slim root: reference docs moved under `reference/`; navigation footers + prev/next links on every phase; jump rows on long files.
- **MkDocs Material site** (single-source from the same markdown) + deploy workflow.
- ASCII/mermaid route map replaced with **draw.io diagrams** (route map + phase loop, sources and SVG committed).

**Reliability fixes.**
- Gate checklists de-duplicated: the phase README's gate is now the **single source of truth**; PROGRESS.md became a pure evidence tracker. All 20 drift items reconciled (competency-bearing additions absorbed into phase gates).
- Retrieval quizzes re-based to "all current-phase terms + 10 random earlier" (previous fixed counts exceeded the glossary's inventory in four places).
- GLOSSARY normalized to a strict machine-parseable grammar; new CI check (`tools/glossary_check.py`, also the Phase-0 parser's reference implementation); weekly link-check now files an issue on failure; gitleaks `.pre-commit-config.yaml` ships in-repo.
- Hour math trued up (P2/P3/P6); phase budgets now sum to ~483 h with practice-exam time counted.

**Technical corrections (externally verified).**
- P2 dbt×S3 Tables catalog pattern stated explicitly (read via Athena's federated `s3tablescatalog`, materialize marts in the Glue catalog; the July-2026 `catalog_type: s3_tables` adapter route noted as a pinned advanced variant).
- Airflow 3 removed SLAs → the P4 build now teaches **Deadline Alerts**.
- The P5 sink names its idempotency mechanism (PyIceberg `upsert()`; naive-append failure demonstrated first) and S5 forewarns the Debezium-envelope extension.
- P4 CDC lab teardown tightened to ≤5 days so the $8 cap holds; Confluent credential named correctly (Data Streaming Engineer Foundations certificate); SEC EDGAR User-Agent requirement noted; CI-to-AWS auth specified as OIDC.

**Learner-journey fixes.** Budget-alarm forced-fire test (the old checkbox was unsatisfiable at $0 spend); dimensional-modeling glossary cluster + P1 terminology (was required but untaught); a 2-h PySpark-basics row before the first hand-written Glue job; the Spark-forensics satellite got an explicit home (local PySpark — serverless can't show the Spark UI it needs); the satellite generator got output destinations, sealing mechanics, an unseal step, and a committed worked example; placement got a no-deck path, an explicit certification rule, and a worked example; prove-it assignments restored in P5/P6; conventions stated once (notes/ home, video hosting, the OLTP generator spec, COMPARISON.md axes).

**Coverage.** Five phantom TOOLS.md placements reconciled; micro-drills added for the five quiz-only terms (CTAS, partition projection, XCom, Arrow; outbox promoted to a fixed S5 objective); the AWARE tier's act-of-output rule stated; `AI-USAGE.md` added as the checked act for AI-assisted DE.

## v1.1 — 2026-08-20 · Expert audit + improvement review reconciled

All 13 findings of an independent expert audit adopted (published hour math with a pre-authorized trim path; external critique required at every gate from G2; secrets story with gitleaks + SSM; dimensional modeling made explicit; pytest+moto testing; PR workflow from P1; regional dataset options + PDPL; per-lab cost caps; link-check CI; re-verify windows). Certifications resequenced — AWS DEA-C01 at gate G2, Databricks DE Associate at gate G3, both by ≈ month 7. Multi-learner edition added: placement protocol, level guarantee, and the satellite-requirements generator with sealed reference solutions. Deliberately declined: a third certificate and pre-P1 SQL video courses.

## v1.0 — 2026-08-20 · Initial framework

Twelve-month, competency-gated framework: one AWS lakehouse platform grown across 7 phases (P0–P6) with satellite projects per phase; gates as named artifacts + spaced-retrieval quizzes; built from six parallel deep-research reports and audits of earlier planning materials.
