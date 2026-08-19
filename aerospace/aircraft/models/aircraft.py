from dataclasses import dataclass

from aerospace.aircraft.geometry.geometry import AircraftGeometry
from aerospace.core.validation import (
    require_non_empty_string,
    require_non_negative,
    require_positive,
)


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

    def __post_init__(self) -> None:
        require_non_empty_string(self.name, "name")
        require_non_empty_string(self.manufacturer, "manufacturer")
        require_positive(self.mass_kg, "mass_kg")
        require_non_negative(self.drag_coefficient, "drag_coefficient")
        require_non_negative(self.thrust_n, "thrust_n")
        require_positive(self.max_speed_ms, "max_speed_ms")
        require_non_negative(self.fuel_burn_kg_s, "fuel_burn_kg_s")
