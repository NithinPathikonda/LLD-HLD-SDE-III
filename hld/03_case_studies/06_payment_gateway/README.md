# System Design: Design Payment Gateway & Ledger (Stripe-lite)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: Mission critical. 100% financial correctness, 0% double spending.

## 2. SDE-III Deep-Dive & Architecture Focus
Idempotency Keys and distributed locking. Double-entry bookkeeping ledger (Assets = Liabilities + Equity). Saga Pattern for distributed transaction orchestration.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
