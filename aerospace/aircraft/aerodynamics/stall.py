from math import radians


def lift_coefficient_with_stall(
    alpha_deg: float,
    cl0: float = 0.2,
    lift_curve_slope: float = 5.7,
    critical_alpha_deg: float = 15.0,
    max_cl: float = 1.6,
) -> float:
    """
    Lift curve with a simple post-stall model.
    """

    if alpha_deg <= critical_alpha_deg:
        alpha_rad = radians(alpha_deg)
        return min(
            cl0 + lift_curve_slope * alpha_rad,
            max_cl,
        )

    excess = alpha_deg - critical_alpha_deg

    cl = max_cl - 0.08 * excess

    return max(cl, 0.2)
