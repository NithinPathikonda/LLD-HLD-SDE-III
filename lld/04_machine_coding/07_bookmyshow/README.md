# Machine Coding: BookMyShow / Movie Booking System
**Difficulty**: `SDE-III Bar Raiser` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Search shows by cinema, movie, and date.
- Select and temporarily lock seats for 10 minutes during checkout.
- Confirm booking upon payment or release locked seats on timeout/cancellation.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Prevent double booking under high concurrency (concurrency lock on seat ids).
- TTL expiration mechanism for temporary seat locks.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
