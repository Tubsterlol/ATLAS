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
