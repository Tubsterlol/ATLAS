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
    phase: str
    x_m: float
    y_m: float
    heading_deg: float


@dataclass
class SatelliteResult:
    time_s: float
    altitude_m: float
    velocity_ms: float
    drag_force_n: float
    decay_rate: float
    orbital_period_s: float
    semi_major_axis_m: float
    orbital_energy_j_kg: float
    apoapsis_m: float
    periapsis_m: float
    inclination_deg: float
    eccentricity: float
    true_anomaly_deg: float
    latitude_deg: float
    longitude_deg: float
