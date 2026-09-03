from analytics.exports.csv_exporter import export_csv
from scripts.load_satellites import load_satellite_dataset
from simulation.core.state import SatelliteState
from simulation.satellite.mission_profile import SatelliteMissionProfile
from simulation.satellite.simulator import (
    SatelliteSimulation,
)
from simulation.scenarios.constellation import (
    ConstellationSimulation,
)

satellites = load_satellite_dataset("datasets/satellites/satellites.csv")

iss = satellites["ISS"]
sat1 = satellites["TESTSAT-1"]
sat2 = satellites["TESTSAT-2"]

simulations = [
    SatelliteSimulation(
        satellite=iss,
        initial_state=SatelliteState(
            satellite_name="ISS",
            altitude_m=iss.altitude_m,
            inclination_deg=51.6,
            eccentricity=0.0007,
        ),
        profile=SatelliteMissionProfile(),
        timestep_s=60,
    ),
    SatelliteSimulation(
        satellite=sat1,
        initial_state=SatelliteState(
            satellite_name="TESTSAT-1",
            altitude_m=sat1.altitude_m,
            inclination_deg=53.0,
            eccentricity=0.0001,
        ),
        profile=SatelliteMissionProfile(),
        timestep_s=60,
    ),
    SatelliteSimulation(
        satellite=sat2,
        initial_state=SatelliteState(
            satellite_name="TESTSAT-2",
            altitude_m=sat2.altitude_m,
            inclination_deg=97.6,
            eccentricity=0.001,
        ),
        profile=SatelliteMissionProfile(),
        timestep_s=60,
    ),
]

constellation = ConstellationSimulation(simulations=simulations)

results = constellation.run_step_count(1000)

export_csv(
    results,
    "outputs/constellation.csv",
)
