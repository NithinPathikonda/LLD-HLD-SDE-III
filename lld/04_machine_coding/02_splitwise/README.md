# Machine Coding: Splitwise / Expense Sharing System
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Users can add expenses and split with other group members.
- Support EQUAL, EXACT, and PERCENTAGE split types.
- View balances (who owes whom how much).

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Validation: Percentage split must equal 100%, exact amounts must equal total.
- Debt simplification graph algorithm to minimize number of transactions.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
