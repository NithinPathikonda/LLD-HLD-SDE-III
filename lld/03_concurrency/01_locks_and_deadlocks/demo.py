"""
Concurrency Drill 1: Locks, Race Conditions, and Deadlock Avoidance
SDE-III Focus:
1. Race Condition Demonstration & Fix via Mutex (threading.Lock).
2. Deadlock Hazard (Circular Wait) & Solution via Global Lock Ordering.
3. Reentrant Locks (threading.RLock) for Recursive/Nested Critical Sections.
"""

from __future__ import annotations
import threading
import time
from typing import List


# ==============================================================================
# 1. RACE CONDITION & MUTEX FIX
# ==============================================================================

class UnsafeCounter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        current = self.value
        time.sleep(0.0001)  # Simulate context switch
        self.value = current + 1


class ThreadSafeCounter:
    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    def increment(self) -> None:
        with self._lock:
            current = self.value
            time.sleep(0.0001)
            self.value = current + 1


# ==============================================================================
# 2. DEADLOCK PREVENTION VIA GLOBAL RESOURCE ORDERING
# ==============================================================================

class BankAccount:
    def __init__(self, account_id: int, balance: int) -> None:
        self.id = account_id
        self.balance = balance
        self.lock = threading.Lock()


def safe_transfer(from_acc: BankAccount, to_acc: BankAccount, amount: int) -> None:
    """Enforces strict global lock ordering to eliminate Circular Wait (Coffman condition)."""
    first_lock = from_acc.lock if from_acc.id < to_acc.id else to_acc.lock
    second_lock = to_acc.lock if from_acc.id < to_acc.id else from_acc.lock

    with first_lock:
        with second_lock:
            if from_acc.balance >= amount:
                from_acc.balance -= amount
                to_acc.balance += amount
                print(f"[Transfer Safe] {amount} from Acc-{from_acc.id} to Acc-{to_acc.id}")


# ==============================================================================
# 3. REENTRANT LOCK (RLOCK)
# ==============================================================================

class ReentrantDataStore:
    """RLock allows the same thread to acquire the lock multiple times without self-deadlocking."""
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._data: dict[str, str] = {}

    def set_value(self, key: str, value: str) -> None:
        with self._lock:
            self._data[key] = value

    def set_multiple(self, items: dict[str, str]) -> None:
        with self._lock:  # First lock acquisition
            for k, v in items.items():
                self.set_value(k, v)  # Reentrant acquisition by same thread!


if __name__ == "__main__":
    print("--- 1. Testing Thread-Safe Counter ---")
    safe_counter = ThreadSafeCounter()
    threads: List[threading.Thread] = []
    for _ in range(20):
        t = threading.Thread(target=safe_counter.increment)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Safe Counter Value: {safe_counter.value} (Expected: 20)")
    assert safe_counter.value == 20

    print("\n--- 2. Testing Deadlock-Free Concurrent Transfers ---")
    acc1 = BankAccount(1, 1000)
    acc2 = BankAccount(2, 1000)

    # Concurrently transfer in opposite directions
    t1 = threading.Thread(target=safe_transfer, args=(acc1, acc2, 100))
    t2 = threading.Thread(target=safe_transfer, args=(acc2, acc1, 50))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(f"Acc-1 Balance: {acc1.balance} | Acc-2 Balance: {acc2.balance}")
    assert acc1.balance + acc2.balance == 2000

    print("\n--- 3. Testing RLock Data Store ---")
    store = ReentrantDataStore()
    store.set_multiple({"k1": "v1", "k2": "v2"})
    print("RLock passed without self-deadlock!")
