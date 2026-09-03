from analytics.exports.csv_exporter import export_csv
from scripts.load_satellites import load_satellite_dataset
from simulation.core.state import SatelliteState
from simulation.satellite.maneuvers import StationKeepingManeuver
from simulation.satellite.mission_profile import SatelliteMissionProfile
from simulation.satellite.simulator import SatelliteSimulation

satellites = load_satellite_dataset("datasets/satellites/satellites.csv")

iss = satellites["ISS"]

state = SatelliteState(
    satellite_name="ISS",
    altitude_m=iss.altitude_m,
    velocity_ms=0.0,
    inclination_deg=51.6,
    eccentricity=0.0007,
)

maneuvers = [
    StationKeepingManeuver(
        target_altitude_m=408000,
        tolerance_m=100,
    )
]

simulation = SatelliteSimulation(
    satellite=iss,
    initial_state=state,
    profile=SatelliteMissionProfile(maneuvers=maneuvers),
    timestep_s=60,
)

results = simulation.run_step_count(1000)

export_csv(
    results,
    "outputs/iss_decay.csv",
)
