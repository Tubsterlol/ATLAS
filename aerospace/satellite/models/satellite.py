from dataclasses import dataclass

from aerospace.core.validation import (
    require_non_empty_string,
    require_non_negative,
    require_positive,
)


@dataclass
class Satellite:
    name: str
    mass_kg: float
    altitude_m: float
    drag_coefficient: float
    cross_sectional_area_m2: float

    def __post_init__(self) -> None:
        require_non_empty_string(self.name, "name")
        require_positive(self.mass_kg, "mass_kg")
        require_non_negative(self.altitude_m, "altitude_m")
        require_non_negative(self.drag_coefficient, "drag_coefficient")
        require_positive(self.cross_sectional_area_m2, "cross_sectional_area_m2")
