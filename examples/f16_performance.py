from analytics.exports.csv_exporter import export_csv
from scripts.load_aircraft import load_aircraft_dataset
from simulation.aircraft_simulator import AircraftSimulation
from simulation.state import AircraftState

aircraft = load_aircraft_dataset("datasets/aircraft/military.csv")

f16 = aircraft["F-16"]

state = AircraftState(
    altitude_m=0,
    velocity_ms=250,
    fuel_kg=3000,
)

simulation = AircraftSimulation(
    aircraft=f16,
    initial_state=state,
    timestep_s=1,
)

results = simulation.run_step_count(1000)

export_csv(results, "outputs/f16_performance.csv")
