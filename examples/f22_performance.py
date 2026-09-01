from analytics.exports.csv_exporter import export_csv
from scripts.load_aircraft import load_aircraft_dataset
from simulation.aircraft_simulator import AircraftSimulation
from simulation.mission_profile import MissionProfile
from simulation.state import AircraftState
from simulation.waypoint import Waypoint
from simulation.waypoint_mission import WaypointMission

aircraft = load_aircraft_dataset("datasets/aircraft/military.csv")

f22 = aircraft["F-22"]

waypoint_mission = WaypointMission(
    [
        Waypoint("WP1", 50000, 0),
        Waypoint("WP2", 50000, 50000),
        Waypoint("WP3", 0, 50000),
    ]
)

mission_profile = MissionProfile(
    cruise_altitude_m=10000.0,
    climb_rate_ms=15.0,
    descent_rate_ms=8.0,
    reserve_fuel_kg=500.0,
    navigation=waypoint_mission,
)
state = AircraftState(
    altitude_m=0,
    velocity_ms=250,
    fuel_kg=f22.mass_kg * 0.2,
    climb_rate_ms=15,
    alpha_deg=5.0,
)

simulation = AircraftSimulation(
    aircraft=f22,
    initial_state=state,
    timestep_s=1,
    profile=mission_profile,
)

results = simulation.run_step_count(1000)

export_csv(results, "outputs/f22_performance.csv")
