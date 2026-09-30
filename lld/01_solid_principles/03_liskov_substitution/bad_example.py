"""
Liskov Substitution Principle (LSP) - ANTI-PATTERN (VIOLATION)
Subclasses must be substitutable for their base types.
Raising NotImplementedError or violating invariants in a subclass violates LSP.
"""

class Bird:
    def fly(self) -> None:
        print("Flying in the sky!")


class Sparrow(Bird):
    pass


class Penguin(Bird):
    def fly(self) -> None:
        # VIOLATION: Penguin cannot fly, breaks expectations of callers expecting a Bird!
        raise NotImplementedError("Penguins cannot fly!")


def make_bird_fly(bird: Bird) -> None:
    bird.fly()


if __name__ == "__main__":
    make_bird_fly(Sparrow())
    try:
        make_bird_fly(Penguin())
    except NotImplementedError as e:
        print(f"[CRASH] LSP Violation caught: {e}")
