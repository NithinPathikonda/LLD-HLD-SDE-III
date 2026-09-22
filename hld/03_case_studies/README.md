# SDE-III High-Level Design (HLD) Case Studies

Curated system design case studies tested in Staff / SDE-III loops, categorized by architectural archetype.

---

### System Design Architecture Archetypes

| # | System Design System | Core Architectural Archetype | Key SDE-III Deep-Dive Focus |
|---|---|---|---|
| **01** | [URL Shortener (TinyURL)](./01_tinyurl/) | Read-Heavy Key-Value Store, Base62 | Hash collision avoidance, 301 vs 302 redirect, caching |
| **02** | [Distributed Cache (Redis-lite)](./02_distributed_cache/) | Consistent Hashing, Replication | Virtual nodes, gossip protocol, eviction, thundering herd |
| **03** | [Ride-Sharing Service (Uber / Lyft)](./03_uber/) | Geospatial Indexing (H3 / S2 / QuadTree) | Driver location updates at scale, matching engine latency |
| **04** | [Real-Time Messaging (WhatsApp / Slack)](./04_whatsapp/) | Persistent WebSockets, Message Queues | End-to-end encryption, delivery receipts, offline message queue |
| **05** | [Video Streaming Platform (YouTube / Netflix)](./05_youtube/) | Video Transcoding Pipeline, Multi-tier CDN | Chunked adaptive bitrate streaming, hot video caching |
| **06** | [Distributed Rate Limiter](./06_rate_limiter/) | Token Bucket with Redis Cluster + Lua | Race conditions in distributed count, sliding window memory |
| **07** | [Distributed Message Queue (Kafka-lite)](./07_kafka/) | Append-Only Commit Log, Partitioning | Zero-copy reads, consumer group rebalancing, leader-follower |
| **08** | [Payment Gateway (Stripe / Razorpay)](./08_payment_gateway/) | Distributed Transactions, 2PC / Sagas | Idempotency keys, reconciliation, double-spend prevention |
| **09** | [Web Crawler / Search Engine Indexer](./09_web_crawler/) | Distributed BFS, URL Frontier | Politeness policy, duplicate detection (Bloom filters), scale |
| **10** | [E-Commerce Flash Sale (Amazon / Flipkart)](./10_flash_sale/) | Inventory Lock, Queue Decoupling | High contention concurrency, optimistic locking, redis inventory |
| **11** | [Metrics & Monitoring System (Datadog / Prometheus)](./11_monitoring_system/) | Time-Series Database (TSDB), Downsampling | High-frequency write ingestion, compaction, alerting engine |
| **12** | [Collaborative Document Editing (Google Docs)](./12_google_docs/) | Operational Transformation (OT) / CRDT | Concurrent conflict resolution, vector clocks, offline sync |
