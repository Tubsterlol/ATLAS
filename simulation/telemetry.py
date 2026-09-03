from dataclasses import dataclass

from simulation.mission_phase import MissionPhase
from analytics.exports import export_csv, export_json
from pathlib import Path


@dataclass(frozen=True)
class TelemetryRecord:
    time_s: float
    altitude_m: float
    velocity_ms: float
    fuel_kg: float
    climb_rate_ms: float
    heading_deg: float
    alpha_deg: float
    phase: MissionPhase
    current_waypoint_id: str | None = None
    distance_to_waypoint_m: float = 0.0
    heading_error_deg: float = 0.0
    remaining_waypoint_count: int = 0
    mission_completed: bool = False


class TelemetryRecorder:
    def __init__(self):
        self.records: list[TelemetryRecord] = []

    def record(self, state):
        navigation_status = getattr(state, "navigation_status", {}) or {}

        self.records.append(
            TelemetryRecord(
                time_s=float(state.time_s),
                altitude_m=float(state.altitude_m),
                velocity_ms=float(state.velocity_ms),
                fuel_kg=float(state.fuel_kg),
                climb_rate_ms=float(state.climb_rate_ms),
                heading_deg=float(state.heading_deg),
                alpha_deg=float(state.alpha_deg),
                phase=state.phase,
                current_waypoint_id=navigation_status.get("current_waypoint_id"),
                distance_to_waypoint_m=float(
                    navigation_status.get("distance_to_waypoint_m", 0.0)
                ),
                heading_error_deg=float(
                    navigation_status.get("heading_error_deg", 0.0)
                ),
                remaining_waypoint_count=int(
                    navigation_status.get("remaining_waypoint_count", 0)
                ),
                mission_completed=bool(navigation_status.get("mission_completed", False)),
            )
        )

    def clear(self):
        self.records.clear()

    def __len__(self):
        return len(self.records)

    def export_csv(self, filepath: str | Path) -> None:
        """Export recorded telemetry to CSV using analytics.exports.export_csv."""
        export_csv(self.records, filepath)

    def export_json(self, filepath: str | Path) -> None:
        """Export recorded telemetry to JSON using analytics.exports.export_json."""
        export_json(self.records, filepath)
