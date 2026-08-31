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
            current_waypoint_id="WP1",
            remaining_waypoint_count=2,
            mission_completed=False,
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
            current_waypoint_id="WP2",
            remaining_waypoint_count=1,
            mission_completed=False,
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
            current_waypoint_id=None,
            remaining_waypoint_count=0,
            mission_completed=True,
        ),
    ]

    evaluator = MissionEvaluator()

    result = evaluator.evaluate(telemetry)

    assert result.completed is True
    assert result.failed is False
    assert result.route_completed is True
    assert result.final_phase == MissionPhase.LANDING
    assert result.flight_time_s == 200.0
    assert result.fuel_consumed_kg == 1000.0
    assert result.final_altitude_m == 0.0
    assert result.final_velocity_ms == 150.0
    assert result.current_waypoint_id is None
    assert result.remaining_waypoint_count == 0
    assert result.heading_error_deg == pytest.approx(0.0)
    assert result.failure_reasons == []


def test_evaluator_reads_route_status_from_telemetry():
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
            current_waypoint_id="WP1",
            distance_to_waypoint_m=183.0,
            heading_error_deg=12.5,
            remaining_waypoint_count=2,
            mission_completed=False,
        ),
        TelemetryRecord(
            time_s=50.0,
            altitude_m=250.0,
            velocity_ms=260.0,
            fuel_kg=2900.0,
            climb_rate_ms=12.0,
            heading_deg=102.0,
            alpha_deg=10.0,
            phase=MissionPhase.CLIMB,
            current_waypoint_id="WP1",
            distance_to_waypoint_m=12.0,
            heading_error_deg=5.0,
            remaining_waypoint_count=1,
            mission_completed=False,
        ),
    ]

    result = MissionEvaluator().evaluate(telemetry)

    assert result.current_waypoint_id == "WP1"
    assert result.distance_to_waypoint_m == pytest.approx(12.0)
    assert result.heading_error_deg == pytest.approx(5.0)
    assert result.remaining_waypoint_count == 1
    assert result.route_completed is False
    assert result.failed is True
    assert "route_not_completed" in result.failure_reasons
    assert "mission_not_landed" in result.failure_reasons


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
    assert result.failed is True
    assert result.final_phase == MissionPhase.CLIMB
    assert "mission_not_landed" in result.failure_reasons


def test_evaluator_marks_route_failure_when_mission_was_not_completed():
    telemetry = [
        TelemetryRecord(
            time_s=0.0,
            altitude_m=0.0,
            velocity_ms=250.0,
            fuel_kg=0.0,
            climb_rate_ms=12.0,
            heading_deg=90.0,
            alpha_deg=10.0,
            phase=MissionPhase.CLIMB,
            current_waypoint_id="WP1",
            remaining_waypoint_count=1,
            mission_completed=False,
        )
    ]

    result = MissionEvaluator().evaluate(telemetry)

    assert result.failed is True
    assert "route_not_completed" in result.failure_reasons
    assert "fuel_depleted" in result.failure_reasons
