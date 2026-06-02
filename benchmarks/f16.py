from aerospace.aircraft.aircraft import Aircraft

F16 = Aircraft(
    name="F-16",
    manufacturer="Lockheed Martin",
    mass_kg=12000,
    wing_area_m2=27.87,
    wingspan_m=9.96,
    drag_coefficient=0.02,
    lift_coefficient=1.4,
    thrust_n=129000,
    max_speed_ms=660
)
