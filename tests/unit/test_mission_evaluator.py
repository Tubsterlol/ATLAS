import pytest

from simulation.mission_evaluator import MissionEvaluator
from simulation.mission_phase import MissionPhase
from simulation.telemetry import TelemetryRecord


def test_evaluator_rejects_empty_telemetry():
    evaluator = MissionEvaluator()

    with pytest.raises(ValueError) as excinfo:
        evaluator.evaluate([])

    assert str(excinfo.value) == "Cannot evaluate mission without telemetry"


def test_evaluator_calculates_mission_result():
    telemetry = [
        TelemetryRecord(
            time_s=0.0,
            altitude_m=0.0,
            velocity_ms=250.0,
            fuel_kg=3000.0,
            climb_rate_ms=12.0,
            heading_deg=90.0,
            alpha_deg=10.0,
            phase=MissionPhase.TAKEOFF,
        ),
        TelemetryRecord(
            time_s=100.0,
            altitude_m=1000.0,
            velocity_ms=300.0,
            fuel_kg=2500.0,
            climb_rate_ms=15.0,
            heading_deg=90.0,
            alpha_deg=6.0,
            phase=MissionPhase.CLIMB,
        ),
        TelemetryRecord(
            time_s=200.0,
            altitude_m=0.0,
            velocity_ms=150.0,
            fuel_kg=2000.0,
            climb_rate_ms=-3.0,
            heading_deg=90.0,
            alpha_deg=8.0,
            phase=MissionPhase.LANDING,
        ),
    ]

    evaluator = MissionEvaluator()

    result = evaluator.evaluate(telemetry)

    assert result.completed is True
    assert result.final_phase == MissionPhase.LANDING
    assert result.flight_time_s == 200.0
    assert result.fuel_consumed_kg == 1000.0
    assert result.final_altitude_m == 0.0
    assert result.final_velocity_ms == 150.0


def test_evaluator_marks_non_landing_mission_incomplete():
    telemetry = [
        TelemetryRecord(
            time_s=0.0,
            altitude_m=0.0,
            velocity_ms=250.0,
            fuel_kg=3000.0,
            climb_rate_ms=12.0,
            heading_deg=90.0,
            alpha_deg=10.0,
            phase=MissionPhase.TAKEOFF,
        ),
        TelemetryRecord(
            time_s=100.0,
            altitude_m=5000.0,
            velocity_ms=300.0,
            fuel_kg=2500.0,
            climb_rate_ms=15.0,
            heading_deg=90.0,
            alpha_deg=6.0,
            phase=MissionPhase.CLIMB,
        ),
    ]

    result = MissionEvaluator().evaluate(telemetry)

    assert result.completed is False
    assert result.final_phase == MissionPhase.CLIMB
