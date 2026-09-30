"""
Splitwise / Expense Sharing App - SDE-III Machine Coding Solution
Features:
- EQUAL, EXACT, and PERCENTAGE split strategies.
- Real-time balance sheet (who owes whom).
- Graph-based Debt Simplification Algorithm (Min Cash Flow) to minimize transactions.
- Thread-safe balance updates and robust domain validation.
"""

from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto
import threading
from typing import Dict, List, Optional, Protocol, Tuple


# ==============================================================================
# 1. DOMAIN MODELS
# ==============================================================================

@dataclass(frozen=True)
class User:
    user_id: str
    name: str
    email: str


class SplitType(Enum):
    EQUAL = auto()
    EXACT = auto()
    PERCENT = auto()


@dataclass
class Split:
    user: User
    amount: Decimal = Decimal("0.00")
    percent: Decimal = Decimal("0.00")


# ==============================================================================
# 2. STRATEGY PATTERN FOR SPLIT COMPUTATION
# ==============================================================================

class SplitStrategy(Protocol):
    def validate_and_compute(self, total_amount: Decimal, splits: List[Split]) -> None:
        ...


class EqualSplitStrategy:
    def validate_and_compute(self, total_amount: Decimal, splits: List[Split]) -> None:
        if not splits:
            raise ValueError("Splits list cannot be empty.")
        num_users = len(splits)
        base_split = (total_amount / Decimal(num_users)).quantize(Decimal("0.01"))
        remainder = total_amount - (base_split * Decimal(num_users))

        for i, s in enumerate(splits):
            s.amount = base_split
            if i == 0:
                s.amount += remainder  # Adjust rounding pennies to first user


class ExactSplitStrategy:
    def validate_and_compute(self, total_amount: Decimal, splits: List[Split]) -> None:
        total_split = sum((s.amount for s in splits), Decimal("0.00"))
        if total_split != total_amount:
            raise ValueError(f"Split sum ({total_split}) != total amount ({total_amount})")


class PercentSplitStrategy:
    def validate_and_compute(self, total_amount: Decimal, splits: List[Split]) -> None:
        total_pct = sum((s.percent for s in splits), Decimal("0.00"))
        if total_pct != Decimal("100.00"):
            raise ValueError(f"Total percentage ({total_pct}%) must equal 100.00%")

        allocated = Decimal("0.00")
        for i, s in enumerate(splits):
            s.amount = ((s.percent * total_amount) / Decimal("100.00")).quantize(Decimal("0.01"))
            allocated += s.amount

        # Distribute rounding discrepancy
        discrepancy = total_amount - allocated
        if splits:
            splits[0].amount += discrepancy


# ==============================================================================
# 3. EXPENSE & EXPENSE SERVICE
# ==============================================================================

class ExpenseManager:
    def __init__(self) -> None:
        self.users: Dict[str, User] = {}
        # balances[u1][u2] = balance (positive means u2 owes u1, negative means u1 owes u2)
        self.balances: Dict[str, Dict[str, Decimal]] = {}
        self._lock = threading.Lock()

    def add_user(self, user: User) -> None:
        with self._lock:
            self.users[user.user_id] = user
            self.balances[user.user_id] = {}

    def add_expense(
        self,
        paid_by: User,
        total_amount: Decimal,
        splits: List[Split],
        strategy: SplitStrategy,
    ) -> None:
        strategy.validate_and_compute(total_amount, splits)

        with self._lock:
            for split in splits:
                if split.user.user_id == paid_by.user_id:
                    continue  # Payer doesn't owe themselves

                owed = split.amount
                u1 = paid_by.user_id
                u2 = split.user.user_id

                # u2 owes u1: balance from u1's perspective increases
                self.balances[u1][u2] = self.balances[u1].get(u2, Decimal("0.00")) + owed
                # from u2's perspective, it decreases
                self.balances[u2][u1] = self.balances[u2].get(u1, Decimal("0.00")) - owed

    def show_balances(self) -> None:
        with self._lock:
            print("\n--- Current Balances ---")
            has_balances = False
            for u1, debts in self.balances.items():
                for u2, amt in debts.items():
                    if amt > Decimal("0.00"):
                        has_balances = True
                        print(f"{self.users[u2].name} owes {self.users[u1].name}: ${amt:.2f}")
            if not has_balances:
                print("All balances are settled!")

    def simplify_debts(self) -> List[Tuple[str, str, Decimal]]:
        """SDE-III Debt Minimization using Min-Cash-Flow Greedy Algorithm."""
        with self._lock:
            # 1. Compute net balance for each user
            net_balances: Dict[str, Decimal] = {u_id: Decimal("0.00") for u_id in self.users}
            for u1, debts in self.balances.items():
                for u2, amt in debts.items():
                    net_balances[u1] += amt

            debtors: List[Tuple[str, Decimal]] = []
            creditors: List[Tuple[str, Decimal]] = []

            for u_id, net in net_balances.items():
                if net < Decimal("0.00"):
                    debtors.append((u_id, -net))
                elif net > Decimal("0.00"):
                    creditors.append((u_id, net))

            simplified_transactions: List[Tuple[str, str, Decimal]] = []

            i, j = 0, 0
            while i < len(debtors) and j < len(creditors):
                deb_id, deb_amt = debtors[i]
                cred_id, cred_amt = creditors[j]

                settled = min(deb_amt, cred_amt)
                simplified_transactions.append((deb_id, cred_id, settled))

                deb_amt -= settled
                cred_amt -= settled

                if deb_amt == Decimal("0.00"):
                    i += 1
                else:
                    debtors[i] = (deb_id, deb_amt)

                if cred_amt == Decimal("0.00"):
                    j += 1
                else:
                    creditors[j] = (cred_id, cred_amt)

            print("\n--- Simplified Debt Settlements ---")
            for debtor, creditor, amount in simplified_transactions:
                print(f"{self.users[debtor].name} pays {self.users[creditor].name}: ${amount:.2f}")

            return simplified_transactions


if __name__ == "__main__":
    mgr = ExpenseManager()
    u1 = User("u1", "Alice", "alice@test.com")
    u2 = User("u2", "Bob", "bob@test.com")
    u3 = User("u3", "Charlie", "charlie@test.com")

    mgr.add_user(u1)
    mgr.add_user(u2)
    mgr.add_user(u3)

    # 1. Equal Split: Alice pays $300 for Alice, Bob, Charlie ($100 each)
    mgr.add_expense(
        paid_by=u1,
        total_amount=Decimal("300.00"),
        splits=[Split(u1), Split(u2), Split(u3)],
        strategy=EqualSplitStrategy(),
    )

    # 2. Exact Split: Bob pays $150 for Charlie ($150)
    mgr.add_expense(
        paid_by=u2,
        total_amount=Decimal("150.00"),
        splits=[Split(u3, amount=Decimal("150.00"))],
        strategy=ExactSplitStrategy(),
    )

    mgr.show_balances()
    mgr.simplify_debts()
