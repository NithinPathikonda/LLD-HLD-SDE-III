"""
SDE-III Low-Level Design (LLD) / Machine Coding Python Template
----------------------------------------------------------------
This template is structured for 45-90 min SDE-III / Staff Machine Coding interviews.

Key Evaluation Criteria for SDE-III:
1. Separation of Concerns & Clean Abstractions (Single Responsibility, Dependency Inversion)
2. Extensibility (Open-Closed Principle: Open for extension via Strategy / Factory / State)
3. Strong Typing (`typing`, `Optional`, `List`, `Dict`, `Protocol` or `ABC`)
4. Thread-Safety & Concurrency Handling (`threading.Lock`, `threading.RLock`)
5. Rich Domain Modeling (`@dataclass(frozen=True)` for Value Objects, Enums for states)
6. Error & Edge Case Handling (Domain-specific Custom Exceptions)
7. Clean Driver / Integration Test verifying non-trivial scenarios
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
import threading
from typing import Dict, List, Optional
import uuid


# ==========================================
# 1. ENUMS & CONSTANTS
# ==========================================
class ItemStatus(Enum):
    PENDING = auto()
    ACTIVE = auto()
    COMPLETED = auto()
    FAILED = auto()


# ==========================================
# 2. CUSTOM DOMAIN EXCEPTIONS
# ==========================================
class DomainException(Exception):
    """Base exception for all domain errors."""
    pass


class ResourceNotFoundException(DomainException):
    pass


class InvalidOperationException(DomainException):
    pass


class ConcurrencyConflictException(DomainException):
    pass


# ==========================================
# 3. DOMAIN MODELS & ENTITIES
# ==========================================
@dataclass(frozen=True)
class EntityId:
    """Immutable Value Object for IDs."""
    value: str = field(default_factory=lambda: str(uuid.uuid4())[:8])


@dataclass
class Item:
    """Core domain entity."""
    id: EntityId
    name: str
    status: ItemStatus = ItemStatus.PENDING
    created_at: datetime = field(default_factory=datetime.utcnow)

    def activate(self) -> None:
        if self.status != ItemStatus.PENDING:
            raise InvalidOperationException(f"Cannot activate item in status {self.status.name}")
        self.status = ItemStatus.ACTIVE


# ==========================================
# 4. STRATEGY / EXTENSION INTERFACES (OCP)
# ==========================================
class ProcessingStrategy(ABC):
    """Interface allowing extensible algorithm strategies."""

    @abstractmethod
    def execute(self, item: Item) -> bool:
        """Process item according to strategy."""
        pass


class DefaultProcessingStrategy(ProcessingStrategy):
    def execute(self, item: Item) -> bool:
        # Business logic for default processing
        item.activate()
        return True


# ==========================================
# 5. REPOSITORY / STORAGE INTERFACE & IN-MEMORY IMPL
# ==========================================
class ItemRepository(ABC):
    """Abstract interface for data access (DIP)."""

    @abstractmethod
    def save(self, item: Item) -> None:
        pass

    @abstractmethod
    def find_by_id(self, item_id: EntityId) -> Optional[Item]:
        pass

    @abstractmethod
    def find_all(self) -> List[Item]:
        pass


class InMemoryItemRepository(ItemRepository):
    """Thread-safe In-Memory Repository Implementation."""

    def __init__(self) -> None:
        self._storage: Dict[str, Item] = {}
        self._lock = threading.RLock()

    def save(self, item: Item) -> None:
        with self._lock:
            self._storage[item.id.value] = item

    def find_by_id(self, item_id: EntityId) -> Optional[Item]:
        with self._lock:
            return self._storage.get(item_id.value)

    def find_all(self) -> List[Item]:
        with self._lock:
            return list(self._storage.values())


# ==========================================
# 6. SERVICE ORCHESTRATOR / CONTROLLER
# ==========================================
class ItemManagerService:
    """
    Central service orchestrator.
    Handles business workflows, concurrency, and strategy delegation.
    """

    def __init__(
        self,
        repository: ItemRepository,
        strategy: ProcessingStrategy
    ) -> None:
        self._repo = repository
        self._strategy = strategy
        self._service_lock = threading.Lock()

    def create_item(self, name: str) -> Item:
        item = Item(id=EntityId(), name=name)
        self._repo.save(item)
        return item

    def process_item(self, item_id: EntityId) -> Item:
        item = self._repo.find_by_id(item_id)
        if not item:
            raise ResourceNotFoundException(f"Item with ID {item_id.value} not found")

        with self._service_lock:
            success = self._strategy.execute(item)
            if success:
                self._repo.save(item)
            return item


# ==========================================
# 7. DRIVER & DEMO TEST
# ==========================================
def main() -> None:
    print("=== SDE-III Machine Coding Python Demo ===")
    repo = InMemoryItemRepository()
    strategy = DefaultProcessingStrategy()
    service = ItemManagerService(repository=repo, strategy=strategy)

    # 1. Create Items
    item_a = service.create_item("Task-Alpha")
    print(f"[CREATED] {item_a.id.value}: {item_a.name} (Status: {item_a.status.name})")

    # 2. Process Item
    processed = service.process_item(item_a.id)
    print(f"[PROCESSED] {processed.id.value}: Status is now {processed.status.name}")

    # 3. Error Case Check
    try:
        service.process_item(EntityId(value="invalid-id"))
    except ResourceNotFoundException as e:
        print(f"[EXPECTED ERROR CAUGHT] {e}")

    print("=== Verification Successful ===")


if __name__ == "__main__":
    main()
