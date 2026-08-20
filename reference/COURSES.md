# Video Courses — the Optional Lane

Some people learn best from documentation and practice; others from a well-taught video course. Where a phase's Learn row has a **vetted video twin**, the phase carries a second table — the **video lane** — offering the swap: same "Pinned by" exercise, hours swap rather than add. This file is the catalog behind those tables, the learner-facing summary of the research in [`sources/research/courses.md`](../sources/research/courses.md) (verified 2026-08-20). Prices and editions churn: **re-verify before buying, and never pay Udemy list price** — every Udemy course here reaches ~$15–25 in the sales that run most weeks.

Jump: [How the lanes work](#how-the-lanes-work) · [Catalog by phase](#catalog-by-phase) · [The Coursera program](#the-coursera-program) · [Honest gaps](#no-video-twin--the-honest-gaps) · [Not researched](#not-researched)

## How the lanes work

1. Open the phase's Learn section. If a row has a video twin, it appears in the phase's **video lane** table, naming the row it swaps.
2. **Pick one lane per row, before you start the row.** Video or default — either is fine; neither is "the right way."
3. Do the chosen resource **and the row's "Pinned by" exercise.** The exercise is identical in both lanes and is never optional — nothing is learn-only.
4. The lane you didn't pick is your **fallback**: open it only when you're stuck on that row. Never work both lanes of the same row — hours swap, they never add ([why](WHY.md#why-one-platform-not-30-projects--the-design-decisions)).
5. Bought a course? Log it in [PROGRESS.md](../PROGRESS.md)'s spend log.

## Catalog by phase

### Phase 0 — Orientation

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [DeepLearning.AI Data Engineering Professional Certificate — **Course 1 only**](https://www.coursera.org/professional-certificates/data-engineering) (Joe Reis + AWS) | Coursera · $49/mo | 6–8 | *Fundamentals of Data Engineering* ch. 1–3 | Same author as the book, as lectures with graded AWS labs. Read [the program section](#the-coursera-program) before subscribing. |

### Phase 1 — Foundations

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [Dremio University: Apache Iceberg courses](https://university.dremio.com/course/apache-iceberg) | Dremio University · free | 3–4 | *Apache Iceberg: The Definitive Guide* ch. 1–4 | Same architecture/metadata ground in course form; the book stays free to consult. |
| [calmcode.io Polars series](https://calmcode.io/course/polars/introduction) | calmcode · free | 1–2 | The **Polars half** of the DuckDB/Polars row | Bite-size screencasts; the DuckDB friendly-SQL + Parquet pages stay in both lanes. |
| [The Complete dbt Bootcamp: Zero to Hero](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/) | Udemy · ~$13–20 | 12–15 | **No swap** — a depth option | The default [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) row is already video (and free). This adds ~8–11 h of depth realigned to the 2026 cert exam — take it only if you want dbt beyond the phase's need. |

### Phase 2 — AWS Lakehouse Core

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [Johnny Chivers: free DEA-C01 full course](https://www.youtube.com/watch?v=6G0bLDIcO7Y) + ["2026 Edition" AWS DE series](https://www.youtube.com/johnnychivers) + [labs repo](https://github.com/johnny-chivers/aws-data-engineering) | YouTube · free | 10–15 | **Both Maarek/Kane tranches** | The $0 prep track. Honest trade: thinner on Redshift/security/ops — backstop those domains with the free [Skill Builder DEA-C01 exam-prep plan](https://skillbuilder.aws/learning-plan/QYZWVSMX4B/exam-prep-plan-aws-certified-data-engineer--associate-deac01--english/YTMBK7R698) ([CERTS.md](CERTS.md) prep item 4). Tutorials Dojo stays mandatory in both lanes. |

### Phase 3 — Spark & Databricks

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [Derar Alhussein: Databricks DE Associate prep course](https://www.udemy.com/course/databricks-certified-data-engineer-associate/) + [practice exams](https://www.udemy.com/course/practice-exams-databricks-certified-data-engineer-associate/) | Udemy · ~$30–40 both, on sale | 15–20 | *Databricks Academy path* | V4, May-2026 syllabus. Keep the Academy course list as your syllabus checklist — the exam guide names those courses. His practice exams are already assumed by gate G3. Skip his O'Reilly *Study Guide* book (targets the pre-2025 exam). |
| [PySpark: Apache Spark Programming for Beginners](https://www.udemy.com/course/apache-spark-programming-in-python-for-beginners/) (Pandey) | Udemy · ~$15–20 | as-needed (14–18 watched through) | *Rioux book* (reference row) | Course-as-reference instead of book-as-reference; runs in Databricks. Watch sections as the labs demand them, not front-to-back. |

### Phase 4 — Orchestration & Ingestion

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| Marc Lamberti: [Airflow 3 intro](https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/) + [Advanced DAG Authoring](https://www.udemy.com/course/apache-airflow-3-advanced-dag-authoring/) | Udemy · ~$15–20 each | 20–30 | *Astronomer Academy* row | Airflow-3-current. Honest note: the free default covers the same ground and is shorter — choose on format, not content. |

### Phase 5 — Streaming & CDC

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [Maarek: Apache Kafka for Beginners](https://www.udemy.com/course/apache-kafka/) | Udemy · ~$15–20 | 6–8 | The **Kafka 101 half** of the Confluent row | Updated for Kafka 4.0. Do Connect 101 and sit the free Data Streaming Engineer Foundations certificate either way — the pin doesn't move. |

### Phase 6 — Production, Serving & Capstone

| Course | Platform · price | Hours | Swaps (phase row) | Notes |
|---|---|---|---|---|
| [freeCodeCamp: Terraform + AWS dev environment](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) | freeCodeCamp · free | 4–6 | *Terraform AWS get-started* row | Build-along video instead of the HashiCorp text track; then Terraform the platform's own resources either way. |
| [More than Certified in Terraform](https://www.morethancertified.com/course/mtc-terraform) | morethancertified.com · ~$15–25 | 12–15 | **No swap** — a depth option | Only if you end up owning IaC beyond this framework's scope. |
| [Zach Wilson / DataExpert free lectures](https://www.youtube.com/watch?v=T4uyvQDtoxE) + [free community bootcamp](https://learn.dataexpert.io/program/free-community-boot-camp) | YouTube / dataexpert.io · free | 15–30 | **No swap** — a beside-the-path layer | Advanced modeling, Spark, and streaming depth for months 9–12, self-paced alongside P5–P6. Not a row swap: nothing in the default path depends on it. |

## The Coursera program

The [DeepLearning.AI Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/data-engineering) (Joe Reis + AWS) is the strongest guided-video coverage of this framework's P0–P2 territory: four courses, graded AWS labs (Kinesis, S3, Glue, Lambda, Airflow, warehousing), ~106 h total, $49/month (financial aid available; one focused month ≈ $49, the full program ~$150–250).

How it maps here:

- **Course 1** (introduction + lifecycle) — the one clean swap: replaces Phase 0's *Fundamentals of Data Engineering* ch. 1–3 row.
- **Courses 2–3** (source systems, ingestion, storage, pipelines) — overlap Phase 2's cert-prep rows, which are already video. Pick **one** DEA-C01 prep track (Maarek/Kane, Chivers, or these) — never two.
- **Course 4** (analytics, serving, modeling) — optional background for Phase 1's modeling cluster; no default row swaps out for it.

Two cautions, both load-bearing:

- **It is not a milestone.** The framework's credential milestones stay the two exams — the program remains skipped *as a credential* ([CERTS.md](CERTS.md#evaluated-and-skipped-for-the-record)); the Coursera certificate PDF is a by-product, not a gate item.
- **Never run the whole ~106 h program in parallel** with the phases — that recreates the overload the framework exists to prevent, the same ruling as the [Zoomcamp evaluation](SOURCES.md#optional-add-on-evaluated-but-not-scheduled). Swap named rows only.

## No video twin — the honest gaps

Rows not named above have no vetted video twin; work them in the default lane. Notably:

- **P0:** the lifecycle primer, the wiki skim, the glossary active-read — the framework's own material, twin-less by design.
- **P1:** *Python Essentials for Data Engineers*; and **SQL drilling has no video lane by design** — pre-P1 SQL video courses were evaluated and declined ([CERTS.md](CERTS.md#evaluated-and-skipped-for-the-record)); DataLemur/LeetCode are the practice surface.
- **P2:** the PySpark-basics quickstart, Glue Immersion Day (it *is* an exercise), and the S3 Tables, dbt-athena, Polaris, and rebrand reading rows.
- **P3:** the Spark performance-tuning docs read.
- **P4:** dlt, the connector-positioning skim, Glue-vs-EMR, MWAA, and the secrets-backend read.
- **P5:** the Debezium docs and the diskless-streaming reading (Kafka 101, Connect 101, and Flink 101 are already free video).
- **P6:** the quality-stack docs, OpenLineage/Marquez, DDIA, the vocabulary passes, and the PDPL primer.

A gap is not an endorsement of text over video — it means the research found no current, high-quality course worth your hours there.

## Not researched

**DataCamp, Udacity, and Coursera beyond the DeepLearning.AI program were never researched** — absence from this file is not a verdict. The research scope is [`sources/research/courses.md`](../sources/research/courses.md); to propose an addition, open an issue that engages that evidence ([CONTRIBUTING.md](../CONTRIBUTING.md)).

---
[README](../README.md) · [Guide](../GUIDE.md) · [Certifications](CERTS.md) · [Sources](SOURCES.md)
