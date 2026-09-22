# Distributed Message Queue Architecture

## Architectural Blueprint & Mechanics
Append-only commit log storage. In-Sync Replicas (ISR) and leader election. Zero-copy transfer (`sendfile`). Push vs Pull delivery models. Consumer rebalancing.

## Failure Modes & Edge Cases
- Node crashes during operation
- Split-brain network partitions
- Clock drift / NTP synchronization jumps
- Thundering herd on cache misses
