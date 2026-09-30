"""
Chain of Responsibility Pattern - SDE-III Implementation
Scenario: HTTP Request Middleware Pipeline (Auth -> RateLimit -> Validation).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class HttpRequest:
    user_token: Optional[str]
    client_ip: str
    body: str


class MiddlewareHandler:
    def __init__(self, next_handler: Optional[MiddlewareHandler] = None) -> None:
        self._next: Optional[MiddlewareHandler] = next_handler

    def set_next(self, handler: MiddlewareHandler) -> MiddlewareHandler:
        self._next = handler
        return handler

    def handle(self, request: HttpRequest) -> bool:
        if self._next:
            return self._next.handle(request)
        return True


class AuthenticationHandler(MiddlewareHandler):
    def handle(self, request: HttpRequest) -> bool:
        if not request.user_token or request.user_token != "valid_token":
            print("[REJECT] 401 Unauthorized: Invalid or missing token.")
            return False
        print("[AUTH] 200 Token validated.")
        return super().handle(request)


class RateLimitHandler(MiddlewareHandler):
    def handle(self, request: HttpRequest) -> bool:
        if request.client_ip == "192.168.1.100":
            print("[REJECT] 429 Too Many Requests: IP throttled.")
            return False
        print("[RATE LIMIT] Request within quota.")
        return super().handle(request)


class BodyValidationHandler(MiddlewareHandler):
    def handle(self, request: HttpRequest) -> bool:
        if len(request.body) == 0:
            print("[REJECT] 400 Bad Request: Empty body.")
            return False
        print("[VALIDATION] Body validated.")
        return super().handle(request)


if __name__ == "__main__":
    # Assemble pipeline
    auth = AuthenticationHandler()
    rate = RateLimitHandler()
    valid = BodyValidationHandler()

    auth.set_next(rate).set_next(valid)

    print("--- Test 1: Valid Request ---")
    r1 = HttpRequest(user_token="valid_token", client_ip="10.0.0.1", body="{'data': 123}")
    auth.handle(r1)

    print("\n--- Test 2: Throttled Request ---")
    r2 = HttpRequest(user_token="valid_token", client_ip="192.168.1.100", body="{'data': 123}")
    auth.handle(r2)
