import math

from aerospace.physics.constants import (
    EARTH_RADIUS_M,
    EARTH_GRAVITATIONAL_PARAMETER
)


# Orbital Radius
# r = R + h

def orbital_radius(
    altitude_m: float
) -> float:

    return EARTH_RADIUS_M + altitude_m


# Orbital Velocity
# v = sqrt(GM / r)

def orbital_velocity(
    altitude_m: float
) -> float:

    radius = orbital_radius(altitude_m)

    return math.sqrt(
        EARTH_GRAVITATIONAL_PARAMETER
        / radius
    )


# Orbital Period
# T = 2pi * sqrt(r^3 / GM)

def orbital_period(
    altitude_m: float
) -> float:

    radius = orbital_radius(altitude_m)

    return (
        2
        * math.pi
        * math.sqrt(
            (radius ** 3)
            / EARTH_GRAVITATIONAL_PARAMETER
        )
    )


# Escape Velocity
# ve = sqrt(2GM / r)

def escape_velocity(
    altitude_m: float
) -> float:

    radius = orbital_radius(altitude_m)

    return math.sqrt(
        (
            2
            * EARTH_GRAVITATIONAL_PARAMETER
        )
        / radius
    )
