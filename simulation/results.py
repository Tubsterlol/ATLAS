from dataclasses import dataclass


@dataclass
class AircraftResult:
    time_s: float
    velocity_ms: float
    lift_n: float
    drag_n: float
    stall_speed_ms: float
    thrust_to_weight: float
    mach: float
    reynolds_number: float
    density: float
    temperature_k: float
    altitude_m: float
    fuel_kg: float
    effective_mass_kg: float


@dataclass
@dataclass
class SatelliteResult:
    time_s: float
    altitude_m: float
    velocity_ms: float
    drag_force_n: float
    decay_rate: float
