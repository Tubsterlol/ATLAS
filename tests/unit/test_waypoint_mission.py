from simulation.mission_phase import MissionPhase
from simulation.state import AircraftState
from simulation.waypoint import Waypoint
from simulation.waypoint_mission import WaypointMission


def test_waypoint_mission_updates_heading():
    mission = WaypointMission(
        [
            Waypoint("WP1", 1000.0, 0.0),
        ]
    )

    state = AircraftState(
        altitude_m=5000.0,
        velocity_ms=250.0,
        fuel_kg=3000.0,
        heading_deg=0.0,
        climb_rate_ms=15.0,
        alpha_deg=5.0,
    )

    mission.update(state)

    assert state.heading_deg == 90.0


def test_waypoint_mission_does_not_modify_phase():
    mission = WaypointMission(
        [
            Waypoint("WP1", 50000.0, 0.0),
        ]
    )

    state = AircraftState(
        altitude_m=12000.0,
        velocity_ms=250.0,
        fuel_kg=3000.0,
        heading_deg=0.0,
        climb_rate_ms=15.0,
        alpha_deg=5.0,
        phase=MissionPhase.CLIMB,
    )

    mission.update(state)

    assert state.phase == MissionPhase.CLIMB
    assert state.climb_rate_ms == 15.0


def test_waypoint_is_reached():
    mission = WaypointMission(
        [
            Waypoint("WP1", 500.0, 0.0),
        ]
    )

    state = AircraftState(
        altitude_m=5000.0,
        velocity_ms=250.0,
        fuel_kg=3000.0,
        x_m=0.0,
        y_m=0.0,
        heading_deg=0.0,
        climb_rate_ms=15.0,
        alpha_deg=5.0,
    )

    mission.update(state)

    assert mission.completed is True
    assert mission.current_index == 1