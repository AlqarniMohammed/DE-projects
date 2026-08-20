# Dataset Inventory — Everything the Framework Uses or Offers

Every dataset the default path uses, plus the vetted menu options for satellite variation (see [`prompts/generate-satellite-requirements.md`](prompts/generate-satellite-requirements.md)). Standing rules: datasets never enter git (`data/` is gitignored); re-verify size/availability before a phase starts; **default** marks what the default path uses.

## The spine's datasets (carried across the year)

| Dataset | Used in | Size | Source | Why chosen |
|---|---|---|---|---|
| **NYC TLC yellow-taxi trips** (Parquet, monthly) — *default* | P0 first contact · P1–P6 spine, all layers | ~50–60 MB/month; take 6+ months | [nyc.gov TLC trip records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) | The proven lakehouse teaching dataset: real volume, real warts (fare outliers, late corrections), monthly cadence for incremental/backfill drills, already Parquet |
| **Taxi-zone lookup** (CSV) | P1 spine — the join/enrichment dimension, later the SCD2 snapshot | ~12 KB | Same TLC page | The dimension table: joins, `dim_zones`, SCD2 practice |
| **Weather API** (e.g., Open-Meteo) | P4 spine — the dlt REST source enriching taxi demand | API, incremental | [open-meteo.com](https://open-meteo.com/) | Free, keyless, incremental-cursor-friendly — ideal dlt teaching source |
| **Citi Bike GBFS live feed** | P4 streaming-lite (Lambda→Kinesis) · P5 event replay | Live JSON feed | [GBFS feed](https://gbfs.citibikenyc.com/gbfs/gbfs.json) | A genuinely live public feed for streaming ingest without credentials |
| **Seeded OLTP database** (synthetic bookings app + generator) | P4 DMS CDC · P5 Debezium (same schema both times — that's the point of the showdown) | Generated, small | You build the generator | CDC needs updates *and* deletes you control; synthetic data lets you force schema changes mid-stream |

## Satellite menus (pick one per satellite; the generator prompt also picks from these)

### S1 — First dbt project (P1) — needs 3+ related entities
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **Hacker News dump** — *default* | ~10 GB full; sample fine | [HN BigQuery/Kaggle mirrors](https://console.cloud.google.com/marketplace/product/y-combinator/hacker-news) | Proven; stories/comments/users = natural 3-layer modeling |
| MovieLens 25M | ~250 MB | [grouplens.org](https://grouplens.org/datasets/movielens/25m/) | Clean relational shape: ratings/movies/tags/links |
| Saudi Open Data pick (e.g., commercial registrations by region + activity) | varies | [open.data.gov.sa](https://open.data.gov.sa/) | Regional differentiator; verify entity richness before committing |

### S2 — Cost-aware Athena mart (P2) — needs ~5–10 GB so costs are feelable
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **SEC EDGAR financial statement sets** — *default* | 5–10 GB selectable | [sec.gov EDGAR](https://www.sec.gov/dera/data/financial-statement-data-sets.html) | Quarterly files → partitioning story writes itself |
| NYC 311 service requests | ~20 GB full; slice it | [NYC Open Data](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9) | Wide table → column-pruning cost demos shine |
| Saudi Open Data large extract (tourism/traffic) | varies | [open.data.gov.sa](https://open.data.gov.sa/) | Regional option; confirm size ≥5 GB or union multiple years |

### S3a — Spark forensics (P3) · S3b — Format bake-off (P3)
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **MovieLens 25M** — *S3a default* | ~250 MB | [grouplens.org](https://grouplens.org/datasets/movielens/25m/) | Ratings join is naturally skewed (popular movies) — perfect forensics material |
| IMDb datasets | ~5 GB | [datasets.imdbws.com](https://developer.imdb.com/non-commercial-datasets/) | Alternative skew story via title popularity |
| **NYC taxi months** — *S3b default* | pick 3–6 months | TLC page above | Same-workload fairness: you already know its shape |
| Spotify charts history | ~1–2 GB | [Kaggle mirrors](https://www.kaggle.com/datasets/dhruvildave/spotify-charts) | Daily-update shape also serves the P3 MERGE labs |

### P3 Databricks labs (fresh dataset for daily-MERGE practice)
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **Spotify charts** — *default* | ~1–2 GB | Kaggle link above | Daily grain → MERGE/SCD2 practice |
| IMDb datasets | ~5 GB | Link above | Weekly refresh files work too |

### S4a — Redshift hybrid (P4) · S4b — Dagster comparison (P4)
Both run on **your own spine data** by design (S4a adds one small native table from any menu above); the comparison satellite rebuilds an existing spine pipeline — no new dataset.

### S6a — Serving layer (P6)
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **Your own gold marts** — *default* | — | the spine | The point is the hot-copy pattern, not new data |
| Tadawul (Saudi Exchange) market summaries | small | [saudiexchange.sa](https://www.saudiexchange.sa/) | Regional differentiator for the dashboard/data-product story |
| Umrah/Hajj seasonal statistics | small | [open.data.gov.sa](https://open.data.gov.sa/) | Strong seasonal patterns → genuinely interesting dashboard |

### S6b — AI-data pipeline (P6) — a document corpus
| Dataset | Size | Source | Notes |
|---|---|---|---|
| **AWS what's-new posts** — *default* | small, grows daily | [aws.amazon.com/new](https://aws.amazon.com/new/) (RSS) | Freshness story built in; you already read them |
| arXiv abstracts | selectable slice | [arxiv.org bulk data](https://info.arxiv.org/help/bulk_data/index.html) | Classic RAG corpus, clean metadata |
| Saudi regulations/open-documents corpus | varies | [open.data.gov.sa](https://open.data.gov.sa/) / agency sites | Regional + pairs with the PDPL governance note |

## Practice-question banks (not datasets, but inventoried for completeness)

| Resource | Used in | Source |
|---|---|---|
| LeetCode SQL 50 | P1 gate (≥40 solved) | [leetcode.com](https://leetcode.com/studyplan/top-sql-50/) |
| DataLemur question bank | P1 learn | [datalemur.com](https://datalemur.com/questions) |
| Tutorials Dojo DEA-C01 sets | P2 exam prep | [tutorialsdojo.com](https://portal.tutorialsdojo.com/courses/aws-certified-data-engineer-associate-practice-exam-dea-c01/) |
| Derar Alhussein DBX practice exams | P3 exam prep | Udemy (see [CERTS.md](CERTS.md)) |
