import pytest

from aerospace.aircraft.geometry.geometry import AircraftGeometry
from aerospace.aircraft.models.aircraft import Aircraft
from aerospace.satellite.models.satellite import Satellite
from simulation.base import BaseSimulation
from simulation.state import AircraftState, SimulationState


def geometry():
    return AircraftGeometry(15.0, 25.0, 2.0, 0.5, 20.0, 12.0, 1.5, 5.0, 3.0)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("wing_area_m2", 0.0, "wing_area_m2 must be greater than zero"),
        ("taper_ratio", 1.1, "taper_ratio must be between 0.0 and 1.0"),
    ],
)
def test_geometry_rejects_non_physical_values(field, value, message):
    values = dict(
        wing_span_m=15.0,
        wing_area_m2=25.0,
        mean_chord_m=2.0,
        taper_ratio=0.5,
        sweep_deg=20.0,
        fuselage_length_m=12.0,
        fuselage_diameter_m=1.5,
        horizontal_tail_area_m2=5.0,
        vertical_tail_area_m2=3.0,
    )
    values[field] = value

    with pytest.raises(ValueError, match=message):
        AircraftGeometry(**values)


def test_aircraft_requires_positive_mass():
    with pytest.raises(ValueError, match="mass_kg must be greater than zero"):
        Aircraft("Demo", "ATLAS", 0.0, 0.02, 20_000.0, 300.0, 0.5, geometry())


def test_satellite_rejects_negative_altitude():
    with pytest.raises(ValueError, match="altitude_m must be non-negative"):
        Satellite("Demo", 100.0, -1.0, 2.2, 1.0)


def test_states_require_valid_timestep_and_non_negative_fuel():
    with pytest.raises(ValueError, match="timestep_s must be greater than zero"):
        SimulationState(timestep_s=0.0)

    with pytest.raises(ValueError, match="fuel_kg must be non-negative"):
        AircraftState(fuel_kg=-1.0)


def test_simulation_rejects_negative_step_counts():
    with pytest.raises(ValueError, match="steps must be a non-negative integer"):
        BaseSimulation().run_step_count(-1)
