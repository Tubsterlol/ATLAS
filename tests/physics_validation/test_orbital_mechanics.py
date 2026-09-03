from aerospace.satellite.orbital.vis_viva import orbital_velocity


def test_leo_orbital_velocity():
    velocity = orbital_velocity(400_000)

    # ISS-like orbit
    assert 7600 < velocity < 7800
