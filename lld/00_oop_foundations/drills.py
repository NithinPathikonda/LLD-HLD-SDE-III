"""
Day 1: OOP Foundations & Modern Python Typing Drills
Demonstrates SDE-III mental models:
1. Value Objects (@dataclass(frozen=True)) vs Domain Entities.
2. Encapsulation & Invariant enforcement (protecting internal state).
3. Composition over Inheritance (injecting behaviors instead of deep subclassing).
4. Structural Subtyping (typing.Protocol) vs Nominal Subtyping (abc.ABC).
"""

from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol
import uuid


# ==============================================================================
# 1. VALUE OBJECT (Immutable, identified by attributes, no lifecycle)
# ==============================================================================

@dataclass(frozen=True)
class Money:
    """Immutable Value Object for financial amounts to avoid float precision drift."""
    amount: Decimal
    currency: str

    def __post_init__(self) -> None:
        if self.amount < Decimal("0.00"):
            raise ValueError(f"Amount cannot be negative: {self.amount}")
        # Standardize currency to uppercase
        object.__setattr__(self, "currency", self.currency.upper())

    def add(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(
                f"Currency mismatch: Cannot add {self.currency} and {other.currency}"
            )
        return Money(amount=self.amount + other.amount, currency=self.currency)

    def subtract(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(
                f"Currency mismatch: Cannot subtract {self.currency} and {other.currency}"
            )
        if other.amount > self.amount:
            raise ValueError(
                f"Insufficient funds: Cannot subtract {other.amount} from {self.amount}"
            )
        return Money(amount=self.amount - other.amount, currency=self.currency)

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"


# ==============================================================================
# 2. DOMAIN ENTITY (Has unique identity, mutable state protected by invariants)
# ==============================================================================

class BankAccount:
    """Domain Entity representing a user bank account with strict encapsulation."""

    def __init__(self, owner: str, initial_balance: Money) -> None:
        self._id: str = str(uuid.uuid4())
        self._owner: str = owner
        self._balance: Money = initial_balance

    @property
    def id(self) -> str:
        return self._id

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> Money:
        """Expose balance as read-only value object. Cannot be reassigned externally."""
        return self._balance

    def deposit(self, money: Money) -> None:
        if money.amount <= Decimal("0.00"):
            raise ValueError("Deposit amount must be strictly positive.")
        self._balance = self._balance.add(money)

    def withdraw(self, money: Money) -> None:
        if money.amount <= Decimal("0.00"):
            raise ValueError("Withdrawal amount must be strictly positive.")
        self._balance = self._balance.subtract(money)

    def __repr__(self) -> str:
        return f"BankAccount(id={self._id[:8]}..., owner='{self._owner}', balance={self._balance})"


# ==============================================================================
# 3. COMPOSITION OVER INHERITANCE & TYPING PROTOCOLS (Interfaces)
# ==============================================================================

class NotificationSender(Protocol):
    """Structural interface (duck-typing) for notification channels.
    Any class implementing send(recipient, message) automatically satisfies this!
    """
    def send(self, recipient: str, message: str) -> bool:
        ...


class EmailSender:
    def send(self, recipient: str, message: str) -> bool:
        print(f"[EMAIL] To: {recipient} -> {message}")
        return True


class SMSSender:
    def send(self, recipient: str, message: str) -> bool:
        print(f"[SMS] To: {recipient} -> {message}")
        return True


class AccountService:
    """Demonstrates Dependency Injection: Injects NotificationSender collaborator."""

    def __init__(self, notifier: NotificationSender) -> None:
        self._notifier = notifier

    def transfer(self, source: BankAccount, target: BankAccount, amount: Money) -> None:
        print(f"\n--- Initiating Transfer of {amount} from {source.owner} to {target.owner} ---")
        source.withdraw(amount)
        target.deposit(amount)
        self._notifier.send(
            source.owner,
            f"Transferred {amount} to {target.owner}. New Balance: {source.balance}",
        )
        self._notifier.send(
            target.owner,
            f"Received {amount} from {source.owner}. New Balance: {target.balance}",
        )


# ==============================================================================
# VERIFICATION RUNNER
# ==============================================================================

if __name__ == "__main__":
    print("=== Testing OOP Foundations Drills ===")

    # 1. Test Value Objects
    m1 = Money(Decimal("100.50"), "USD")
    m2 = Money(Decimal("50.25"), "USD")
    m3 = m1.add(m2)
    print(f"Money addition: {m1} + {m2} = {m3}")
    assert m3.amount == Decimal("150.75")

    # 2. Test Account Entity
    alice_acc = BankAccount("Alice", Money(Decimal("500.00"), "USD"))
    bob_acc = BankAccount("Bob", Money(Decimal("100.00"), "USD"))
    print(f"Initialized: {alice_acc}")
    print(f"Initialized: {bob_acc}")

    # 3. Test Service with Dependency Injection
    service = AccountService(notifier=EmailSender())
    service.transfer(alice_acc, bob_acc, Money(Decimal("150.00"), "USD"))

    print("\nState after transfer:")
    print(f"Alice: {alice_acc.balance}")
    print(f"Bob:   {bob_acc.balance}")
    assert alice_acc.balance.amount == Decimal("350.00")
    assert bob_acc.balance.amount == Decimal("250.00")

    # Swap collaborator dynamically (SMS instead of Email)
    sms_service = AccountService(notifier=SMSSender())
    sms_service.transfer(bob_acc, alice_acc, Money(Decimal("50.00"), "USD"))

    print("\nAll OOP foundation checks passed successfully!")
