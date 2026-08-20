# Tool Universe — Verdicts, Phase Placement, Cert Mapping

Jump: [CORE](#core--hands-on-scheduled-in-a-phase) · [AWARE](#aware--concepts--1-day-exposure) · [SKIP](#skip--deliberately-excluded-this-year) · [Contested](#contested-calls-know-these-exist--theyre-honest-judgment-calls)

Every tool considered for this framework, with a verdict grounded in the 2026 research (full evidence + URLs in [`sources/research/tool-landscape.md`](../sources/research/tool-landscape.md); demand data in [`sources/research/job-market.md`](../sources/research/job-market.md)). **Every tool name links to its official documentation — the source of truth that outlives any course or blog post.** When a tutorial and the docs disagree, the docs win.

> **CORE** = learn hands-on, it's in the platform or a satellite. **AWARE** = understand the concepts + ≤1 day exposure. **SKIP** = deliberately excluded this year (reason given). Cert columns: **DBX** = Databricks DE Associate, **DEA** = AWS DEA-C01.

## CORE — hands-on, scheduled in a phase

| Tool | Phase(s) | Cert | Role in the framework |
|---|---|---|---|
| [SQL](https://www.postgresql.org/docs/current/queries.html) (advanced/analytical; Postgres dialect as reference) | P0–P6 (permanent) | DBX, DEA | The permanent spine; in 70–94% of job postings |
| [Python](https://docs.python.org/3/) (+ [uv](https://docs.astral.sh/uv/), [pytest](https://docs.pytest.org/), typing) | P0–P6 (permanent) | DBX, DEA | The other permanent spine; all ingestion/glue code (moto powers the P2 AWS-mocking tests) |
| [Parquet](https://parquet.apache.org/docs/) | P1 | DEA | The physical layer under everything |
| [DuckDB](https://duckdb.org/docs/) | P1 | — | Local dev warehouse; SQL-on-files default |
| [Apache Iceberg](https://iceberg.apache.org/docs/latest/) | P1, P2 | DEA | The platform's table format (local → S3 Tables); v3 era (PyIceberg is the Python client — used in P1 and the P5 sink) |
| [dbt](https://docs.getdbt.com/) (Core, 3-layer project, tests, snapshots, incremental) | P1, P2, P6 | DEA (transform concepts) | The transformation layer, one project grown all year |
| [Amazon S3](https://docs.aws.amazon.com/s3/) + zones | P2 | DEA | The lakehouse's storage |
| [AWS Glue](https://docs.aws.amazon.com/glue/) (Catalog, Crawlers, ETL) | P2 | DEA (~25% of exam surface) | Catalog + serverless Spark ETL |
| [Amazon Athena](https://docs.aws.amazon.com/athena/) | P2 | DEA | The platform's query engine; cost mechanics |
| [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) | P2 | DEA | Managed Iceberg: compaction/snapshot maintenance handled |
| [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/) (scoped) | P2 | DEA (Domain 4) | Governance grants over the lake |
| [AWS Lambda](https://docs.aws.amazon.com/lambda/) | P4 (exam theory arrives in the P2 course) | DEA | Serverless glue: triggers, light transforms |
| [PySpark / Spark 4.x](https://spark.apache.org/docs/latest/) | P3 | DBX, DEA (Glue/EMR) | Distributed compute; Spark UI literacy |
| [Delta Lake](https://docs.delta.io/latest/) | P3 | DBX | Databricks phase table format; MERGE, time travel, Liquid Clustering (delta-rs drives the P3 bake-off's non-Spark leg) |
| [Databricks](https://docs.databricks.com/) (Free Edition: Lakeflow Jobs/SDP, Auto Loader, UC, Asset Bundles) | P3 | DBX | The entire cert phase environment |
| [Apache Airflow 3.x](https://airflow.apache.org/docs/) | P4 | DEA (MWAA) | The platform's orchestrator (local/Astro CLI) |
| [dlt](https://dlthub.com/docs/intro) (dltHub) | P4 | — | Declarative API/database ingestion; breakout tool of the cycle |
| [AWS DMS](https://docs.aws.amazon.com/dms/) | P4 | DEA | AWS-native CDC into the platform (Postgres on RDS is the operated OLTP source here and in P5/P6) |
| [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/) (Streams + Firehose) | P2 (mini-lab), P4 | DEA (Domain 1) | AWS streaming ingest path |
| [Amazon Redshift](https://docs.aws.amazon.com/redshift/) (+ Spectrum, Serverless) | P2 (taste), P4 | DEA | Warehouse satellite; heavy exam presence |
| [AWS SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) (+ [gitleaks](https://github.com/gitleaks/gitleaks)) | P0, P4 | DEA (security concepts) | The secrets story: nothing in git, DAGs pull at runtime |
| [Apache Kafka 4.x](https://kafka.apache.org/documentation/) (KRaft) | P5 | DEA (MSK trade-offs) | Event backbone fundamentals, run locally |
| [Debezium](https://debezium.io/documentation/) | P5 | — | Open-source CDC; the DMS-comparison satellite |
| [dbt tests](https://docs.getdbt.com/docs/build/data-tests) + [dbt-expectations (metaplane)](https://hub.getdbt.com/metaplane/dbt_expectations/latest/) + [Elementary](https://docs.elementary-data.com/) | P6 | DEA (data quality concepts) | The 2026 quality/observability stack for a dbt lakehouse |
| [Terraform](https://developer.hashicorp.com/terraform/docs) | P6 | DEA (IaC concepts) | Codify the platform's core resources (tfsec scans the config in P6) |
| [Apache Superset](https://superset.apache.org/docs/intro) | P6 | — | The platform's visible BI layer |
| [ClickHouse](https://clickhouse.com/docs) | P6 (satellite) | — | The serving/speed layer fed from gold marts (Tweeq pattern) |
| [pgvector](https://github.com/pgvector/pgvector) + embedding pipeline | P6 (satellite) | — | The AI-data differentiator module (~12% of postings, climbing) |
| [Docker / Docker Compose](https://docs.docker.com/) | P0–P6 | — | Local infra for everything above |
| [Git](https://git-scm.com/doc) + [GitHub Actions](https://docs.github.com/actions) | P0–P6 | DEA (CI/CD concepts) | Version control; interim scheduler (MoJ pattern); CI for dbt |
| [LLM-assisted DE](https://code.claude.com/docs) (Claude Code, MCP awareness) | P0–P6 (practice) | — | Assumed in 2026 job specs; used deliberately per the per-phase AI rules, and checked once: `AI-USAGE.md` (what you delegated vs hand-typed, one MCP tool tried) is a G6 gate item |

## AWARE — concepts + ≤1 day exposure

> Standing rule: every AWARE item ends with **one written comparison sentence** — what it is, and when you'd pick it over the CORE choice — filed in your platform repo's `notes/`. Awareness that produced no sentence didn't happen.

| Tool | Where covered | Why not CORE |
|---|---|---|
| [Polars](https://docs.pola.rs/) | P1 (half-day lab) | DuckDB covers the local niche; jobs still say pandas/Spark |
| [Apache Flink](https://nightlies.apache.org/flink/flink-docs-stable/) | P5 (Flink SQL lab, Confluent 101) | Stateful-streaming depth is a post-job specialization |
| [Redpanda](https://docs.redpanda.com/) | P5 (as the local Kafka) | It *is* the dev vehicle; Kafka is the skill |
| [MSK / MSK Connect](https://docs.aws.amazon.com/msk/) | P5 (theory + a written MSK-vs-self-managed trade-off note; no lab — the phase runs near-$0) | Deployment vehicle for Kafka skills; $-heavy to keep running |
| [MWAA](https://docs.aws.amazon.com/mwaa/) | P4 (theory + short-lived lab) | ~$350+/mo baseline; Airflow-the-skill is learned locally |
| [EMR / EMR Serverless](https://docs.aws.amazon.com/emr/) | P4 (reading: a written Glue-vs-EMR decision note) | Know Glue-vs-EMR trade-off; Glue covers Spark-on-AWS hands-on |
| [Step Functions](https://docs.aws.amazon.com/step-functions/) + [EventBridge](https://docs.aws.amazon.com/eventbridge/) | P4 (one state machine lab) | Know when they beat Airflow |
| [SageMaker Lakehouse](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/lakehouse.html) (branding) | P2 (reading) | Umbrella rebrand of Glue/Athena/Redshift — know the diagram |
| [Dagster](https://docs.dagster.io/) | P4 (satellite) | Airflow leads demand; Dagster = one strong comparison satellite |
| [SQLMesh](https://sqlmesh.readthedocs.io/) | P6 (reading + 2-hr taste) | Credible dbt challenger, now LF-governed; market still dbt-first |
| [dbt Fusion engine](https://docs.getdbt.com/docs/fusion/about-fusion) | P2 (reading) | Arrives with dbt v2; know why it matters (Rust, static analysis) |
| [Delta UniForm](https://docs.delta.io/latest/delta-uniform.html) / format convergence | P3 (reading) | Explains why Iceberg knowledge transfers to Delta shops |
| [DuckLake](https://ducklake.select/) | P1 (reading) | Format to watch; one year old vs the Iceberg ecosystem |
| [Apache Polaris](https://polaris.apache.org/) (Iceberg REST catalog) | P2 (reading) | Know the REST-catalog concept; Glue/S3 Tables covers the doing |
| [DataHub](https://docs.datahub.com/) / [OpenMetadata](https://docs.open-metadata.org/) | P6 (reading + optional quickstart) | Catalog concepts; a full deployment is overkill solo |
| [OpenLineage](https://openlineage.io/docs) / [Marquez](https://marquezproject.github.io/marquez/) | P6 (1-hr demo) | The lineage standard; demo-level is interview-sufficient |
| [Soda](https://docs.soda.io/) (v4 contracts) | P6 (reading) | Contracts vocabulary; dbt model contracts cover the hands-on |
| [Great Expectations (GX)](https://docs.greatexpectations.io/) | P6 (vocabulary only) | Acquired by FICO 2026, GX Cloud shut down; dbt tests + Elementary replaced the pattern |
| [Pandera](https://pandera.readthedocs.io/) | P6 (reading) | DataFrame validation niche; right-sized awareness |
| [Monte Carlo](https://docs.getmontecarlo.com/) | P6 (vocabulary) | Category-defining, $50K+/yr, can't self-host |
| Semantic layers ([MetricFlow](https://docs.getdbt.com/docs/build/about-metricflow), [Cube](https://cube.dev/docs)) | P6 (reading) | Fast-moving AI-agent infrastructure; awareness suffices |
| [Airbyte](https://docs.airbyte.com/) / [Fivetran](https://fivetran.com/docs/getting-started) / [Sling](https://docs.slingdata.io/) | P4 (reading: connector-ELT positioning note next to the dlt build) | Connector-ELT concepts; dlt is the hands-on pick |
| [Snowflake](https://docs.snowflake.com/) | P6 (half-day reading) | Global demand hedge (29% of postings); Databricks chosen for Gulf weighting |
| Azure data stack ([ADF](https://learn.microsoft.com/azure/data-factory/)/[Synapse](https://learn.microsoft.com/azure/synapse-analytics/)/[Fabric](https://learn.microsoft.com/fabric/) vocabulary) | P6 (half-day reading) | Regional-enterprise hedge (Azure-heavy shops); vocabulary only, no builds |
| [WarpStream](https://docs.warpstream.com/)-style diskless streaming / [Confluent Tableflow](https://docs.confluent.io/cloud/current/topics/tableflow/overview.html) | P5 (reading) | Architecture direction; concept-level |
| [MotherDuck](https://motherduck.com/docs/) / [Evidence](https://docs.evidence.dev/) / [Metabase](https://www.metabase.com/docs/) | opportunistic | Nice satellite garnish, not scheduled |
| [CloudWatch](https://docs.aws.amazon.com/cloudwatch/) + [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) | P0 (alarms) + P6 (dashboard) | Scoped to what the platform needs |

## SKIP — deliberately excluded this year

| Tool | Reason |
|---|---|
| Hadoop/HDFS, Hive-only patterns | Legacy; concepts arrive via Spark/Glue |
| Apache Hudi | Niche upsert estates; Iceberg + Delta cover table-format concepts |
| Prefect, Kestra | A third Python orchestrator adds no employability over Airflow + Dagster |
| StarRocks, Apache Doris | Second OLAP engine adds nothing at entry level; ClickHouse covers the category |
| chDB | Embedded-ClickHouse niche; DuckDB fills it locally |
| Unity Catalog OSS, Gravitino | Catalog federation layers most AWS shops don't run (managed UC is CORE in P3) |
| Estuary Flow | Adoption evidence is mostly vendor marketing |
| AppFlow | Stagnant; dlt/Fivetran own the space |
| Kubernetes administration | Not a DE entry requirement; everything here runs serverless or in Compose |
| Scala / Scala Spark | PySpark-first; revisit only on employer demand |
| Deep Flink (state backends, ops) | Post-job specialization |
| GCP / a third cloud | One cloud deep beats three shallow; Azure gets vocabulary only |

## Contested calls (know these exist — they're honest judgment calls)

- **Iceberg CORE despite <10% production penetration** — direction is unanimous (AWS/Snowflake/Databricks all standardized on it) and hands-on Iceberg is a differentiator, but hiring managers may probe Spark/SQL harder.
- **Airflow CORE / Dagster satellite** — AWS-weighted call; a dbt-centric greenfield framework could defensibly flip it (Tweeq chose Dagster).
- **Debezium CORE** — pure AWS employability might say DMS-only; Debezium earns CORE because the comparison satellite demonstrates transferable CDC mechanics no managed service shows.
- **dbt over SQLMesh** — installed base + hiring surface; both now sit under the same corporate parent (Fivetran), so watch for convergence.

Full reasoning and 45+ sources: [`sources/research/tool-landscape.md`](../sources/research/tool-landscape.md).
