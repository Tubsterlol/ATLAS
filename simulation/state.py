from dataclasses import dataclass

from aerospace.core.validation import (
    require_in_range,
    require_non_empty_string,
    require_non_negative,
    require_positive,
)
from simulation.mission_phase import MissionPhase


@dataclass
class SimulationState:
    time_s: float = 0.0
    timestep_s: float = 1.0
    running: bool = True

    def __post_init__(self) -> None:
        require_non_negative(self.time_s, "time_s")
        require_positive(self.timestep_s, "timestep_s")


@dataclass
class AircraftState:
    time_s: float = 0.0
    altitude_m: float = 0.0
    velocity_ms: float = 0.0
    fuel_kg: float = 0.0
    climb_rate_ms: float = 0.0
    phase: MissionPhase = MissionPhase.CLIMB
    x_m: float = 0.0
    y_m: float = 0.0
    heading_deg: float = 0.0
    alpha_deg: float = 0.0

    def __post_init__(self) -> None:
        require_non_negative(self.time_s, "time_s")
        require_non_negative(self.altitude_m, "altitude_m")
        require_non_negative(self.velocity_ms, "velocity_ms")
        require_non_negative(self.fuel_kg, "fuel_kg")


@dataclass
class SatelliteState:
    satellite_name: str
    time_s: float = 0.0
    altitude_m: float = 0.0
    velocity_ms: float = 0.0
    inclination_deg: float = 0.0
    eccentricity: float = 0.0
    semi_major_axis_m: float = 0.0
    orbital_period_s: float = 0.0
    orbital_energy_j_kg: float = 0.0
    apoapsis_m: float = 0.0
    periapsis_m: float = 0.0
    true_anomaly_deg: float = 0.0
    latitude_deg: float = 0.0
    longitude_deg: float = 0.0

    def __post_init__(self) -> None:
        require_non_empty_string(self.satellite_name, "satellite_name")
        require_non_negative(self.time_s, "time_s")
        require_non_negative(self.altitude_m, "altitude_m")
        require_non_negative(self.velocity_ms, "velocity_ms")
        require_in_range(self.inclination_deg, "inclination_deg", 0.0, 180.0)
        if not 0.0 <= self.eccentricity < 1.0:
            raise ValueError(
                "eccentricity must be greater than or equal to 0.0 and less than 1.0; "
                f"got {self.eccentricity}"
            )
