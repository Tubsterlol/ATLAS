from aerospace.satellite.drag import satellite_drag_force
from aerospace.satellite.orbit import orbital_velocity

# Simplified Orbital Decay Model


def altitude_decay_rate(
    mass_kg: float, drag_force_n: float, velocity_ms: float
) -> float:

    acceleration = drag_force_n / mass_kg

    return acceleration


# Update Satellite State


def update_altitude(altitude_m: float, decay_rate: float, timestep_s: float) -> float:

    altitude_loss = 0.5 * decay_rate * timestep_s**2

    return altitude_m - altitude_loss


# Single Simulation Step


def simulate_decay_step(satellite, timestep_s: float):

    velocity = orbital_velocity(satellite.altitude_m)

    drag = satellite_drag_force(
        altitude_m=satellite.altitude_m,
        velocity_ms=velocity,
        drag_coefficient=satellite.drag_coefficient,
        cross_sectional_area_m2=satellite.cross_sectional_area_m2,
    )

    decay_rate = altitude_decay_rate(
        mass_kg=satellite.mass_kg, drag_force_n=drag, velocity_ms=velocity
    )

    satellite.altitude_m = update_altitude(
        altitude_m=satellite.altitude_m, decay_rate=decay_rate, timestep_s=timestep_s
    )

    satellite.velocity_ms = velocity

    return {
        "altitude_m": satellite.altitude_m,
        "velocity_ms": velocity,
        "drag_force_n": drag,
        "decay_rate": decay_rate,
    }
