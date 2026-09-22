# System Design: Design Ride-Sharing Platform (Uber / Lyft)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 5M active drivers sending GPS every 4 seconds. Latency < 1s for ride matching.

## 2. SDE-III Deep-Dive & Architecture Focus
Geospatial indexing: Uber H3 (Hexagonal hierarchical) vs Google S2 vs QuadTree. Decoupling location ingestion via Kafka. Localized driver search and matching engine locking.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
