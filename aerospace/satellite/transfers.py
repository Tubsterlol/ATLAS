import math

from aerospace.physics.constants import (
    EARTH_GRAVITATIONAL_PARAMETER,
    EARTH_RADIUS_M,
)


def hohmann_delta_v1(
    altitude1_m: float,
    altitude2_m: float,
) -> float:

    r1 = EARTH_RADIUS_M + altitude1_m
    r2 = EARTH_RADIUS_M + altitude2_m

    transfer_axis = (r1 + r2) / 2

    return (EARTH_GRAVITATIONAL_PARAMETER / r1) ** 0.5 * (
        (2 * r2 / (r1 + r2)) ** 0.5 - 1
    )


def hohmann_delta_v2(
    altitude1_m: float,
    altitude2_m: float,
) -> float:

    r1 = EARTH_RADIUS_M + altitude1_m
    r2 = EARTH_RADIUS_M + altitude2_m

    return (EARTH_GRAVITATIONAL_PARAMETER / r2) ** 0.5 * (
        1 - (2 * r1 / (r1 + r2)) ** 0.5
    )


def hohmann_transfer_time(
    altitude1_m: float,
    altitude2_m: float,
) -> float:

    r1 = EARTH_RADIUS_M + altitude1_m
    r2 = EARTH_RADIUS_M + altitude2_m

    transfer_axis = (r1 + r2) / 2

    return math.pi * (transfer_axis**3 / EARTH_GRAVITATIONAL_PARAMETER) ** 0.5
