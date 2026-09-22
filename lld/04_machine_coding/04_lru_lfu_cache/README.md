# Machine Coding: In-Memory LRU & LFU Cache
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- `get(key)` returns value if present, else None.
- `put(key, value)` inserts or updates key.
- When capacity is reached, evict least recently used (LRU) or least frequently used (LFU) key.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Strict O(1) time complexity for both get and put operations.
- Thread-safe operations using `threading.RLock`.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
