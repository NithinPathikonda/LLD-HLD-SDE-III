# Interface Segregation Principle (ISP)

## Core Concept
Clients should not be forced to depend upon interfaces that they do not use.

## SDE-III Anti-Pattern to Avoid
> [!WARNING]
> A monolithic `Worker` interface forcing `HumanWorker` and `RobotWorker` to both implement `eat()` and `sleep()`.

## SDE-III Production Design Pattern
> [!TIP]
> Use small, focused `typing.Protocol` or lean ABCs.

## Practice Exercise
Implement a Python solution demonstrating:
1. `bad_example.py` highlighting the violation.
2. `good_example.py` refactored using clean abstractions and modern type hints.
