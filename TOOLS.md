# Tool Universe — Verdicts, Phase Placement, Cert Mapping

Every tool considered for this framework, with a verdict grounded in the 2026 research (full evidence + URLs in [`sources/research/tool-landscape.md`](sources/research/tool-landscape.md); demand data in [`sources/research/job-market.md`](sources/research/job-market.md)).

> **CORE** = learn hands-on, it's in the spine or a satellite. **AWARE** = understand the concepts + ≤1 day exposure. **SKIP** = deliberately excluded this year (reason given). Cert columns: **DBX** = Databricks DE Associate, **DEA** = AWS DEA-C01.

## CORE — hands-on, scheduled in a phase

| Tool | Phase(s) | Cert | Role in the framework |
|---|---|---|---|
| SQL (advanced/analytical) | P0–P6 (permanent) | DBX, DEA | The permanent spine; in 69–94% of job postings |
| Python (+ uv, pytest, typing) | P0–P6 (permanent) | DBX, DEA | The other permanent spine; all ingestion/glue code |
| Parquet | P1 | DEA | The physical layer under everything |
| DuckDB | P1 | — | Local dev warehouse; SQL-on-files default |
| Apache Iceberg | P1, P2 | DEA | The spine's table format (local → S3 Tables); v3 era |
| dbt (Core, 3-layer project, tests, incremental) | P1, P2, P6 | DEA (transform concepts) | The transformation layer, one project grown all year |
| Amazon S3 + zones | P2 | DEA | The lakehouse's storage |
| AWS Glue (Catalog, Crawlers, ETL) | P2 | DEA (~25% of exam surface) | Catalog + serverless Spark ETL |
| Amazon Athena | P2 | DEA | The spine's query engine; cost mechanics |
| Amazon S3 Tables | P2 | DEA | Managed Iceberg: compaction/snapshot maintenance handled |
| AWS Lake Formation (scoped) | P2 | DEA (Domain 4) | Governance grants over the lake |
| AWS Lambda | P2, P4 | DEA | Serverless glue: triggers, light transforms |
| PySpark / Spark 4.x | P3 | DBX, DEA (Glue/EMR) | Distributed compute; Spark UI literacy |
| Delta Lake | P3 | DBX | Databricks phase table format; MERGE, time travel, Liquid Clustering |
| Databricks (Free Edition: Lakeflow Jobs/SDP, Auto Loader, UC, Asset Bundles) | P3 | DBX | The entire cert phase environment |
| Apache Airflow 3.x | P4 | DEA (MWAA) | The spine's orchestrator (local/Astro CLI) |
| dlt (dltHub) | P4 | — | Declarative API/database ingestion; breakout tool of the cycle |
| AWS DMS | P4 | DEA | AWS-native CDC into the spine |
| Amazon Kinesis (Streams + Firehose) | P4 | DEA (Domain 1) | AWS streaming ingest path |
| Amazon Redshift (+ Spectrum, Serverless) | P4 | DEA | Warehouse satellite; heavy exam presence |
| Apache Kafka 4.x (KRaft) | P5 | DEA (MSK trade-offs) | Event backbone fundamentals, run locally |
| Debezium | P5 | — | Open-source CDC; the DMS-comparison satellite |
| dbt tests + dbt-expectations (metaplane) + Elementary | P6 | DEA (data quality concepts) | The 2026 quality/observability stack for a dbt lakehouse |
| Terraform | P6 | DEA (IaC concepts) | Codify the spine's core resources |
| Apache Superset | P6 | — | The portfolio's visible BI layer |
| ClickHouse | P6 (satellite) | — | The serving/speed layer fed from gold marts (Tweeq pattern) |
| pgvector + embedding pipeline | P6 (satellite) | — | The AI-data differentiator module (~12% of postings, climbing) |
| Docker / Docker Compose | P0–P6 | — | Local infra for everything above |
| Git + GitHub Actions | P0–P6 | DEA (CI/CD concepts) | Version control; interim scheduler (MoJ pattern); CI for dbt |
| LLM-assisted DE (Claude Code, MCP awareness) | P0–P6 (practice) | — | Assumed in 2026 job specs; used deliberately per phase rules |

## AWARE — concepts + ≤1 day exposure

| Tool | Where covered | Why not CORE |
|---|---|---|
| Polars | P1 (half-day lab) | DuckDB covers the local niche; jobs still say pandas/Spark |
| Apache Flink | P5 (Flink SQL lab, Confluent 101) | Stateful-streaming depth is a post-job specialization |
| Redpanda | P5 (as the local Kafka) | It *is* the dev vehicle; Kafka is the skill |
| MSK / MSK Connect | P5 (theory + costed mini-lab) | Deployment vehicle for Kafka skills; $-heavy to keep running |
| MWAA | P4 (theory + short-lived lab) | ~$350+/mo baseline; Airflow-the-skill is learned locally |
| EMR / EMR Serverless | P4 (one job) | Know Glue-vs-EMR trade-off; Glue covers Spark-on-AWS hands-on |
| Step Functions + EventBridge | P4 (one state machine lab) | Know when they beat Airflow |
| SageMaker Lakehouse (branding) | P2 (reading) | Umbrella rebrand of Glue/Athena/Redshift — know the diagram |
| Dagster | P4 (satellite) | Airflow leads demand; Dagster = one strong comparison satellite |
| SQLMesh | P6 (reading + 2-hr taste) | Credible dbt challenger, now LF-governed; market still dbt-first |
| dbt Fusion engine | P2/P6 (reading) | Arrives with dbt v2; know why it matters (Rust, static analysis) |
| Delta UniForm / format convergence | P3 (reading) | Explains why Iceberg knowledge transfers to Delta shops |
| DuckLake | P1 (reading) | Format to watch; one year old vs the Iceberg ecosystem |
| Apache Polaris (Iceberg REST catalog) | P2 (reading) | Know the REST-catalog concept; Glue/S3 Tables covers the doing |
| DataHub / OpenMetadata | P6 (reading + optional quickstart) | Catalog concepts; a full deployment is overkill solo |
| OpenLineage / Marquez | P6 (1-hr demo) | The lineage standard; demo-level is interview-sufficient |
| Soda (v4 contracts) | P6 (reading) | Contracts vocabulary; dbt model contracts cover the hands-on |
| Great Expectations (GX) | P6 (vocabulary only) | Acquired by FICO 2026, GX Cloud shut down; dbt tests + Elementary replaced the pattern |
| Pandera | P6 (reading) | DataFrame validation niche; right-sized awareness |
| Monte Carlo | P6 (vocabulary) | Category-defining, $50K+/yr, can't self-host |
| Semantic layers (MetricFlow, Cube) | P6 (reading) | Fast-moving AI-agent infrastructure; awareness suffices |
| Airbyte / Fivetran / Sling | P4 (reading) | Connector-ELT concepts; dlt is the hands-on pick |
| Snowflake | P6 (half-day reading) | Global demand hedge (29% of postings); Databricks chosen for Gulf weighting |
| Azure data stack (ADF/Synapse/Fabric vocabulary) | P6 (half-day reading) | Saudi enterprise hedge; no builds |
| WarpStream-style diskless streaming / Confluent Tableflow | P5 (reading) | Architecture direction; concept-level |
| MotherDuck / Evidence / Metabase | opportunistic | Nice satellite garnish, not scheduled |
| CloudWatch + AWS Budgets | P0 (alarms) + P6 (dashboard) | Scoped to what the spine needs |

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

Full reasoning and 45+ sources: [`sources/research/tool-landscape.md`](sources/research/tool-landscape.md).
