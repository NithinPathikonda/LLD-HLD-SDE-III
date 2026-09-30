"""
Dependency Inversion Principle (DIP) - SDE-III REFACTORED
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
"""

from typing import Protocol, List


# 1. Abstractions (Protocols)
class OrderRepository(Protocol):
    def save(self, order_id: str, amount: float) -> None:
        ...


class NotificationService(Protocol):
    def notify(self, recipient: str, message: str) -> None:
        ...


# 2. Low-Level Implementations (Details)
class PostgresOrderRepository:
    def save(self, order_id: str, amount: float) -> None:
        print(f"[PostgreSQL] Saved order {order_id} with amount ${amount:.2f}")


class MockOrderRepository:
    """Test Double / Mock for lightning fast unit tests!"""
    def __init__(self) -> None:
        self.orders: list[tuple[str, float]] = []

    def save(self, order_id: str, amount: float) -> None:
        self.orders.append((order_id, amount))
        print(f"[MockDB] Recorded order {order_id} in memory.")


class MockNotificationService:
    def __init__(self) -> None:
        self.sent_messages: list[tuple[str, str]] = []

    def notify(self, recipient: str, message: str) -> None:
        self.sent_messages.append((recipient, message))
        print(f"[MockNotifier] Captured message to {recipient}")


# 3. High-Level Module depending purely on abstractions
class OrderProcessor:
    def __init__(self, repo: OrderRepository, notifier: NotificationService) -> None:
        # Dependencies injected from outside!
        self._repo = repo
        self._notifier = notifier

    def checkout(self, order_id: str, customer_contact: str, amount: float) -> None:
        self._repo.save(order_id, amount)
        self._notifier.notify(customer_contact, f"Order {order_id} confirmed for ${amount:.2f}")


if __name__ == "__main__":
    print("--- Running DIP Refactored (Unit Testing Mode) ---")
    mock_db = MockOrderRepository()
    mock_notify = MockNotificationService()

    processor = OrderProcessor(repo=mock_db, notifier=mock_notify)
    processor.checkout("ORD-999", "alice@example.com", 149.50)

    assert len(mock_db.orders) == 1
    assert len(mock_notify.sent_messages) == 1
    print("Unit test verified cleanly without touching external networks or databases!")
