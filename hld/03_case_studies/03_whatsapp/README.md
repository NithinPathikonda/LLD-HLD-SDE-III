# System Design: Design Real-Time Chat (WhatsApp / Slack)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 2 Billion users, 100 Billion messages/day. Strict delivery guarantees.

## 2. SDE-III Deep-Dive & Architecture Focus
Persistent WebSocket connections, connection gateway routing tables. Message ordering, delivery receipts (Sent, Delivered, Read), offline queue storage in Cassandra.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
