from simulation.scenario_runner import run_aircraft_scenario
from simulation.scenarios import AircraftScenario

scenario = AircraftScenario(
    name="F16 Cruise",
    aircraft_name="F-16",
    velocity_ms=250,
    duration_seconds=3600,
    timestep_seconds=60,
)

results = run_aircraft_scenario(scenario, "datasets/aircraft/military.csv")

print(f"Records generated: {len(results)}")
print(results[0])
print(results[-1])
