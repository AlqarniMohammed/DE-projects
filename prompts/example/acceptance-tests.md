# Acceptance Tests — Rakan Wholesale Coffee (black-box)

Derived from the Success Criteria plus the S1 block's fixed gate artifact (public project + live documentation site). No tool or architecture is named or assumed; every test is observable from outside.

| # | What must be proven | How to measure | Pass condition |
|---|---|---|---|
| 1 | Revenue is deterministic | Produce the March revenue figure twice, a day apart, from a fresh start | Identical to the riyal, both runs |
| 2 | Duplicate files change nothing | Load a chosen day's orders file, record all totals; load the same file again (renamed) | Every total identical after the second load |
| 3 | Correction re-sends are handled by a written rule | Feed an order that is later re-sent with a different quantity | The reported number matches the documented resolution of the "what counts as an order" question — and that rule is written down |
| 4 | The churn flag is complete and exact | Construct one café with weekly orders last quarter and none for 30 days; one with no such history | First café flagged, second not |
| 5 | The quarterly report is fast and repeatable | Produce the mall operator's Q2 volume report twice | Under one hour each, matching outputs |
| 6 | Every number is traceable | Pick any figure on the management view | Its source files and every step it passed through can be shown from the project's documentation, not from memory |
| 7 | History and growth hold | Load all three years, then simulate one further year of daily files | Nothing breaks; the daily views still meet the 9 a.m. expectation |
| 8 | **Operational failure:** a missing-then-double day | Skip one day's file, deliver two the next morning | The week's totals equal the totals of an uninterrupted week with the same orders |

Sign-off: a non-engineer (play the owner) walks tests 1, 4, and 5 and agrees the pass conditions were met.
