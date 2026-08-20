# Certification Plan — Databricks DE Associate + AWS DEA-C01

Two cert milestones anchor the year. Blueprints below were verified against the **official exam guide PDFs** on 2026-08-20 (full report: [`sources/research/certs.md`](sources/research/certs.md)). Both exams revise — **re-check the official exam guide ~2 weeks before booking.**

> Reality check from the job-market research: certs appear in only ~4% of DE postings — they are tie-breakers and structured-learning devices, not the goal. The portfolio (spine + satellites) is the differentiator. That's why this framework has 2 certs, not 4.

---

## Milestone 1 — Databricks Certified Data Engineer Associate

**When:** end of Phase 3 (≈ end of month 6 / start of month 7). Take it *early*: validity is 2 years, the exam revises every 6–10 months, and its Spark/medallion content reinforces DEA-C01 later.

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
4. **Voucher:** the recurring **Databricks Learning Festival** grants a **50% cert voucher** for completing one self-paced pathway (recent windows: Jan and Mar 2026 — a window will likely fall inside P3). Check [community events](https://community.databricks.com/t5/learning-events/databricks-learning-festival-self-paced-global/ev-p/150223) before booking: $200 → $100.

---

## Milestone 2 — AWS Certified Data Engineer – Associate (DEA-C01)

**When:** end of Phase 4 / start of Phase 5 (≈ end of month 8 – month 9), immediately after the AWS-native block while Glue/Kinesis/Redshift labs are fresh. Note: Kinesis (exam Domain 1) is deliberately built in P4 so it precedes the exam.

**Current version: v1.0, live and current** ([official guide PDF](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf)) — launched March 2024, no DEA-C02 announced.

| Domain | Weight | Framework coverage |
|---|---|---|
| 1. Data Ingestion and Transformation (Kinesis/MSK/DMS streaming vs Glue/EMR/Lambda batch; EventBridge triggers; Spark transforms; orchestration; SQL/Git/CI-CD/IaC concepts) | **34%** | P2 (Glue/Lambda) + P4 (Kinesis, DMS, Airflow/MWAA, Step Functions) |
| 2. Data Store Management (store selection; Redshift + Spectrum; Glue Catalog/crawlers/partitions; S3 lifecycle; **data modeling & schema evolution**) | **26%** | P2 spine + P4 Redshift satellite; modeling = existing strength |
| 3. Data Operations and Support (MWAA/Step Functions automation; Athena/DataBrew/QuickSight; CloudWatch/CloudTrail; Glue Data Quality) | **22%** | P2 (Athena) + P4 + P6 (observability) |
| 4. Data Security and Governance (IAM, VPC, KMS, Lake Formation, Macie, CloudTrail) | **18%** | Largely covered by SAA-C03 knowledge + P2 Lake Formation |

**Logistics:** 65 questions (50 scored) · 130 min · **$150** · pass 720/1000, compensatory · valid 3 years.

**Prep plan (~50–70 h total; most of it *is* the P2/P4 build):**
1. **Maarek/Kane Udemy course (already owned)** — still the consensus #1. Watch it in two tranches: storage/Glue/Athena sections during P2, orchestration/streaming/Redshift/security sections during P4. Skim SAA-overlap at 1.5×.
2. **Tutorials Dojo (Jon Bonso) practice exams — $14.99, treat as mandatory.** 4 timed + 4 review sets; start 3 weeks before the exam; target ≥80% on timed sets before booking.
3. **AWS Skill Builder** — free DEA-C01 exam-prep plan + official 20-question set; optionally one month of the $29 tier for Builder Labs during P4.
4. **Your own spine is the lab** — the exam is heavy on "which service/feature" discrimination, and you'll have operated most of them for real.

**SAA discount:** Domain 4 and the IAM/VPC/S3/KMS substrate (~25% of the exam) is already yours. Passers with your profile report the low end of study time; still the hardest associate — don't go under ~50 h.

---

## Cost summary

| Item | Cost |
|---|---|
| Databricks exam | $200 (→ **$100** with Learning Festival voucher) |
| Derar Alhussein course + practice exams | ~$30–40 on sale |
| AWS DEA-C01 exam | $150 |
| Tutorials Dojo practice exams | $15 |
| Maarek/Kane course | owned |
| Skill Builder paid tier (optional, 1 month) | $29 |
| **Total certification spend** | **~$295–435** |

## Audit note (for the record)

The old plan targeted a **"dbt Foundational Certificate" — which does not exist**. The real credential is the **dbt Analytics Engineering Certification** ($200, updated May 2026, targets dbt Core v1.11); the free "dbt Fundamentals" course grants a badge, not a cert. Decision: not pursued — dbt skill is demonstrated through the spine's dbt project instead, and the free Fundamentals badge is picked up in Phase 1 anyway.
