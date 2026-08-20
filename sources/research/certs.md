# Research Report — Certification Blueprints & Prep
*Researched 2026-08-20. All blueprint claims verified against the official exam guide PDFs (read directly, not from summaries).*

---

## 1. AWS Certified Data Engineer – Associate (DEA-C01)

**Status check (Aug 2026):** The exam is **live and current**. The official certification page shows open registration with no retirement banner, no DEA-C02, and no announced version change; the exam guide AWS serves is still **Version 1.0**. Context: DEA-C01 launched March 2024 as the *replacement* for the retired Data Analytics – Specialty, so it is the newest associate cert, not a retirement candidate. Re-check the cert page ~2 weeks before booking as routine hygiene.

### (a) Blueprint — official domains ([DEA-C01 Exam Guide, Version 1.0, PDF](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf))

| Domain | Weight | What it actually tests |
|---|---|---|
| 1. Data Ingestion and Transformation | **34%** | Streaming ingestion (Kinesis Data Streams/Firehose, MSK, DynamoDB Streams, DMS) vs batch (S3, Glue, EMR, AppFlow, Lambda); event triggers & schedulers (EventBridge, S3 Event Notifications); Spark-based transformation and format conversion (CSV→Parquet) with Glue/EMR/Lambda/Redshift; orchestration (Step Functions, MWAA/Airflow, Glue workflows, SNS/SQS alerts); programming concepts — SQL transforms/optimization, Git, CI/CD, IaC (CloudFormation/CDK/SAM), Lambda concurrency tuning |
| 2. Data Store Management | **26%** | Choosing stores (Redshift vs RDS vs DynamoDB vs S3 vs Kinesis/MSK); Redshift Spectrum, federated queries, materialized views; Glue Data Catalog + crawlers, Hive metastore, partition sync; S3 Lifecycle/versioning, DynamoDB TTL, hot/cold tiering; **data modeling & schema evolution** (Redshift/DynamoDB/Lake Formation schema design, SCT/DMS schema conversion, indexing/partitioning/compression) — the SQL/modeling strength lands here |
| 3. Data Operations and Support | **22%** | Automating pipelines (MWAA, Step Functions, Lambda, EventBridge); analyzing data with Athena (queries, views, Spark notebooks), Glue DataBrew, QuickSight; monitoring/troubleshooting with CloudWatch (Logs Insights), CloudTrail, OpenSearch; data quality rules, profiling, validation (Glue Data Quality/DataBrew) |
| 4. Data Security and Governance | **18%** | IAM roles/policies, VPC security groups, Secrets Manager/Parameter Store; Lake Formation permissions across Redshift/EMR/Athena/S3; KMS encryption (client vs server side, cross-account), masking/anonymization; CloudTrail (Lake), Macie for PII, Redshift data sharing, AWS Config |

Out of scope: AI/ML tasks, language-specific syntax, business analysis. In-scope service list is in the guide's appendix (Athena, EMR, Glue, Redshift, Kinesis, MSK, Flink, DynamoDB, Lake Formation, MWAA, Step Functions, etc.).

### (b) Logistics ([official cert page](https://aws.amazon.com/certification/certified-data-engineer-associate/) + exam guide)
- **65 questions** (50 scored + 15 unscored), multiple choice / multiple response
- **130 minutes**; scaled score 100–1,000, **pass = 720**, compensatory scoring (no per-domain minimum)
- **$150 USD**; Pearson VUE test center or online proctored; valid 3 years

