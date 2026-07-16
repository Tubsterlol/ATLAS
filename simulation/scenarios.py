from dataclasses import dataclass, field

from aerospace.core.validation import (
    require_in_range,
    require_non_empty_string,
    require_non_negative,
    require_positive,
)


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

    def __post_init__(self) -> None:
        require_non_empty_string(self.name, "name")
        require_non_empty_string(self.satellite_name, "satellite_name")
        require_non_negative(self.initial_altitude_m, "initial_altitude_m")
        require_non_negative(self.initial_velocity_ms, "initial_velocity_ms")
        require_in_range(self.inclination_deg, "inclination_deg", 0.0, 180.0)
        if not 0.0 <= self.eccentricity < 1.0:
            raise ValueError("eccentricity must be greater than or equal to 0.0 and less than 1.0")
        require_positive(self.duration_hours, "duration_hours")
        require_positive(self.timestep_s, "timestep_s")


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

    def __post_init__(self) -> None:
        require_non_empty_string(self.name, "name")
        require_non_empty_string(self.aircraft_name, "aircraft_name")
        require_non_negative(self.initial_altitude_m, "initial_altitude_m")
        require_non_negative(self.initial_velocity_ms, "initial_velocity_ms")
        require_non_negative(self.initial_fuel_kg, "initial_fuel_kg")
        require_positive(self.duration_seconds, "duration_seconds")
        require_positive(self.timestep_s, "timestep_s")
