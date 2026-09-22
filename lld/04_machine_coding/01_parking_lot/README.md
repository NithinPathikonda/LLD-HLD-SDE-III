# Machine Coding: Multilevel Parking Lot System
**Difficulty**: `Hard` | **Language**: `Python 3.10+`

---

## 1. Functional Requirements (FR)
- Multi-floor parking lot with different spot types (Compact, Large, Motorcycle, EV).
- Vehicle entry gives ticket with timestamp and allocated spot.
- Vehicle exit calculates fee based on duration and vehicle type.
- Support multiple entry and exit gates.

---

## 2. Non-Functional Requirements (NFR) & SDE-III Bar
- Thread-safe spot allocation under concurrent entry gates.
- Extensible fee calculation strategies (Flat, Hourly, Peak hour).

---

## 3. Recommended Design Patterns
- Strategy Pattern for pluggable policies
- Factory Pattern for object instantiation
- Thread-safe repository / state handling

---

## 4. Starter File
Use `templates/lld_template.py` as your structural blueprint. Implement your solution in `solution.py`.
