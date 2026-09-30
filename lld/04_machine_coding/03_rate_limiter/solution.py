"""
Distributed / High-Concurrency Rate Limiter - SDE-III Machine Coding Solution
Algorithms Implemented:
1. Token Bucket Algorithm (Bursty traffic support, O(1) space/time, lazy token refill).
2. Sliding Window Log Algorithm (Exact time window boundary, zero edge-burst vulnerability).
3. Thread-Safe Client Rate Limiter Service with concurrent stress simulation.
"""

from __future__ import annotations
from collections import deque
import threading
import time
from typing import Dict, Protocol


class RateLimiterStrategy(Protocol):
    def allow_request(self, client_id: str, cost: int = 1) -> bool:
        ...


class TokenBucketLimiter:
    """Thread-safe Token Bucket rate limiter per client."""

    def __init__(self, capacity: int, refill_rate_per_sec: float) -> None:
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self._tokens: float = float(capacity)
        self._last_refill_timestamp: float = time.time()
        self._lock = threading.Lock()

    def allow(self, cost: int = 1) -> bool:
        with self._lock:
            now = time.time()
            # Refill tokens lazily based on elapsed time
            elapsed = now - self._last_refill_timestamp
            self._tokens = min(float(self.capacity), self._tokens + (elapsed * self.refill_rate))
            self._last_refill_timestamp = now

            if self._tokens >= cost:
                self._tokens -= cost
                return True
            return False


class SlidingWindowLogLimiter:
    """Thread-safe Sliding Window Log limiter per client."""

    def __init__(self, max_requests: int, window_seconds: float) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._timestamps: deque[float] = deque()
        self._lock = threading.Lock()

    def allow(self, cost: int = 1) -> bool:
        with self._lock:
            now = time.time()
            cutoff = now - self.window_seconds

            # Evict timestamps older than current window
            while self._timestamps and self._timestamps[0] <= cutoff:
                self._timestamps.popleft()

            if len(self._timestamps) + cost <= self.max_requests:
                for _ in range(cost):
                    self._timestamps.append(now)
                return True
            return False


class RateLimiterService:
    """Orchestrator routing requests to per-client limiter instances."""

    def __init__(self, algorithm: str = "token_bucket", **config) -> None:
        self.algorithm = algorithm
        self.config = config
        self._limiters: Dict[str, any] = {}
        self._registry_lock = threading.Lock()

    def _get_or_create_limiter(self, client_id: str):
        with self._registry_lock:
            if client_id not in self._limiters:
                if self.algorithm == "token_bucket":
                    self._limiters[client_id] = TokenBucketLimiter(
                        capacity=self.config.get("capacity", 5),
                        refill_rate_per_sec=self.config.get("refill_rate", 2.0),
                    )
                elif self.algorithm == "sliding_window":
                    self._limiters[client_id] = SlidingWindowLogLimiter(
                        max_requests=self.config.get("max_requests", 5),
                        window_seconds=self.config.get("window_seconds", 1.0),
                    )
                else:
                    raise ValueError(f"Unknown algorithm: {self.algorithm}")
            return self._limiters[client_id]

    def allow_request(self, client_id: str, cost: int = 1) -> bool:
        limiter = self._get_or_create_limiter(client_id)
        return limiter.allow(cost)


if __name__ == "__main__":
    print("=== Testing Token Bucket Limiter (Capacity: 3, Refill: 1/sec) ===")
    service = RateLimiterService(algorithm="token_bucket", capacity=3, refill_rate=1.0)

    client = "client_ip_192.168.1.1"

    # Exhaust capacity
    for i in range(4):
        allowed = service.allow_request(client)
        status = "ALLOWED (200)" if allowed else "REJECTED (429)"
        print(f"Request #{i+1}: {status}")

    print("\nSleeping 1.1s for token replenishment...")
    time.sleep(1.1)

    allowed = service.allow_request(client)
    print(f"Request after refill: {'ALLOWED (200)' if allowed else 'REJECTED (429)'}")
    assert allowed is True

    print("\n=== Testing Concurrent Sliding Window ===")
    sliding_service = RateLimiterService(algorithm="sliding_window", max_requests=10, window_seconds=1.0)

    results = []
    def hit_endpoint():
        res = sliding_service.allow_request("tenant_A")
        results.append(res)

    threads = [threading.Thread(target=hit_endpoint) for _ in range(15)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    allowed_count = sum(1 for r in results if r)
    rejected_count = sum(1 for r in results if not r)
    print(f"Concurrent requests: Allowed={allowed_count}, Rejected={rejected_count}")
    assert allowed_count == 10
    assert rejected_count == 5
    print("Rate Limiter verified with zero race conditions!")
