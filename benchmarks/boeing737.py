from aerospace.aircraft.aircraft import Aircraft

BOEING_737 = Aircraft(
    name="737-800",
    manufacturer="Boeing",
    mass_kg=79015,
    wing_area_m2=124.6,
    wingspan_m=35.8,
    drag_coefficient=0.024,
    lift_coefficient=1.5,
    thrust_n=242000,
    max_speed_ms=230
)
