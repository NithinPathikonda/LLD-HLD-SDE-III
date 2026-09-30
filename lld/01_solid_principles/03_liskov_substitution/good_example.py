"""
Liskov Substitution Principle (LSP) - SDE-III REFACTORED
Segregate hierarchies based on true capabilities.
Callers expecting FlyingBird can safely invoke fly() on any instance without surprises.
"""

from typing import Protocol, List


class Bird(Protocol):
    def eat(self) -> None:
        ...


class FlyingBird(Bird, Protocol):
    def fly(self) -> None:
        ...


class SwimmingBird(Bird, Protocol):
    def swim(self) -> None:
        ...


class Eagle:
    def eat(self) -> None:
        print("Eagle is hunting and eating.")

    def fly(self) -> None:
        print("Eagle is soaring high!")


class Penguin:
    def eat(self) -> None:
        print("Penguin is eating fish.")

    def swim(self) -> None:
        print("Penguin is swimming underwater!")


def let_birds_fly(birds: List[FlyingBird]) -> None:
    for b in birds:
        b.fly()


def feed_birds(birds: List[Bird]) -> None:
    for b in birds:
        b.eat()


if __name__ == "__main__":
    eagle = Eagle()
    penguin = Penguin()

    print("--- Feeding all birds (LSP compliant) ---")
    feed_birds([eagle, penguin])

    print("\n--- Flying birds only (LSP strictly preserved) ---")
    let_birds_fly([eagle])
