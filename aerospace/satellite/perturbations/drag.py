from aerospace.atmosphere.orbital_density import orbital_density
from aerospace.physics.aerodynamics import drag_force

# Satellite Drag Force
# D = 0.5 * rho * v^2 * Cd * A


def satellite_drag_force(
    altitude_m: float,
    velocity_ms: float,
    drag_coefficient: float,
    cross_sectional_area_m2: float,
) -> float:

    density = orbital_density(altitude_m)

    return drag_force(
        density=density,
        velocity=velocity_ms,
        drag_coefficient=drag_coefficient,
        reference_area=cross_sectional_area_m2,
    )
