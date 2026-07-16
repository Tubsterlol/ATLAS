from dataclasses import dataclass


@dataclass
class Satellite:
    name: str
    mass_kg: float
    altitude_m: float
    drag_coefficient: float
    cross_sectional_area_m2: float
