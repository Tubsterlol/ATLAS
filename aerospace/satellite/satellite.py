from dataclasses import dataclass


@dataclass
class Satellite:
    name: str
    mass_kg: float
    cross_sectional_area_m2: float
    drag_coefficient: float
    altitude_m: float
    velocity_ms: float = 0.0
