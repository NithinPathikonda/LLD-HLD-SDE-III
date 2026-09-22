# Distributed Cache Architecture

## Architectural Blueprint & Mechanics
Consistent Hashing Ring with Virtual Nodes (e.g. 256 virtual nodes/physical node). Data replication across successor nodes. Eviction policies (LRU/LFU). Cluster membership with Gossip protocol.

## Failure Modes & Edge Cases
- Node crashes during operation
- Split-brain network partitions
- Clock drift / NTP synchronization jumps
- Thundering herd on cache misses
