# System Design: Design Distributed Metrics Monitoring (Datadog / Prometheus)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: Millions of metrics data points ingested per second across thousands of servers.

## 2. SDE-III Deep-Dive & Architecture Focus
Time-Series Database (TSDB) storage engine. Downsampling (Rollups) and data retention policies. Alerting rule evaluation engine and Grafana-style dashboard queries.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
