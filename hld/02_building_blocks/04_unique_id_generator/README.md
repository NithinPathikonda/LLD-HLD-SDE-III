# Distributed 64-bit Unique ID Generator

## Architectural Blueprint & Mechanics
Twitter Snowflake ID breakdown: 1 bit sign, 41 bit timestamp, 10 bit worker ID, 12 bit sequence number. NTP clock backward jump handling. UUIDv4 vs UUIDv7 comparison.

## Failure Modes & Edge Cases
- Node crashes during operation
- Split-brain network partitions
- Clock drift / NTP synchronization jumps
- Thundering herd on cache misses
