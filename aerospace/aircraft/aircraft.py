from dataclasses import dataclass


@dataclass
class Aircraft:
    name: str
    manufacturer: str
    mass_kg: float
    wing_area_m2: float
    wingspan_m: float
    drag_coefficient: float
    lift_coefficient: float
    thrust_n: float
    max_speed_ms: float
    fuel_burn_kg_s: float
