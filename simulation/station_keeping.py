from aerospace.satellite.maneuvers import orbit_raise


def station_keep(
    current_altitude_m: float,
    target_altitude_m: float,
    tolerance_m: float,
) -> float:

    if current_altitude_m >= target_altitude_m - tolerance_m:
        return current_altitude_m

    altitude_error = target_altitude_m - current_altitude_m

    delta_v_ms = altitude_error / 1000.0

    return orbit_raise(
        altitude_m=current_altitude_m,
        delta_v_ms=delta_v_ms,
    )
