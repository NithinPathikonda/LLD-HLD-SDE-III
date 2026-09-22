# Thread Safety, Locks & Deadlock Avoidance

## Core Concepts & Interview Focus
- Mutex Locks (`threading.Lock`), Reentrant Locks (`threading.RLock`), Deadlock conditions (Coffman conditions), Resource ordering.

## SDE-III Evaluation Standard
- Must identify potential race conditions under concurrent threads.
- Prevent deadlocks by enforcing strict lock ordering.
- Demonstrate non-blocking operations or fine-grained locks over global locks.
