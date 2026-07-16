from dataclasses import dataclass, field


@dataclass
class SatelliteScenario:
    name: str
    satellite_name: str
    initial_altitude_m: float
    initial_velocity_ms: float
    inclination_deg: float
    eccentricity: float
    duration_hours: float
    timestep_s: float = 60.0
    maneuvers: list = field(default_factory=list)


@dataclass
class AircraftScenario:
    name: str
    aircraft_name: str
    initial_altitude_m: float
    initial_velocity_ms: float
    initial_fuel_kg: float
    climb_rate_ms: float
    heading_deg: float
    alpha_deg: float
    duration_seconds: float
    timestep_s: float = 1.0
    profile: object | None = None
