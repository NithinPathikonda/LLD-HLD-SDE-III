# Liskov Substitution Principle (LSP)

## Core Concept
Subtypes must be substitutable for their base types without altering correctness.

## SDE-III Anti-Pattern to Avoid
> [!WARNING]
> Square inheriting from Rectangle and breaking `set_width()`, or ReadOnlyFile inheriting from File and raising `NotImplementedError` on `write()`.

## SDE-III Production Design Pattern
> [!TIP]
> Separate mutable vs immutable interfaces, or use composition over inheritance.

## Practice Exercise
Implement a Python solution demonstrating:
1. `bad_example.py` highlighting the violation.
2. `good_example.py` refactored using clean abstractions and modern type hints.
