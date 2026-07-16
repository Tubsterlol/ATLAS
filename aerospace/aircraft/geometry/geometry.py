from dataclasses import dataclass

from aerospace.core.validation import (
    require_in_range,
    require_non_negative,
    require_positive,
)


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

    def __post_init__(self) -> None:
        require_positive(self.wing_span_m, "wing_span_m")
        require_positive(self.wing_area_m2, "wing_area_m2")
        require_positive(self.mean_chord_m, "mean_chord_m")
        require_in_range(self.taper_ratio, "taper_ratio", 0.0, 1.0)
        require_non_negative(self.sweep_deg, "sweep_deg")
        require_positive(self.fuselage_length_m, "fuselage_length_m")
        require_positive(self.fuselage_diameter_m, "fuselage_diameter_m")
        require_non_negative(self.horizontal_tail_area_m2, "horizontal_tail_area_m2")
        require_non_negative(self.vertical_tail_area_m2, "vertical_tail_area_m2")
