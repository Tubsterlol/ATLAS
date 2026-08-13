from scripts.load_aircraft import load_aircraft_dataset
from scripts.load_satellites import load_satellite_dataset
from simulation.aircraft_simulator import AircraftSimulation
from simulation.satellite_mission_profile import SatelliteMissionProfile
from simulation.satellite_simulator import SatelliteSimulation
from simulation.scenarios import (
    AircraftScenario,
    SatelliteScenario,
)
from simulation.state import (
    AircraftState,
    SatelliteState,
)


def run_aircraft_scenario(
    scenario: AircraftScenario,
    dataset_path: str,
):
    aircraft_dataset = load_aircraft_dataset(dataset_path)

    aircraft = aircraft_dataset[scenario.aircraft_name]

    state = AircraftState(
        altitude_m=scenario.initial_altitude_m,
        velocity_ms=scenario.initial_velocity_ms,
        fuel_kg=scenario.initial_fuel_kg,
        climb_rate_ms=scenario.climb_rate_ms,
        heading_deg=scenario.heading_deg,
        alpha_deg=scenario.alpha_deg,
    )

    simulation = AircraftSimulation(
        aircraft=aircraft,
        initial_state=state,
        profile=scenario.profile,
        timestep_s=scenario.timestep_s,
    )

    steps = int(scenario.duration_seconds / scenario.timestep_s)

    return simulation.run_step_count(steps)


def run_satellite_scenario(
    scenario: SatelliteScenario,
    dataset_path: str,
):
    satellite_dataset = load_satellite_dataset(dataset_path)

    satellite = satellite_dataset[scenario.satellite_name]

    state = SatelliteState(
        satellite_name=satellite.name,
        altitude_m=scenario.initial_altitude_m,
        velocity_ms=scenario.initial_velocity_ms,
        inclination_deg=scenario.inclination_deg,
        eccentricity=scenario.eccentricity,
    )

    simulation = SatelliteSimulation(
        satellite=satellite,
        initial_state=state,
        profile=scenario.profile or SatelliteMissionProfile(
            maneuvers=scenario.maneuvers,
        ),
        timestep_s=scenario.timestep_s,
    )

    steps = int((scenario.duration_hours * 3600) / scenario.timestep_s)

    return simulation.run_step_count(steps)
