from simulation.maneuvers import (
    OrbitRaiseManeuver,
    StationKeepingManeuver,
)
from simulation.satellite_mission_phase import SatelliteMissionPhase
from simulation.satellite_mission_profile import SatelliteMissionProfile
from simulation.state import SatelliteState


def test_satellite_profile_defaults_to_coast():
    profile = SatelliteMissionProfile()

    state = SatelliteState(
        satellite_name="TestSat",
        altitude_m=400_000.0,
        velocity_ms=7_700.0,
        inclination_deg=51.6,
        eccentricity=0.0007,
    )

    profile.update(state)

    assert state.phase == SatelliteMissionPhase.COAST
    assert profile.current_phase == SatelliteMissionPhase.COAST
    assert profile.mission_targets.phase == SatelliteMissionPhase.COAST
    assert profile.mission_targets.target_altitude_m == 400_000.0


def test_orbit_raise_maneuver_sets_transfer_phase_once():
    profile = SatelliteMissionProfile(
        maneuvers=[
            OrbitRaiseManeuver(
                time_s=10.0,
                delta_v_ms=20.0,
            )
        ]
    )

    state = SatelliteState(
        satellite_name="TestSat",
        time_s=10.0,
        altitude_m=400_000.0,
        velocity_ms=7_700.0,
        inclination_deg=51.6,
        eccentricity=0.0007,
    )

    before = state.altitude_m

    profile.update(state)

    assert state.altitude_m != before
    assert state.phase == SatelliteMissionPhase.TRANSFER
    assert profile.current_phase == SatelliteMissionPhase.TRANSFER
    assert len(profile.executed_maneuvers) == 1


def test_station_keeping_sets_target_and_phase():
    profile = SatelliteMissionProfile(
        maneuvers=[
            StationKeepingManeuver(
                target_altitude_m=408_000.0,
                tolerance_m=100.0,
            )
        ]
    )

    state = SatelliteState(
        satellite_name="ISS",
        altitude_m=400_000.0,
        velocity_ms=7_700.0,
        inclination_deg=51.6,
        eccentricity=0.0007,
    )

    profile.update(state)

    assert state.phase == SatelliteMissionPhase.STATION_KEEPING
    assert profile.current_phase == SatelliteMissionPhase.STATION_KEEPING
    assert profile.mission_targets.phase == SatelliteMissionPhase.STATION_KEEPING
    assert profile.mission_targets.target_altitude_m == 408_000.0
