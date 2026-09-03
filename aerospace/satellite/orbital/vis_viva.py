import math

from aerospace.physics.constants import (
    EARTH_GRAVITATIONAL_PARAMETER,
    EARTH_RADIUS_M,
)


def orbital_radius(
    altitude_m: float,
) -> float:
    """
    Computes orbital radius from altitude.

    r = R + h
    """

    return EARTH_RADIUS_M + altitude_m


def orbital_velocity(
    altitude_m: float,
) -> float:
    """
    Circular orbit velocity.

    v = sqrt(mu / r)
    """

    radius = orbital_radius(altitude_m)

    return math.sqrt(EARTH_GRAVITATIONAL_PARAMETER / radius)


def vis_viva_velocity(
    semi_major_axis_m: float,
    orbital_radius_m: float,
) -> float:
    """
    General vis-viva equation.

    v = sqrt(mu * (2/r - 1/a))
    """

    return math.sqrt(
        EARTH_GRAVITATIONAL_PARAMETER
        * ((2 / orbital_radius_m) - (1 / semi_major_axis_m))
    )


def escape_velocity(
    altitude_m: float,
) -> float:
    """
    Escape velocity.

    v = sqrt(2mu / r)
    """

    radius = orbital_radius(altitude_m)

    return math.sqrt(2 * EARTH_GRAVITATIONAL_PARAMETER / radius)
