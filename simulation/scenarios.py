from dataclasses import dataclass


@dataclass
class SatelliteScenario:

    name: str

    satellite_name: str

    duration_hours: float

    timestep_seconds: float


@dataclass
class AircraftScenario:

    name: str

    aircraft_name: str

    velocity_ms: float

    duration_seconds: float

    timestep_seconds: float
