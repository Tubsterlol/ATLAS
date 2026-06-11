from aerospace.physics.constants import (
    EARTH_MASS_KG,
    EARTH_RADIUS_M,
    GRAVITATIONAL_CONSTANT,
)

# Newton's Law of Gravitation
# F = G * (m1 * m2) / r^2


def gravitational_force(mass_1: float, mass_2: float, distance: float) -> float:

    return GRAVITATIONAL_CONSTANT * mass_1 * mass_2 / (distance**2)


# Gravitational acceleration
# g = GM / r^2


def gravitational_acceleration(planet_mass: float, radius: float) -> float:

    return GRAVITATIONAL_CONSTANT * planet_mass / (radius**2)


# Gravity decreases with altitude


def gravity_at_altitude(altitude_m: float) -> float:

    orbital_radius = EARTH_RADIUS_M + altitude_m

    return gravitational_acceleration(EARTH_MASS_KG, orbital_radius)