### (c) Ranked prep resources
1. **Stephane Maarek & Frank Kane — "AWS Certified Data Engineer Associate 2026 – Hands On!" (Udemy)** — *already owned; still the consensus #1 video course.* ~24h video, actively maintained (2026 edition). [udemy.com/course/aws-data-engineer](https://www.udemy.com/course/aws-data-engineer/) (~$15–20 on sale)
2. **Tutorials Dojo (Jon Bonso) DEA-C01 Practice Exams** — **$14.99**; 4 timed sets + 4 review-mode sets + section-based tests + flashcards, updated continuously; 2025 passers report ~60% overlap in style/coverage with the real exam. [portal.tutorialsdojo.com](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) — treat as mandatory
3. **AWS Skill Builder 4-step Exam Prep plan** — free tier includes the official 20-question practice set and exam-prep course; paid tier (~$29/mo) adds the Official Practice Exam and **Builder Labs**. Linked from the [official cert page](https://aws.amazon.com/certification/certified-data-engineer-associate/)
4. **Hands-on labs in your own account** — cheapest realistic lab: Glue crawler + Athena + S3 lifecycle + a Step Functions/EventBridge pipeline on free-tier-ish scale; Redshift Serverless has a free trial credit. Prioritize Glue/Athena/Redshift/Kinesis — the exam is heavy on "which service/feature" discrimination.

### (d) Study-hour estimate: **~50–70 hours** (7–10 weeks at 6–10 h/wk)
Prep guides for average candidates cite 6–10 weeks at 1–2 h/day (~60–100+ h; [ExamCert 2026 guide](https://www.examcert.app/blog/aws-dea-c01-complete-guide/)). Discounts apply: SAA-C03 already covers most of Domain 4 and the IAM/VPC/S3/KMS substrate (~25% of the exam); strong SQL/modeling covers Redshift/Athena modeling questions. Budget: ~24h course video (skim SAA-overlap at 1.5×) + ~15h Tutorials Dojo + ~10–20h targeted labs. Still regarded as the hardest associate — don't go below ~50h.

### (e) Recommended timing in the 12-month program
Sit DEA-C01 at **end of month 8 or in month 9** — immediately after the AWS-native services block, so Glue/Kinesis/Redshift labs are fresh. Start Tutorials Dojo sets in the final 3 weeks. Sequencing after Databricks spaces the two exam fees ~2–3 months apart and leaves months 10–12 as retake buffer.

---

## 2. Databricks Certified Data Engineer Associate

**Version check — important:** The mid-2025 overhaul is confirmed, and it has **already been superseded again**. Timeline, all from official guides: pre-July-2025 exam (old Lakehouse/DLT/Repos era) → **July 25, 2025 major rewrite** ([July 2025 exam guide PDF](https://www.databricks.com/sites/default/files/2025-11/databricks-certified-data-engineer-associate-exam-guide-july-25-2025-04.pdf)) → a Nov 2025 syllabus adjustment → **current version effective May 4, 2026** ([May 2026 exam guide PDF](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf)). The guide tells candidates to re-check it two weeks before the exam — this exam now revises roughly every 6–10 months.

**What changed vs the old exam:** the old (pre-2025) exam was SQL-first, Hive-metastore/DBFS-era, with "Delta Live Tables," "Repos," and "Workflows" terminology. The current exam is **PySpark-first**, assumes **Unity Catalog governs everything**, uses **Lakeflow branding throughout** (Lakeflow Connect for ingestion, Lakeflow Jobs for orchestration, Lakeflow Spark Declarative Pipelines as DLT's successor), adds a dedicated **CI/CD section** (Databricks Asset Bundles — being renamed "Declarative Automation Bundles" — Git Folders, Databricks CLI), and tests **serverless compute, Liquid Clustering, predictive optimization, and Unity Catalog ABAC**. If prep material still centers on DLT syntax, hive_metastore, or SQL-only ELT, it's for the retired exam.

### (a) Blueprint — official sections ([May 4, 2026 exam guide PDF](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf), cross-checked with the [exam webpage](https://www.databricks.com/learn/certification/data-engineer-associate))

| Section | Weight | What it actually tests |
|---|---|---|
| 1. Databricks Intelligence Platform | **6%** | Platform architecture, Delta Lake, Unity Catalog basics; choosing compute (serverless vs clusters) by characteristics, limits, cost model |
| 2. Data Ingestion and Loading | **21%** | Batch/streaming/incremental patterns; **COPY INTO** from S3/ADLS/GCS; **Auto Loader** (schema enforcement/evolution, directory listing vs file notification); **Lakeflow Connect** connectors; JDBC/ODBC/REST ingestion; semi/unstructured (JSON, nested) into UC-governed Delta tables |
| 3. Data Transformation and Modeling | **22%** | Medallion bronze→silver→gold cleaning in **PySpark/SQL**; joins (incl. broadcast), unions, explode, dedup, aggregations; core Spark tuning params (`spark.sql.shuffle.partitions`, `autoBroadcastJoinThreshold`, executor/driver memory); gold-layer objects — **materialized views vs views vs streaming tables vs tables** in UC; data-quality checks |
| 4. Working with Lakeflow Jobs | **16%** | Control flow (retries, branching, looping), task types in DAG task graphs; trigger types — **scheduled vs file-arrival vs table-update** |
| 5. Implementing CI/CD | **10%** | Git Folders (branches, commits, PRs); **Asset Bundles** — variables/overrides across dev→test→prod; Databricks CLI validate/deploy |
| 6. Troubleshooting, Monitoring, and Optimization | **10%** | Lakeflow Jobs run-history & DAG monitoring; Spark UI stage metrics (skew, shuffle, spill); **Liquid Clustering & predictive optimization**; cluster startup/library/OOM diagnosis |
| 7. Governance and Security | **15%** | UC managed vs external tables; GRANT/REVOKE/DENY on the securable hierarchy; column masking & row-level security; **UC ABAC policies** |

### (b) Logistics (official exam guide + webpage)
- **45 scored multiple-choice questions**; **90 minutes**; **$200 USD** + tax; online proctored or test center
- No prerequisites (recommended: training + 6 months hands-on); code items PySpark-primary with SQL; **valid 2 years**

### (c) Prep resources (free-first ranking)
1. **Databricks Academy self-paced Data Engineer learning path — FREE.** All self-paced Academy courses became free in June 2025 under Databricks' $100M education investment ([press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-free-edition-and-announces-100-million)). The exam guide names the exact courses: *Data Ingestion with Lakeflow Connect; Deploy Workloads with Lakeflow Jobs; DevOps Essentials for Data Engineering; Data Interoperability with Unity Catalog; Build Data Pipelines with Lakeflow Spark Declarative Pipelines; Get Started with Data Governance on Databricks.* Only material guaranteed aligned with the May 2026 outline.
2. **Databricks Free Edition — FREE** ([overview](https://www.databricks.com/learn/free-edition), [limitations](https://docs.databricks.com/aws/en/getting-started/free-edition-limitations)). Community Edition's successor — **serverless-only with Unity Catalog on by default, exactly the environment the exam now assumes**. Can practice: notebooks, SQL, Lakeflow Jobs, **Lakeflow Spark Declarative Pipelines (quota: 1 active pipeline per type)**, Auto Loader/COPY INTO, UC grants/masking, Git Folders. Can't practice: classic cluster configuration (note the exam still asks cluster-type questions), R/Scala, account-console admin; quotas raisable via LinkedIn identity verification.
3. **Derar Alhussein (Udemy)** — top third-party pick, **confirmed updated to V4 in May 2026 for the new syllabus**: [prep course](https://www.udemy.com/course/databricks-certified-data-engineer-associate/) (4.6★, ~17k reviews) + [practice exams](https://www.udemy.com/course/practice-exams-databricks-certified-data-engineer-associate/) (V4, May 2026). ~$15–20 each on sale. Caution: his O'Reilly *Study Guide* book targets the pre-2025 exam — skip it.
4. **Free extras:** [freeCodeCamp prep course](https://www.freecodecamp.org/news/prepare-for-the-databricks-data-engineer-associate-certification-exam-and-pass/) (verify version alignment) + the official guide's sample questions.
5. **Cost hack:** the recurring **Databricks Learning Festival** (recent windows Jan 9–30 and Mar 16–Apr 3, 2026) grants a **50% certification voucher** for completing one self-paced pathway — $200 → $100 ([community events page](https://community.databricks.com/t5/learning-events/databricks-learning-festival-self-paced-global/ev-p/150223)). Watch for the next window before booking.

### (d) Study-hour estimate: **~30–45 hours** (4–6 weeks at this pace)
Databricks recommends 6 months hands-on, but the program's Spark/Databricks block *is* that hands-on. 2025–2026 passers of the post-rewrite exam typically report 2–6 weeks of targeted prep on top of working Spark knowledge. Budget: ~15–20h Academy courses, ~10–15h Free Edition labs (jobs, one declarative pipeline, UC grants/masks, a small Asset Bundle deploy via CLI), ~8–10h practice exams + Spark-UI/tuning review.

### (e) Recommended timing in the 12-month program
Sit it at **end of month 6 / start of month 7**, as the direct capstone of the Spark/Databricks block — before context-switching into AWS-native services. Take it *early* rather than late: (1) the 2-year validity clock and fast revision cadence mean delaying buys nothing; (2) its Spark-tuning and medallion content reinforces DEA-C01's Glue/EMR questions. If a Learning Festival window falls in month 5–6, complete the pathway inside it for the 50% voucher.

---

## 3. dbt credential — fact check (audit note)

There is **no "dbt Foundational Certificate."** dbt Labs' actual certification is the **"dbt Analytics Engineering Certification Exam"** — [official page](https://www.getdbt.com/certifications/analytics-engineer-certification-exam) (currently listing supported dbt version 1.11) — **$200 USD** (65 questions, 2 hours, online proctored; 2-year validity), plus a dbt Cloud Administrator Certification, also $200. The free **"dbt Fundamentals"** course confers a completion **badge**, not a certification — the likely source of the "foundational" confusion. Correct audit wording: *"dbt Analytics Engineering Certification, $200, not pursued."*

---

### Primary sources
- [AWS DEA-C01 Exam Guide (official PDF, v1.0)](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf) · [AWS DEA cert page](https://aws.amazon.com/certification/certified-data-engineer-associate/)
- [Databricks DE Associate exam guide — May 4, 2026 (official PDF)](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf) · [July 25, 2025 guide (official PDF)](https://www.databricks.com/sites/default/files/2025-11/databricks-certified-data-engineer-associate-exam-guide-july-25-2025-04.pdf) · [exam webpage](https://www.databricks.com/learn/certification/data-engineer-associate)
- [Databricks Free Edition limitations](https://docs.databricks.com/aws/en/getting-started/free-edition-limitations) · [Free Edition + $100M free-training press release](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-free-edition-and-announces-100-million) · [Learning Festival (50% voucher)](https://community.databricks.com/t5/learning-events/databricks-learning-festival-self-paced-global/ev-p/150223)
- Prep: [Maarek/Kane Udemy](https://www.udemy.com/course/aws-data-engineer/) · [Tutorials Dojo DEA-C01](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) · [Derar Alhussein course](https://www.udemy.com/course/databricks-certified-data-engineer-associate/) · [his practice exams](https://www.udemy.com/course/practice-exams-databricks-certified-data-engineer-associate/) · [freeCodeCamp](https://www.freecodecamp.org/news/prepare-for-the-databricks-data-engineer-associate-certification-exam-and-pass/) · [ExamCert study-time guide](https://www.examcert.app/blog/aws-dea-c01-complete-guide/)
- [dbt Analytics Engineering Certification (official)](https://www.getdbt.com/certifications/analytics-engineer-certification-exam)
