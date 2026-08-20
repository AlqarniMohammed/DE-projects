You are an elite **Principal Data Engineer**, **Lakehouse Architect**, and **Brutally Honest Technical Career Coach** with deep experience designing modern data platforms inside top-tier consulting firms (such as McKinsey QuantumBlack, BCG X, or Accenture). You have personally shipped Lakehouse architectures on AWS, written dbt projects against Redshift / Athena / Databricks, operated Spark on EMR and Databricks, instrumented CDC pipelines with Debezium/Kafka, and coached associates through the **Databricks Data Engineer Associate, AWS SAA-C03, AWS DEA-C01, and dbt Foundational Certificate** in compressed timelines.

I am giving you (a) my professional reality and constraints, (b) my four target certifications, (c) a complete 2026 Data Engineering Master Guide attached as a reference document, and (d) a single, ruthless output mandate: **design exactly 30 personal, weekly data engineering projects** that I will execute solo to expand my experience as a data engineer.

---

## 1. My Professional Reality & "The Gap" (Crucial Context)

* **Current Role & Level:** Data Science Specialist at **Associate level** inside a technical consulting firm.
* **Reality of the Company:** The firm has **no active Data or AI projects**. There is no pipeline above me to learn from — I have to *become* the pipeline.
* **What I Actually Do Daily:** Database design and data modeling for standard company projects. I am strong at relational modeling, ERDs, normalization, and SQL — this is leverage, not a liability.
* **The Real Skill Gap:** I am distant from **production data engineering** — building pipelines, running Spark, orchestrating workflows, operating a Lakehouse, CDC, streaming, and cloud-native data services. Courses alone will not close this gap. **Shipped projects will.**
* **My Core Goal (non-negotiable):** Become exceptionally strong in **Data Engineering**. Not data science, not ML engineering, not generic backend. Data Engineering — on the modern Lakehouse stack, on AWS, with dbt as the transformation layer.
---

## 2. Strategic Constraints

* **Certification Focus (these four, in this order of priority):**
  1. **AWS Certified Solutions Architect – Associate (SAA-C03)** — cloud architecture foundation
  2. **Databricks Certified Data Engineer Associate** — Lakehouse / Spark / Delta credibility
  3. **AWS Certified Data Engineer – Associate (DEA-C01)** — AWS-native DE services mastery
  4. **dbt Foundational Certificate** — modern transformation layer credential
  Every project must visibly contribute to mastery of **at least one** of these four exam domains. Map it explicitly.
* **2026 Modern Data Stack Alignment:** Lakehouse paradigm over legacy warehousing. Separation of compute and storage. Open table formats (Iceberg, Delta). Software-engineering practices in data via dbt. Asset-based orchestration (Dagster) alongside the still-dominant Airflow. CDC-first ingestion. The attached **2026 Data Engineering Master Guide** is the source of truth for tool selection — every project must use tools the guide endorses, and skip the ones it flags as legacy.
* **Claude Code Advantage:** I will use **Claude Code (Agentic CLI/IDE)** to accelerate every project. Assume that scaffolding, boilerplate, IaC, and test generation are agent-accelerated. Target weekly effort: **6–10 focused hours per project**, not 40. Projects must be ambitious *because* the agent compresses the build time, not in spite of it.
* **Personal, Solo, One Week Each:** All 30 projects are **personal** (not internal to the firm, not commercial offerings). Each is built and shipped in **one calendar week**. Each ends with a GitHub repo + a LinkedIn post.
* **Three Things Every Project Must Deliver:**
  1. **A concrete new skill or knowledge unit** (a tool learned, a pattern internalized, a service operated).
  2. **A new dataset** — never the same dataset twice across the 30 projects. Use public datasets (NYC Taxi, GHArchive, Stack Overflow, Common Crawl, Kaggle, government open data, OpenWeather, GDELT, MovieLens, IMDb, Reddit Pushshift, FRED economic data, OpenStreetMap, Wikipedia dumps, BLS, World Bank, SEC EDGAR filings, NOAA, eBird, GTFS transit feeds, Spotify charts, Steam reviews, Hacker News, etc.).
  3. **Multiple skills/tools combined** — no single-tool toy projects. Each project must integrate **3 or more** distinct tools, services, or concepts from the attached 2026 guide.
---

## 3. Reference Inputs You MUST Use

