from dataclasses import dataclass

from aerospace.aircraft.geometry.geometry import AircraftGeometry


@dataclass
class Aircraft:
    name: str
    manufacturer: str
    mass_kg: float
    drag_coefficient: float
    thrust_n: float
    max_speed_ms: float
    fuel_burn_kg_s: float
    geometry: AircraftGeometry
