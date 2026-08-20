# Research Report — DE Learning Resources (verified current as of 2026-08-20)

**Audience fit criteria applied throughout:** AWS SAA-certified, strong SQL/data-modeling, 6-10 hrs/week, free/cheap preferred, short theory ramp then hands-on building. All currency claims verified against live sources on 2026-08-19/20.

---

## 1. DE Fundamentals & Big-Picture

| Pick | Resource | Format | Cost | Hours | Why it fits |
|---|---|---|---|---|---|
| Top | [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) (Reis/Housley, O'Reilly 2022) | Book | ~$35-45 (free via O'Reilly trial/library) | 20-25 | Still canonical — **no 2nd edition exists or is announced**. Tech-agnostic lifecycle theory = the short ramp; also the textbook basis for the Coursera cert below. |
| Top | [DeepLearning.AI Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/data-engineering) (Joe Reis + AWS) | Coursera, 4 courses, graded **AWS labs** | $49/mo (~$150-250 total); financial aid available | ~106 (3-5 mo at 6-10 hrs/wk) | Labs on Kinesis/S3/Glue/Lambda/Airflow/warehousing — converts SAA knowledge directly into DE reps. 4.7★. Content is a 2024 snapshot but still current. |
| Alt | [Deciphering Data Architectures](https://www.oreilly.com/library/view/deciphering-data-architectures/9781098150754/) (James Serra, Feb 2024) | Book, 242 pp | ~$40 | 10-12 | Concise warehouse vs lakehouse vs mesh vs fabric comparison. |

**Verified:** Joe Reis's [Jan 2025 retrospective](https://joereis.substack.com/p/fundamentals-of-data-engineering) confirms no FoDE revision — he's writing a data modeling book instead (*Mixed Model Arts*, unpublished as of Aug 2026; free chapters at [practicaldatamodeling.substack.com](https://practicaldatamodeling.substack.com)). Track [Data Engineering Design Patterns](https://www.amazon.com/Data-Engineering-Design-Patterns-Problems/dp/1098165810) (Konieczny, O'Reilly, May 2025) as a later project-hardening book.

## 2. DataTalksClub DE Zoomcamp

- Repo: [github.com/DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) · [2026 platform](https://courses.datatalks.club/de-zoomcamp-2026/)
- 2026 syllabus: 7 modules + 2 workshops + capstone: 1) Docker + **Terraform/GCP**, 2) Orchestration with **Kestra**, 3) **BigQuery**, 4) **dbt** (+ DuckDB), 5) **Bruin** (new 2026, DuckDB + AI/MCP), 6) **Spark**, 7) **Kafka**; workshops: **dlt** ingestion + AI-assisted ingestion. Still GCP-based.
- 2026 cohort ran Jan-May 2026 (finished). **Next cohort: January 2027, announced on the repo.** Cohort adds deadlines, leaderboard, peer-reviewed capstone, certificate; self-paced = anytime, no cert.
- Free. Official 5-15 hrs/wk × 9 weeks + 3-4 project weeks ≈ **80-130 hrs**.
- **Slotting:** the Jan 2027 cohort would fall in months 5-8 of a Sept 2026 start. Adds real community + accountability; duplicates fundamentals; **GCP mismatch** (concepts transfer; building the capstone on AWS instead is a differentiator move). Caveat: Kestra/Bruin/dlt are sponsor-influenced picks, rarer than Airflow/Glue in AWS-heavy postings.

