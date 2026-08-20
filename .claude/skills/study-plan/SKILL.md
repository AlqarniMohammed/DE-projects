---
name: study-plan
description: Build an honest, personalized pacing forecast from a target duration in months and weekly hours, written into PROGRESS.md. Use when the learner wants to fit the framework into a specific number of months, asks "how long will this take me", or their pace changes mid-year.
---

# Study Plan

Turn "I want to finish in N months" into an honest phase-by-phase forecast, written into `PROGRESS.md`. The plan is a **pacing forecast, never a promise and never a gate** — the standing rule holds: gates decide advancement, not the calendar.

## Inputs

- **Target months** — from the invocation args; otherwise ask.
- **Weekly hours** — ask for **one number** (the 12-month arc assumes ~10 focused h/week). If the learner gives a range, compute with its bottom — the honest floor — and mention the top's faster finish as the stretch case.
- **Current position** — the first phase whose `**Gate G<n> passed on:**` line in `PROGRESS.md` is blank. If the header records an **Entry phase** (placement), phases before it count as passed. If the tracker looks blank but the learner says they placed or already did work, ask before inferring — never assume Phase 0 over their objection.

## Compute

1. **Read the budgets live.** Each phase README's header line carries its hour budget (`phases/phase-*/README.md`, "**Budget:** ~NN hours"). Never hardcode the numbers — the phase files are the source of truth.
2. **Remaining hours** = the sum of budgets from the current phase onward. For a phase already started, ask the learner roughly what fraction of its budget they've spent (the Weekly hours log in `PROGRESS.md` is the evidence) and subtract that; a placement entry phase counts full.
3. **Available weeks** = months × 4.33 − buffer, where **buffer = 2 × (months ÷ 6), rounded up to a whole week** (slack is scheduled, not stolen — `reference/WHY.md`). Never compute "available hours"; all comparisons are in h/week.
4. **Required pace** = remaining hours ÷ available weeks, **rounded up to the nearest 0.5 h/week**.
5. **Feasibility verdict.** Two comparisons, in order — and if the first fails, stop:
   - **Required vs stated:** if the required pace exceeds the learner's stated hours, the months and the hours disagree — **draw no table.** Show both honest fixes (the duration their stated hours actually support, and the hours their stated duration actually demands), write the verdict-only block (see Output), and re-run when they pick one.
   - **Required vs sustainable:** **≤ ~10 h/wk** — realistic, say so plainly. **~10–15 h/wk** — possible but sustained-sprint territory; warn honestly and point at the **pre-authorized trim path** in `reference/WHY.md` (nothing outside that path is ever trimmed; the platform and both certs never are). **> ~15 h/wk** — draw it only if the learner confirms this is their full-time focus (≥ 25 disposable h/week, e.g. between jobs); alongside a job, refuse: an unrealistic plan costs months, a refused one costs a minute.
6. **Map phases onto the available weeks** (the buffer stays outside the phase windows — show it as an explicit "scheduled slack" line, not hidden inside phases), proportionally to their budgets. Anchor windows on `PROGRESS.md`'s **Started:** date as real month names when it's filled; otherwise use month indices (M1, M2, …). Omit placement-credited phases from the table. A gate's forecast month is the end of its phase's window; certifications stay pinned to **gates** — AWS DEA-C01 at G2, Databricks at G3 — never to fixed exam dates.

## Output — write it, don't just say it

Replace the contents under `PROGRESS.md`'s `## My study plan (generated)` heading (it ships as an empty placeholder near the top of the tracker), dated, containing:

- The stated pace and duration, and the feasibility verdict in one sentence.
- If the verdict was "months and hours disagree": the two honest fixes and **no table** — regenerate after the learner picks.
- Otherwise: a table — phase · hour budget · forecast calendar window · gate (⭐ on the two cert gates) — plus one "scheduled slack" line naming the buffer weeks.
- Update the header's **Target pace:** field to the planned number.
- Both standing caveats, verbatim:
  - *Gates decide advancement — this schedule is a forecast.*
  - *If time runs short: the pre-authorized trim path only ([WHY.md](reference/WHY.md)).*

Regenerate freely — replace the block whenever the pace changes or a gate slips, recomputing from the current `PROGRESS.md` position.

## Rules

- Never soften the feasibility verdict to please the learner.
- Never move a certification off its gate.
- Never propose trimming anything outside the pre-authorized path; any trim taken is recorded in `PROGRESS.md` the way that path requires.
- No Claude Code? The manual recipe lives in `GUIDE.md` § "Pacing the year to your life".
