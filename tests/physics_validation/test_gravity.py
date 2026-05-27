from aerospace.physics.gravity import (
    gravity_at_altitude
)


def test_surface_gravity():

    g = gravity_at_altitude(0)

    assert 9.7 < g < 9.9