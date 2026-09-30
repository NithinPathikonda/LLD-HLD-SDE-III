"""
Open/Closed Principle (OCP) - SDE-III REFACTORED
Open for extension, closed for modification.
New payment methods (e.g. CryptoPayment) can be added without changing PaymentContext!
"""

from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


@dataclass(frozen=True)
class PaymentRequest:
    order_id: str
    amount: Decimal
    currency: str


class PaymentStrategy(Protocol):
    """Protocol defining payment contract."""
    def pay(self, request: PaymentRequest) -> bool:
        ...


class CreditCardPayment:
    def __init__(self, card_number_last4: str) -> None:
        self._last4 = card_number_last4

    def pay(self, request: PaymentRequest) -> bool:
        print(f"[CARD] Charging {request.amount} {request.currency} via card ending in {self._last4}.")
        return True


class UPIPayment:
    def __init__(self, vpa: str) -> None:
        self._vpa = vpa

    def pay(self, request: PaymentRequest) -> bool:
        print(f"[UPI] Requesting {request.amount} {request.currency} from VPA: {self._vpa}.")
        return True


class CryptoPayment:
    """Extension: Added without touching existing payment classes or context!"""
    def __init__(self, wallet_address: str) -> None:
        self._wallet = wallet_address

    def pay(self, request: PaymentRequest) -> bool:
        print(f"[CRYPTO] Transferring {request.amount} {request.currency} to wallet {self._wallet[:6]}...")
        return True


class PaymentService:
    """Context class: Closed for modification, works with any PaymentStrategy."""
    def execute(self, request: PaymentRequest, strategy: PaymentStrategy) -> bool:
        print(f"\nProcessing order #{request.order_id}...")
        return strategy.pay(request)


if __name__ == "__main__":
    service = PaymentService()
    req = PaymentRequest("ORD-101", Decimal("250.00"), "USD")

    # Swapping strategies seamlessly
    service.execute(req, CreditCardPayment("4242"))
    service.execute(req, UPIPayment("user@okhdfc"))
    service.execute(req, CryptoPayment("0x71C...B42"))
