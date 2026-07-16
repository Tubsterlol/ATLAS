import pytest

from aerospace.aircraft.geometry.geometry import AircraftGeometry
from aerospace.aircraft.models.aircraft import Aircraft
from simulation.aircraft_simulator import AircraftSimulation
from simulation.flight_profiles import CruiseProfile
from simulation.state import AircraftState


def make_aircraft():
    return Aircraft(
        name="Test aircraft",
        manufacturer="ATLAS",
        mass_kg=2_000.0,
        drag_coefficient=0.02,
        thrust_n=20_000.0,
        max_speed_ms=300.0,
        fuel_burn_kg_s=0.5,
        geometry=AircraftGeometry(
            wing_span_m=15.0,
            wing_area_m2=25.0,
            mean_chord_m=2.0,
            taper_ratio=0.5,
            sweep_deg=20.0,
            fuselage_length_m=12.0,
            fuselage_diameter_m=1.5,
            horizontal_tail_area_m2=5.0,
            vertical_tail_area_m2=3.0,
        ),
    )


def test_step_updates_time_fuel_altitude_and_position():
    state = AircraftState(
        altitude_m=1_000.0,
        velocity_ms=100.0,
        fuel_kg=100.0,
        climb_rate_ms=5.0,
        heading_deg=90.0,
    )
    simulation = AircraftSimulation(make_aircraft(), state, timestep_s=2.0)

    result = simulation.step()

    assert result.time_s == 2.0
    assert state.time_s == 2.0
    assert state.altitude_m == pytest.approx(1_010.0)
    assert state.fuel_kg == pytest.approx(99.0)
    assert state.x_m > 200.0
    assert state.y_m == pytest.approx(0.0, abs=1e-10)
    assert result.drag_n > 0.0
    assert result.lift_n > 0.0
    assert result.reynolds_number > 0.0


def test_step_respects_speed_and_fuel_lower_bounds():
    state = AircraftState(velocity_ms=299.0, fuel_kg=0.25)
    simulation = AircraftSimulation(make_aircraft(), state, timestep_s=1.0)

    result = simulation.step()

    assert result.velocity_ms <= 300.0
    assert result.fuel_kg == 0.0


def test_profile_updates_state_before_the_aircraft_is_propagated():
    state = AircraftState(altitude_m=1_000.0, velocity_ms=100.0, fuel_kg=50.0, climb_rate_ms=10.0)
    simulation = AircraftSimulation(
        make_aircraft(), state, profile=CruiseProfile(), timestep_s=5.0
    )

    result = simulation.step()

    assert result.phase == "climb"
    assert state.climb_rate_ms == 0.0
    assert result.altitude_m == pytest.approx(1_000.0)
