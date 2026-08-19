import math

import pytest

from aerospace.aircraft.aerodynamics.drag import aircraft_drag
from aerospace.aircraft.aerodynamics.induced_drag import induced_drag_coefficient
from aerospace.aircraft.aerodynamics.lift import aircraft_lift
from aerospace.aircraft.aerodynamics.lift_curve import lift_coefficient
from aerospace.aircraft.aerodynamics.stall import lift_coefficient_with_stall
from aerospace.aircraft.aerodynamics.trim import trim_angle_of_attack
from aerospace.aircraft.aerodynamics.wave_drag import wave_drag_coefficient


def test_aircraft_lift_uses_dynamic_pressure_equation():
    lift = aircraft_lift(
        density=1.225,
        velocity_ms=100.0,
        lift_coefficient=1.2,
        wing_area_m2=20.0,
    )

    assert lift == pytest.approx(147_000.0)


def test_aircraft_drag_uses_reference_area_and_drag_coefficient():
    drag = aircraft_drag(
        density=1.225,
        velocity_ms=100.0,
        drag_coefficient=0.02,
        reference_area_m2=20.0,
    )

    assert drag == pytest.approx(2_450.0)


def test_induced_drag_coefficient_matches_standard_formula():
    coefficient = induced_drag_coefficient(
        lift_coefficient=0.5,
        aspect_ratio=10.0,
        oswald_efficiency=0.8,
    )

    assert coefficient == pytest.approx(0.25 / (math.pi * 0.8 * 10.0))


def test_lift_curve_is_limited_to_maximum_lift_coefficient():
    assert lift_coefficient(alpha_deg=0.0) == pytest.approx(0.2)
    assert lift_coefficient(alpha_deg=30.0) == pytest.approx(1.6)


def test_stall_model_reduces_lift_after_critical_angle():
    at_stall = lift_coefficient_with_stall(alpha_deg=15.0)
    post_stall = lift_coefficient_with_stall(alpha_deg=20.0)
    deep_stall = lift_coefficient_with_stall(alpha_deg=100.0)

    assert at_stall == pytest.approx(1.6)
    assert post_stall == pytest.approx(1.2)
    assert deep_stall == pytest.approx(0.2)


def test_trim_angle_returns_zero_without_dynamic_pressure():
    assert (
        trim_angle_of_attack(
            required_lift_n=10_000.0,
            density=1.225,
            velocity_ms=0.0,
            wing_area_m2=20.0,
        )
        == 0.0
    )


def test_trim_angle_recreates_requested_lift_coefficient():
    alpha_deg = trim_angle_of_attack(
        required_lift_n=73_500.0,
        density=1.225,
        velocity_ms=100.0,
        wing_area_m2=20.0,
    )

    assert alpha_deg == pytest.approx(math.degrees((0.6 - 0.2) / 5.7))


@pytest.mark.parametrize(
    ("mach", "expected"),
    [
        (0.79, 0.0),
        (0.90, 0.075),
        (1.10, 0.20),
        (1.20, 0.25),
        (2.0, 0.25),
    ],
)
def test_wave_drag_has_expected_regime_boundaries(mach, expected):
    assert wave_drag_coefficient(mach) == pytest.approx(expected)
