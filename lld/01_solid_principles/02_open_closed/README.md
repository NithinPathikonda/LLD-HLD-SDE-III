# Open/Closed Principle (OCP)

## Core Concept
Software entities should be open for extension, but closed for modification.

## SDE-III Anti-Pattern to Avoid
> [!WARNING]
> Using if/elif/else chains or match-case to inspect object types when calculating discounts or processing payment methods.

## SDE-III Production Design Pattern
> [!TIP]
> Define an abstract base strategy (`PaymentMethod` / `DiscountPolicy`), allowing new business strategies to be plugged in without modifying existing code.

## Practice Exercise
Implement a Python solution demonstrating:
1. `bad_example.py` highlighting the violation.
2. `good_example.py` refactored using clean abstractions and modern type hints.
