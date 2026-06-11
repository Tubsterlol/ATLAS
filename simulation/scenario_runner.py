from scripts.load_aircraft import load_aircraft_dataset
from scripts.load_satellites import load_satellite_dataset
from simulation.aircraft_simulator import AircraftSimulation
from simulation.satellite_simulator import SatelliteSimulation
from simulation.scenarios import AircraftScenario, SatelliteScenario


def run_aircraft_scenario(
    scenario: AircraftScenario,
    dataset_path: str
):
    aircraft_dataset = load_aircraft_dataset(dataset_path)

    aircraft = aircraft_dataset[
        scenario.aircraft_name
    ]

    simulation = AircraftSimulation(
        aircraft=aircraft,
        velocity_ms=scenario.velocity_ms,
        timestep_s=scenario.timestep_seconds
    )

    steps = int(
        scenario.duration_seconds
        / scenario.timestep_seconds
    )

    return simulation.run_step_count(steps)


def run_satellite_scenario(
    scenario: SatelliteScenario,
    dataset_path: str
):
    satellite_dataset = load_satellite_dataset(
        dataset_path
    )

    satellite = satellite_dataset[
        scenario.satellite_name
    ]

    simulation = SatelliteSimulation(
        satellite=satellite,
        timestep_s=scenario.timestep_seconds
    )

    steps = int(
        (scenario.duration_hours * 3600)
        / scenario.timestep_seconds
    )

    return simulation.run_step_count(steps)