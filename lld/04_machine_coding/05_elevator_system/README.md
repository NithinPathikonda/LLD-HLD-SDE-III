# Machine Coding: Elevator Control Dispatcher
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Multiple elevators across multiple floors.
- Internal panel (destination floor) and External panel (Up/Down call).
- Elevator moves, stops at requested floors, opens doors.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Efficient dispatch algorithm (LOOK / SCAN) to minimize wait times.
- State Pattern for elevator states (IDLE, UP, DOWN, MAINTENANCE).

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
