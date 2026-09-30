"""
Builder Pattern (Creational) - SDE-III Implementation
Scenario: Complex HTTP / SQL Query or Microservice Client Configuration Builder.
Solves the 'Telescoping Constructor' anti-pattern and enforces immutability on build.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class DatabaseConfig:
    """Immutable target object."""
    host: str
    port: int
    database_name: str
    username: str
    password: str
    max_connections: int
    timeout_seconds: float
    ssl_enabled: bool
    connection_properties: Dict[str, str]


class DatabaseConfigBuilder:
    """Fluent Builder for DatabaseConfig with step-by-step validation."""

    def __init__(self) -> None:
        self._host: Optional[str] = None
        self._port: int = 5432  # Default PostgreSQL port
        self._database_name: Optional[str] = None
        self._username: Optional[str] = None
        self._password: Optional[str] = None
        self._max_connections: int = 10
        self._timeout_seconds: float = 30.0
        self._ssl_enabled: bool = True
        self._connection_properties: Dict[str, str] = {}

    def with_host(self, host: str) -> DatabaseConfigBuilder:
        self._host = host
        return self

    def with_port(self, port: int) -> DatabaseConfigBuilder:
        if not (1 <= port <= 65535):
            raise ValueError(f"Invalid port: {port}")
        self._port = port
        return self

    def with_database(self, name: str) -> DatabaseConfigBuilder:
        self._database_name = name
        return self

    def with_credentials(self, username: str, password: str) -> DatabaseConfigBuilder:
        self._username = username
        self._password = password
        return self

    def with_pool_size(self, max_connections: int) -> DatabaseConfigBuilder:
        if max_connections <= 0:
            raise ValueError("Connection pool must be > 0")
        self._max_connections = max_connections
        return self

    def with_timeout(self, seconds: float) -> DatabaseConfigBuilder:
        self._timeout_seconds = seconds
        return self

    def with_ssl(self, enabled: bool) -> DatabaseConfigBuilder:
        self._ssl_enabled = enabled
        return self

    def add_property(self, key: str, value: str) -> DatabaseConfigBuilder:
        self._connection_properties[key] = value
        return self

    def build(self) -> DatabaseConfig:
        """Validate invariant state before returning immutable object."""
        if not self._host:
            raise ValueError("Host is required.")
        if not self._database_name:
            raise ValueError("Database name is required.")
        if not self._username or not self._password:
            raise ValueError("Credentials are required.")

        return DatabaseConfig(
            host=self._host,
            port=self._port,
            database_name=self._database_name,
            username=self._username,
            password=self._password,
            max_connections=self._max_connections,
            timeout_seconds=self._timeout_seconds,
            ssl_enabled=self._ssl_enabled,
            connection_properties=dict(self._connection_properties),
        )


if __name__ == "__main__":
    config = (
        DatabaseConfigBuilder()
        .with_host("db.internal.prod.aws")
        .with_port(5432)
        .with_database("payments_ledger")
        .with_credentials("service_user", "superSecurePass#99")
        .with_pool_size(50)
        .with_timeout(5.0)
        .with_ssl(True)
        .add_property("application_name", "order_service")
        .build()
    )
    print("Successfully built immutable configuration:")
    print(f"Host: {config.host}:{config.port} | DB: {config.database_name}")
    print(f"Pool: {config.max_connections} | SSL: {config.ssl_enabled}")
