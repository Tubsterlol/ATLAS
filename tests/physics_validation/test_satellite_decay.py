from aerospace.satellite.decay import simulate_decay_step
from aerospace.satellite.satellite import Satellite


def test_altitude_decay():

    satellite = Satellite(
        name="TestSat",
        mass_kg=500,
        cross_sectional_area_m2=4,
        drag_coefficient=2.2,
        altitude_m=400_000,
    )

    initial_altitude = satellite.altitude_m

    simulate_decay_step(satellite, timestep_s=10)

    assert satellite.altitude_m < initial_altitude
