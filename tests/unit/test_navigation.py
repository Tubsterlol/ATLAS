import pytest

from simulation.aircraft.navigation import NavigationCalculator, Waypoint


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

    with pytest.raises(AttributeError):
        waypoint.altitude_m = 6000.0


def test_distance_to_waypoint():
    waypoint = Waypoint(
        latitude_deg=0.0,
        longitude_deg=1.0,
        altitude_m=0.0,
    )

    distance = NavigationCalculator.distance_to_waypoint(
        latitude_deg=0.0,
        longitude_deg=0.0,
        waypoint=waypoint,
    )

    assert 111_000.0 < distance < 112_000.0


def test_bearing_to_waypoint():
    waypoint = Waypoint(
        latitude_deg=1.0,
        longitude_deg=0.0,
        altitude_m=0.0,
    )

    bearing = NavigationCalculator.bearing_to_waypoint(
        latitude_deg=0.0,
        longitude_deg=0.0,
        waypoint=waypoint,
    )

    assert bearing == 0.0


def test_bearing_to_east():
    waypoint = Waypoint(
        latitude_deg=0.0,
        longitude_deg=1.0,
        altitude_m=0.0,
    )

    bearing = NavigationCalculator.bearing_to_waypoint(
        latitude_deg=0.0,
        longitude_deg=0.0,
        waypoint=waypoint,
    )

    assert bearing == 90.0
