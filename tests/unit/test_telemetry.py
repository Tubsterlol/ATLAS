from dataclasses import FrozenInstanceError

import pytest

from simulation.mission_phase import MissionPhase
from simulation.state import AircraftState
from simulation.telemetry import TelemetryRecorder


def test_telemetry_records_aircraft_state():
    state = AircraftState(
        altitude_m=5000.0,
        velocity_ms=300.0,
        fuel_kg=2500.0,
        climb_rate_ms=15.0,
        heading_deg=90.0,
        alpha_deg=6.0,
    )

    state.time_s = 10.0
    state.phase = MissionPhase.CLIMB

    recorder = TelemetryRecorder()
    recorder.record(state)

    record = recorder.records[0]

    assert record.time_s == 10.0
    assert record.altitude_m == 5000.0
    assert record.velocity_ms == 300.0
    assert record.fuel_kg == 2500.0
    assert record.climb_rate_ms == 15.0
    assert record.heading_deg == 90.0
    assert record.alpha_deg == 6.0
    assert record.phase == MissionPhase.CLIMB


def test_telemetry_records_multiple_states():
    recorder = TelemetryRecorder()

    state = AircraftState(
        altitude_m=0.0,
        velocity_ms=250.0,
        fuel_kg=3000.0,
        climb_rate_ms=12.0,
        heading_deg=90.0,
        alpha_deg=10.0,
    )

    state.time_s = 0.0
    recorder.record(state)

    state.time_s = 1.0
    state.altitude_m = 12.0
    recorder.record(state)

    assert len(recorder.records) == 2
    assert recorder.records[0].time_s == 0.0
    assert recorder.records[1].time_s == 1.0


def test_telemetry_records_navigation_status_when_available():
    state = AircraftState(
        altitude_m=1000.0,
        velocity_ms=300.0,
        fuel_kg=2500.0,
        climb_rate_ms=15.0,
        heading_deg=90.0,
        alpha_deg=6.0,
    )
    state.time_s = 10.0
    state.phase = MissionPhase.CLIMB
    state.x_m = 0.0
    state.y_m = 0.0
    state.navigation_status = {
        "current_waypoint_id": "WP1",
        "distance_to_waypoint_m": 1000.0,
        "heading_error_deg": 0.0,
        "remaining_waypoint_count": 1,
        "mission_completed": False,
    }

    recorder = TelemetryRecorder()
    recorder.record(state)

    record = recorder.records[0]
    assert record.current_waypoint_id == "WP1"
    assert record.distance_to_waypoint_m == pytest.approx(1000.0)
    assert record.heading_error_deg == pytest.approx(0.0)
    assert record.remaining_waypoint_count == 1
    assert record.mission_completed is False


def test_telemetry_records_immutable_observation_snapshot():
    state = AircraftState(
        altitude_m=5000.0,
        velocity_ms=300.0,
        fuel_kg=2500.0,
        climb_rate_ms=15.0,
        heading_deg=90.0,
        alpha_deg=6.0,
    )
    state.time_s = 10.0
    state.phase = MissionPhase.CLIMB

    recorder = TelemetryRecorder()
    recorder.record(state)

    with pytest.raises(FrozenInstanceError):
        recorder.records[0].altitude_m = 42.0

    state.altitude_m = 99.0
    state.velocity_ms = 123.0
    assert recorder.records[0].altitude_m == 5000.0
    assert recorder.records[0].velocity_ms == 300.0
