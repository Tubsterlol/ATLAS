import math

from aerospace.physics.constants import (
    EARTH_RADIUS_M,
    EARTH_GRAVITATIONAL_PARAMETER
)

# Orbital Velocity
# v = sqrt(GM / r)

def orbital_velocity(
    altitude_m: float
) -> float:

    orbital_radius = EARTH_RADIUS_M + altitude_m

    return math.sqrt(
        EARTH_GRAVITATIONAL_PARAMETER
        / orbital_radius
    )


# Escape Velocity
# ve = sqrt(2GM / r)

def escape_velocity(
    radius_m: float
) -> float:

    return math.sqrt(
        (
            2
            * EARTH_GRAVITATIONAL_PARAMETER
        )
        / radius_m
    )


# Orbital Period
# T = 2pi * sqrt(r^3 / GM)

def orbital_period(
    orbital_radius_m: float
) -> float:

    return (
        2
        * math.pi
        * math.sqrt(
            (orbital_radius_m ** 3)
            / EARTH_GRAVITATIONAL_PARAMETER
        )
    )


# Circular Orbit Energy
# E = -GMm / 2r

def circular_orbit_energy(
    mass: float,
    orbital_radius_m: float
) -> float:

    return -(
        EARTH_GRAVITATIONAL_PARAMETER
        * mass
    ) / (
        2 * orbital_radius_m
    )
