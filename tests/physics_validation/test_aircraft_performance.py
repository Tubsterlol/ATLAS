from aerospace.aircraft.performance import stall_speed


def test_stall_speed():

    speed = stall_speed(mass_kg=10_000, wing_area_m2=30, lift_coefficient=1.5)

    assert speed > 0
