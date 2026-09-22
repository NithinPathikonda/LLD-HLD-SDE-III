# Single Responsibility Principle (SRP)

## Core Concept
A class should have one, and only one, reason to change.

## SDE-III Anti-Pattern to Avoid
> [!WARNING]
> A God class handling user profile data, DB SQL persistence, password hashing, and sending welcome emails.

## SDE-III Production Design Pattern
> [!TIP]
> Decompose into User entity, UserRepository, PasswordHasher, and EmailNotifier. Inject dependencies cleanly.

## Practice Exercise
Implement a Python solution demonstrating:
1. `bad_example.py` highlighting the violation.
2. `good_example.py` refactored using clean abstractions and modern type hints.
