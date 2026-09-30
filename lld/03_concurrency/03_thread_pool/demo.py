"""
Concurrency Drill 3: Custom Thread Pool & Worker Queue
SDE-III Focus:
1. Thread pool implementation from scratch.
2. Worker lifecycle management & task queuing.
3. Graceful shutdown using Sentinel/Poison Pill values.
"""

from __future__ import annotations
import queue
import threading
import time
from typing import Callable, List, Optional

Task = Callable[[], None]
_SHUTDOWN_SENTINEL = object()


class CustomThreadPool:
    def __init__(self, num_workers: int) -> None:
        self.num_workers = num_workers
        self.task_queue: queue.Queue = queue.Queue()
        self.workers: List[threading.Thread] = []
        self._is_shutdown = False

        for i in range(num_workers):
            worker = threading.Thread(target=self._worker_loop, name=f"Worker-{i+1}")
            worker.start()
            self.workers.append(worker)

    def _worker_loop(self) -> None:
        while True:
            task = self.task_queue.get()
            if task is _SHUTDOWN_SENTINEL:
                self.task_queue.task_done()
                break  # Exit worker thread cleanly
            try:
                task()
            except Exception as e:
                print(f"[{threading.current_thread().name}] Task failed with error: {e}")
            finally:
                self.task_queue.task_done()

    def submit(self, task: Task) -> None:
        if self._is_shutdown:
            raise RuntimeError("Cannot submit tasks to a shut-down pool.")
        self.task_queue.put(task)

    def shutdown(self, wait: bool = True) -> None:
        self._is_shutdown = True
        # Send poison pills to all workers
        for _ in range(self.num_workers):
            self.task_queue.put(_SHUTDOWN_SENTINEL)
        if wait:
            for w in self.workers:
                w.join()


def sample_task(task_id: int) -> None:
    print(f"[{threading.current_thread().name}] Processing Task #{task_id}")
    time.sleep(0.02)


if __name__ == "__main__":
    print("--- Testing Custom Thread Pool ---")
    pool = CustomThreadPool(num_workers=3)

    for i in range(6):
        pool.submit(lambda idx=i: sample_task(idx))

    # Gracefully shut down and join all workers
    pool.shutdown(wait=True)
    print("All tasks processed and thread pool gracefully terminated!")
