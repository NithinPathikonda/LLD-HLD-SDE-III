# Machine Coding: Vending Machine System
**Difficulty**: `Medium` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Select product by item code.
- Insert coins/cash (1, 5, 10, 20).
- Dispense item and return optimal change.
- Cancel transaction and refund inserted money.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- State Pattern (IdleState, HasMoneyState, DispenseState, SoldOutState).
- Greedy change dispensing algorithm.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
