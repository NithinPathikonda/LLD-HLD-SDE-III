"""
Observer Pattern (Behavioral) - SDE-III Implementation
Scenario: Live Cricket Match Score Update / Pub-Sub Event Bus.
Subscribers subscribe to specific event types and get notified asynchronously.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Dict, List


@dataclass(frozen=True)
class ScoreEvent:
    match_id: str
    runs: int
    wickets: int
    overs: float
    commentary: str


ObserverCallback = Callable[[ScoreEvent], None]


class MatchEventPublisher:
    """The Subject / Event Bus."""
    def __init__(self) -> None:
        self._observers: List[ObserverCallback] = []

    def subscribe(self, observer: ObserverCallback) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: ObserverCallback) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: ScoreEvent) -> None:
        for obs in self._observers:
            obs(event)


# Concrete Observers
def push_notification_service(event: ScoreEvent) -> None:
    if "SIX" in event.commentary or "WICKET" in event.commentary:
        print(f"[PUSH NOTIF] 🚨 {event.commentary} | Score: {event.runs}/{event.wickets}")


def leaderboard_cache_updater(event: ScoreEvent) -> None:
    print(f"[CACHE] Updated Redis match:{event.match_id} -> {event.runs}/{event.wickets} ({event.overs} ov)")


def analytics_logger(event: ScoreEvent) -> None:
    print(f"[ANALYTICS] Ingested event at {event.overs} ov for match {event.match_id}")


if __name__ == "__main__":
    match = MatchEventPublisher()
    match.subscribe(push_notification_service)
    match.subscribe(leaderboard_cache_updater)
    match.subscribe(analytics_logger)

    print("--- Event 1: Normal Single ---")
    match.notify(ScoreEvent("IND-AUS", 145, 2, 18.1, "1 run to deep midwicket"))

    print("\n--- Event 2: High Priority Event ---")
    match.notify(ScoreEvent("IND-AUS", 151, 2, 18.2, "SIX! Smashed over long-on!"))
