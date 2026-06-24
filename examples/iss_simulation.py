from analytics.exports.csv_exporter import export_csv
from scripts.load_satellites import load_satellite_dataset
from simulation.maneuver import OrbitalManeuver
from simulation.satellite_simulator import SatelliteSimulation
from simulation.state import SatelliteState

satellites = load_satellite_dataset("datasets/satellites/satellites.csv")

iss = satellites["ISS"]

maneuvers = [
    OrbitalManeuver(
        time_s=3600,
        delta_v_ms=25,
    ),
]

state = SatelliteState(
    altitude_m=iss.altitude_m,
    velocity_ms=0.0,
    inclination_deg=51.6,
    eccentricity=0.0007,
)

simulation = SatelliteSimulation(
    satellite=iss,
    initial_state=state,
    maneuvers=maneuvers,
    timestep_s=60,
)

results = simulation.run_step_count(1000)

export_csv(
    results,
    "outputs/iss_decay.csv",
)
