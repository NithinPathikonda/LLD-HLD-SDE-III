# Machine Coding: Logging Framework (Log4j-lite)
**Difficulty**: `Medium` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Support log levels: DEBUG, INFO, WARN, ERROR, FATAL.
- Support log formatting (Timestamp, Thread ID, Level, Message).
- Multiple sinks: Console, File, Network.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Asynchronous queue: `logger.info()` returns immediately without blocking on I/O.
- Chain of Responsibility for log level threshold filtering.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
