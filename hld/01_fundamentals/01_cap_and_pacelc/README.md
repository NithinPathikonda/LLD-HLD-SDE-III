# CAP Theorem & PACELC Trade-Offs

## Key Concepts & Interview Focus
Consistency, Availability, Partition Tolerance. Why P cannot be sacrificed in real networks. PACELC theorem (Partition -> A or C; Else -> Latency or Consistency). Quorum reads and writes ($R + W > N$).

## SDE-III Bar Raiser Questions
1. How do you defend your choice between consistency and latency when network health is normal?
2. What are the operational pitfalls when adding nodes or re-sharding?
3. How do you mitigate cascading failures in dependent downstream services?
