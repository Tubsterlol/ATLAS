from math import pi


def induced_drag_coefficient(
    lift_coefficient: float,
    aspect_ratio: float,
    oswald_efficiency: float = 0.8,
) -> float:
    """
    Calculates the induced drag coefficient.

    Cdi = Cl² / (π e AR)
    """

    return lift_coefficient**2 / (pi * oswald_efficiency * aspect_ratio)
