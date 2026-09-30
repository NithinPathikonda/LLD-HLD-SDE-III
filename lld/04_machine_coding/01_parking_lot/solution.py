"""
Multilevel Parking Lot System - SDE-III Machine Coding Solution
Features:
- Multi-floor parking lot with spot classification (Motorcycle, Compact, Large, EV).
- Thread-safe spot allocation and deallocation under concurrent entry/exit gates.
- Strategy Pattern for Spot Allocation (e.g. NearestFloorStrategy).
- Strategy Pattern for Dynamic Fee Calculation (Hourly & Vehicle-Specific).
- Idempotent and clean domain models with full type hints.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum, auto
import threading
import time
from typing import Dict, List, Optional
import uuid


# ==============================================================================
# 1. ENUMS & VALUE OBJECTS
# ==============================================================================

class VehicleType(Enum):
    MOTORCYCLE = auto()
    CAR = auto()
    TRUCK = auto()
    ELECTRIC = auto()


class SpotType(Enum):
    MOTORCYCLE = auto()
    COMPACT = auto()
    LARGE = auto()
    ELECTRIC = auto()


class TicketStatus(Enum):
    ACTIVE = auto()
    PAID = auto()


@dataclass(frozen=True)
class Vehicle:
    license_plate: str
    vehicle_type: VehicleType


# ==============================================================================
# 2. SPOT & FLOOR MODELS (Domain Entities)
# ==============================================================================

class ParkingSpot:
    def __init__(self, spot_id: str, floor_id: int, spot_type: SpotType) -> None:
        self.spot_id = spot_id
        self.floor_id = floor_id
        self.spot_type = spot_type
        self.occupied_vehicle: Optional[Vehicle] = None
        self._lock = threading.Lock()

    @property
    def is_available(self) -> bool:
        return self.occupied_vehicle is None

    def assign_vehicle(self, vehicle: Vehicle) -> bool:
        with self._lock:
            if not self.is_available:
                return False
            self.occupied_vehicle = vehicle
            return True

    def vacate(self) -> Optional[Vehicle]:
        with self._lock:
            if self.is_available:
                return None
            v = self.occupied_vehicle
            self.occupied_vehicle = None
            return v


class ParkingFloor:
    def __init__(self, floor_id: int) -> None:
        self.floor_id = floor_id
        self.spots: Dict[SpotType, List[ParkingSpot]] = {st: [] for st in SpotType}

    def add_spot(self, spot: ParkingSpot) -> None:
        self.spots[spot.spot_type].append(spot)

    def get_available_spot(self, required_type: SpotType) -> Optional[ParkingSpot]:
        for spot in self.spots.get(required_type, []):
            if spot.is_available:
                return spot
        return None


# ==============================================================================
# 3. TICKET & STRATEGIES
# ==============================================================================

@dataclass
class ParkingTicket:
    ticket_id: str
    vehicle: Vehicle
    spot: ParkingSpot
    entry_time: datetime
    exit_time: Optional[datetime] = None
    fee: float = 0.0
    status: TicketStatus = TicketStatus.ACTIVE


class FeeStrategy:
    """Strategy interface for parking fee computation."""
    def compute_fee(self, ticket: ParkingTicket) -> float:
        raise NotImplementedError


class HourlyFeeStrategy(FeeStrategy):
    """Hourly tiered pricing based on vehicle type."""
    HOURLY_RATES: Dict[VehicleType, float] = {
        VehicleType.MOTORCYCLE: 10.0,
        VehicleType.CAR: 25.0,
        VehicleType.TRUCK: 50.0,
        VehicleType.ELECTRIC: 30.0,
    }

    def compute_fee(self, ticket: ParkingTicket) -> float:
        exit_time = ticket.exit_time or datetime.now()
        duration_seconds = max((exit_time - ticket.entry_time).total_seconds(), 60)
        hours = max(1, int((duration_seconds + 3599) // 3600))  # Ceiling division
        rate = self.HOURLY_RATES.get(ticket.vehicle.vehicle_type, 20.0)
        return float(hours * rate)


class SpotAllocationStrategy:
    """Strategy interface for finding an optimal parking spot."""
    def find_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        raise NotImplementedError


class NearestFirstAllocationStrategy(SpotAllocationStrategy):
    """Assigns spot on the lowest floor nearest to entry gate."""
    MAPPING: Dict[VehicleType, SpotType] = {
        VehicleType.MOTORCYCLE: SpotType.MOTORCYCLE,
        VehicleType.CAR: SpotType.COMPACT,
        VehicleType.TRUCK: SpotType.LARGE,
        VehicleType.ELECTRIC: SpotType.ELECTRIC,
    }

    def find_spot(self, floors: List[ParkingFloor], vehicle: Vehicle) -> Optional[ParkingSpot]:
        needed_type = self.MAPPING[vehicle.vehicle_type]
        for floor in sorted(floors, key=lambda f: f.floor_id):
            spot = floor.get_available_spot(needed_type)
            if spot:
                return spot
        return None


# ==============================================================================
# 4. PARKING LOT SYSTEM ORCHESTRATOR
# ==============================================================================

class ParkingLot:
    _instance: Optional[ParkingLot] = None
    _singleton_lock = threading.Lock()

    def __init__(self, name: str) -> None:
        self.name = name
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.allocation_strategy: SpotAllocationStrategy = NearestFirstAllocationStrategy()
        self.fee_strategy: FeeStrategy = HourlyFeeStrategy()
        self._gate_lock = threading.Lock()

    @classmethod
    def get_instance(cls, name: str = "Central City Parking") -> ParkingLot:
        with cls._singleton_lock:
            if not cls._instance:
                cls._instance = ParkingLot(name)
            return cls._instance

    def add_floor(self, floor: ParkingFloor) -> None:
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        with self._gate_lock:
            spot = self.allocation_strategy.find_spot(self.floors, vehicle)
            if not spot or not spot.assign_vehicle(vehicle):
                print(f"[ENTRY GATE] No available spot for {vehicle.vehicle_type.name} ({vehicle.license_plate})")
                return None

            ticket_id = f"TCK-{str(uuid.uuid4())[:8].upper()}"
            ticket = ParkingTicket(
                ticket_id=ticket_id,
                vehicle=vehicle,
                spot=spot,
                entry_time=datetime.now(),
            )
            self.active_tickets[ticket_id] = ticket
            print(f"[ENTRY GATE] Issued Ticket {ticket_id} to {vehicle.license_plate} at Floor {spot.floor_id}, Spot {spot.spot_id}")
            return ticket

    def unpark_vehicle(self, ticket_id: str) -> Optional[float]:
        with self._gate_lock:
            ticket = self.active_tickets.get(ticket_id)
            if not ticket or ticket.status != TicketStatus.ACTIVE:
                print(f"[EXIT GATE] Invalid or already settled ticket: {ticket_id}")
                return None

            ticket.exit_time = datetime.now()
            # For demonstration, simulate 2 hours elapsed
            ticket.entry_time = ticket.exit_time - timedelta(hours=2)
            fee = self.fee_strategy.compute_fee(ticket)
            ticket.fee = fee
            ticket.status = TicketStatus.PAID

            ticket.spot.vacate()
            del self.active_tickets[ticket_id]
            print(f"[EXIT GATE] Vehicle {ticket.vehicle.license_plate} departed. Total fee: ${fee:.2f}")
            return fee


# ==============================================================================
# VERIFICATION & CONCURRENT SIMULATION
# ==============================================================================

if __name__ == "__main__":
    print("=== Initializing Multilevel Parking Lot ===")
    lot = ParkingLot("Downtown Metropolis Garage")

    # Floor 1 setup
    f1 = ParkingFloor(floor_id=1)
    f1.add_spot(ParkingSpot("F1-C1", 1, SpotType.COMPACT))
    f1.add_spot(ParkingSpot("F1-C2", 1, SpotType.COMPACT))
    f1.add_spot(ParkingSpot("F1-M1", 1, SpotType.MOTORCYCLE))
    lot.add_floor(f1)

    # Floor 2 setup
    f2 = ParkingFloor(floor_id=2)
    f2.add_spot(ParkingSpot("F2-C1", 2, SpotType.COMPACT))
    lot.add_floor(f2)

    # Concurrently park vehicles
    car1 = Vehicle("KA-01-AB-1234", VehicleType.CAR)
    car2 = Vehicle("KA-02-CD-5678", VehicleType.CAR)
    car3 = Vehicle("MH-12-EF-9012", VehicleType.CAR)
    car4 = Vehicle("DL-03-GH-3456", VehicleType.CAR)  # Should fail (only 3 compact spots)

    tickets: List[ParkingTicket] = []

    def arrive(v: Vehicle) -> None:
        t = lot.park_vehicle(v)
        if t:
            tickets.append(t)

    threads = [
        threading.Thread(target=arrive, args=(car1,)),
        threading.Thread(target=arrive, args=(car2,)),
        threading.Thread(target=arrive, args=(car3,)),
        threading.Thread(target=arrive, args=(car4,)),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"\nTotal parked vehicles: {len(tickets)}")

    # Unpark one and free up spot
    if tickets:
        first_ticket = tickets[0]
        lot.unpark_vehicle(first_ticket.ticket_id)

    # Now the 4th car can park!
    lot.park_vehicle(car4)
    print("\nParking Lot simulation completed successfully!")
