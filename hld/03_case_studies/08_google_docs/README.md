# System Design: Design Collaborative Document Editor (Google Docs)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: Multiple active editors per document, real-time character sync.

## 2. SDE-III Deep-Dive & Architecture Focus
Operational Transformation (OT) vs Conflict-free Replicated Data Types (CRDT). Vector clocks for causal ordering. Offline edit buffer & server reconciliation.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
