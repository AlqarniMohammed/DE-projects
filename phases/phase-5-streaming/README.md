# Phase 5 — Streaming & CDC

**Duration:** months 9–10 · **Budget:** ~65 hours · **AWS cost:** near-$0 — Kafka runs locally (Redpanda/KRaft Docker); the platform's AWS bill stays at its P4 baseline

Now you learn Kafka and open-source CDC — the transferable mechanics behind every streaming stack. You already ingested streams the AWS way (Kinesis, P4); the big deliverable here: compare **Debezium and DMS** using your own measurements, on the same workload.

## Objectives

1. Kafka fundamentals in the **4.x KRaft world**: topics, partitions, consumer groups, offsets, delivery guarantees.
2. Open-source CDC: Debezium → Kafka → Iceberg, including schema changes mid-stream and tombstones.
3. Event-time vs processing-time and watermarks — the concept that separates streaming engineers from batch engineers (one Flink SQL lab, semantics-level).
4. Idempotent stream-to-lakehouse writes (at-least-once delivery + idempotent sink = effectively exactly-once).

## New terminology → [GLOSSARY.md](../../GLOSSARY.md) `[P5]`

Kafka · topic/partition/offset/consumer group · Redpanda · Kafka Connect · Debezium · delivery guarantees · event time vs processing time · watermark · Flink · tombstone · outbox pattern · diskless streaming.

## Learn (~20 h)

Every resource is **pinned** to an exercise — nothing here is learn-only.

