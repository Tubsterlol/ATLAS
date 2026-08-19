def aircraft_drag(
    density: float,
    velocity_ms: float,
    drag_coefficient: float,
    reference_area_m2: float,
) -> float:
    dynamic_pressure = 0.5 * density * velocity_ms**2

    return dynamic_pressure * drag_coefficient * reference_area_m2