You have two attached documents:
1. **The 2026 Data Engineering Master Guide** — tool selection, AWS service mappings, the Lakehouse reference architecture, and the prioritized learning sequence (SQL → Python → Spark → dbt → Airflow → AWS Core → Kafka → Iceberg/Delta → Terraform → Streaming → Advanced).
2. **My existing roadmap audit** — the broader 6-month context. Treat it as background only; **do not regenerate it**. Your job is the 30-project list.
You must:
* Pull the **tool universe** for the 30 projects directly from the master guide (Spark/PySpark, dbt, Airflow, Dagster, Kafka, Debezium, Flink, Iceberg, Delta, Parquet, Trino/Athena, Glue, EMR, MSK, MWAA, Redshift, S3 Tables, Lake Formation, DMS, AppFlow, EventBridge, Lambda, Step Functions, Terraform, Great Expectations, OpenLineage, dlt, Airbyte, DuckDB, Polars).
* Honor the **sequencing principle** in the guide. Early weeks reinforce SQL/Python/Spark/dbt fundamentals. Middle weeks introduce orchestration, AWS-native services, and Iceberg/Delta. Later weeks layer in streaming, CDC, governance, lineage, observability, and IaC. The final weeks are integrative capstones.
---

## 4. The 30-Project Sequencing Plan (Non-Negotiable Structure)

Group the 30 projects into **five phases of six projects each**, mapped to a learning arc that compounds:

* **Phase 1 — Weeks 1–6: SQL, Python, Lakehouse Foundations & dbt Fundamentals**
  *(Target cert pressure: dbt Foundational + SAA-C03 storage/IAM domains)*
  Establish DuckDB + Iceberg locally, advanced SQL on real public data, first dbt project with tests, medallion architecture on a laptop, intro to S3 + Parquet, intro to Glue Data Catalog.
* **Phase 2 — Weeks 7–12: PySpark, Databricks & Delta Lake Mastery**
  *(Target cert pressure: Databricks DE Associate)*
  PySpark fundamentals on Databricks Community Edition, Delta Lake mechanics (ACID, time travel, OPTIMIZE/ZORDER), Delta Live Tables, Spark performance tuning (skew, AQE, broadcast joins), Databricks Workflows, Unity Catalog basics.
* **Phase 3 — Weeks 13–18: AWS-Native Data Engineering**
  *(Target cert pressure: AWS DEA-C01 + remaining SAA-C03 domains)*
  Glue ETL jobs and Crawlers, Athena optimization, Redshift + Redshift Spectrum, S3 Tables (native Iceberg), Lake Formation governance, Kinesis Data Streams + Firehose, AWS DMS for CDC, EMR Serverless for Spark.
* **Phase 4 — Weeks 19–24: Orchestration, Streaming, CDC & Open Source Stack**
  Apache Airflow (and MWAA) DAGs, Dagster software-defined assets, Kafka + Debezium CDC end-to-end, Flink stream processing, dlt ingestion patterns, Great Expectations for data quality, OpenLineage for lineage.
* **Phase 5 — Weeks 25–30: Production Concerns, IaC, Observability & Capstone**
  Terraform for the full Lakehouse stack, CI/CD for dbt projects, data contracts in CI, cost-aware query routing, observability (CloudWatch + custom metrics), capstone integrating CDC → Iceberg → dbt → Athena → orchestrated by Dagster/Airflow, all IaC-managed.
---

## 5. The Output Specification (EXACTLY 30 PROJECTS)

Produce **exactly 30 projects**, numbered 1 through 30, grouped under the five phases above. For **every single project**, use this rigid template — do not deviate, do not abbreviate:

---

### Week N — "<Punchy, LinkedIn-Postable Project Title>"

* **Phase:** <Phase 1 / 2 / 3 / 4 / 5>
* **One-line pitch:** A single sentence describing what the project is and why it matters.
* **Primary new skill gained:** The single most important new skill or concept I will internalize. Be specific (e.g., "Iceberg hidden partitioning and partition evolution," not "data lake stuff").
* **Secondary skills reinforced:** 2–4 supporting skills.
* **Tool stack (3+ tools):** Concrete list of every tool, library, service, and table format used. Pulled from the 2026 guide.
* **Cert exam domains touched:** Map explicitly to **SAA-C03 / Databricks DE Associate / DEA-C01 / dbt Foundational** exam domains. Use real domain names from each exam blueprint. If a project touches none of the four, **cut it and replace it.**
* **Dataset (must be unique across all 30 projects):** Name the public dataset, its source URL or origin, approximate size, and why it suits this project.
* **Architecture in 3–5 lines:** Source → ingest → store → transform → serve. Concrete, not generic.
* **Concrete weekly deliverables:**
  1. GitHub repo contents (code, README, architecture diagram, Makefile, Dockerfile/compose if applicable, tests)
  2. The specific working artifact a viewer should be able to run (e.g., `make demo` produces X)
  3. The LinkedIn post hook — one sentence, post-ready
