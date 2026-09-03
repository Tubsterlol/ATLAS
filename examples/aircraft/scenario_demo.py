from simulation.scenarios.definitions import AircraftScenario
from simulation.scenarios.runner import run_aircraft_scenario

scenario = AircraftScenario(
    name="Takeoff",
    aircraft_name="F-16",
    initial_altitude_m=0.0,
    initial_velocity_ms=250.0,
    initial_fuel_kg=3000.0,
    climb_rate_ms=15.0,
    heading_deg=90.0,
    alpha_deg=5.0,
    duration_seconds=1000.0,
    timestep_s=1.0,
)

results = run_aircraft_scenario(
    scenario,
    "datasets/aircraft/military.csv",
)

print(f"Records generated: {len(results)}")
print(results[0])
print(results[-1])
