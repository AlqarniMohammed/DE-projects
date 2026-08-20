# Requirements — Rakan Wholesale Coffee (fictional)

*Generator's selection note: S1 block · MovieLens excluded (used in a previous pass) · Hacker News dump excluded (tech-forum shape reused too often) → data.gov.sa commercial-registrations menu option, wrapped in a wholesale-trade scenario. Difficulty calibrated to Phase 1: clean scope, one messy dimension.*

## 1. Company & Context

Rakan Wholesale Coffee is a 40-person coffee importer and roaster in Jeddah supplying ~600 cafés across the western region. The "data team" is one operations analyst, Huda, who inherited a shared spreadsheet named `FINAL_orders_v7_REAL.xlsx`. Orders arrive from three channels: a small web portal, WhatsApp messages the sales reps re-type, and a legacy phone-order form. Finance exports a monthly CSV from the accounting system and emails it around. Management meetings regularly stall on "whose number is right."

## 2. The Problem

- The Monday management meeting uses sales figures that are 8–12 days old by the time anyone sees them.
- Two departments report different monthly revenue for the same month, and nobody can explain the gap.
- The owner wants to know which cafés are growing and which are about to churn — today that's Huda's gut feeling.
- A large mall operator (their biggest prospect) asks for quarterly volume reports as a condition of listing; producing one takes Huda most of a week.

## 3. The Data

Three files land in a shared folder, at different rhythms:

- **Orders** (daily-ish): one row per order line — café, product, quantity, unit price, order date, channel. Some days the file doesn't show up; then two show up the next day, **and sometimes the same day's file shows up twice with a different name**. Reps sometimes re-send corrected orders — the same order number appears again with different quantities.
- **Cafés** (whenever someone remembers): the customer list — name, district, size category, onboarding date. **Names are typed differently across files** ("Cafe Lavender", "Lavender Café"), and when a café changes owners it just gets a new row with the same name.
- **Products** (rarely changes): the catalogue — product code, name, roast type, pack size. Last year the pack sizes were relabeled, so old files use old codes for about 30 products.

Roughly 1,500 order lines a day, growing ~20% a year. History exists back three years.

## 4. Functional Requirements

- One place where anyone in management can see: daily/weekly/monthly revenue, by channel, by district, by product family — without asking Huda.
- A per-café view: their ordering history, trend, and a flag when a previously regular café has gone quiet.
- The mall operator's quarterly volume report producible in under an hour.

## 5. Non-Functional Requirements

- "Yesterday's numbers by 9 a.m." is the freshness expectation for the daily views.
- Three years of history loaded; three more years of growth must not break anything.
- Consumers: 5 managers (read-only, weekly), Huda (daily), the owner (monthly, from a phone screen).

## 6. Constraints

- The company is cost-averse: no new spend beyond "an intern's laptop" — whatever is built must cost effectively nothing to run.
- Customer data stays in-Kingdom and is handled under Saudi PDPL expectations — no café's information leaves the company's control.
- The mall operator's listing decision is in four months; the quarterly report must be reliable before then.

## 7. Success Criteria

1. For any chosen month, the revenue number is **identical** no matter who produces it or when — and re-loading a day's file never changes it.
2. A duplicate or re-sent orders file changes **nothing** in the reported totals.
3. The churn-risk flag identifies every café with no orders for 28+ days that ordered weekly in the prior quarter.
4. The quarterly volume report is produced from the system in under an hour, twice in a row.
5. Huda can explain where any number came from, down to the source file, in one sitting.

*Deliberately left open (surface and resolve these in writing before building): what exactly counts as "an order" when a correction re-send arrives — latest wins, or both kept? At what level is revenue "the" revenue — order line, order, or delivered order? And which of the two café rows is "the café" after an ownership change?*
