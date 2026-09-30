"""
Factory Pattern & Self-Registering Registry - SDE-III Implementation
Scenario: Pluggable Notification Transport Factory.
Eliminates if/elif chains in factories by using a decorator-based registry!
"""

from __future__ import annotations
from typing import Callable, ClassVar, Dict, Protocol


class Notifier(Protocol):
    def send(self, recipient: str, message: str) -> None:
        ...


class NotifierFactory:
    """Self-registering factory registry."""
    _registry: ClassVar[Dict[str, Callable[[], Notifier]]] = {}

    @classmethod
    def register(cls, channel_type: str) -> Callable[[Callable[[], Notifier]], Callable[[], Notifier]]:
        def decorator(subclass_or_builder: Callable[[], Notifier]) -> Callable[[], Notifier]:
            cls._registry[channel_type.lower()] = subclass_or_builder
            return subclass_or_builder
        return decorator

    @classmethod
    def create(cls, channel_type: str) -> Notifier:
        key = channel_type.lower()
        builder = cls._registry.get(key)
        if not builder:
            valid = list(cls._registry.keys())
            raise ValueError(f"Unknown channel '{channel_type}'. Supported: {valid}")
        return builder()


# Self-registering concrete implementations using decorators!
@NotifierFactory.register("email")
class EmailNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[EMAIL] To {recipient}: {message}")


@NotifierFactory.register("sms")
class SMSNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[SMS] To {recipient}: {message}")


@NotifierFactory.register("slack")
class SlackNotifier:
    def send(self, recipient: str, message: str) -> None:
        print(f"[SLACK] To #{recipient}: {message}")


if __name__ == "__main__":
    channels = ["email", "sms", "slack"]
    for ch in channels:
        client = NotifierFactory.create(ch)
        client.send("dev-team", "Alert: CPU > 90%")
