"""
Single Responsibility Principle (SRP) - SDE-III REFACTORED
Each class has exactly one reason to change:
1. User (Domain Entity): Invariants and business identity.
2. PasswordHasher: Hashing algorithms and salt policies.
3. UserRepository (Protocol): Persistence contracts.
4. EmailService (Protocol): Notification transport.
5. RegistrationService: Orchestration coordinator.
"""

from __future__ import annotations
from dataclasses import dataclass
import hashlib
from typing import Dict, Optional, Protocol
import uuid


@dataclass(frozen=True)
class User:
    id: str
    username: str
    email: str
    password_hash: str


class PasswordHasher(Protocol):
    def hash(self, raw_password: str) -> str:
        ...


class SHA256PasswordHasher:
    def hash(self, raw_password: str) -> str:
        return hashlib.sha256(raw_password.encode("utf-8")).hexdigest()


class UserRepository(Protocol):
    def save(self, user: User) -> None:
        ...

    def find_by_username(self, username: str) -> Optional[User]:
        ...


class InMemoryUserRepository:
    def __init__(self) -> None:
        self._store: Dict[str, User] = {}

    def save(self, user: User) -> None:
        self._store[user.username] = user
        print(f"[DB] Persisted user id={user.id} username='{user.username}'")

    def find_by_username(self, username: str) -> Optional[User]:
        return self._store.get(username)


class EmailNotifier(Protocol):
    def send_welcome(self, email: str, username: str) -> None:
        ...


class ConsoleEmailNotifier:
    def send_welcome(self, email: str, username: str) -> None:
        print(f"[EMAIL] To: {email} | Body: Welcome to the platform, {username}!")


class RegistrationService:
    def __init__(
        self,
        repository: UserRepository,
        hasher: PasswordHasher,
        notifier: EmailNotifier,
    ) -> None:
        self._repo = repository
        self._hasher = hasher
        self._notifier = notifier

    def register_user(self, username: str, email: str, raw_password: str) -> User:
        if self._repo.find_by_username(username):
            raise ValueError(f"Username '{username}' already exists.")

        hashed_pwd = self._hasher.hash(raw_password)
        new_user = User(
            id=str(uuid.uuid4())[:8],
            username=username,
            email=email,
            password_hash=hashed_pwd,
        )

        self._repo.save(new_user)
        self._notifier.send_welcome(email, username)
        return new_user


if __name__ == "__main__":
    print("--- Running SRP Compliant Architecture ---")
    service = RegistrationService(
        repository=InMemoryUserRepository(),
        hasher=SHA256PasswordHasher(),
        notifier=ConsoleEmailNotifier(),
    )
    user = service.register_user("john_doe", "john@example.com", "mySuperSecret123")
    print(f"Successfully registered: {user}")
