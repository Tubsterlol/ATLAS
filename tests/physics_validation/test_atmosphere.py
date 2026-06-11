from aerospace.atmosphere.density import atmospheric_density


def test_density_decreases():

    sea_level = atmospheric_density(0)

    high_altitude = atmospheric_density(10_000)

    assert high_altitude < sea_level
