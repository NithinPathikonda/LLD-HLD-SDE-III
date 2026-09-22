# System Design: Design Flash Sale System (Amazon / Flipkart)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 1 Million users competing for 1,000 inventory items within 5 seconds.

## 2. SDE-III Deep-Dive & Architecture Focus
Atomic inventory decrement using Redis + Lua script. Virtual waiting room / queue to throttle backend pressure. Async order fulfillment via message queue.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
