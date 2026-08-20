# Phase 0 — Orientation & Setup

**Duration:** ~2 weeks · **Budget:** ~18 hours · **AWS cost:** $0 (plus you *install the guardrails* that keep the year ≤$25/mo)

Setup is isolated here on purpose — the single most-reported failure mode of public DE courses is the "week-1 setup wall" where Docker + cloud + IaC land on top of new concepts. Here, setup is the *whole* phase, so Phase 1 starts with everything working.

## Objectives

1. Hold the **data engineering lifecycle** in your head as the map every later phase plugs into.
2. Speak the ~10 Phase-0 contrast pairs confidently (they carry 80% of DE conversations).
3. Have a working local toolchain and a guard-railed AWS account.

## New terminology (read first → [GLOSSARY.md](../../GLOSSARY.md) `[P0]` section)

Lifecycle · OLTP vs OLAP · ETL vs ELT · batch vs streaming · warehouse vs lake vs lakehouse · schema-on-write vs schema-on-read · row vs column orientation · pipeline · medallion · **idempotency** (the year's most important word).

## Learn (~8 h)

Every resource is **pinned** to an exercise — nothing here is learn-only (framework rule: information that isn't exercised evaporates).

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [`sources/de-lifecycle-reference.md`](../../sources/de-lifecycle-reference.md) — your own lifecycle notes | Full read; it's the best asset you already have | 2 | G0 voice memo: lifecycle explained aloud, no notes |
| *Fundamentals of Data Engineering* (Reis/Housley) | Ch. 1–3 (what DE is, the lifecycle, architecting) — the rest is referenced by later phases | 4 | Same voice memo + the 20-term self-quiz |
| [dataengineering.wiki Getting Started](https://dataengineering.wiki/Guides/Getting+Started+With+Data+Engineering) | Skim; bookmark as your second glossary | 1 | 20-term self-quiz (it's your cross-check source) |
| [GLOSSARY.md](../../GLOSSARY.md) `[P0]` terms | Active read: cover the definition, explain each term aloud in your own words | 1 | The Anki-generator assignment (you parse this very file) + self-quiz ≥17/20 |

## Build — environment (~6 h)

1. **Local toolchain:** [uv](https://docs.astral.sh/uv/) (Python env manager) · Docker Desktop/Engine + Compose · VS Code · Git configured. Verify: `uv run python -c "import duckdb"` works in a fresh project. Install a **[gitleaks](https://github.com/gitleaks/gitleaks) pre-commit hook** in every repo you create this year — the standing rule from day one is: **no secret ever enters git** (the runtime half of this rule arrives in Phase 4 with a real secrets backend).
2. **First contact:** download one month of [NYC TLC yellow-taxi Parquet](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), query it with DuckDB CLI (`SELECT count(*), avg(trip_distance) ...`) — sixty seconds of magic that grounds everything Phase 1 does.
3. **AWS guardrails (non-negotiable, from your existing account):**
   - AWS Budget: $25/month with email alert at 50/80/100%.
   - A dedicated `de-framework` IAM role/profile for all framework work (no root, least privilege — you know this from SAA).
   - Billing alarm verified by the confirmation email.
4. **Portfolio home:** create the GitHub repo that will hold the spine platform (suggested name: `aws-lakehouse-platform`). README with a one-paragraph mission statement. This repo is your portfolio centerpiece for the year.
5. **This framework repo:** push it to GitHub too — maintaining it in public *is* part of the portfolio story (like your `solutions-architecture-projects`).

**AI rule for this phase:** use Claude Code freely to explain concepts and debug setup; type every shell command yourself so the toolchain is in your fingers.

### Prove-it assignment (~3 h): the Anki generator

Your first Python artifact, and the tool that powers every retrieval checkpoint of the year: a small script that parses [GLOSSARY.md](../../GLOSSARY.md) (its format is machine-parseable) and emits an **Anki deck** — term → definition + contrast pair, tagged by `[P#]` phase. Include a pytest for the parser (a malformed glossary line must fail loudly, not silently drop a card). Hand-type it; it's small enough to own completely.

## Competency gate G0

- [ ] Explain the lifecycle stages and where a lakehouse fits, out loud, no notes (record a 3-minute voice memo — seriously; it exposes gaps reading hides).
- [ ] 20-term self-quiz on `[P0]` glossary terms: cover the right column, define, check. ≥17/20 or repeat tomorrow.
- [ ] `duckdb` query over a local Parquet file runs and you can say *why* Parquet made it fast (columns + compression).
- [ ] AWS budget alert email received; `de-framework` profile works.
- [ ] Both GitHub repos exist with real READMEs; gitleaks pre-commit hook installed in both.
- [ ] Anki generator works: deck imported, parser test green.

## Publish checkpoint

Optional but recommended: a short post — "I'm spending the next 12 months becoming a data engineer in public; here's the framework I'm following." Sets the accountability stake.

## Interview questions you can now answer

- "Explain ETL vs ELT and when you'd choose each."
- "What's a lakehouse and why did it emerge?"
- "Why is Parquet faster than CSV for analytics?"
