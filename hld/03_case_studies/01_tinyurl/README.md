# System Design: Design URL Shortener (TinyURL / Bitly)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 100M new URLs/month, 100:1 Read-to-Write ratio, 10B redirects/month.

## 2. SDE-III Deep-Dive & Architecture Focus
Base62 encoding vs MD5 hash collision handling. Pre-generated Token Service. 301 Permanent Redirect (client caches) vs 302 Found (server tracks metrics). Cache sizing.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
