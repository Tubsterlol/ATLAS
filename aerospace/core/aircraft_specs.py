from dataclasses import dataclass


@dataclass
class AircraftSpecs:
    name: str
    manufacturer: str
    mass_kg: float
    wing_area_m2: float
    wingspan_m: float
    thrust_n: float
