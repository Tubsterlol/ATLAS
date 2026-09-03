from aerospace.satellite.perturbations.decay import simulate_decay_step
from aerospace.satellite.satellite import Satellite


def test_altitude_decay():
    satellite = Satellite(
        name="TestSat",
        mass_kg=500,
        cross_sectional_area_m2=4,
        drag_coefficient=2.2,
        altitude_m=400_000,
    )

    result = simulate_decay_step(
        altitude_m=satellite.altitude_m,
        mass_kg=satellite.mass_kg,
        drag_coefficient=satellite.drag_coefficient,
        cross_sectional_area_m2=satellite.cross_sectional_area_m2,
        timestep_s=10,
    )

    assert result["altitude_m"] < satellite.altitude_m
    assert result["velocity_ms"] > 0
    assert result["drag_force_n"] > 0
    assert result["decay_rate"] > 0
