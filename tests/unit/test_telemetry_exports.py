import json
from pathlib import Path

from simulation.telemetry import TelemetryRecorder
from simulation.state import AircraftState
from simulation.mission_phase import MissionPhase


def test_telemetry_export_csv_and_json(tmp_path):
    recorder = TelemetryRecorder()

    s1 = AircraftState(
        altitude_m=1000.0,
        velocity_ms=200.0,
        fuel_kg=500.0,
        climb_rate_ms=5.0,
        heading_deg=90.0,
        alpha_deg=2.0,
    )
    s1.time_s = 0.0
    s1.phase = MissionPhase.TAKEOFF

    s2 = AircraftState(
        altitude_m=1500.0,
        velocity_ms=220.0,
        fuel_kg=480.0,
        climb_rate_ms=3.0,
        heading_deg=90.0,
        alpha_deg=3.0,
    )
    s2.time_s = 1.0
    s2.phase = MissionPhase.CLIMB

    recorder.record(s1)
    recorder.record(s2)

    csv_path = tmp_path / "telemetry.csv"
    json_path = tmp_path / "telemetry.json"

    recorder.export_csv(csv_path)
    recorder.export_json(json_path)

    assert csv_path.exists()
    assert csv_path.stat().st_size > 0

    assert json_path.exists()
    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) == 2
