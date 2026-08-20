# Audit & Improvement Review — `DE-projects` (The Data Engineer Framework 2026–2027)

**Audit date:** 2026-08-20 · **Scope:** full repo — README, all 7 phase specs, GLOSSARY, TOOLS, CERTS, PROGRESS, SOURCES, audits · **Method:** cloned at commit `c8457cc` and read every file

---

## 1. Overall assessment

This is an unusually well-constructed self-study framework. Before the findings, what should **not** change:

- **The spine + satellites model** is the right call and is well-defended by the platform-journeys research. Keep it.
- **Competency gates with named artifacts** solve the real failure mode of calendar-driven plans.
- **The contrast-pair glossary and spaced-retrieval checkpoints** are genuinely differentiated — no public roadmap has them.
- **The skip-list with reasons** and the "contested calls" section in TOOLS.md show honest judgment; that transparency is itself portfolio material.
- **Cost guardrails from day zero** ($25/mo, teardown discipline, budget alarms) are production thinking applied to learning.
The findings below are refinements, not restructuring. They fall into four groups: **critical** (fix before Phase 0), **content gaps**, **process improvements**, and **minor polish**.

---

## 2. Critical findings — address before starting Phase 0

### 2.1 The time-budget math only works at the top of your stated range

The phase budgets sum to **~465 hours** (15 + 70 + 70 + 80 + 85 + 65 + 80). Against the stated pace of 6–10 h/week:

| Weekly pace | Time to finish | Verdict |
|---|---|---|
| 6 h/week | ~78 weeks (**~18 months**) | Framework silently becomes an 18-month plan |
| 8 h/week | ~58 weeks (~13.5 months) | Close, no slack |
| 10 h/week | ~47 weeks | Fits in 12 months, ~5 weeks of slack |

The gates absorb *slipping*, but the README promises a 12-month arc without stating that it requires ~9–10 focused h/week with almost no buffer for illness, work crunches, or Ramadan-month reality.

**Recommendation:**
- State the math openly in the README ("465 h ≈ 12 months at 9 h/wk, 18 months at 6 h/wk — both are wins").
- Define a **pre-authorized trim path**: which satellites get cut first if time runs short. Suggested order: S4a Redshift hybrid (exam theory can substitute) → Polars/Flink labs → S1 first-dbt satellite (the spine already teaches dbt). The spine and both certs are never trimmed.
- Add 2 explicit **buffer weeks** per half-year to the map so slack is planned, not stolen.
### 2.2 The career workstream starts 3–5 months too late

Everything career-facing — resume rewrite, mock interviews, portfolio surfacing, pinned repos — lives in Phase 6 (months 11–12). But:

