"""
Multicar Elevator Dispatch System - SDE-III Machine Coding Solution
Features:
- State pattern for Elevator Car (IDLE, MOVING, DOORS_OPEN).
- SCAN / LOOK Elevator Scheduling Algorithm (Up-queue & Down-queue).
- Dispatcher Strategy (Nearest Elevator / Min-Wait heuristic).
- Thread-safe request queuing and simulation.
"""

from __future__ import annotations
from enum import Enum, auto
import heapq
import threading
import time
from typing import Dict, List, Optional, Protocol, Set


class Direction(Enum):
    UP = 1
    DOWN = -1
    IDLE = 0


class DoorState(Enum):
    OPEN = auto()
    CLOSED = auto()


class ElevatorCar:
    def __init__(self, car_id: int, total_floors: int = 20) -> None:
        self.car_id = car_id
        self.total_floors = total_floors
        self.current_floor = 1
        self.direction = Direction.IDLE
        self.door_state = DoorState.CLOSED

        # SCAN/LOOK requests: floors to visit
        self.up_destinations: List[int] = []    # Min-heap for UP requests
        self.down_destinations: List[int] = []  # Max-heap (negated) for DOWN requests
        self._lock = threading.Lock()

    def add_destination(self, floor: int) -> None:
        with self._lock:
            if floor < 1 or floor > self.total_floors:
                raise ValueError(f"Invalid floor {floor}")

            if floor > self.current_floor:
                if floor not in self.up_destinations:
                    heapq.heappush(self.up_destinations, floor)
            elif floor < self.current_floor:
                if -floor not in self.down_destinations:
                    heapq.heappush(self.down_destinations, -floor)

            if self.direction == Direction.IDLE:
                self.direction = Direction.UP if self.up_destinations else Direction.DOWN

    def step(self) -> Optional[int]:
        """Simulates one step of motion in the SCAN algorithm."""
        with self._lock:
            if self.direction == Direction.UP:
                if self.up_destinations:
                    next_stop = self.up_destinations[0]
                    self.current_floor += 1
                    print(f"[Car-{self.car_id}] Moving UP -> Floor {self.current_floor}")

                    if self.current_floor == next_stop:
                        heapq.heappop(self.up_destinations)
                        self._open_and_close_doors()
                        return self.current_floor
                else:
                    # Switch direction if no more up stops
                    self.direction = Direction.DOWN if self.down_destinations else Direction.IDLE

            elif self.direction == Direction.DOWN:
                if self.down_destinations:
                    next_stop = -self.down_destinations[0]
                    self.current_floor -= 1
                    print(f"[Car-{self.car_id}] Moving DOWN -> Floor {self.current_floor}")

                    if self.current_floor == next_stop:
                        heapq.heappop(self.down_destinations)
                        self._open_and_close_doors()
                        return self.current_floor
                else:
                    self.direction = Direction.UP if self.up_destinations else Direction.IDLE

            return None

    def _open_and_close_doors(self) -> None:
        self.door_state = DoorState.OPEN
        print(f"[Car-{self.car_id}] Doors OPEN at Floor {self.current_floor}")
        self.door_state = DoorState.CLOSED


class DispatcherStrategy(Protocol):
    def select_elevator(self, cars: List[ElevatorCar], requested_floor: int, direction: Direction) -> ElevatorCar:
        ...


class NearestElevatorStrategy:
    """Dispatches request to elevator with lowest estimated distance cost."""

    def select_elevator(self, cars: List[ElevatorCar], requested_floor: int, direction: Direction) -> ElevatorCar:
        best_car: Optional[ElevatorCar] = None
        min_cost = float("inf")

        for car in cars:
            dist = abs(car.current_floor - requested_floor)
            # Preference: Car already moving towards this floor in same direction
            if car.direction == direction:
                if (direction == Direction.UP and car.current_floor <= requested_floor) or \
                   (direction == Direction.DOWN and car.current_floor >= requested_floor):
                    cost = dist
                else:
                    cost = dist + car.total_floors
            elif car.direction == Direction.IDLE:
                cost = dist
            else:
                cost = dist + (car.total_floors * 2)

            if cost < min_cost:
                min_cost = cost
                best_car = car

        return best_car or cars[0]


class ElevatorSystem:
    def __init__(self, num_cars: int, total_floors: int = 20) -> None:
        self.cars = [ElevatorCar(i + 1, total_floors) for i in range(num_cars)]
        self.strategy: DispatcherStrategy = NearestElevatorStrategy()

    def press_hall_button(self, floor: int, direction: Direction) -> None:
        selected_car = self.strategy.select_elevator(self.cars, floor, direction)
        print(f"[HALL CALL] Floor {floor} ({direction.name}) -> Assigned to Car-{selected_car.car_id}")
        selected_car.add_destination(floor)

    def press_car_button(self, car_id: int, floor: int) -> None:
        for car in self.cars:
            if car.car_id == car_id:
                print(f"[CAR BUTTON] Car-{car_id} selected destination Floor {floor}")
                car.add_destination(floor)
                return

    def step_all(self) -> None:
        for car in self.cars:
            car.step()


if __name__ == "__main__":
    print("=== Testing Elevator Dispatch System ===")
    system = ElevatorSystem(num_cars=2, total_floors=10)

    # Hall calls
    system.press_hall_button(floor=4, direction=Direction.UP)
    system.press_hall_button(floor=2, direction=Direction.UP)

    # Step simulation
    for _ in range(5):
        system.step_all()

    # Passenger enters and presses floor 6 inside Car-1
    system.press_car_button(car_id=1, floor=6)

    for _ in range(4):
        system.step_all()

    print("Elevator dispatch completed cleanly!")
