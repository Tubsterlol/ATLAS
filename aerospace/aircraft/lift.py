from aerospace.physics.aerodynamics import lift_force

# Aircraft Lift Wrapper


def aircraft_lift(
    density: float, velocity_ms: float, lift_coefficient: float, wing_area_m2: float
) -> float:

    return lift_force(
        density=density,
        velocity=velocity_ms,
        lift_coefficient=lift_coefficient,
        wing_area=wing_area_m2,
    )
