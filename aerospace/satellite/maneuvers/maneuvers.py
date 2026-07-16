from aerospace.physics.constants import (
    EARTH_GRAVITATIONAL_PARAMETER,
    EARTH_RADIUS_M,
)


def orbit_raise(
    altitude_m: float,
    delta_v_ms: float,
) -> float:

    r = EARTH_RADIUS_M + altitude_m

    v = (EARTH_GRAVITATIONAL_PARAMETER / r) ** 0.5

    new_v = v + delta_v_ms

    specific_energy = (new_v**2 / 2) - (EARTH_GRAVITATIONAL_PARAMETER / r)

    new_a = -EARTH_GRAVITATIONAL_PARAMETER / (2 * specific_energy)

    return max(
        0.0,
        new_a - EARTH_RADIUS_M,
    )


def orbit_lower(
    altitude_m: float,
    delta_v_ms: float,
) -> float:

    return orbit_raise(
        altitude_m,
        -abs(delta_v_ms),
    )
