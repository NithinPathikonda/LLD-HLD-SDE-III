"""
Strategy Pattern (Behavioral) - SDE-III Implementation
Scenario: Dynamic Pricing Engine for E-commerce / Ride Sharing.
Allows runtime selection of fee / discount calculation algorithm without modifying the client.
"""

from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Protocol


@dataclass(frozen=True)
class OrderContext:
    base_price: Decimal
    is_vip: bool
    distance_km: float
    is_peak_hours: bool


class PricingStrategy(Protocol):
    def calculate_price(self, context: OrderContext) -> Decimal:
        ...


class RegularPricingStrategy:
    """Standard baseline pricing."""
    def calculate_price(self, context: OrderContext) -> Decimal:
        return context.base_price


class SurgePricingStrategy:
    """Surge multiplier during peak demand."""
    def __init__(self, multiplier: Decimal = Decimal("1.50")) -> None:
        self._multiplier = multiplier

    def calculate_price(self, context: OrderContext) -> Decimal:
        return (context.base_price * self._multiplier).quantize(Decimal("0.01"))


class VIPDiscountStrategy:
    """Flat 20% discount for loyalty members."""
    def calculate_price(self, context: OrderContext) -> Decimal:
        discount = context.base_price * Decimal("0.20")
        return (context.base_price - discount).quantize(Decimal("0.01"))


class PricingEngine:
    """Context object holding current strategy and delegating calculation."""
    def __init__(self, strategy: PricingStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: PricingStrategy) -> None:
        """Dynamically swap strategy at runtime."""
        self._strategy = strategy

    def compute_total(self, context: OrderContext) -> Decimal:
        final_price = self._strategy.calculate_price(context)
        print(f"[{self._strategy.__class__.__name__}] Base: ${context.base_price:.2f} -> Final: ${final_price:.2f}")
        return final_price


if __name__ == "__main__":
    ctx = OrderContext(base_price=Decimal("100.00"), is_vip=True, distance_km=12.5, is_peak_hours=True)

    engine = PricingEngine(RegularPricingStrategy())
    engine.compute_total(ctx)

    # Dynamic swap to Surge
    engine.set_strategy(SurgePricingStrategy(multiplier=Decimal("1.75")))
    engine.compute_total(ctx)

    # Dynamic swap to VIP
    engine.set_strategy(VIPDiscountStrategy())
    engine.compute_total(ctx)
