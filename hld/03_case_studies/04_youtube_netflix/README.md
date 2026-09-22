# System Design: Design Video Streaming Service (YouTube / Netflix)

## 1. Scale & Back-of-the-Envelope
- **Traffic / Volume**: 2 Billion active users, 500 hours of video uploaded every minute.

## 2. SDE-III Deep-Dive & Architecture Focus
Asynchronous DAG video transcoding pipeline. Adaptive Bitrate Streaming (HLS / MPEG-DASH). Multi-tier edge CDN caching, origin shielding, and blob storage.

## 3. 45-Minute Interview Progression
Follow `templates/hld_framework.md`:
1. Scope & Requirements (Functional & Non-Functional)
2. Capacity & Estimation
3. API Contracts & Database Schema
4. High-Level Component Architecture
5. Deep Dives, Bottlenecks, and Fault Tolerance
