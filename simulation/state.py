from dataclasses import dataclass


@dataclass
class SimulationState:
    time_s: float = 0.0
    timestep_s: float = 1.0
    running: bool = True


@dataclass
class AircraftState:
    time_s: float = 0.0

    altitude_m: float = 0.0
    velocity_ms: float = 0.0
    fuel_kg: float = 0.0

    climb_rate_ms: float = 0.0

    phase: str = "climb"

    x_m: float = 0.0
    y_m: float = 0.0

    heading_deg: float = 0.0


@dataclass
class SatelliteState:
    time_s: float = 0.0
    altitude_m: float = 0.0
    velocity_ms: float = 0.0
