from dataclasses import dataclass

from simulation.mission_phase import MissionPhase


@dataclass
class TelemetryRecord:
    time_s: float
    altitude_m: float
    velocity_ms: float
    fuel_kg: float
    climb_rate_ms: float
    heading_deg: float
    alpha_deg: float
    phase: MissionPhase


class TelemetryRecorder:
    def __init__(self):
        self.records: list[TelemetryRecord] = []

    def record(self, state):
        self.records.append(
            TelemetryRecord(
                time_s=state.time_s,
                altitude_m=state.altitude_m,
                velocity_ms=state.velocity_ms,
                fuel_kg=state.fuel_kg,
                climb_rate_ms=state.climb_rate_ms,
                heading_deg=state.heading_deg,
                alpha_deg=state.alpha_deg,
                phase=state.phase,
            )
        )

    def clear(self):
        self.records.clear()

    def __len__(self):
        return len(self.records)
