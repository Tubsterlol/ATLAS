from dataclasses import dataclass


@dataclass
class AircraftGeometry:
    wing_span_m: float
    wing_area_m2: float
    mean_chord_m: float
    taper_ratio: float
    sweep_deg: float
    fuselage_length_m: float
    fuselage_diameter_m: float
    horizontal_tail_area_m2: float
    vertical_tail_area_m2: float
