from aerospace.physics.constants import (
    EARTH_GRAVITATIONAL_PARAMETER,
    EARTH_RADIUS_M,
)


def semi_major_axis(altitude_m: float) -> float:
    return EARTH_RADIUS_M + altitude_m


def orbital_period(altitude_m: float) -> float:
    a = semi_major_axis(altitude_m)

    return 2.0 * 3.141592653589793 * (a**3 / EARTH_GRAVITATIONAL_PARAMETER) ** 0.5


def orbital_energy(altitude_m: float) -> float:
    a = semi_major_axis(altitude_m)

    return -EARTH_GRAVITATIONAL_PARAMETER / (2.0 * a)


def apoapsis(altitude_m: float) -> float:
    return altitude_m


def periapsis(altitude_m: float) -> float:
    return altitude_m
