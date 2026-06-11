from dataclasses import dataclass


@dataclass
class AircraftState:
    time_s: float = 0.0
    altitude_m: float = 0.0
    velocity_ms: float = 0.0
    fuel_kg: float = 0.0


@dataclass
class SatelliteState:
    time_s: float = 0.0
    altitude_m: float = 0.0
    velocity_ms: float = 0.0
