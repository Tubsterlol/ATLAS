from simulation.navigation import Waypoint


def test_waypoint_stores_coordinates():
    waypoint = Waypoint(
        latitude_deg=18.5204,
        longitude_deg=73.8567,
        altitude_m=5000.0,
    )

    assert waypoint.latitude_deg == 18.5204
    assert waypoint.longitude_deg == 73.8567
    assert waypoint.altitude_m == 5000.0


def test_waypoint_is_immutable():
    waypoint = Waypoint(
        latitude_deg=18.5204,
        longitude_deg=73.8567,
        altitude_m=5000.0,
    )

    try:
        waypoint.altitude_m = 6000.0
        assert False
    except AttributeError:
        pass