| Resource | Scope | Hours | Pinned by |
|---|---|---|---|
| [Confluent Developer: Kafka 101 + Connect 101](https://developer.confluent.io/courses/) — free, KRaft-era | Both courses + the free **[Data Streaming Engineer Foundations certificate](https://developer.confluent.io/certificates/data-streaming-engineer/)** ($0 exam + badge) | 8 | Build step 1 (produce/consume, kill-a-consumer drill) + the certificate exam |
| [Conduktor Kafkademy](https://www.conduktor.io/kafka) | Reference reading alongside | 2 | Same drills — it's the second-source cross-check |
| [Debezium docs](https://debezium.io/documentation/) — Postgres connector + tutorial | Working level | 4 | Satellite S5: the CDC showdown |
| [Confluent Apache Flink 101](https://developer.confluent.io/courses/apache-flink/intro/) — Flink-SQL-focused | Full (semantics: windows, watermarks) | 5 | The Flink SQL lab (windows + watermark note) |
| Reading: diskless streaming (WarpStream-style) + Confluent Tableflow | Concept notes — where streaming-to-lakehouse is heading | 1 | Half-page concept note in `notes/` + one written `SELF-CHECK.md` answer |

*Before starting, re-verify:* Kafka/Redpanda current majors, the Confluent course lineup and the free certificate's availability, PyIceberg upsert support status.

*Avoid:* apache/flink-training (stale, Flink 1.17) and any Kafka tutorial teaching ZooKeeper ops (pre-2025, obsolete).

## Build — Platform v3: the event path (~20 h)

1. **Local Kafka:** Redpanda (single binary) or Kafka 4.x KRaft via Docker Compose. Produce/consume with Python (`confluent-kafka`): a producer replaying your GBFS/taxi events into a topic; two consumer groups doing different jobs — *feel* partition ownership and offsets by killing/restarting consumers mid-stream.
2. **Stream → lakehouse (this is also the prove-it, below):** a consumer that batches events into Iceberg. **A plain Iceberg append cannot dedup** — start the drill by proving that: send duplicates through a naive append and watch them land twice. Then make the sink idempotent with **PyIceberg `upsert()` on the event key** (or overwrite-by-batch-partition for larger batches — note the row-level cost trade-off), send the duplicates again, and prove the table stays correct. **Sink target (decided up front so it doesn't cost you an evening mid-phase):** the local consumer writes to the *AWS-side* curated table via **PyIceberg against the Glue/S3 Tables REST catalog**, authenticating with the `de-framework` profile — local compute, cloud table. That is what makes the gate's "event → visible in Athena in minutes" demo real; configuring the catalog endpoint + credentials path is part of the lesson, not friction to route around.
3. **Semantics drill:** replay events out of order; implement a small event-time window aggregation (in your consumer or the Flink lab) and watch late data land; a half-page note in `notes/` on what a watermark bought you.
4. **Airflow tie-in:** the streaming path's health check (lag monitoring: latest offset vs committed offset) as a sensor-style DAG with an alert.

### Prove-it assignment (inside build step 2): the idempotent sink

Duplicates sent on purpose, table provably correct — naive-append failure shown first, then the upsert fix. Recorded as part of the streaming demo. This is the phase's hardest claim made concrete.

## Flink SQL lab (1 day)

From the Confluent course: one tumbling-window + one sliding-window aggregation over your event topic in Flink SQL; note where Flink's watermark syntax makes explicit what your hand-rolled consumer fudged. Semantics-level; deep Flink stays on the skip-list.

**AI rule:** Compose files and producer scaffolding are fair game for your assistant; hand-write the consumer logic, the idempotent sink, and the event-time window — delivery semantics have to live in your head, not your clipboard.

## Build — Satellite S5: Debezium vs DMS — the CDC showdown (~18 h)

Docker Compose: Postgres (`wal_level=logical`) + Debezium (Kafka Connect) + Redpanda + your Iceberg sink consumer. Same seeded OLTP schema and transaction generator you built to spec in P4 (menu of scenario flavors: the S5 section of [`DATASETS.md`](../../reference/DATASETS.md)). **Fair warning that saves you a mid-satellite surprise:** Debezium emits CDC *envelopes* (before/after images, op codes, tombstones) — your P5 sink must be extended to parse them and apply upserts/deletes (PyIceberg upsert, or stage-then-`MERGE` via Athena). Budget 3–4 h for that extension; it is part of the point. Drive identical workloads through both paths and publish `CDC-SHOWDOWN.md`:

- end-to-end latency (histogram, 1-hour run)
- schema-change behavior (add a column mid-stream in both)
- delete handling (tombstones vs DMS delete records)
- ops burden, cost model, failure modes
- **the outbox pattern demonstrated with one table** (write business row + event row in one transaction; CDC ships the event table)
- verdict: when DMS, when Debezium

Nobody publishes honest side-by-side CDC numbers — after this, you have them. Unique briefs: the `/satellite-brief` skill or [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Competency gate G5

- [ ] **Named artifact:** `CDC-SHOWDOWN.md` published with real measured numbers (incl. the outbox demo).
- [ ] Streaming platform demo: event produced → visible in Athena within minutes, narrated on video.
- [ ] Idempotent-sink proof (duplicates sent → naive append fails → upsert holds), shown in the demo.
- [ ] Kill-a-consumer rebalance demo: explain what happened to partitions and offsets.
- [ ] Flink SQL lab done (windows + watermark note in `notes/`).
- [ ] **Data Streaming Engineer Foundations certificate** earned (free).
- [ ] **External critique requested:** `CDC-SHOWDOWN.md` posted to a practitioner community — request thread linked.
- [ ] `SELF-CHECK.md` updated with this phase's written answers.
- [ ] **Retrieval checkpoint:** all `[P5]` terms + 10 random earlier terms, ≥80%.
- [ ] Showdown post published (see below).

## Publish checkpoint

Post (any public platform): the CDC showdown — "I built the same CDC pipeline twice: AWS DMS and Debezium. Here's the honest trade-off matrix nobody publishes," with the latency histogram.

## Check yourself — questions you can now answer

- "Explain consumer groups and what happens when a consumer dies."
- "Exactly-once: what does it really mean end-to-end?"
- "Event time vs processing time — why do watermarks exist?"
- "DMS or Debezium?" (with your own data)
- "How would you replicate 20 operational tables into a lakehouse with minute-level freshness?"

---
← [Phase 4 — Orchestration & Ingestion](../phase-4-orchestration-ingestion/README.md) · [Route map](../../README.md) · [Guide](../../GUIDE.md) · [Progress](../../PROGRESS.md) · **Next: [Phase 6 — Production, Serving & Capstone →](../phase-6-production-serving/README.md)**
