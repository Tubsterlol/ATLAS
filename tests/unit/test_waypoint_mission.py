import pytest

from simulation.mission_phase import MissionPhase
from simulation.state import AircraftState
from simulation.waypoint import Waypoint
from simulation.waypoint_mission import WaypointMission


def test_waypoint_mission_updates_heading_towards_target():
    mission = WaypointMission([Waypoint("WP1", 1000.0, 0.0)])
    state = AircraftState(x_m=0.0, y_m=0.0)

    mission.update(state)

    assert state.heading_deg == pytest.approx(90.0)


def test_waypoint_mission_ramps_down_climb_rate_as_altitude_increases():
    mission = WaypointMission(
        [Waypoint("WP1", 0.0, 1000.0)],
        cruise_altitude_m=10000.0,
        max_climb_rate_ms=15.0,
    )
    state = AircraftState(x_m=0.0, y_m=0.0, altitude_m=0.0)

    mission.update(state)
    assert state.climb_rate_ms == pytest.approx(15.0)
    assert state.phase == MissionPhase.CLIMB

    state.altitude_m = 5000.0
    mission.update(state)
    assert state.climb_rate_ms == pytest.approx(7.5)
    assert state.phase == MissionPhase.CLIMB

    state.altitude_m = 10000.0
    mission.update(state)
    assert state.climb_rate_ms == pytest.approx(0.0)
    assert state.phase == MissionPhase.CRUISE
