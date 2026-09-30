"""
Decorator Pattern (Structural) - SDE-III Implementation
Scenario: Decorating a Database Query Service with In-Memory Caching and Metrics Timing.
Allows dynamic extension of behavior without modifying original class.
"""

from __future__ import annotations
import time
from typing import Dict, Protocol


class DataService(Protocol):
    def fetch_data(self, key: str) -> str:
        ...


class SlowDatabaseService:
    """Core concrete component with expensive queries."""
    def fetch_data(self, key: str) -> str:
        time.sleep(0.05)  # Simulate network / I/O latency
        return f"result_for_{key}"


class CachingDecorator:
    """Decorator adding transparent LRU/Dict caching."""
    def __init__(self, wrapped: DataService) -> None:
        self._wrapped = wrapped
        self._cache: Dict[str, str] = {}

    def fetch_data(self, key: str) -> str:
        if key in self._cache:
            print(f"[CACHE HIT] Returning '{key}' from cache.")
            return self._cache[key]
        print(f"[CACHE MISS] Fetching '{key}' from upstream...")
        val = self._wrapped.fetch_data(key)
        self._cache[key] = val
        return val


class MetricsTimingDecorator:
    """Decorator adding execution time metrics."""
    def __init__(self, wrapped: DataService) -> None:
        self._wrapped = wrapped

    def fetch_data(self, key: str) -> str:
        start = time.perf_counter()
        result = self._wrapped.fetch_data(key)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"[METRIC] Query '{key}' took {elapsed_ms:.2f}ms")
        return result


if __name__ == "__main__":
    # Layer decorators: Metrics -> Caching -> Core Database
    core_db = SlowDatabaseService()
    cached_db = CachingDecorator(core_db)
    instrumented_service = MetricsTimingDecorator(cached_db)

    print("--- 1st Call (Miss & Slow) ---")
    instrumented_service.fetch_data("user:101")

    print("\n--- 2nd Call (Hit & Fast) ---")
    instrumented_service.fetch_data("user:101")
