# System Design: Design Distributed Web Crawler

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 1 Billion web pages/month, 400 pages/second continuous throughput.

## 2. SDE-III Deep-Dive & Architecture Focus
Distributed URL Frontier with Politeness & Priority queues. Duplicate URL & content detection via Bloom Filters and MinHash. DNS caching & robot.txt compliance.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
