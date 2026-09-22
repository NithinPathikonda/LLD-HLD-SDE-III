# SOLID Principles in Python (SDE-III Master Guide)

SOLID principles form the bedrock of clean, maintainable, and extensible object-oriented code. In SDE-III machine coding rounds, failure to follow SOLID is the #1 reason candidates get down-leveled.

---

### The 5 Principles at a Glance

| Principle | Meaning | Typical Python Idiom / Pattern | SDE-III Anti-Pattern to Avoid |
| :--- | :--- | :--- | :--- |
| **S** - Single Responsibility | A class should have only one reason to change. | Separate domain logic from persistence and notification. | A `User` class that saves itself to DB, sends welcome emails, and validates passwords. |
| **O** - Open / Closed | Open for extension, closed for modification. | Use Strategy Pattern, ABC (`from abc import ABC, abstractmethod`), or Polymorphism. | Massive `if/elif/else` or `match/case` blocks checking object types. |
| **L** - Liskov Substitution | Subtypes must be substitutable for their base types. | Adhere to contract signatures; do not raise `NotImplementedError` or weaken preconditions. | `Square` inheriting from `Rectangle` and breaking `set_width()`. |
| **I** - Interface Segregation | Clients should not be forced to depend on interfaces they do not use. | Lean, focused ABCs or `typing.Protocol`. | A giant `Machine` interface requiring `print()`, `fax()`, and `scan()` when simple printers only print. |
| **D** - Dependency Inversion | High-level modules should depend on abstractions, not details. | Inject dependencies (e.g. `PaymentGateway` ABC injected into `CheckoutService`). | Instantiating concrete `StripeGateway()` directly inside `CheckoutService.__init__`. |

---

### Folder Exercises
- `01_single_responsibility/`
- `02_open_closed/`
- `03_liskov_substitution/`
- `04_interface_segregation/`
- `05_dependency_inversion/`
