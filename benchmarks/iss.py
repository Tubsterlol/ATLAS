from aerospace.satellite.satellite import Satellite

ISS = Satellite(
    name="ISS",
    mass_kg=419725,
    cross_sectional_area_m2=2500,
    drag_coefficient=2.0,
    altitude_m=408000,
)
