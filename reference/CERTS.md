# Certification Plan — AWS DEA-C01 + Databricks DE Associate

Two cert milestones anchor the **first half** of the year — both passed by ≈ month 7, while the builds that cover their exam surface are still fresh. Blueprints below were verified against the **official exam guide PDFs** on 2026-08-20 (full report: [`certs.md`](../sources/research/certs.md)). Both exams revise — **re-check the official exam guide ~6 weeks before booking** (2 weeks is not enough to swap prep material if a new version dropped). Fallback if a revision lands mid-prep: sit the *current* version inside its retirement grace window rather than re-prepping.

> Certs are structured-learning devices and tie-breakers, not the goal — the built platform is the differentiator. That's why this framework has 2 certs, not 4 (the reasoning and evidence live in [WHY.md](WHY.md)).

**Why DEA first, and why both in the first half:** the DEA's core exam surface is exactly what Phase 2 builds (S3 · Glue · Athena · Lake Formation), and its cloud-fundamentals substrate (IAM/VPC/S3/KMS ≈ 25% of the exam) matches the framework's entry prerequisites — sitting the exam at gate G2 keeps prep and build perfectly aligned. The cost of the earlier date — Kinesis/DMS/Redshift not yet operated in depth — is bought down with two short P2 mini-labs plus theory, and P4 then deepens all three hands-on *after* the exam, with no exam pressure attached.

---

## Milestone 1 — AWS Certified Data Engineer – Associate (DEA-C01)

**When:** gate **G2**, end of Phase 2 (≈ end of month 4 – month 5). The P2 build covers Domains 2–4's hands-on surface; Domain 1's streaming/CDC services are covered theory-first (see mitigation below) and operated for real in P4 after the exam.

