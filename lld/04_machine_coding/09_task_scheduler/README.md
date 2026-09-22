# Machine Coding: Task Scheduler / Cron Engine
**Difficulty**: `SDE-III Bar Raiser` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Schedule one-off tasks with delay `schedule_after(delay, task)`.
- Schedule recurring cron jobs `schedule_cron(expression, task)`.
- Execute tasks using a pool of worker threads.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Thread-safe PriorityQueue ordered by execution timestamp.
- Workers sleep efficiently using Condition Variable without busy waiting.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
