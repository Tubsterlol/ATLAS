from aerospace.satellite.drag import satellite_drag_force
from aerospace.satellite.orbit import orbital_velocity


def altitude_decay_rate(
    mass_kg: float,
    drag_force_n: float,
    velocity_ms: float,
) -> float:

    return drag_force_n / mass_kg


def update_altitude(
    altitude_m: float,
    decay_rate: float,
    timestep_s: float,
) -> float:

    altitude_loss = 0.5 * decay_rate * timestep_s**2

    return altitude_m - altitude_loss


def simulate_decay_step(
    altitude_m: float,
    mass_kg: float,
    drag_coefficient: float,
    cross_sectional_area_m2: float,
    timestep_s: float,
):

    velocity = orbital_velocity(altitude_m)

    drag = satellite_drag_force(
        altitude_m=altitude_m,
        velocity_ms=velocity,
        drag_coefficient=drag_coefficient,
        cross_sectional_area_m2=cross_sectional_area_m2,
    )

    decay_rate = altitude_decay_rate(
        mass_kg=mass_kg,
        drag_force_n=drag,
        velocity_ms=velocity,
    )

    altitude = update_altitude(
        altitude_m=altitude_m,
        decay_rate=decay_rate,
        timestep_s=timestep_s,
    )

    return {
        "altitude_m": altitude,
        "velocity_ms": velocity,
        "drag_force_n": drag,
        "decay_rate": decay_rate,
    }
