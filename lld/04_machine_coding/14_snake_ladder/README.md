# Machine Coding: Snake and Ladder Game
**Difficulty**: `Medium` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Configurable board (e.g., 100 cells) with customizable snakes and ladders.
- N players take turns rolling a dice.
- First player reaching exact cell 100 wins.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Strategy Pattern for Dice (Normal 1-6, Crooked even-only, Multi-dice).
- Cycle detection preventing infinite loops during board configuration.

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