**Current version: v1.0, live and current** ([official guide PDF](https://d1.awsstatic.com/training-and-certification/docs-data-engineer-associate/AWS-Certified-Data-Engineer-Associate_Exam-Guide.pdf)) — launched March 2024, no DEA-C02 announced. Sitting it early also shrinks the revision-risk window.

| Domain | Weight | Framework coverage |
|---|---|---|
| 1. Data Ingestion and Transformation (Kinesis/MSK/DMS streaming vs Glue/EMR/Lambda batch; EventBridge triggers; Spark transforms; orchestration; SQL/Git/CI-CD/IaC concepts) | **34%** | P2 (Glue, Kinesis mini-lab; DMS/MSK/EMR theory via course) — deepened hands-on in P4, post-exam |
| 2. Data Store Management (store selection; Redshift + Spectrum; Glue Catalog/crawlers/partitions; S3 lifecycle; **data modeling & schema evolution**) | **26%** | P2 platform build + Redshift Serverless taste lab; modeling built explicitly in P1 (SCD2 + `MODELING.md`), deepened by P4's Redshift satellite |
| 3. Data Operations and Support (MWAA/Step Functions automation; Athena/DataBrew/QuickSight; CloudWatch/CloudTrail; Glue Data Quality) | **22%** | P2 (Athena, Glue, CloudWatch basics) + course theory; P6 observability extends it later |
| 4. Data Security and Governance (IAM, VPC, KMS, Lake Formation, Macie, CloudTrail) | **18%** | Largely covered by the cloud-fundamentals prerequisite + P2 Lake Formation |

**Logistics:** 65 questions (50 scored) · 130 min · **$150** · pass 720/1000, compensatory · valid 3 years.

**Prep plan (~50–70 h, woven through P2):**
1. **[Maarek/Kane Udemy course](https://www.udemy.com/course/aws-data-engineer/)** (~$15–20 on sale) — still the consensus #1. Both tranches during P2: storage/Glue/Athena/Lake Formation sections alongside the build, then orchestration/streaming/Redshift/security sections in the phase's second half. Skim sections you already know at 1.5×.
2. **Domain-1 mitigation labs (in the P2 spec):** a configure-once Kinesis Streams→Firehose→S3 mini-lab and a Redshift Serverless free-credit taste (DISTKEY/SORTKEY, Spectrum concept) — enough operated reality to anchor the exam's "which service/feature" discrimination; the deep builds stay in P4.
3. **Tutorials Dojo (Jon Bonso) practice exams — $14.99, treat as mandatory.** 4 timed + 4 review sets; start 3 weeks before the exam; target ≥80% on timed sets before booking.
4. **AWS Skill Builder** — free DEA-C01 exam-prep plan + official 20-question set; optionally one month of the $29 tier for Builder Labs.
5. **Your P2 platform is the lab for Domains 2–4** — you'll have operated S3/Glue/Athena/S3 Tables/Lake Formation for real before sitting it.

**Prior-cert discount:** if you already hold an AWS associate-level certification, Domain 4 and the IAM/VPC/S3/KMS substrate (~25% of the exam) will be familiar — expect the low end of the study-time range. Still the hardest associate — don't go under ~50 h.

---

## Milestone 2 — Databricks Certified Data Engineer Associate

**When:** end of Phase 3 (≈ month 6–7). Validity is 2 years and the exam revises every 6–10 months — check the guide 6 weeks out. **Voucher check:** see whether a **Learning Festival** window falls inside your Phase-3 months (recent windows: Jan, Mar, Jun) — plan the Academy pathway inside it if so.

**Current version: effective May 4, 2026** ([official guide PDF](https://www.databricks.com/sites/default/files/2026-05/databricks-certified-data-engineer-associate-exam-guide-may-2026-000.pdf)). The exam was rewritten July 2025 and again May 2026 — it is now **PySpark-first, Unity-Catalog-everywhere, Lakeflow-branded**. Any prep material centered on DLT syntax, hive_metastore, or SQL-only ELT targets the retired exam.

| Section | Weight | Framework coverage |
|---|---|---|
| 1. Databricks Intelligence Platform (serverless vs clusters, Delta, UC basics) | 6% | P3 learn block |
| 2. Data Ingestion and Loading (COPY INTO, Auto Loader, Lakeflow Connect) | 21% | P3 labs 1–2 |
| 3. Data Transformation and Modeling (PySpark medallion, joins/broadcast, tuning params, MV vs view vs streaming table) | 22% | P3 labs 2–3 + Spark forensics satellite |
| 4. Lakeflow Jobs (task graphs, retries, scheduled vs file-arrival vs table-update triggers) | 16% | P3 lab 4 |
| 5. CI/CD (Git Folders, Asset Bundles, Databricks CLI) | 10% | P3 lab 7 |
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
| Maarek/Kane course | ~$15–20 (watch for Udemy sales) |
| Skill Builder paid tier (optional, 1 month) | $29 |
| Databricks exam | $200 (→ **$100** with Learning Festival voucher) |
| Derar Alhussein course + practice exams | ~$30–40 on sale |
| **Total certification spend** | **~$310–455** (low end assumes the voucher) |

## Evaluated and skipped (for the record)

- A **"dbt Foundational Certificate" does not exist** — the real credential is the dbt Analytics Engineering Certification ($200, updated May 2026). Not pursued: dbt skill is demonstrated through the platform's dbt project instead, and the free "dbt Fundamentals" badge is picked up in Phase 1 anyway.
- The **DeepLearning.AI Data Engineering Professional Certificate** — still skipped **as a credential**: a course certificate, not an industry credential, and the framework replaces watch-only learning with pinned exercises. As a *learning resource* it earns a different verdict — Joe Reis lectures with graded AWS labs are the strongest guided-video coverage of P0–P2 territory — so it returns as an optional **video lane** ([COURSES.md](COURSES.md)). Take the courses if video suits you; the certificate PDF is a by-product, never a milestone.
- **General SQL/PostgreSQL video courses** — below the framework's entry bar of strong SQL; DataLemur/LeetCode cover applied SQL practice.
- More certificates ≠ more signal: the two chosen certs are milestones; the platform is the proof.

---
[README](../README.md) · [Guide](../GUIDE.md) · [Why it looks this way](WHY.md)
