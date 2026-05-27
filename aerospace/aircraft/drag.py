from aerospace.physics.aerodynamics import (
    drag_force
)


# Aircraft Drag Wrapper

def aircraft_drag(
    density: float,
    velocity_ms: float,
    drag_coefficient: float,
    reference_area_m2: float
) -> float:

    return drag_force(
        density=density,
        velocity=velocity_ms,
        drag_coefficient=drag_coefficient,
        reference_area=reference_area_m2
    )
