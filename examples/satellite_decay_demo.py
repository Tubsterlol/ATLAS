from aerospace.satellite.models.satellite import Satellite
from simulation.satellite_mission_profile import SatelliteMissionProfile
from simulation.satellite_simulator import SatelliteSimulation
from simulation.state import SatelliteState

satellite = Satellite(
    name="ATLAS-1",
    mass_kg=500,
    cross_sectional_area_m2=4,
    drag_coefficient=2.2,
    altitude_m=400_000,
)

simulation = SatelliteSimulation(
    satellite=satellite,
    initial_state=SatelliteState(
        satellite_name="ATLAS-1",
        altitude_m=satellite.altitude_m,
        velocity_ms=0.0,
        inclination_deg=0.0,
        eccentricity=0.0,
    ),
    profile=SatelliteMissionProfile(),
    timestep_s=60,
)

results = simulation.run_step_count(10)

for result in results:
    print(result)
