# Custom Thread Pool & Worker Queues

## Core Concepts & Interview Focus
- Task queue, fixed number of worker threads, `concurrent.futures.ThreadPoolExecutor`, graceful shutdown.

## SDE-III Evaluation Standard
- Must identify potential race conditions under concurrent threads.
- Prevent deadlocks by enforcing strict lock ordering.
- Demonstrate non-blocking operations or fine-grained locks over global locks.
