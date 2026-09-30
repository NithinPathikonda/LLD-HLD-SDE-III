"""
Concurrency Drill 2: Producer-Consumer with Condition Variables
SDE-III Focus:
1. Thread coordination using threading.Condition.
2. Bounded Blocking Queue implementation from scratch (no queue.Queue).
3. Correct use of `while` loop (not `if`) to guard against Spurious Wakeups.
"""

from __future__ import annotations
import threading
import time
from typing import Generic, List, TypeVar

T = TypeVar("T")


class BoundedBlockingQueue(Generic[T]):
    """Thread-safe bounded queue implemented with a single Condition variable."""
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.capacity = capacity
        self.buffer: List[T] = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def put(self, item: T) -> None:
        with self.condition:
            # While loop to handle spurious wakeups!
            while len(self.buffer) >= self.capacity:
                self.condition.wait()
            self.buffer.append(item)
            # Notify waiting consumers that an item is available
            self.condition.notify()

    def get(self) -> T:
        with self.condition:
            # While loop to handle spurious wakeups!
            while len(self.buffer) == 0:
                self.condition.wait()
            item = self.buffer.pop(0)
            # Notify waiting producers that a slot has freed up
            self.condition.notify()
            return item


def producer(queue: BoundedBlockingQueue[int], count: int) -> None:
    for i in range(count):
        queue.put(i)
        print(f"[Producer] Produced item: {i}")
        time.sleep(0.01)


def consumer(queue: BoundedBlockingQueue[int], count: int, name: str) -> None:
    for _ in range(count):
        item = queue.get()
        print(f"[{name}] Consumed item: {item}")
        time.sleep(0.02)


if __name__ == "__main__":
    print("--- Running Producer-Consumer with Condition Variable ---")
    q: BoundedBlockingQueue[int] = BoundedBlockingQueue(capacity=3)

    p_thread = threading.Thread(target=producer, args=(q, 6))
    c1_thread = threading.Thread(target=consumer, args=(q, 3, "Consumer-1"))
    c2_thread = threading.Thread(target=consumer, args=(q, 3, "Consumer-2"))

    p_thread.start()
    c1_thread.start()
    c2_thread.start()

    p_thread.join()
    c1_thread.join()
    c2_thread.join()
    print("Producer-Consumer completed successfully without deadlock!")
