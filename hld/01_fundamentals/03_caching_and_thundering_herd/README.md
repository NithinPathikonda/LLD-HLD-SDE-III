# Caching Strategies & Cache Stampede Prevention

## Key Concepts & Interview Focus
Cache-Aside, Read-Through, Write-Through, Write-Behind (Write-Back). Thundering Herd problem, Cache Stampede, Mutex locking vs Probabilistic Early Expiration (XFetch algorithm).

## SDE-III Bar Raiser Questions
1. How do you defend your choice between consistency and latency when network health is normal?
2. What are the operational pitfalls when adding nodes or re-sharding?
3. How do you mitigate cascading failures in dependent downstream services?
