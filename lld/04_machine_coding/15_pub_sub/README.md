# Machine Coding: In-Memory Pub-Sub Messaging Broker
**Difficulty**: `SDE-III Bar Raiser` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Publishers publish messages to named Topics.
- Consumers subscribe to Topics as part of a Consumer Group.
- Messages dispatched to all consumer groups; within a group, load-balanced.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Thread-safe offset tracking per consumer group.
- Non-blocking publish with async subscriber workers.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
