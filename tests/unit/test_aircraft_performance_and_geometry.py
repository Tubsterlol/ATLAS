import pytest

from aerospace.aircraft.geometry.geometry_calculations import (
    aspect_ratio,
    mean_chord,
    wing_loading,
)
from aerospace.aircraft.performance.flight_conditions import (
    mach_number,
    reynolds_number,
    speed_of_sound,
)
from aerospace.aircraft.performance.performance import (
    aircraft_thrust_to_weight,
    aircraft_weight,
    aircraft_wing_loading,
    climb_rate,
    stall_speed,
)
from aerospace.physics.constants import EARTH_STANDARD_GRAVITY


def test_geometry_calculations_return_standard_planform_values():
    assert aspect_ratio(wing_span_m=30.0, wing_area_m2=100.0) == pytest.approx(9.0)
    assert mean_chord(wing_area_m2=100.0, wing_span_m=30.0) == pytest.approx(
        100.0 / 30.0
    )
    assert wing_loading(weight_n=98_066.5, wing_area_m2=100.0) == pytest.approx(980.665)


def test_weight_and_wing_loading_use_standard_gravity():
    assert aircraft_weight(10_000.0) == pytest.approx(10_000.0 * EARTH_STANDARD_GRAVITY)
    assert aircraft_wing_loading(10_000.0, 50.0) == pytest.approx(1_961.33)


def test_stall_speed_decreases_with_more_wing_area():
    small_wing = stall_speed(mass_kg=10_000.0, wing_area_m2=25.0, lift_coefficient=1.5)
    large_wing = stall_speed(mass_kg=10_000.0, wing_area_m2=50.0, lift_coefficient=1.5)

    assert small_wing > large_wing
    assert large_wing == pytest.approx(46.204, abs=0.001)


def test_thrust_to_weight_and_climb_rate_use_excess_thrust():
    assert aircraft_thrust_to_weight(
        thrust_n=98_066.5, mass_kg=10_000.0
    ) == pytest.approx(1.0)
    assert climb_rate(
        thrust_n=120_000.0,
        drag_n=20_000.0,
        velocity_ms=100.0,
        mass_kg=10_000.0,
    ) == pytest.approx(101.9716, abs=0.0001)


def test_flight_conditions_match_standard_atmosphere_values():
    assert speed_of_sound(288.15) == pytest.approx(340.29, abs=0.01)
    assert mach_number(velocity_ms=340.29, temperature_k=288.15) == pytest.approx(
        1.0, abs=0.001
    )
    assert reynolds_number(
        density=1.225,
        velocity_ms=100.0,
        characteristic_length_m=2.0,
    ) == pytest.approx(13_535_911.6, abs=0.1)
