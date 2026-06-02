from aerospace.satellite.satellite import Satellite

CUBESAT = Satellite(
    name="CubeSat",
    mass_kg=5,
    cross_sectional_area_m2=0.03,
    drag_coefficient=2.2,
    altitude_m=500000
)
