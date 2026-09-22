# Producer-Consumer with Condition Variables

## Core Concepts & Interview Focus
- Bounded buffer queue, `threading.Condition` (`wait()`, `notify()`, `notify_all()`), Poison pill shutdown pattern.

## SDE-III Evaluation Standard
- Must identify potential race conditions under concurrent threads.
- Prevent deadlocks by enforcing strict lock ordering.
- Demonstrate non-blocking operations or fine-grained locks over global locks.
