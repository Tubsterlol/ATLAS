from math import degrees


def trim_angle_of_attack(
    required_lift_n: float,
    density: float,
    velocity_ms: float,
    wing_area_m2: float,
    cl0: float = 0.2,
    lift_curve_slope: float = 5.7,
) -> float:
    """
    Computes the trimmed angle of attack required to
    generate the requested lift.
    """

    q = 0.5 * density * velocity_ms**2

    if q <= 0:
        return 0.0

    cl = required_lift_n / (q * wing_area_m2)

    alpha_rad = (cl - cl0) / lift_curve_slope

    return degrees(alpha_rad)
