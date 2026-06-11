from aerospace.satellite.satellite import Satellite
from simulation.satellite_simulator import SatelliteSimulation

satellite = Satellite(
    name="ATLAS-1",
    mass_kg=500,
    cross_sectional_area_m2=4,
    drag_coefficient=2.2,
    altitude_m=400_000,
)

simulation = SatelliteSimulation(satellite=satellite, timestep_s=60)

results = simulation.run_step_count(10)

for result in results:
    print(result)
