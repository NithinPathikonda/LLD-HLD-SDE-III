# Object-Oriented Programming (OOP) Foundations in Python

> **For Engineers with 1–3 Years of Experience**: Master the first-principles of OOP in modern Python 3.10+ so you write production-grade, extensible code instead of simple scripting.

---

## 1. The 4 Pillars of OOP (and SDE-III Nuances)

### A. Encapsulation & Information Hiding
- **Definition**: Bundling data with the methods that operate on that data, while restricting direct access to internal state.
- **Python Reality**: Python does not have true `private` keywords.
  - `_variable` (single underscore): Protected convention. Indicates internal usage.
  - `__variable` (double underscore): Name mangling (e.g., `_ClassName__variable`) to avoid inheritance collisions.
- **SDE-III Best Practice**: Use `@property` for getters/setters with validation, or `@dataclass(frozen=True)` for immutable data.

### B. Abstraction
- **Definition**: Exposing only the essential interface to the consumer while hiding complex implementation details.
- **Python Tooling**:
  - `abc.ABC` with `@abstractmethod`: Strict nominal subtyping (subclasses must implement).
  - `typing.Protocol`: Structural subtyping / Duck-typing (if an object has the right method signatures, it satisfies the protocol without explicit inheritance).

### C. Inheritance vs Composition (CRITICAL)
- **The Golden Rule**: **Favor object composition over class inheritance.**
- **The Anti-Pattern**: Deep inheritance trees (`Animal -> Mammal -> Dog -> Labrador`). Changing the base class breaks descendants (Fragile Base Class problem).
- **The SDE-III Pattern**: Inject behavior as a dependency (Strategy pattern). A `Car` *has an* `Engine`, it is not a subclass of `Engine`.

### D. Polymorphism
- **Definition**: The ability of different classes to respond to the same interface or method call in their own specific way.
- **Python Power**: Eliminates `if/elif/else type == ...` blocks. The caller invokes `payment_strategy.pay(amount)`, and the concrete class determines whether it is UPI, CreditCard, or Crypto.

---

## 2. Python-Specific OOP Power Features

### Modern Type Hints (`typing` module)
```python
from typing import List, Dict, Optional, Protocol, Union
from dataclasses import dataclass

# Value Object (Immutable)
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

# Protocol (Interface via structural typing)
class PaymentProcessor(Protocol):
    def process_payment(self, amount: Money) -> bool:
        ...
```

### Essential Dunder (Magic) Methods
| Dunder Method | Purpose | SDE-III Usage |
| :--- | :--- | :--- |
| `__init__` | Object initializer | Dependency injection of collaborators. |
| `__repr__` | Unambiguous string representation | Crucial for debugging and production logging. |
| `__eq__` | Equality comparison | Comparing domain entities by ID rather than memory reference. |
| `__hash__` | Hash value for dictionary keys & sets | Allows value objects to be stored in sets and used as dict keys. |
| `__enter__` / `__exit__` | Context management (`with` statement) | Safe acquisition and release of locks, DB sessions, files. |

---

## 3. Checklist for 2 YoE Engineers
- [ ] Are all classes adhering to Single Responsibility (one clear job)?
- [ ] Are domain entities decoupled from database queries?
- [ ] Are dependencies passed in through `__init__` (Dependency Injection)?
- [ ] Are immutable value objects marked with `@dataclass(frozen=True)`?
- [ ] Are all public method signatures fully typed with Python type hints?
