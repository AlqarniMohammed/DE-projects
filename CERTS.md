# Certification Plan — AWS DEA-C01 + Databricks DE Associate

Two cert milestones anchor the **first half** of the year — both passed by ≈ month 7, so the job search starts mid-year with two associate certs and a live platform behind them. Blueprints below were verified against the **official exam guide PDFs** on 2026-08-20 (full report: [`sources/research/certs.md`](sources/research/certs.md)). Both exams revise — **re-check the official exam guide ~6 weeks before booking** (2 weeks is not enough to swap prep material if a new version dropped). Fallback if a revision lands mid-prep: sit the *current* version inside its retirement grace window rather than re-prepping.

> Reality check from the job-market research: certs appear in only ~4% of DE postings — they are tie-breakers and structured-learning devices, not the goal. The portfolio (spine + satellites) is the differentiator. That's why this framework has 2 certs, not 4.

**Why DEA first, and why both in the first half (v1.1 decision):** the SAA substrate (IAM/VPC/S3/KMS ≈ 25% of DEA) is freshest in the framework's early months; Gulf/Saudi hiring cycles run 2–5 months, so the strongest ATS signals need to exist by mid-year, when applications begin; and P2's build *is* the exam's core surface (S3 · Glue · Athena · Lake Formation). The cost of the earlier date — Kinesis/DMS/Redshift not yet operated in depth — is bought down with two short P2 mini-labs plus theory, and P4 then deepens all three hands-on *after* the exam, with no exam pressure attached.

---

## Milestone 1 — AWS Certified Data Engineer – Associate (DEA-C01)

**When:** gate **G2**, end of Phase 2 (≈ end of month 4 – month 5). The P2 build covers Domains 2–4's hands-on surface; Domain 1's streaming/CDC services are covered theory-first (see mitigation below) and operated for real in P4 after the exam.

**Current version: v1.0, live and current** ([official guide PDF](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf)) — launched March 2024, no DEA-C02 announced. Sitting it early also shrinks the revision-risk window.