* **"Wow-factor" — the demoable moment:** The 30-second clip or screenshot that makes a hiring manager pause. Be specific.
* **Stretch goal (only if Claude Code finishes the core fast):** One optional advanced extension.
* **Why this project (90 words, brutally honest):** Why does *this* project earn a week of my life over alternatives? What gap does it close? What does it signal on my resume? If you cannot defend it in 90 words, the project is filler — replace it.
---

## 6. Hard Rules You Must Follow

1. **Exactly 30 projects. Not 29, not 31.** Numbered 1–30. Grouped under the five phases.
2. **No dataset is reused.** Each project introduces a fresh public dataset. Maintain mental tracking; if you find yourself repeating, swap.
3. **No project relies on a single tool.** Minimum three distinct tools / services / concepts each.
4. **Every project maps to at least one of the four certs.** If a project does not, replace it. State the mapping explicitly.
5. **No legacy tooling.** No Hadoop/HDFS-as-target, no raw S3 dumps without table format, no hand-rolled ETL in pure Python when dbt or dlt fits, no Hive-only patterns. Follow the master guide's cut list.
6. **No project depends on infrastructure that costs more than ~$20 to operate for a week.** Default to AWS Free Tier, Databricks Community Edition, local Docker Compose, DuckDB, MinIO, Redpanda (lighter Kafka), and Iceberg/Delta on local filesystem when AWS is overkill. State the cost posture per project if non-obvious.
7. **Sequencing compounds.** Project N+1 reuses or extends a skill from Project N where possible. Do not jump from "intro SQL" in Week 1 to "stateful Flink streaming" in Week 2.
8. **Each project must give me something I do not already have.** I already know SQL, relational/dimensional modeling, ERDs, normalization, Python basics, and database design. Do not waste a week teaching me those — assume them and build forward.
9. **Capstone discipline.** Weeks 28, 29, 30 must be increasingly integrative. Week 30 is the portfolio centerpiece — a multi-component, end-to-end Lakehouse platform tying earlier projects together into one demoable repo.
10. **No filler.** If you cannot defend a project in the 90-word "Why this project" block, the project does not belong on the list. Cut and replace.
---

## 7. Final Deliverable Structure (Exact Output Order)

Produce your response in **this exact order**:

1. **Opening Auditor's Statement** (max 150 words): brutally honest framing of what these 30 projects will and will not do for my career, anchored to the four certs and to the gap diagnosis above.
2. **The Skill & Tool Coverage Matrix:** A single markdown table with the rows being the major skill/tool families from the 2026 master guide (PySpark, Delta, Iceberg, dbt, Airflow, Dagster, Kafka, Debezium, Flink, Glue, Athena, Redshift, S3 Tables, Lake Formation, DMS, MWAA, EMR, Terraform, Great Expectations, OpenLineage, dlt, DuckDB, etc.) and the columns being the four certs. Each cell lists the **Week numbers** that hit that intersection. Any row that is empty across all four certs means a tool that does not belong on the list — remove it. Any cert column that is sparsely covered means I have not earned that cert — rebalance.
3. **The Dataset Inventory:** A single markdown table — `Week # | Project Title | Dataset | Source | Approx Size | Why this dataset`. Used to verify zero dataset reuse at a glance.
4. **The 30 Projects, in order, using the template in Section 5.** Five phase headers, six projects per phase.
5. **Cross-Project Skill Compounding Map:** A short narrative (max 250 words) showing how Week N skills feed Week N+5, N+10, N+15, etc. Prove the sequence compounds rather than scatters.
6. **The Capstone Architecture Diagram (Week 30):** An ASCII architecture diagram in a fenced code block showing how the Week 30 capstone integrates components from prior weeks. Label which earlier weeks each component traces back to.
7. **The Honest Failure Modes:** A 200-word section listing the three most likely ways I will fail to ship these 30 projects in 30 weeks, and the specific countermeasures.
8. **The Year-End Resume Statement:** A single paragraph (under 120 words) I can put on my CV after finishing all 30 projects, written as accomplishments-with-numbers, not aspirations.
---

## ⚠️ CRITICAL OUTPUT FORMAT INSTRUCTION

You MUST provide your entire final output (every section, every project, every table, every diagram, every word) enclosed within a **SINGLE markdown code block** (using triple backticks ```markdown ... ```). Do NOT write any conversational text outside of this code block. I want to copy the entire response with a single click of the "Copy" button.

Begin now. Do not ask clarifying questions — every clarification you would ask is already answered above. Produce the 30 projects.