## 3. SQL for DE

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [DataLemur SQL tutorial](https://datalemur.com/sql-tutorial) (jump to [window functions](https://datalemur.com/sql-tutorial/sql-aggregate-window-functions)) + free question bank | Free | 8-12 | Skip basics, drill windows/CTEs on FAANG-style questions. Doubles as interview prep. |
| Top | [Use The Index, Luke!](https://use-the-index-luke.com/) / [SQL Performance Explained](https://sql-performance-explained.com/) (Winand) | Free web; PDF €9.95 | 10-12 | The canonical indexing/execution-plan resource — the "why is it slow" layer. Still maintained (verified Aug 2026). |
| Alt | [8 Week SQL Challenge](https://8weeksqlchallenge.com/) (Danny Ma) | Free | 10-40 | Window-function-heavy realistic case studies; portfolio-friendly. |

Extras: [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/), [pgexercises.com](https://pgexercises.com/), [Mode SQL tutorial](https://mode.com/sql-tutorial), [windowfunctions.com](https://windowfunctions.com).

## 4. Python for DE + Modern Tooling + Polars/DuckDB

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [Python Essentials for Data Engineers](https://www.startdataengineering.com/post/python-for-de/) (Start Data Engineering) | Free | 8-12 | **Updated July 8, 2026.** DE-specific Python: API extraction, boto3, DuckDB/Spark transforms, quality checks, testing. |
| Top | Official-docs stack: [uv](https://docs.astral.sh/uv/) · [Polars guide](https://docs.pola.rs/) · [DuckDB docs](https://duckdb.org/docs/) · [typing.python.org](https://typing.python.org/) + [mypy](https://mypy.readthedocs.io/) | Free | 15-20 | All actively maintained (DuckDB v1.5.5 Jul 2026, [v2.0 preview Aug 17, 2026](https://duckdb.org/2026/08/17/duckdb-20-highlights)). Pair with [*DuckDB in Action* free PDF via MotherDuck](https://motherduck.com/duckdb-book-form/). |
| Alt | [calmcode.io](https://calmcode.io/course/polars/introduction) (pytest, Polars series) | Free | ~1/course | Bite-size. Paid upgrades: [*Python Polars: The Definitive Guide*](https://polarsguide.com/) (O'Reilly, Apr 2025); [*Python Testing with pytest* 2nd ed](https://pragprog.com/titles/bopytest2/python-testing-with-pytest-second-edition/). |

## 5. dbt

**Landscape (verified):** Fivetran-dbt merger completed June 1, 2026; Rust **Fusion engine relicensed Apache 2.0**, powers [dbt Core v2.0 (alpha)](https://docs.getdbt.com/blog/dbt-core-v2-is-here); **learn.getdbt.com survived**; free Developer plan still exists (1 seat, 3,000 model builds/mo); [Analytics Engineering cert updated May 20, 2026](https://www.getdbt.com/certifications/analytics-engineer-certification-exam) targeting Core v1.11.

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [dbt Fundamentals](https://learn.getdbt.com/courses/dbt-fundamentals) + new [VS Code variant](https://learn.getdbt.com/courses/dbt-fundamentals-vs-code) | Free | ~5 | Fastest official on-ramp; VS Code variant teaches the current Fusion-era workflow. |
| Top | [DE Zoomcamp Module 4](https://github.com/DataTalksClub/data-engineering-zoomcamp) (dbt + DuckDB/BigQuery) | Free | 8-10 | Real NYC-taxi project; strongest free build-something option. |
| Alt | [The Complete dbt Bootcamp: Zero to Hero](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/) (Toth/Petridisz) | $13-20 sale | 12-15 | 4.5★ (6.7k), realigned to the 2026 cert exam. (Kahan Data Solutions' paid playbook was pulled Dec 2025.) |

## 6. Apache Spark / PySpark (Spark 4.x era)

**Status:** Spark 4.1.x current; Databricks **Community Edition retired Jan 1, 2026** — replaced by serverless [**Databricks Free Edition**](https://www.databricks.com/learn/free-edition).

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [Databricks Academy: Data Engineering with Databricks path](https://www.databricks.com/training/catalog/data-engineering-with-databricks-911) + Free Edition | Free | 16-25 | Feeds the Databricks DE Associate cert. [Learning Festival cohorts](https://community.databricks.com/t5/learning-events/databricks-learning-festival-self-paced-global/ev-p/150223) offer 50% cert vouchers. |
| Top (book) | [Data Analysis with Python and PySpark](https://www.manning.com/books/data-analysis-with-python-and-pyspark) (Rioux, Manning) | ~$33 ebook | 30-40 | Best PySpark teaching book for a Python-first, SQL-strong learner. Spark-3 API — essentially unchanged in 4.x. |
| Alt | [PySpark - Apache Spark Programming for Beginners (2026)](https://www.udemy.com/course/apache-spark-programming-in-python-for-beginners/) (Pandey) | $15-20 sale | 14-18 | 4.6★/16k, runs in Databricks. |

**Book landscape verified:** no *Learning Spark* 3rd ed, no *Definitive Guide* 2nd ed. The one true Spark-4 book: [**High Performance Spark, 2nd ed**](https://www.oreilly.com/library/view/high-performance-spark/9781098145842/) (O'Reilly, **May 2026**) — buy later as the optimization follow-on. **Skip Rock the JVM** for this path (Scala-only, Spark-3 era).

## 7. Airflow + Dagster

**Status:** Airflow 3.3.1 current (Aug 12, 2026).

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [Astronomer Academy: Airflow 101 (Airflow 3)](https://academy.astronomer.io/path/airflow-101) + [DAG Authoring path](https://academy.astronomer.io/path/airflow-dag-authoring) | Free (optional [certs](https://www.astronomer.io/certification/) $150) | 12-15 | The definitive free, Airflow-3-native path (assets, DAG versioning). |
| Top | [Dagster University](https://courses.dagster.io/) — Essentials, Dagster & dbt, Testing, ETL, AI-Driven DE | Free | 12-16 | All refreshed 2025-2026 (ETL course covers Components; AI course Mar 2026). |
| Alt | Marc Lamberti Udemy: [Airflow 3 intro](https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/) (upd. Dec 2025) + [Advanced DAG Authoring](https://www.udemy.com/course/apache-airflow-3-advanced-dag-authoring/) (upd. Jan 2026) | $15-20 each | 10-15 each | Airflow-3-current, but Astronomer's free paths cover the same ground. |

**Order:** Airflow first (enterprise default, ~14% of postings vs ~9% Dagster/Prefect per [jobstrack.io](https://jobstrack.io/blog/roles/data-engineer)); Dagster Essentials after as a portfolio differentiator.

## 8. Kafka & Streaming (+ Flink intro)

**Status:** Kafka 4.2.0 (Feb 2026, KRaft-only); Flink 2.2.x.

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [Confluent Developer courses](https://developer.confluent.io/courses/): Kafka 101, Connect 101, Streams 101 + free [Data Streaming Engineer certificates](https://developer.confluent.io/certificates/) | Free, **certs $0** (cloud credit codes: KAFKA101 / CONFLUENTDEV1) | 8-12 | KRaft-era, recently refreshed, zero-cost credential. |
| Top (Flink) | [Confluent Apache Flink 101](https://developer.confluent.io/courses/apache-flink/intro/) | Free | 5-6 | Flink-SQL-focused — ideal for a SQL-strong learner. **Avoid [apache/flink-training](https://github.com/apache/flink-training)** — verified stale (Flink 1.17). |
| Alt | [Conduktor Kafkademy](https://www.conduktor.io/kafka) (free, no signup) or [Maarek's Kafka for Beginners](https://www.udemy.com/course/apache-kafka/) (updated for Kafka 4.0, Aug 2025) | Free / $15-20 | 6-10 | Kafkademy is the best free text reference. |

**Book:** [Kafka: The Definitive Guide, 2nd ed](https://www.amazon.com/Kafka-Definitive-Real-Time-Stream-Processing/dp/1492043087) (2021, still latest; free PDF via Confluent) — canonical for concepts; pair with KRaft-era content for ops.

## 9. Apache Iceberg & Lakehouse Table Formats

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [Apache Iceberg: The Definitive Guide — free via Dremio](https://www.dremio.com/guides/apache-iceberg-the-definitive-guide/) (O'Reilly 2024) | $0 | 15-20 | SQL-first framing of table-format internals. |
| Top | [Iceberg Spark quickstart](https://iceberg.apache.org/spark-quickstart/) (Docker: Spark + Jupyter + REST catalog + MinIO) + fuller labs ([iceberg-local-setup](https://github.com/ijaniszewski/iceberg-local-setup), [Polaris+Iceberg+MinIO+Spark](https://github.com/AlexMercedCoder/Apache-Polaris-Apache-Iceberg-Minio-Spark-Quickstart)) | Free | 7-14 | Verified current (Iceberg 1.11.0). Laptop-scale lakehouse, zero cloud spend. |
| Alt | [Dremio University free Iceberg courses](https://university.dremio.com/course/apache-iceberg); or [*Architecting an Apache Iceberg Lakehouse*](https://www.manning.com/books/architecting-an-apache-iceberg-lakehouse) (Merced, Manning, **Apr 2026**, ~$29) | Free / ~$29 | 2-6 / 20-25 | The Manning book builds a Postgres → Iceberg → Superset mini-lakehouse. Optional: free [*Apache Polaris: The Definitive Guide*](https://www.dremio.com/guides/oreilly-definitive-guide-to-apache-polaris/) (Sept 2025). |

**Verdict:** prioritize **Iceberg** (AWS S3 Tables, Databricks Iceberg v3 preview, Snowflake/Polaris, BigQuery managed Iceberg). Delta as vocabulary (deep-dive happens in the Databricks phase anyway); skim Hudi.

## 10. AWS Data Services Hands-On (beyond cert courses)

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | AWS Workshop Studio: [Glue Immersion Day](https://catalog.workshops.aws/glue-immersion-day/en-US), [Serverless Data Lake Immersion Day](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/ea7ddf16-5e0a-4ec7-b54e-5cadf3028b78/en-US/introduction), [DE Immersion Day labs](https://github.com/aws-samples/data-engineering-for-aws-immersion-day) + [SageMaker Lakehouse / S3 Tables walkthrough](https://builder.aws.com/content/2voduyQmGbAaMbTC0O5pieY5CkK/getting-started-with-amazon-sagemaker-lakehouse) | Content free; ~$5-15/workshop AWS spend | 12-18 | SAA holder already knows IAM/S3/VPC — these become pure data-service reps. S3 Tables/Lakehouse is where AWS analytics converged at [re:Invent 2025](https://aws.amazon.com/blogs/big-data/aws-analytics-at-reinvent-2025-unifying-data-ai-and-governance-at-scale/). |
| Top | [AWS Skill Builder](https://skillbuilder.aws/subscriptions): free Data Engineer Learning Plan + [free DEA-C01 exam prep plan](https://skillbuilder.aws/learning-plan/QYZWVSMX4B/exam-prep-plan-aws-certified-data-engineer--associate-deac01--english/YTMBK7R698) | Free tier; $29/mo for Builder Labs + practice exams | 15-25 | 1-2 months of the $29 sub for labs is the only spend worth making. |
| Alt | [Johnny Chivers YouTube](https://www.youtube.com/johnnychivers) — "2026 Edition" AWS DE series + [free course repo](https://github.com/johnny-chivers/aws-data-engineering) + [DEA-C01 full course](https://www.youtube.com/watch?v=6G0bLDIcO7Y) | Free | 5-10 | Verified active Feb 2026. **Skip the [Open Guide to AWS](https://github.com/open-guides/og-aws)** — last commit Aug 2022. |

## 11. Terraform / IaC for Data Infra

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [HashiCorp Terraform AWS get-started track](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) | Free | 4-6 | Shortest credible ramp; then terraform your own Glue/Athena/S3 labs — better than any course. |
| Top | [freeCodeCamp: Terraform + AWS Dev Environment](https://www.freecodecamp.org/news/learn-terraform-and-aws-by-building-a-dev-environment/) + [DE Zoomcamp module 01-docker-terraform](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform) | Free | 4-6 | Zoomcamp module targets GCP — do it for the workflow, swap in the AWS provider yourself. |
| Alt | [More than Certified in Terraform 2025](https://www.morethancertified.com/course/mtc-terraform) (Terraform 1.10+) | $15-25 sale | 12-15 | Only if you end up owning IaC at work. *Terraform: Up & Running* still 3rd ed (2022). |

**Terraform vs OpenTofu (2026):** learn **Terraform HCL** — skills transfer 1:1 to OpenTofu; know OpenTofu exists for interviews ([comparison](https://encore.dev/articles/opentofu-vs-terraform-2026)).

## 12. Data Quality / Observability / Lineage

**Critical currency finding:** Great Expectations was **acquired by FICO (May 6, 2026)**; **GX Cloud shut down publicly June 1, 2026**; GX Core OSS moved to Fivetran stewardship ([announcement](https://greatexpectations.io/blog/an-update-from-great-expectations/); repo redirects to `fivetran/great_expectations`). Know the vocabulary; **don't build the plan on GX**.

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [dbt tests](https://docs.getdbt.com/docs/build/data-tests) + [dbt-expectations (metaplane fork)](https://hub.getdbt.com/metaplane/dbt_expectations/latest/) | Free | 4-6 | The most interview-relevant DQ skill for a SQL-strong learner. Use the **metaplane** namespace — the original Calogica package is unmaintained since Dec 2024. |
| Top | [Elementary OSS](https://docs.elementary-data.com/oss/quickstart/quickstart-cli-package) ([repo](https://github.com/elementary-data/elementary), v0.25.1 Jul 2026) | Free | 3-5 | One evening turns dbt tests into an observability report + Slack alerts + anomaly detection. |
| Alt | [Soda Core v4](https://github.com/sodadata/soda-core) (awareness — pivoted to **data contracts**, v4, Jan 2026) + [Astronomer OpenLineage/Marquez tutorial](https://www.astronomer.io/docs/learn/marquez) + [openlineage.io](https://openlineage.io/getting-started/) | Free | 2-4 | OpenLineage is the industry lineage spec; run the 1-hr Marquez demo. |

Concepts: skim [*Data Quality Fundamentals*](https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/) (O'Reilly 2022) ch. 1-4. **Total compact path: ~12-16 hrs, ~$0.**

## 13. DE Interview Prep

| Pick | Resource | Cost | Hours | Why |
|---|---|---|---|---|
| Top | [DataExpert-io/data-engineer-handbook](https://github.com/DataExpert-io/data-engineer-handbook) (43.8k stars, active Aug 2026) + Zach Wilson's [free community bootcamp](https://learn.dataexpert.io/program/free-community-boot-camp) / [YouTube lectures](https://www.youtube.com/watch?v=T4uyvQDtoxE) | Free | 15-30 | Best single free DE resource index; covers modeling, Spark, Flink/Kafka, quality — portfolio + interview vocabulary. |
| Top | [DDIA 2nd edition](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) (Kleppmann & Riccomini) — **published March 2026** ([author's site](https://martin.kleppmann.com/)) | ~$45-60 | 15-25 targeted | The canonical data system-design interview text. Buy the 2E, not the 2017 edition. |
| Top (SQL grind) | [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/) + [DataLemur free tier](https://datalemur.com/questions) | Free | 10-15 | FAANG-realistic; polish only, given existing SQL strength. |
| Alt | [Exponent free 2026 DE guides](https://www.tryexponent.com/blog/data-engineering-interview) + [question bank](https://www.tryexponent.com/questions?role=data-engineer) + [peer mocks](https://www.tryexponent.com/practice) (**5 free mock credits/month**) | Free tier | 6-8 | Best free live-mock option in 2026. |

**Verified:** no "Ace the Data Engineering Interview" book exists. [*Data Engineering Design Patterns*](https://www.oreilly.com/library/view/data-engineering-design/9781098165826/) (Konieczny 2025) works as an interview-pattern refresher.

---

## Backbone Candidates Ranked

1. **DeepLearning.AI Data Engineering Professional Certificate** — best-fit backbone #1 on paper: AWS labs, Joe Reis, compounds with SAA. ~106 hrs, ~$150-250. Weaknesses: 2024 tool snapshot, no dbt, shallow Kafka, and it would displace hands-on spine-building time.
2. **DataTalksClub DE Zoomcamp, Jan 2027 cohort** — free, community + peer-reviewed capstone; GCP-based (mitigate by building the capstone on AWS); sponsor-influenced tool picks.
3. **DataExpert.io free bootcamp + handbook** — strong third pillar for the final third of the year: advanced modeling, Spark, streaming, interview prep.
4. **Databricks Academy + Free Edition** — best free Spark/lakehouse backbone but vendor-shaped; slot as the Spark block.
5. **FoDE + DDIA 2E as the book spine** — FoDE in month 1 (theory ramp), DDIA 2E in months 9-12 (interview-grade depth).

**Recommended composite (lean):** FoDE + targeted per-phase free courses (dbt Fundamentals, Databricks Academy, Astronomer Academy, Confluent) around the owned Maarek/Kane DEA course → optional Zoomcamp Jan 2027 cohort as an accountability layer → DataExpert/DDIA interview layer in months 9-12. Total cash outlay run lean: roughly **$250-450 including both exam fees** — everything else has a free path.
