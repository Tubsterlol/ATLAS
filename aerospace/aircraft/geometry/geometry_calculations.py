def aspect_ratio(
    wing_span_m: float,
    wing_area_m2: float,
) -> float:
    return wing_span_m**2 / wing_area_m2


def wing_loading(
    weight_n: float,
    wing_area_m2: float,
) -> float:
    return weight_n / wing_area_m2


def mean_chord(
    wing_area_m2: float,
    wing_span_m: float,
) -> float:
    return wing_area_m2 / wing_span_m
