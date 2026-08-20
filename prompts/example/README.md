# Worked Example — What Generated Requirements Look Like

A complete example of the generator's first two outputs, for satellite **S1** (first standalone dbt project), so you can calibrate your own generated briefs against a known-good shape:

- [`requirements.md`](requirements.md) — the stakeholder brief. Notice: no tool names anywhere, the data warts are phrased as complaints, and three points are deliberately underspecified.
- [`acceptance-tests.md`](acceptance-tests.md) — the black-box validation plan. Notice: measurable pass/fail conditions, one operational-failure scenario, still zero tool names.

**The third output (`.reference-solution.md`) is deliberately not shown.** Its whole value is that you build first and compare after — publishing an example would teach you to peek. Your own generated one stays sealed until your build passes the acceptance tests.
