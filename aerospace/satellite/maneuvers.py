from aerospace.physics.constants import EARTH_GRAVITATIONAL_PARAMETER, EARTH_RADIUS_M


def orbit_raise(
    altitude_m: float,
    delta_v_ms: float,
) -> float:

    orbital_radius = EARTH_RADIUS_M + altitude_m

    velocity = (EARTH_GRAVITATIONAL_PARAMETER / orbital_radius) ** 0.5

    new_velocity = velocity + delta_v_ms

    new_radius = EARTH_GRAVITATIONAL_PARAMETER / (new_velocity**2)

    return max(
        0.0,
        new_radius - EARTH_RADIUS_M,
    )


def orbit_lower(
    altitude_m: float,
    delta_v_ms: float,
) -> float:

    return orbit_raise(
        altitude_m=altitude_m,
        delta_v_ms=-abs(delta_v_ms),
    )
