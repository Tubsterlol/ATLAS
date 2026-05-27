from aerospace.aircraft.aircraft import (
    Aircraft
)

from simulation.aircraft_simulator import (
    AircraftSimulation
)


aircraft = Aircraft(
    name="F-16",
    manufacturer="Lockheed Martin",
    mass_kg=12_000,
    wing_area_m2=27.87,
    wingspan_m=9.96,
    drag_coefficient=0.02,
    lift_coefficient=1.4,
    thrust_n=129_000,
    max_speed_ms=660
)

simulation = AircraftSimulation(
    aircraft=aircraft,
    velocity_ms=250,
    timestep_s=1
)

results = simulation.run_step_count(
    5
)

for result in results:
    print(result)
