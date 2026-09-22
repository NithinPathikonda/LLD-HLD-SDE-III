# System Design: Design Distributed Append-Only Log (Kafka-lite)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: Millions of events/sec, sub-millisecond produce latency, multi-tenant consumers.

## 2. SDE-III Deep-Dive & Architecture Focus
Log segment index files. Zero-copy read using OS page cache. Controller broker & consensus (ZooKeeper / KRaft). Consumer group rebalance protocol.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