| Domain | Weight | Framework coverage |
|---|---|---|
| 1. Data Ingestion and Transformation (Kinesis/MSK/DMS streaming vs Glue/EMR/Lambda batch; EventBridge triggers; Spark transforms; orchestration; SQL/Git/CI-CD/IaC concepts) | **34%** | P2 (Glue, Lambda, Kinesis mini-lab; DMS/MSK/EMR theory via course) — deepened hands-on in P4, post-exam |
| 2. Data Store Management (store selection; Redshift + Spectrum; Glue Catalog/crawlers/partitions; S3 lifecycle; **data modeling & schema evolution**) | **26%** | P2 spine + Redshift Serverless taste lab; modeling = existing strength (P4's Redshift satellite deepens it) |
| 3. Data Operations and Support (MWAA/Step Functions automation; Athena/DataBrew/QuickSight; CloudWatch/CloudTrail; Glue Data Quality) | **22%** | P2 (Athena, Glue, CloudWatch basics) + course theory; P6 observability extends it later |
| 4. Data Security and Governance (IAM, VPC, KMS, Lake Formation, Macie, CloudTrail) | **18%** | Largely covered by SAA-C03 knowledge + P2 Lake Formation |

**Logistics:** 65 questions (50 scored) · 130 min · **$150** · pass 720/1000, compensatory · valid 3 years.

**Prep plan (~50–70 h, woven through P2):**
1. **Maarek/Kane Udemy course (already owned)** — still the consensus #1. Both tranches during P2: storage/Glue/Athena/Lake Formation sections alongside the build, then orchestration/streaming/Redshift/security sections in the phase's second half. Skim SAA-overlap at 1.5×.
2. **Domain-1 mitigation labs (in the P2 spec):** a configure-once Kinesis Streams→Firehose→S3 mini-lab and a Redshift Serverless free-credit taste (DISTKEY/SORTKEY, Spectrum concept) — enough operated reality to anchor the exam's "which service/feature" discrimination; the deep builds stay in P4.
3. **Tutorials Dojo (Jon Bonso) practice exams — $14.99, treat as mandatory.** 4 timed + 4 review sets; start 3 weeks before the exam; target ≥80% on timed sets before booking.
4. **AWS Skill Builder** — free DEA-C01 exam-prep plan + official 20-question set; optionally one month of the $29 tier for Builder Labs.
5. **Your P2 spine is the lab for Domains 2–4** — you'll have operated S3/Glue/Athena/S3 Tables/Lake Formation for real before sitting it.

**SAA discount:** Domain 4 and the IAM/VPC/S3/KMS substrate (~25% of the exam) is already yours — and freshest now, months after passing SAA. Passers with your profile report the low end of study time; still the hardest associate — don't go under ~50 h.

---

## Milestone 2 — Databricks Certified Data Engineer Associate

**When:** end of Phase 3 (≈ month 6–7). Validity is 2 years and the exam revises every 6–10 months — check the guide 6 weeks out. Timing bonus: month 6–7 ≈ Feb–Mar 2027, squarely in a plausible **Learning Festival** voucher window (recent windows: Jan and Mar).

**Current version: effective May 4, 2026** ([official guide PDF](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf)). The exam was rewritten July 2025 and again May 2026 — it is now **PySpark-first, Unity-Catalog-everywhere, Lakeflow-branded**. Any prep material centered on DLT syntax, hive_metastore, or SQL-only ELT targets the retired exam.

| Section | Weight | Framework coverage |
|---|---|---|
| 1. Databricks Intelligence Platform (serverless vs clusters, Delta, UC basics) | 6% | P3 learn block |
| 2. Data Ingestion and Loading (COPY INTO, Auto Loader, Lakeflow Connect) | 21% | P3 labs 1–2 |
| 3. Data Transformation and Modeling (PySpark medallion, joins/broadcast, tuning params, MV vs view vs streaming table) | 22% | P3 labs 2–3 + Spark forensics satellite |
| 4. Lakeflow Jobs (task graphs, retries, scheduled vs file-arrival vs table-update triggers) | 16% | P3 lab 4 |
| 5. CI/CD (Git Folders, Asset Bundles, Databricks CLI) | 10% | P3 lab 5 |
| 6. Troubleshooting, Monitoring, Optimization (Spark UI, Liquid Clustering, predictive optimization) | 10% | P3 Spark forensics satellite |
| 7. Governance and Security (UC managed vs external, GRANT/REVOKE, masking, ABAC) | 15% | P3 lab 6 |

**Logistics:** 45 scored questions · 90 min · **$200** · online proctored or test center · valid 2 years · PySpark-primary code items.

**Prep plan (~30–45 h, overlapping with P3 itself):**
1. **Databricks Academy self-paced DE learning path — free** (all self-paced Academy courses are free since June 2025). The exam guide names the exact courses; they're listed in the P3 README.
2. **Databricks Free Edition — free** (Community Edition's successor; serverless + UC by default = exactly the exam's assumed environment). Quotas: 1 active declarative pipeline — enough. Can't practice classic cluster config — cover those concepts from the course.
3. **Derar Alhussein's Udemy course + practice exams** (~$15–20 each on sale; confirmed updated to V4 May 2026 for the new syllabus). Skip his O'Reilly book — it targets the pre-2025 exam.
4. **Voucher:** the recurring **Databricks Learning Festival** grants a **50% cert voucher** for completing one self-paced pathway. Check [community events](https://community.databricks.com/t5/learning-events/databricks-learning-festival-self-paced-global/ev-p/150223) before booking: $200 → $100.
5. **Tailwind from DEA:** the DEA-C01 pass means Spark-on-AWS, lakehouse storage, and CI/CD concepts arrive pre-loaded; P3's new surface is genuinely Databricks-specific (UC, Lakeflow, Delta).

---

## Cost summary

| Item | Cost |
|---|---|
| AWS DEA-C01 exam | $150 |
| Tutorials Dojo practice exams | $15 |
| Maarek/Kane course | owned |
| Skill Builder paid tier (optional, 1 month) | $29 |
| Databricks exam | $200 (→ **$100** with Learning Festival voucher) |
| Derar Alhussein course + practice exams | ~$30–40 on sale |
| **Total certification spend** | **~$295–435** |

## Audit note (for the record)

The old plan targeted a **"dbt Foundational Certificate" — which does not exist**. The real credential is the **dbt Analytics Engineering Certification** ($200, updated May 2026, targets dbt Core v1.11); the free "dbt Fundamentals" course grants a badge, not a cert. Decision: not pursued — dbt skill is demonstrated through the spine's dbt project instead, and the free Fundamentals badge is picked up in Phase 1 anyway.

Also evaluated and skipped (v1.1): the **DeepLearning.AI Data Engineering Specialization** (a course certificate, not an industry credential — duplicates P0–P2 content in watch-only form) and general SQL/PostgreSQL video courses (below the framework's entry bar of strong SQL; DataLemur/LeetCode cover interview SQL). More certificates ≠ more signal at ~4% posting share.
