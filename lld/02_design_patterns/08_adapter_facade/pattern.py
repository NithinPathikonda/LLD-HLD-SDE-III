"""
Adapter & Facade Patterns (Structural) - SDE-III Implementation
1. Adapter: Converts the incompatible interface of a 3rd-party legacy payment gateway to match internal protocol.
2. Facade: Provides a simplified, unified interface to complex subsystems (Billing, Inventory, Shipping).
"""

from __future__ import annotations
from typing import Protocol


# ==============================================================================
# 1. ADAPTER PATTERN
# ==============================================================================

class TargetPaymentGateway(Protocol):
    """Internal standardized payment interface expected across our services."""
    def charge(self, user_id: str, amount_cents: int) -> bool:
        ...


class LegacyStripeVendorSdk:
    """Incompatible 3rd-party legacy class with different method signature."""
    def make_transaction(self, customer_token: str, dollars: float, currency_code: str) -> dict:
        print(f"[3rd-Party Vendor] Processed ${dollars:.2f} {currency_code} for token {customer_token}")
        return {"status": "SUCCESS", "tx_id": "tx_998877"}


class StripePaymentAdapter:
    """Adapter bridging TargetPaymentGateway protocol to LegacyStripeVendorSdk."""
    def __init__(self, vendor_sdk: LegacyStripeVendorSdk) -> None:
        self._sdk = vendor_sdk

    def charge(self, user_id: str, amount_cents: int) -> bool:
        dollars = amount_cents / 100.0
        response = self._sdk.make_transaction(
            customer_token=f"tok_{user_id}",
            dollars=dollars,
            currency_code="USD"
        )
        return response.get("status") == "SUCCESS"


# ==============================================================================
# 2. FACADE PATTERN
# ==============================================================================

class InventoryService:
    def reserve_stock(self, item_id: str, quantity: int) -> bool:
        print(f"[Inventory] Reserved {quantity}x item {item_id}.")
        return True


class ShippingService:
    def schedule_pickup(self, item_id: str, destination: str) -> str:
        print(f"[Shipping] Scheduled courier delivery to '{destination}'.")
        return "TRACK-12345"


class ECommerceOrderFacade:
    """Facade exposing a clean checkout method while orchestrating complex subsystems."""
    def __init__(
        self,
        payment_gateway: TargetPaymentGateway,
        inventory: InventoryService,
        shipping: ShippingService,
    ) -> None:
        self._payment = payment_gateway
        self._inventory = inventory
        self._shipping = shipping

    def place_order(self, user_id: str, item_id: str, quantity: int, price_cents: int, address: str) -> bool:
        print(f"\n--- [Facade] Starting checkout for User: {user_id} ---")
        if not self._inventory.reserve_stock(item_id, quantity):
            print("[Facade] Order failed: Inventory shortage.")
            return False

        if not self._payment.charge(user_id, price_cents * quantity):
            print("[Facade] Order failed: Payment declined.")
            return False

        tracking_id = self._shipping.schedule_pickup(item_id, address)
        print(f"[Facade] Order completed successfully! Tracking ID: {tracking_id}")
        return True


if __name__ == "__main__":
    # 1. Setup Adapter
    vendor_sdk = LegacyStripeVendorSdk()
    adapted_gateway = StripePaymentAdapter(vendor_sdk)

    # 2. Setup Facade
    facade = ECommerceOrderFacade(
        payment_gateway=adapted_gateway,
        inventory=InventoryService(),
        shipping=ShippingService(),
    )

    facade.place_order(
        user_id="usr_888",
        item_id="MacBookPro16",
        quantity=1,
        price_cents=249900,
        address="100 Silicon Way, CA"
    )
