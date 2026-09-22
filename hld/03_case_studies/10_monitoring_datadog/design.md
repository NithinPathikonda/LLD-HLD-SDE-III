# System Design Architecture: Design Distributed Metrics Monitoring (Datadog / Prometheus)

## 1. Requirements & Scope
- **Scale**: Ingest 10 Million metric data points per second across 100,000 servers.
- **Latency**: Real-time query dashboard latency < 500ms for p95.
- **Data Durability**: High availability, long-term retention via downsampling.

---

## 2. Scale & Back-of-the-Envelope Estimation
- **Ingestion Volume**: 10M metrics/sec * 16 bytes (metric_id 8B, timestamp 4B, value 4B) ≈ 160 MB/sec ingestion write bandwidth.
- **Storage Daily**: 160 MB/s * 86,400s ≈ 13.8 TB/day raw uncompressed metrics.
- **Compression**: Time-series delta-of-delta and Gorilla/XOR compression reduces size by ~10x to ~1.4 TB/day.

---

## 3. High-Level System Architecture
```mermaid
graph TD
    Agent[Host Monitoring Daemon / StatsD] --> Gateway[Metrics Ingestion Gateway]
    Gateway --> Kafka[Kafka Metrics Topic]
    Kafka --> IngestionEngine[Ingestion & Compaction Workers]
    IngestionEngine --> TSDB[(Distributed TSDB - ClickHouse / VictoriaMetrics)]
    IngestionEngine --> Cache[(Hot Memory Cache - Redis)]
    AlertEngine[Alert Rule Evaluator] --> Cache
    AlertEngine --> PagerDuty[Alert Dispatcher (Slack / PagerDuty)]
    Dashboard[Grafana / UI Dashboard] --> QueryService[Distributed Query Engine]
    QueryService --> TSDB
```

---

## 4. SDE-III Deep Dives & Bottlenecks
### Gorilla Time-Series Compression Algorithm
- Facebook's Gorilla paper algorithm:
  - **Timestamps**: Most points arrive at regular intervals (e.g. every 10s). Store the *delta-of-deltas* using variable bit lengths (often 1 bit if interval is identical).
  - **Float Values**: XOR the current float with the previous float. Most floats share identical leading and trailing zero bits. Achieves 1.37 bytes per metric point.

### Rollups & Downsampling Lifecycle
- Raw 1-second resolution retained for 7 days.
- Rollup to 1-minute averages/max/p99 retained for 30 days.
- Rollup to 1-hour resolution retained for 1 year.
- Performed asynchronously via LSM-tree style compaction passes in ClickHouse.
