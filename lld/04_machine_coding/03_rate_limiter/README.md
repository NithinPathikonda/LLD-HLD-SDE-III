# Machine Coding: Distributed Rate Limiter
**Difficulty**: `SDE-III Bar Raiser` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Rate limit requests per client (by IP or User ID).
- Support Token Bucket, Sliding Window Log, and Leaky Bucket algorithms.
- Return 429 Too Many Requests when limit exceeded.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Zero race conditions under concurrent client calls.
- Low memory footprint and thread-safe sliding window cleanup.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
