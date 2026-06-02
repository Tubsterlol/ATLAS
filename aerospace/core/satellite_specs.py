from dataclasses import dataclass


@dataclass
class SatelliteSpecs:
    name: str
    mass_kg: float
    cross_sectional_area_m2: float
    drag_coefficient: float