- Gulf/Saudi hiring cycles commonly run **2–5 months** from application to offer.
- Your two strongest ATS signals (Databricks cert ≈ month 6–7, DEA-C01 ≈ month 8–9) land mid-year — that is the natural moment to start applying, with the spine already at v2 (orchestrated, CDC, streaming-lite).
- SOURCES.md itself flags "monitor Saudi fintech career pages during the job-search phase" — but no phase schedules that monitoring.
**Recommendation:** add a lightweight **parallel career track** (≤1 h/week) starting at Phase 3:
- **P3 gate:** LinkedIn profile rewritten around the cert + spine; begin a `JOB-SEARCH.md` watchlist (Tamara, Tabby, stc pay, Lean, Tweeq, NEOM/PIF entities, Aramco Digital, banks' data teams).
- **P4 gate:** first informational interviews / warm outreach; resume v1 drafted from PROGRESS.md evidence (don't wait for P6).
- **P5 onward:** 3–5 targeted applications per month. Interviewing *while* finishing P5–P6 turns interview feedback into curriculum — the strongest possible gate.
- Phase 6 then becomes polish and scale-up, not a cold start.
### 2.3 Every gate is self-graded — add external feedback loops

Self-assessment is the framework's single point of failure: the capstone rubric says "self-graded honestly," but solo learners systematically miss their own gaps (the same reason the plan mandates voice memos). External signal currently arrives only via LinkedIn post reactions and P6 mocks.

**Recommendation:**
- Add **one external review per gate** from G2 onward: post the phase artifact to r/dataengineering, the dbt Slack, or DataTalksClub Slack and request critique; link the thread as gate evidence.
- Move the **first mock interview to the G3/G4 boundary** (post-cert), not month 11. Exponent's free tier already allows this.
- Consider one paid or community **mentor checkpoint** at mid-year (month 6) reviewing the spine repo — a 1-hour review then is worth ten at month 12.
### 2.4 Repo hygiene — five quick fixes while the repo is one commit old

| Issue | Fix |
|---|---|
| `.claude/scheduled_tasks.lock` is committed (internal tool lock file with a session ID/PID) | Delete it; it should never be in git |
| No `.gitignore` | Add one now: `.claude/`, `data/`, `.env`, `__pycache__/`, `*.duckdb`, `.terraform/`, `target/` (dbt) |
| No LICENSE | The README invites public use of the framework — add CC-BY-4.0 (docs) or MIT. Unlicensed = legally "all rights reserved," which suppresses forks/stars |
| Filename typos: `de-lifecycle-refrence.md` (→ *reference*), `original-outcoms.md` (→ *outcomes*) | Rename **now** (only Phase-0 links break, and the repo is 1 commit old). Typos in filenames undercut the "documentation quality is the differentiator" story this repo tells |
| README's "for whom" note is author-specific but the repo is public | One line — "Forking this? Re-derive the market assumptions for your region from `sources/research/`" — turns a personal plan into a reusable artifact, and community traction on *this* repo is itself portfolio signal |

---

## 3. Content gaps — high-value additions

### 3.1 Secrets management is absent from the entire year
The builds accumulate real credentials — RDS passwords, Slack webhooks, API keys for dlt sources, Databricks tokens, Kafka SASL configs — yet no phase teaches how to handle them. This is both a genuine production skill and a common interview probe ("how do your DAGs get credentials?").

**Add to P4** (where Airflow + RDS + dlt all arrive): Airflow connections/secrets backend wired to **AWS SSM Parameter Store or Secrets Manager**; a stated rule "no secret ever enters git — pre-commit hook with `gitleaks`" from P0. Cost: ~2–3 h, fits inside the existing P4 budget.

### 3.2 Dimensional modeling is assumed, never demonstrated
The profile says data modeling is an existing strength, and DEA Domain 2 leans on it — but the portfolio never *shows* it: the spine's marts are named (`fct_trips`, `dim_zones`) without an explicit star-schema treatment, and SCD2 appears only once, inside a Databricks lab. DE interviews hit dimensional modeling hard and interviewers can't see "existing strength."

**Add to P1/P2 spine:** one documented **SCD2 dimension in the dbt project itself** (dbt snapshots on `dim_zones` or a synthetic driver dimension) and a short `MODELING.md` in the spine repo — grain statements per fact table, conformed-dimension note, one Kimball-vs-OBT paragraph. ~4 h, mostly writing you'd want for interviews anyway.

### 3.3 Pipeline testing (the software-engineering story) is named but not taught
P1 says the ingester is "typed, tested" and pytest sits in TOOLS.md, but no phase teaches *how to test pipelines* — unit vs. integration boundaries, fixtures, mocking AWS. Job specs increasingly filter on SWE fundamentals.

**Add to P2:** a half-day lab — pytest + **moto** (mock S3) for the ingester, one integration test that runs dbt against a DuckDB fixture in CI. This also makes the GitHub Actions workflow (already in P2) test-gated, which reads as production discipline.

### 3.4 Adopt a PR-based git workflow from Phase 1, not Phase 6
P6's flagship contract demo is "a breaking PR blocked by CI" — but nothing before P6 establishes working via PRs at all. A year of `main`-only commits also makes the repo history read as a tutorial, not an operated platform.

**Add to P1 as a standing rule:** every spine change = branch → PR → self-review checklist → squash-merge. Zero extra hours; by P6 the contract demo is a natural extension, and the commit history becomes hiring-manager evidence.

### 3.5 Regionalize part of the portfolio
Every dataset is US-centric (NYC taxi, Citi Bike, MovieLens, Hacker News) — proven but generic; hiring managers see taxi lakehouses weekly. For a Saudi/Gulf-first search, one regional artifact differentiates strongly.

**Swap one satellite's dataset** (S2 cost-mart or S6a serving layer) to a Gulf source — e.g., Saudi Open Data portal (data.gov.sa), Tadawul market data, or Umrah/Hajj seasonal datasets. Same skills, better interview conversation. Also add a **1-hour PDPL (Saudi Personal Data Protection Law) reading** to P6's vocabulary passes — governance-aware candidates are rare and it pairs with the Lake Formation work.

### 3.6 Small spec gap in Phase 5
The G5 demo says "event produced → visible in Athena within minutes," but P5 runs Kafka **locally** and never specifies how the local consumer writes to the AWS-side Iceberg table (credentials, catalog endpoint, network posture). Either (a) state the mechanism — local consumer with the `de-framework` profile writing via PyIceberg to the Glue/S3 Tables REST catalog — or (b) keep the P5 sink fully local and demo Athena-visibility only through the P4 Kinesis path. One paragraph fixes it; deciding it mid-phase costs an evening.

---

## 4. Process improvements

| # | Finding | Recommendation | Effort |
|---|---|---|---|
| 4.1 | **Retrieval checkpoints have no tooling** — the flagship innovation is implemented as "cover the column and quiz yourself" | GLOSSARY.md's format is machine-parseable: write a small script that generates an **Anki deck** (term → definition + contrast) tagged by phase. Doubles as a first Python artifact in P0 | ~3 h, P0 |
| 4.2 | **No re-entry protocol** after life interruptions — gates absorb slipping but nothing defines how to resume after 3 dark weeks | Add a "Resume ritual" box to PROGRESS.md: re-run last retrieval checkpoint → re-read current phase objectives → one 30-min warm-up task. Cheap insurance for the plan's most likely failure mode | 15 min |
| 4.3 | **P4's chargeable labs lack per-lab dollar estimates** — RDS+DMS left running can eat the $25 cap in days; only MWAA (~$10–15) and Glue (~$5–10) are costed | Add an estimated cost + hard teardown deadline to each P4 lab (e.g., "RDS+DMS: ≤$8, teardown ≤10 days after first CDC event"); add a **billing-alert threshold check mid-phase**, not only at the gate | 30 min |
| 4.4 | **Link rot is certain** — dozens of deep external links (course pages, exam-guide PDFs); per-phase "re-verify" notes are good but manual | Add a **lychee link-check GitHub Action** on this framework repo — dogfoods CI on the repo that preaches it, and catches dead course links before a phase starts | ~1 h |
| 4.5 | **Interview questions are listed but answers are never captured** | Add `INTERVIEW.md` to the spine repo: after each gate, write 3–5-sentence answers to that phase's questions, linking evidence. By P6 the interview-prep doc writes itself | ~1 h/phase |
| 4.6 | **Cert re-verification window is too tight** — CERTS.md says re-check guides "~2 weeks before booking," but the Databricks exam revises every 6–10 months and P3 lands ~Feb–Mar 2027, a plausible revision window; 2 weeks isn't enough to swap prep material | Change to **6 weeks before booking**, with a fallback note: if a new exam version drops mid-P3, sit the current version inside its retirement grace window rather than re-prepping | 5 min |
| 4.7 | **Publish checkpoints are broadcast-only** — posts create visibility but no relationships; referrals dominate Gulf hiring | Pair each phase post with **one interactive act**: comment substantively on 3 practitioners' posts, or answer one community question with your artifact. Feeds finding 2.2 | ~30 min/phase |

---

## 5. Minor / optional polish

- **PROGRESS.md**: add an ISO-week log line per week worked (`2026-W38: 7 h, P1 ingest`) — a year of honest hours is itself a rare, credible portfolio artifact and feeds the resume's numbers.
- **Demo videos**: standardize hosting (unlisted YouTube or Loom) and link format now, so P6 packaging isn't a scavenger hunt.
- **GLOSSARY.md** invites additions ("this file is yours to grow") — add a tiny CI check that every term carries a `[P#]` tag so the Anki generator (4.1) never breaks.
- **README map diagram**: the ASCII map is good; consider mirroring it as a Mermaid diagram so it renders on GitHub mobile, where ASCII tables wrap badly.
- **AI-rule consistency**: each phase states a hand-type rule (excellent); collect them into one table in README so the policy is visible at a glance to portfolio reviewers — "used AI deliberately, here's the per-phase rule" is a 2026 hiring conversation you want to start on your terms.
---

## 6. Prioritized action list

| Priority | Action | When | Cost |
|---|---|---|---|
| 🔴 1 | Remove `.claude/` artifact, add `.gitignore`, LICENSE, fix filename typos | Now, pre-Phase 0 | 30 min |
| 🔴 2 | Publish the 465-hour math + trim path + buffer weeks in README | Now | 1 h |
| 🔴 3 | Add the parallel career track (P3 onward) to README + PROGRESS gates | Now | 1–2 h |
| 🔴 4 | Add external-review requirement to gates G2+; move first mock to G3/G4 | Now | 30 min |
| 🟠 5 | Secrets-management block in P4 + gitleaks pre-commit rule in P0 | Before P0/P4 | 2–3 h |
| 🟠 6 | SCD2 + `MODELING.md` in the spine spec (P1/P2) | Before P1 | edit: 30 min |
| 🟠 7 | PR-workflow standing rule from P1 | Before P1 | 15 min |
| 🟠 8 | pytest + moto lab in P2 | Before P2 | edit: 30 min |
| 🟠 9 | Resolve the P5 local-Kafka → AWS sink spec gap | Before P5 | 30 min |
| 🟡 10 | Anki generator from GLOSSARY (P0 micro-project) | P0 | 3 h |
| 🟡 11 | Per-lab cost caps in P4; cert re-verify window → 6 weeks | Anytime | 45 min |
| 🟡 12 | Regional dataset swap for one satellite + PDPL reading in P6 | Before P2/P6 | 1 h |
| 🟡 13 | lychee link-check Action; `INTERVIEW.md`; re-entry ritual; ISO-week log | Anytime | ~3 h total |

**Bottom line:** the framework's architecture is sound — the biggest risks to the *outcome* are not technical but logistical: an optimistic hour budget, a career track that starts after the finish line, and a feedback loop that never leaves the author's head. Items 1–4 fix those; everything else sharpens an already strong plan.
