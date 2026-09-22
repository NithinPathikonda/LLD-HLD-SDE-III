# Distributed Rate Limiter (HLD)

## Architectural Blueprint & Mechanics
Centralized Redis Cluster vs Local in-memory with gossip sync. Token bucket with atomic Lua scripts. Handling multi-region latency and clock drift.

## Failure Modes & Edge Cases
- Node crashes during operation
- Split-brain network partitions
- Clock drift / NTP synchronization jumps
- Thundering herd on cache misses
