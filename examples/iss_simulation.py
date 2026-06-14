from analytics.exports.csv_exporter import export_csv
from scripts.load_satellites import load_satellite_dataset
from simulation.satellite_simulator import SatelliteSimulation
from simulation.state import SatelliteState

satellites = load_satellite_dataset("datasets/satellites/satellites.csv")

iss = satellites["ISS"]

state = SatelliteState(time_s=60.0, altitude_m=40000, velocity_ms=7668.0)

simulation = SatelliteSimulation(
    satellite=iss,
    timestep_s=1.0,
)

results = simulation.run_step_count(1000)

export_csv(results, "outputs/iss_decay.csv")
