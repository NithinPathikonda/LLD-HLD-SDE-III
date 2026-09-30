"""
State Pattern (Behavioral) - SDE-III Implementation
Scenario: Finite State Machine (FSM) for E-Commerce Order Lifecycle.
Transitions: Created -> Paid -> Shipped -> Delivered (or Cancelled).
Eliminates massive nested if/elif statements checking current status!
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def pay(self, order: Order) -> None:
        pass

    @abstractmethod
    def ship(self, order: Order) -> None:
        pass

    @abstractmethod
    def cancel(self, order: Order) -> None:
        pass


class CreatedState(OrderState):
    def pay(self, order: Order) -> None:
        print("[ORDER] Payment successful. Moving to Paid state.")
        order.set_state(PaidState())

    def ship(self, order: Order) -> None:
        print("[ERROR] Cannot ship unpaid order.")

    def cancel(self, order: Order) -> None:
        print("[ORDER] Order cancelled.")
        order.set_state(CancelledState())


class PaidState(OrderState):
    def pay(self, order: Order) -> None:
        print("[ERROR] Order is already paid.")

    def ship(self, order: Order) -> None:
        print("[ORDER] Order dispatched to courier. Moving to Shipped state.")
        order.set_state(ShippedState())

    def cancel(self, order: Order) -> None:
        print("[ORDER] Order cancelled. Initiating refund.")
        order.set_state(CancelledState())


class ShippedState(OrderState):
    def pay(self, order: Order) -> None:
        print("[ERROR] Already paid & shipped.")

    def ship(self, order: Order) -> None:
        print("[ERROR] Order is already in transit.")

    def cancel(self, order: Order) -> None:
        print("[ERROR] Cannot cancel order after shipment. Must initiate return.")


class CancelledState(OrderState):
    def pay(self, order: Order) -> None:
        print("[ERROR] Cannot pay for a cancelled order.")

    def ship(self, order: Order) -> None:
        print("[ERROR] Cannot ship a cancelled order.")

    def cancel(self, order: Order) -> None:
        print("[ERROR] Already cancelled.")


class Order:
    """Context holding the current state reference."""
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self._state: OrderState = CreatedState()

    def set_state(self, state: OrderState) -> None:
        self._state = state

    def pay(self) -> None:
        self._state.pay(self)

    def ship(self) -> None:
        self._state.ship(self)

    def cancel(self) -> None:
        self._state.cancel(self)


if __name__ == "__main__":
    order = Order("ORD-501")
    order.ship()    # Error: cannot ship unpaid
    order.pay()     # Success: transitions to Paid
    order.ship()    # Success: transitions to Shipped
    order.cancel()  # Error: cannot cancel shipped order
