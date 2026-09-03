import pytest

from aerospace.satellite.satellite import Satellite
from simulation.core.state import SatelliteState
from simulation.satellite.maneuvers import StationKeepingManeuver
from simulation.satellite.mission_phase import SatelliteMissionPhase
from simulation.satellite.mission_profile import SatelliteMissionProfile
from simulation.satellite.simulator import SatelliteSimulation


def make_satellite():
    return Satellite(
        name="TestSat",
        mass_kg=500.0,
        cross_sectional_area_m2=4.0,
        drag_coefficient=2.2,
        altitude_m=400_000.0,
    )


def test_step_updates_state_and_phase():
    state = SatelliteState(
        satellite_name="TestSat",
        altitude_m=400_000.0,
        velocity_ms=7_700.0,
        inclination_deg=51.6,
        eccentricity=0.0007,
    )
    simulation = SatelliteSimulation(
        satellite=make_satellite(),
        initial_state=state,
        profile=SatelliteMissionProfile(
            maneuvers=[
                StationKeepingManeuver(
                    target_altitude_m=408_000.0,
                    tolerance_m=100.0,
                )
            ]
        ),
        timestep_s=60.0,
    )

    result = simulation.step()

    assert result.time_s == pytest.approx(60.0)
    assert state.time_s == pytest.approx(60.0)
    assert result.phase == SatelliteMissionPhase.STATION_KEEPING
    assert state.phase == SatelliteMissionPhase.STATION_KEEPING
    assert result.orbital_period_s > 0.0
    assert result.semi_major_axis_m > 0.0
    assert result.orbital_energy_j_kg < 0.0


def test_simulation_owns_profile_not_raw_maneuvers():
    state = SatelliteState(
        satellite_name="TestSat",
        altitude_m=400_000.0,
        velocity_ms=7_700.0,
        inclination_deg=51.6,
        eccentricity=0.0007,
    )
    simulation = SatelliteSimulation(
        satellite=make_satellite(),
        initial_state=state,
        maneuvers=[
            StationKeepingManeuver(
                target_altitude_m=408_000.0,
                tolerance_m=100.0,
            )
        ],
        timestep_s=60.0,
    )

    result = simulation.step()

    assert result.phase == SatelliteMissionPhase.STATION_KEEPING
    assert state.phase == SatelliteMissionPhase.STATION_KEEPING
