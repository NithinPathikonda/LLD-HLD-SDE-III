# Machine Coding: Cricbuzz / Live Score Tracker
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Ball-by-ball commentary and score update.
- Support match types (T20, ODI, Test) and innings state.
- Calculate bowler economy, batsman strike rates, and team totals.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Observer Pattern pushing real-time score events to subscribers.
- State Machine validating legal vs illegal deliveries (No-ball, Wide, Wicket).

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
