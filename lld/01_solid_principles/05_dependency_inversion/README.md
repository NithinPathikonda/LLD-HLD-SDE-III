# Dependency Inversion Principle (DIP)

## Core Concept
High-level modules should not depend on low-level modules; both should depend on abstractions.

## SDE-III Anti-Pattern to Avoid
> [!WARNING]
> `OrderService` directly instantiating concrete `MySQLDatabase` and `StripeClient` inside `__init__`.

## SDE-III Production Design Pattern
> [!TIP]
> Inject `DatabaseInterface` and `PaymentGatewayInterface` into `OrderService` constructor.

## Practice Exercise
Implement a Python solution demonstrating:
1. `bad_example.py` highlighting the violation.
2. `good_example.py` refactored using clean abstractions and modern type hints.
