# Phase 0 — Orientation & Setup

**Duration:** ~2 weeks · **Budget:** ~18 hours · **AWS cost:** $0 (you install the guardrails that keep the year ≤ $25/mo)

This phase is only setup and orientation. When it's done, everything works — and Phase 1 is pure learning.

## Objectives

1. Hold the **data engineering lifecycle** in your head as the map every later phase plugs into.
2. Speak the 10 Phase-0 contrast pairs confidently (they carry 80% of DE conversations).
3. Have a working local toolchain and a guard-railed AWS account.

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P0]`

Lifecycle · OLTP vs OLAP · ETL vs ELT · batch vs streaming · warehouse vs lake vs lakehouse · schema-on-write vs schema-on-read · row vs column orientation · pipeline · medallion · **idempotency** (the year's most important word).

## Learn (~8 h)

Every resource is **pinned** to an exercise — nothing here is learn-only (framework rule: information that isn't exercised evaporates).

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [The lifecycle primer](../../sources/research/de-lifecycle-primer.md) | Full read — the framework's own walkthrough of the lifecycle in project order | 2 | G0 voice memo: lifecycle explained aloud, no notes |
| *Fundamentals of Data Engineering* (Reis/Housley) — [O'Reilly](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) (~$45, often in libraries; if you can't get it, the primer + wiki row below cover G0) | Ch. 1–3: what DE is, the lifecycle, architecting. Later phases reference the rest | 4 | Same voice memo + the glossary self-quiz |
| [dataengineering.wiki Getting Started](https://dataengineering.wiki/Guides/Getting+Started+With+Data+Engineering) | Skim; bookmark as your second glossary | 1 | Glossary self-quiz (it's your cross-check source) |
| [GLOSSARY.md](../../GLOSSARY.md) `[P0]` terms | Active read: cover the definition, explain each term aloud in your own words | 1 | The Anki-generator assignment (you parse this very file) + self-quiz ≥8/10 |

**Video lane — optional swap.** Each row below **replaces** the default row it names: same "Pinned by" exercise, hours swap rather than add. Pick one lane per row before starting ([the rule](../../GUIDE.md#the-phase-loop)); prices, details, and the rows with no video twin: [COURSES.md](../../reference/COURSES.md).

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [DeepLearning.AI Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/data-engineering) — **Course 1 only** (Joe Reis + AWS) | Swaps the *Fundamentals of Data Engineering* ch. 1–3 row — the same lifecycle material from the same author, as lectures with graded AWS labs (Coursera $49/mo; one billing month covers it — read [COURSES.md](../../reference/COURSES.md) before subscribing) | 6–8 (vs 4 — the labs add time) | Same voice memo + the glossary self-quiz |

*Before starting, re-verify:* current install steps for uv and Docker (they change), and the FoDE edition/availability.

## Build — environment (~6 h)

1. **Local toolchain:** [uv](https://docs.astral.sh/uv/) (Python env manager) · Docker Desktop/Engine + Compose · VS Code · Git configured · the [DuckDB CLI](https://duckdb.org/docs/installation/) (separate from the Python package). Verify: `uv run python -c "import duckdb"` works in a fresh project. Install the **[gitleaks](https://github.com/gitleaks/gitleaks) pre-commit hook** in every repo you create this year — this repo ships the config ([`.pre-commit-config.yaml`](../../.pre-commit-config.yaml); install with `uvx pre-commit install`). The standing rule from day one: **no secret ever enters git** (the runtime half arrives in Phase 4 with a real secrets backend).
2. **First contact:** download one month of [NYC TLC yellow-taxi Parquet](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page), query it with the DuckDB CLI (`SELECT count(*), avg(trip_distance) ...`) — sixty seconds of magic that grounds everything Phase 1 does.
3. **AWS guardrails (non-negotiable):**
   - AWS Budget: $25/month with email alerts at 50/80/100%.
   - A dedicated `de-framework` IAM role/profile for all framework work (no root, least privilege).
   - **Prove the alarm fires:** create a temporary second budget at $0.01 (or set the real budget's first threshold to 0.01%), confirm the alert email arrives within 24 h, then restore the real thresholds. A budget alarm you've never seen fire is a hope, not a guardrail.
4. **Platform home:** create the GitHub repo that will hold the platform (suggested name: `aws-lakehouse-platform`). README with a one-paragraph mission statement. This repo is the centerpiece of your year — everything the framework builds lands here.
5. **This framework repo:** fork it and push your fork — your [`PROGRESS.md`](../../PROGRESS.md) lives there, and working in public keeps you honest.

**AI rule for this phase:** use your AI assistant freely to explain concepts and debug setup; type every shell command yourself so the toolchain is in your fingers. (Your fork also ships six helper skills for Claude Code — `/quiz`, `/gate-check`, `/start-phase`, `/resume`, `/explain`, `/satellite-brief` — see [the guide](../../GUIDE.md).)

### Prove-it assignment (~3 h): the Anki generator

Your first Python artifact, and the tool that powers every retrieval checkpoint of the year: a small script in your fork (suggested home: `tools/anki/`) that parses [GLOSSARY.md](../../GLOSSARY.md) (its format is strictly machine-parseable) and emits a flashcard deck — a **TSV file importable by [Anki Desktop](https://apps.ankiweb.net/)** (add Anki to your toolchain): term → definition + contrast pair, tagged by `[P#]` phase. Include a pytest for the parser: a malformed glossary line must **fail loudly**, not silently drop a card. Hand-type it; it's small enough to own completely. *(A reference parser ships at [`tools/glossary_check.py`](../../tools/glossary_check.py) for CI — build yours before reading it.)*

## Competency gate G0

- [ ] Explain the lifecycle stages and where a lakehouse fits, out loud, no notes (record a 3-minute voice memo — seriously; it exposes gaps reading hides).
- [ ] Self-quiz on **all 10** `[P0]` glossary terms: cover the definition, explain, check. **≥8/10** or repeat tomorrow (the `/quiz` skill runs this for you).
- [ ] DuckDB query over a local Parquet file runs, and you can say *why* Parquet made it fast (columns + compression).
- [ ] Budget-alarm test email received (the forced-fire test above); `de-framework` profile works.
- [ ] Both repos exist with real READMEs; gitleaks pre-commit hook installed in both.
- [ ] Anki generator works: deck imported into Anki, parser test green.

## Publish checkpoint

Optional but recommended: a short public post — "I'm spending the next 12 months becoming a data engineer in public; here's the framework I'm following." Sets the accountability stake.

## Check yourself — questions you can now answer

- "Explain ETL vs ELT and when you'd choose each."
- "What's a lakehouse and why did it emerge?"
- "Why is Parquet faster than CSV for analytics?"

---
← [Start here](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 1 — Foundations →](../phase-1-foundations/README.md)**
