# Distributed Locking (Redlock vs ZooKeeper)

## Architectural Blueprint & Mechanics
Redlock algorithm and Martin Kleppmann's critique. Clock drift, GC pauses, and safety violations. Fencing tokens (monotonically increasing counter) to protect storage integrity.

## Failure Modes & Edge Cases
- Node crashes during operation
- Split-brain network partitions
- Clock drift / NTP synchronization jumps
- Thundering herd on cache misses
