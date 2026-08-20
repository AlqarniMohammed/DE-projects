# Research Report — DE Job-Market Signals (compiled 2026-08-20)

Scope: web research via search + direct fetches. Confidence flags used throughout: **[solid]** = quantified scrape/report, **[directional]** = credible but small/biased sample, **[anecdotal]** = blog/vendor/commentary.

---

## (a) Global skill-demand table

Two quantified scrapes anchor this section, with very different samples — read them together:

- **365 Data Science / Glassdoor scrape** — 943 US Glassdoor DE postings, published Apr 2026 ([source](https://365datascience.com/career-advice/data-engineer-job-outlook-2025/)). General-market sample. **[solid]**
- **jobstrack.io Q1-2026 scrape** — 500+ DE postings "across major tech companies, startups, and enterprises" ([source](https://jobstrack.io/blog/roles/data-engineer)). Skews modern-stack/tech-company; numbers run much hotter for dbt/Airflow. **[directional]**

| Category | Skill | Glassdoor scrape (943 posts) | jobstrack scrape (500+ posts) | Trend note |
|---|---|---|---|---|
| Language | Python | 70% | 94% | Co-#1 everywhere |
| Language | SQL | 69% (79% in the 2025 edition) | 94% | Co-#1 everywhere |
| Language | Java / Scala | 32% / 25% | — | Differentiators, not core |
| Cloud | **AWS** | **40.3%** | — | #1 cloud in DE postings |
| Cloud | Azure | 34.3% | — | Strong #2 (enterprise) |
| Cloud | GCP | 12.3% | — | Distant #3 |
| Compute | Spark | 38.7% | 43% | Still the dominant framework |
| Warehouse | Snowflake | 29.2% | 54% (Snowflake *or* BigQuery) | Rising |
| Warehouse | Redshift | 21.8% | — | Legacy-AWS heavy |
| Lakehouse | Databricks | 16.8% | — | Rising fast from smaller base |
| Streaming | Kafka | 24.4% | 31% | Streaming is a growth axis; 67% of enterprises now run batch+streaming vs 41% in 2022 (Databricks State of Data+AI, via jobstrack) |
| Orchestration | Airflow | 15.8% | 58% (Airflow or Prefect) | #1 orchestrator in every source; Dagster/Prefect rarely named |
| Transform | dbt | not in top-tools list | **61%** | Conflict: the 61% figure (also attributed to a dbt Labs survey — vendor-adjacent, [via jobstrack](https://jobstrack.io/blog/roles/data-engineer)) reflects modern-stack companies; general Glassdoor sample barely surfaces dbt. Real demand is somewhere between. **[directional]** |
| DevOps | CI/CD / K8s / Docker / Terraform | 15.9% / 9.7% / 8.1% / 7.3% | 28% (Docker or K8s) | "1 in 6 postings mention CI/CD" |
| BI | Tableau/Power BI | ~10% | — | Creeping into DE scope |
| Certs | AWS / Azure / GCP certs | 4.2% / 3.6% / 1.2% of listings | — | Certs are tie-breakers, rarely requirements ([365DS](https://365datascience.com/career-advice/data-engineer-job-outlook-2025/)) |

**Iceberg/lakehouse:** analyst consensus says open table formats standardized around Iceberg/Delta ([lakeFS State of Data & AI Engineering 2025](https://lakefs.io/blog/the-state-of-data-ai-engineering-2025/)) **[anecdotal]**, but posting-level evidence is weak: Iceberg doesn't register in the Glassdoor scrape, and UK posting data ([ITJobsWatch](https://www.itjobswatch.co.uk/jobs/uk/apache%20iceberg.do)) shows Iceberg citations *falling* from 222 → 25 postings YoY (0.023% of UK vacancies; 72% of those co-cite AWS). Iceberg is an architecture trend, not yet a screening keyword. **[solid, for the negative claim]**

Market size: DE roles grew ~23% YoY, ~260k projected US openings in 2025; most postings ask 2–6 years' experience — mid-level is the fattest part of the market, true-entry (0–2 yrs) is only ~2% of postings ([365DS](https://365datascience.com/career-advice/data-engineer-job-outlook-2025/)).

---

## (b) Saudi/Gulf findings

Evidence here is thinner — no quantified KSA posting scrape exists; this is assembled from job boards and employer postings. **[directional throughout]**

- **Volume exists:** Glassdoor lists ~608 DE jobs in Saudi Arabia ([glassdoor.com](https://www.glassdoor.com/Job/saudi-arabia-data-engineer-jobs-SRCH_IL.0,12_IN207_KO13,26.htm)); Bayt, GulfTalent, NaukriGulf all carry active DE listings.
- **AWS vs Azure — mixed, not Azure-dominant:** Bayt keyword counts show "AWS data engineer" jobs (~880 KSA-wide, ~260 Riyadh) far outnumbering "Azure data engineer" (~10+ Riyadh) ([Bayt AWS](https://www.bayt.com/en/saudi-arabia/jobs/aws-data-engineer-jobs/) vs [Bayt Azure](https://www.bayt.com/en/saudi-arabia/jobs/azure-data-engineer-jobs-in-riyadh/)) — treat as directional (fuzzy keyword matching). Counter-signal: government/enterprise leans Microsoft, and a Saudi IT-leader guide ([aroundbits.com](https://aroundbits.com/microsoft-azure-vs-aws-vs-google-cloud-in-2026/)) notes Google Cloud is the only hyperscaler with a **live** in-Kingdom region (Dammam, Nov 2023), with **AWS's $5.3B Saudi region launching 2026** and Azure "Saudi East" planned Q4 2026. SAMA/NCA data-residency rules currently push regulated banking workloads to Google Cloud or local players (STC Cloud, Oracle). Net: the market is genuinely multi-cloud; the imminent AWS region is a tailwind for AWS skills.
- **Databricks is clearly valued:** Bayt has a dedicated Middle-East Databricks jobs category ([bayt.com](https://www.bayt.com/en/international/jobs/databricks-jobs/)); regional postings repeatedly pair "Azure + Databricks" or "AWS + Databricks + PySpark," e.g., Databricks Lakehouse architect roles specifying medallion architecture and Unity Catalog, and senior roles asking "Python, PySpark, Databricks, AWS Cloud, SQL" at 7–10 yrs ([careersingulf example](https://careersingulf.com/job/i-t-and-services/data-engineer-azure-databricks/35186), [naukrigulf](https://www.naukrigulf.com/azure-data-engineer-jobs-in-saudi-arabia)).
- **Aramco (bellwether employer)** posts Data Engineering Specialist roles asking: Python/SQL/Scala; Spark, Kafka, Airflow, Flink; "AWS, GCP, Azure" (any); "Databricks, Cloudera, Snowflake"; data lakes/warehouses/ELT; **governance, metadata, data quality frameworks**; OT/SCADA familiarity preferred ([careers.aramco.com](https://careers.aramco.com/expat_us/job/Data-Engineering-Specialist/857087823/)). Cloud-agnostic, fundamentals-heavy.
- **GulfTalent samples:** Riyadh Senior DE — SQL, Python, Airflow/Spark/Hadoop, ETL, any of AWS/Azure/GCP ([gulftalent.com](https://www.gulftalent.com/saudi-arabia/jobs/senior-data-engineer-488085)); Michael Page Data Engineering Specialist — Python/Java/Scala + MS SQL/PostgreSQL/MongoDB ([gulftalent.com](https://www.gulftalent.com/saudi-arabia/jobs/data-engineering-specialist-446339)).
- **Certs in KSA:** no Saudi posting found explicitly requiring AWS/Databricks/Snowflake certs — same pattern as globally (preferred, tie-breaker). AWS SAA won't be a screening filter, but AWS-stack fluency will be. **[thin evidence — absence of data, not proof]**
- **Experience bar is high:** Gulf postings skew senior (5–10 yrs common); recruiter commentary notes SDAIA, NEOM Tech, STC, SNB, Aramco Digital source via LinkedIn KSA with Vision-2030/regulatory vocabulary; Arabic helps for government-data roles but technical work is English ([nucamp](https://www.nucamp.co/blog/coding-bootcamp-saudi-arabia-sau-top-10-tech-companies-to-work-for-in-saudi-arabia-in-2025)). Public stack details for Tamara/Tabby/stc pay/Lean DE roles were **not** findable — their career pages need direct monitoring. **[explicit gap]**

---

## (c) Junior vs mid-level expectations

- **Junior (0–2 yrs):** assist on pipelines under guidance; Python + SQL + one cloud + one orchestrator. Only ~2% of postings target 0–2 yrs ([365DS](https://365datascience.com/career-advice/data-engineer-job-outlook-2025/)) — transitions typically land at the 2–4 yr band by leveraging adjacent experience.
- **Mid (2–6 yrs, the fattest band):** own end-to-end pipelines; orchestration, cloud warehouse, CI/CD, data quality; explain *why*, not just *how* ([careery roadmap](https://careery.pro/blog/data-engineer-careers/data-engineer-roadmap), [doit.software JD templates](https://doit.software/blog/data-engineer-job-description)).
- **Portfolio signals hiring managers score** ([Data Engineer Academy 2026 checklist](https://dataengineeracademy.com/blog/data-engineer-portfolio-review-checklist-2026-what-hiring-managers-actually-score/)) **[anecdotal but consistent across sources]**: real business problem (not Titanic/Kaggle); messy/large data; multi-tool end-to-end (e.g., Kafka + Spark + Snowflake + Streamlit); clean modular code with error handling/logging; README + architecture diagram; automation/scheduling. Key stat repeated across sources: **fewer than 1 in 10 junior candidates submit any portfolio** — having one is itself a differentiator. 2–3 deep projects beat 10 shallow ones. Zach Wilson adds: include a frontend/BI layer so pipelines are demonstrable, document DQ checks and run cadence, have something *running in production* ([dataexpert.io roadmap](https://blog.dataexpert.io/p/the-2025-breaking-into-data-engineering-roadmap)).
- **Senior separators:** idempotency, retries/dead-letter queues, backpressure, cost-vs-latency trade-offs, system-design narrative ([The Data Forge](https://thedataforge.medium.com/how-to-build-a-senior-level-data-engineering-portfolio-2026-version-56f045146acc)) — worth seeding at month 9–12 even if targeting mid.

---

## (d) AI impact on DE postings

- LLM-engineering skills in **DE** postings jumped **~3% → ~12%** between late 2025 and early 2026, and ~45% of data/analytics roles now mention AI expertise ([recruiter.daily.dev](https://recruiter.daily.dev/resources/hire-data-engineers-analytics-talent/)) **[directional — single source]**.
- The shift is toward **unstructured-data pipelines feeding retrieval systems** (docs, transcripts, PDFs → embeddings/vector stores) and "context engineering" ([sartechlabs](https://www.sartechlabs.com/blog/the-data-engineers-role-in-ai-skills-infrastructure-and-career-path-for-2026), [Medium: DE role in 2026](https://alper-korukcu.medium.com/the-data-engineer-role-in-2026-whats-actually-changing-and-what-s-just-noise-6eeeddd809b9)).
- RAG/vector numbers like "35.9% of postings" apply to **AI-engineer** roles, not DE ([supercareer.co](https://www.supercareer.co/blog/rag-skills-vector-database-ai-career)) — don't over-index.
- 80% of practitioners use AI daily in workflows; LLMs compress ETL boilerplate 60–70% (dbt Labs State of Analytics Engineering 2025, [via jobstrack](https://jobstrack.io/blog/roles/data-engineer)) — AI-assisted development is assumed, and core DE fundamentals matter *more* because boilerplate is cheap.
- Verdict: for DE roles AI skills are a fast-growing **minority requirement (~10–15%)** — a differentiator module, not the spine.

---

## (e) Framework weighting implications

1. **SQL + Python are non-negotiable co-#1s (~70–94% of postings)** — weight them as the permanent spine of all 12 months, not an early module to "finish."
2. **Stay AWS-first; don't switch to Azure.** AWS leads global DE postings (40.3% vs 34.3% Azure), Bayt shows heavy AWS-tagged DE volume in KSA, and AWS's $5.3B in-Kingdom region lands in 2026 — timing favors AWS skills in Saudi. Hedge with a light Azure-literacy unit (ADF/Synapse vocabulary, ~1–2 weeks) because Saudi government/enterprise leans Microsoft.
3. **Weight Spark/Databricks above Snowflake for the Saudi-first path.** Globally Snowflake edges Databricks (29.2% vs 16.8%), but Gulf postings conspicuously pair Databricks + PySpark, and Spark (38.7–43%) transfers to both. Teach Spark deeply via Databricks (medallion, Delta, Unity Catalog); cover Snowflake at working-knowledge level for the remote-global fallback.
4. **Airflow is the only orchestrator worth deep investment** — #1 in every source (15.8% general sample; 58% modern-stack sample); mention Dagster/Prefect in passing only.
5. **Give dbt a real module but not a pillar.** The 61% figure is modern-stack/vendor-skewed; the general Glassdoor sample barely registers it. Cheap to learn, high-signal in portfolios, dominant in the remote-global analytics-engineering segment — strong effort-to-value at ~3–4 weeks.
6. **Kafka/streaming deserves a full module (~month 7–8):** 24–31% of postings, fastest-growing architectural axis (batch+streaming enterprises 41%→67%), and Aramco explicitly lists Kafka/Flink. Kafka first, Flink as an elective.
7. **Treat Iceberg as concepts-week, not a pillar:** the lakehouse *architecture* is now assumed knowledge, but Iceberg the keyword barely appears in postings and even declined in UK data. Delta Lake via Databricks covers the concept with more market surface.
8. **Add a capstone-grade AI-data module (month 10–11):** unstructured-data ingestion → chunking/embedding → vector store (pgvector lowest-friction) → RAG evaluation. ~12% of DE postings and climbing — a differentiator that compounds in the Gulf (Vision-2030 AI spending). Don't let it displace fundamentals.
9. **Bake in governance/data-quality early:** Aramco and Gulf enterprise postings name governance, metadata, and DQ frameworks explicitly (SAMA/NCA regulatory context makes this a Saudi-specific differentiator vs generic global curricula).
10. **Weight portfolio over certifications:** certs appear in only ~4% of postings (AWS certs the most-cited); fewer than 10% of junior candidates show any portfolio. Target 2–3 production-style end-to-end projects (orchestrated, tested, documented, with a visible BI/frontend layer, one with streaming, one with an AI/RAG element) and aim the resume at the 2–4-year band, since 0–2-year postings are ~2% of the market.

**Evidence caveats:** no quantified skills scrape exists for KSA specifically — Saudi conclusions are assembled from board listings and a handful of postings; fintech (Tamara/Tabby/stc pay/Lean) stack data was not publicly findable and should be verified against their career pages directly; the dbt 61% and LLM-in-DE 12% figures each rest on a single, potentially biased source.
