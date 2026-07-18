import pytest

from simulation.mission_phase import MissionPhase
from simulation.mission_profile import MissionProfile
from simulation.state import AircraftState


@pytest.fixture
def mission_profile():
    return MissionProfile(
        cruise_altitude_m=10000.0,
        climb_rate_ms=15.0,
        descent_rate_ms=8.0,
        reserve_fuel_kg=500.0,
    )


@pytest.fixture
def aircraft_state():
    return AircraftState(
        altitude_m=0.0,
        velocity_ms=250.0,
        fuel_kg=3000.0,
        climb_rate_ms=0.0,
        heading_deg=90.0,
        alpha_deg=5.0,
    )


def test_mission_starts_in_takeoff(mission_profile):
    assert mission_profile.current_phase == MissionPhase.TAKEOFF


def test_takeoff_transitions_to_climb(
    mission_profile,
    aircraft_state,
):
    aircraft_state.altitude_m = 200.0

    mission_profile.update(aircraft_state)

    assert mission_profile.current_phase == MissionPhase.CLIMB
    assert aircraft_state.phase == MissionPhase.CLIMB


def test_climb_transitions_to_cruise(
    mission_profile,
    aircraft_state,
):
    mission_profile.current_phase = MissionPhase.CLIMB

    aircraft_state.altitude_m = 10000.0

    mission_profile.update(aircraft_state)

    assert mission_profile.current_phase == MissionPhase.CRUISE
    assert aircraft_state.phase == MissionPhase.CRUISE


def test_cruise_transitions_to_descent(
    mission_profile,
    aircraft_state,
):
    mission_profile.current_phase = MissionPhase.CRUISE

    aircraft_state.altitude_m = 10000.0
    aircraft_state.fuel_kg = 400.0

    mission_profile.update(aircraft_state)

    assert mission_profile.current_phase == MissionPhase.DESCENT
    assert aircraft_state.phase == MissionPhase.DESCENT


def test_descent_transitions_to_landing(
    mission_profile,
    aircraft_state,
):
    mission_profile.current_phase = MissionPhase.DESCENT

    aircraft_state.altitude_m = 500.0

    mission_profile.update(aircraft_state)

    assert mission_profile.current_phase == MissionPhase.LANDING
    assert aircraft_state.phase == MissionPhase.LANDING


def test_complete_mission_sequence(
    mission_profile,
    aircraft_state,
):
    history = []

    history.append(mission_profile.current_phase)

    aircraft_state.altitude_m = 200.0
    mission_profile.update(aircraft_state)
    history.append(mission_profile.current_phase)

    aircraft_state.altitude_m = 10000.0
    mission_profile.update(aircraft_state)
    history.append(mission_profile.current_phase)

    aircraft_state.fuel_kg = 400.0
    mission_profile.update(aircraft_state)
    history.append(mission_profile.current_phase)

    aircraft_state.altitude_m = 500.0
    mission_profile.update(aircraft_state)
    history.append(mission_profile.current_phase)

    assert history == [
        MissionPhase.TAKEOFF,
        MissionPhase.CLIMB,
        MissionPhase.CRUISE,
        MissionPhase.DESCENT,
        MissionPhase.LANDING,
    ]
