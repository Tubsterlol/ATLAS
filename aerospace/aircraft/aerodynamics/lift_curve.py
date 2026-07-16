from math import radians


def lift_coefficient(
    alpha_deg: float,
    cl0: float = 0.2,
    lift_curve_slope: float = 5.7,
    cl_max: float = 1.6,
) -> float:
    alpha_rad = radians(alpha_deg)

    cl = cl0 + lift_curve_slope * alpha_rad

    return min(cl, cl_max)
