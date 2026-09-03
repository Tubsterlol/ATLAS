import pytest

from simulation.aircraft.waypoint import Waypoint
from simulation.aircraft.waypoint_mission import WaypointMission


def test_current_waypoint():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
            Waypoint("WP2", 2000.0, 0.0),
        ]
    )

    assert mission.current_index == 0
    assert mission.current_waypoint.id == "WP1"
    assert mission.completed is False
    assert mission.waypoint_count == 2
    assert mission.reach_radius_m == 1000.0


def test_previous_and_remaining_waypoints():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
            Waypoint("WP2", 2000.0, 0.0),
            Waypoint("WP3", 3000.0, 0.0),
        ]
    )

    assert mission.previous_waypoint is None
    assert [waypoint.id for waypoint in mission.remaining_waypoints] == [
        "WP2",
        "WP3",
    ]


def test_completed_mission_has_no_current_waypoint():
    mission = WaypointMission(
        [
            Waypoint("WP1", 500.0, 0.0),
        ]
    )

    mission.current_index = 1

    assert mission.completed is True
    assert mission.current_waypoint is None


def test_current_waypoint_changes_with_index():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
            Waypoint("WP2", 2000.0, 0.0),
        ]
    )

    assert mission.current_waypoint.id == "WP1"

    mission.current_index = 1

    assert mission.current_waypoint.id == "WP2"


def test_update_advances_on_reach_radius():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
            Waypoint("WP2", 2000.0, 0.0),
        ],
        reach_radius_m=10.0,
    )

    state = type("State", (), {"x_m": 995.0, "y_m": 0.0, "heading_deg": 90.0})()

    mission.update(state)

    assert mission.current_index == 1
    assert mission.previous_waypoint.id == "WP1"
    assert mission.current_waypoint.id == "WP2"
    assert state.heading_deg == 90.0


def test_final_waypoint_completes_mission():
    mission = WaypointMission([Waypoint("WP1", 1000.0, 0.0)], reach_radius_m=10.0)

    assert mission.is_final_waypoint is True

    state = type("State", (), {"x_m": 995.0, "y_m": 0.0, "heading_deg": 90.0})()

    mission.update(state)

    assert mission.completed is True
    assert mission.current_waypoint is None
    assert mission.previous_waypoint.id == "WP1"
    assert mission.remaining_waypoints == []


def test_empty_mission_is_completed_and_safe():
    mission = WaypointMission([])

    assert mission.completed is True


def test_reach_radius_must_be_positive():
    with pytest.raises(ValueError) as excinfo:
        WaypointMission([Waypoint("WP1", 0.0, 0.0)], reach_radius_m=0.0)

    assert "reach_radius_m" in str(excinfo.value)


def test_waypoint_mission_reports_navigation_telemetry():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
            Waypoint("WP2", 2000.0, 0.0),
        ],
        reach_radius_m=10.0,
    )

    state = type(
        "State",
        (),
        {"x_m": 0.0, "y_m": 0.0, "heading_deg": 90.0},
    )()

    status = mission.status(state)

    assert status["current_waypoint_id"] == "WP1"
    assert status["distance_to_waypoint_m"] == pytest.approx(1000.0)
    assert status["heading_error_deg"] == pytest.approx(0.0)
    assert status["remaining_waypoint_count"] == 1
    assert status["mission_completed"] is False


def test_waypoint_mission_status_tracks_completion_state():
    mission = WaypointMission(
        [Waypoint("WP1", 1000.0, 0.0)],
        reach_radius_m=10.0,
    )

    state = type(
        "State",
        (),
        {"x_m": 995.0, "y_m": 0.0, "heading_deg": 90.0},
    )()

    mission.update(state)
    status = mission.status(state)

    assert mission.completed is True
    assert status["current_waypoint_id"] is None
    assert status["remaining_waypoint_count"] == 0
    assert status["mission_completed"] is True
