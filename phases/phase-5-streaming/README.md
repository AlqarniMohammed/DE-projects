# Phase 5 — Streaming & CDC, Open-Source Edition

**Duration:** months 9–10 · **Budget:** ~65 hours · **AWS cost:** near-$0 — Kafka runs locally (Redpanda/KRaft Docker); the spine's AWS bill stays at its P4 baseline

Streaming fundamentals on the open-source stack the whole industry shares. You already ingested streams the AWS way (Kinesis, P4); now you learn the transferable mechanics — Kafka's model, CDC with Debezium, event-time semantics — and produce the phase's crown jewel: an honest **Debezium vs DMS** comparison, built on your own two implementations.

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
| [Confluent Developer: Kafka 101 + Connect 101](https://developer.confluent.io/courses/) — free, KRaft-era, with **$0 certificates** | Both courses + the free Data Streaming Engineer certificate | 8 | Build step 1 (produce/consume, kill-a-consumer drill) + the course's own assessments |
| [Conduktor Kafkademy](https://www.conduktor.io/kafka) | Reference reading alongside | 2 | Same drills — it's the second-source cross-check |
| [Debezium docs](https://debezium.io/documentation/) — Postgres connector + tutorial | Working level | 4 | Satellite S5: the CDC showdown |
| [Confluent Apache Flink 101](https://developer.confluent.io/courses/apache-flink/intro/) — Flink-SQL-focused | Full (semantics: windows, watermarks) | 5 | The Flink SQL lab (windows + watermark note) |
| Reading: diskless streaming (WarpStream-style) + Confluent Tableflow | Concept notes — where streaming-to-lakehouse is heading | 1 | Half-page concept note + `[P5]` glossary card |

*Avoid:* apache/flink-training (stale, Flink 1.17) and any Kafka tutorial teaching ZooKeeper ops (pre-2025, obsolete).

## Build — Spine v3: the event path (~20 h)

1. **Local Kafka:** Redpanda (single binary) or Kafka 4.x KRaft via Docker Compose. Produce/consume with Python (`confluent-kafka`): a producer replaying your GBFS/taxi events into a topic; two consumer groups doing different jobs — *feel* partition ownership and offsets by killing/restarting consumers mid-stream.
2. **Stream → lakehouse:** a consumer that batches events into Iceberg (append with dedup keys) — build the idempotent-sink pattern by sending duplicates on purpose and proving the table stays correct. **Sink mechanism (decided up front so it doesn't cost you an evening mid-phase):** the local consumer writes to the *AWS-side* curated table via **PyIceberg against the Glue/S3 Tables REST catalog**, authenticating with the `de-framework` profile — local compute, cloud table. That is what makes the gate's "event → visible in Athena in minutes" demo real; configuring the catalog endpoint + credentials path is part of the lesson, not friction to route around.
3. **Semantics drill:** replay events out of order; implement a small event-time window aggregation (in your consumer or the Flink lab) and watch late data land; write a half-page note on what a watermark bought you.
4. **Airflow tie-in:** the streaming path's health check (lag monitoring: latest offset vs committed offset) as a sensor-style DAG with an alert.

**AI rule:** Compose files and producer scaffolding are fair game for Claude Code; hand-write the consumer logic, the idempotent sink, and the event-time window — delivery semantics have to live in your head, not your clipboard.

## Build — Satellite S5: Debezium vs DMS — the CDC showdown (~18 h)

*(Recycled Weeks 18+22, merged into one comparison.)* Docker Compose: Postgres (`wal_level=logical`) + Debezium (Kafka Connect) + Redpanda + your Iceberg sink consumer. Same seeded OLTP schema and transaction generator you used for DMS in P4. Drive identical workloads through both paths and publish `CDC-SHOWDOWN.md`:

- end-to-end latency (histogram, 1-hour run)
- schema-change behavior (add a column mid-stream in both)
- delete handling (tombstones vs DMS delete records)
- ops burden, cost model, failure modes
- verdict: when DMS, when Debezium

One stretch lab: the **outbox pattern** demonstrated with one table. This artifact is the most interview-potent thing in the streaming phase — nobody publishes honest side-by-side CDC numbers. Generated, unique requirements: [`prompts/generate-satellite-requirements.md`](../../prompts/generate-satellite-requirements.md).

## Career track (≤1 h/wk)

Applications continue at **3–5 per month**; you now interview with a CDC comparison nobody else has. Keep logging unanswerable interview questions into `INTERVIEW.md` — they are next-phase curriculum.

## Flink SQL lab (1 day)

From the Confluent course: one tumbling-window + one sliding-window aggregation over your event topic in Flink SQL; note where Flink's watermark syntax makes explicit what your hand-rolled consumer fudged. Semantics-level; deep Flink stays on the skip-list.

## Competency gate G5

- [ ] **Named artifact:** `CDC-SHOWDOWN.md` published with real measured numbers.
- [ ] Streaming spine demo: event produced → visible in Athena within minutes, narrated on video.
- [ ] Kill-a-consumer rebalance demo: explain what happened to partitions and offsets.
- [ ] Confluent's free certificates earned (Kafka 101 at minimum).
- [ ] **External critique requested:** `CDC-SHOWDOWN.md` posted to a practitioner community — request thread linked.
- [ ] Career: ≥3 applications sent this phase · `INTERVIEW.md` updated.
- [ ] **Retrieval checkpoint:** 10 random earlier terms + 15 `[P5]` terms (≥80%).

## Publish checkpoint

Post: the CDC showdown — "I built the same CDC pipeline twice: AWS DMS and Debezium. Here's the honest trade-off matrix nobody publishes," with the latency histogram.

## Interview questions you can now answer

- "Explain consumer groups and what happens when a consumer dies."
- "Exactly-once: what does it really mean end-to-end?"
- "Event time vs processing time — why do watermarks exist?"
- "DMS or Debezium?" (with your own data)
- "How would you replicate 20 operational tables into a lakehouse with minute-level freshness?"
