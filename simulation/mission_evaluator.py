from dataclasses import dataclass

from .mission_phase import MissionPhase
from .telemetry import TelemetryRecord


@dataclass
class MissionResult:
    completed: bool
    final_phase: MissionPhase
    flight_time_s: float
    fuel_consumed_kg: float
    final_altitude_m: float
    final_velocity_ms: float


class MissionEvaluator:
    def evaluate(
        self,
        telemetry: list[TelemetryRecord],
    ) -> MissionResult:
        if not telemetry:
            raise ValueError("Cannot evaluate mission without telemetry")

        first = telemetry[0]
        final = telemetry[-1]

        fuel_consumed_kg = max(
            0.0,
            first.fuel_kg - final.fuel_kg,
        )

        completed = final.phase == MissionPhase.LANDING

        return MissionResult(
            completed=completed,
            final_phase=final.phase,
            flight_time_s=final.time_s - first.time_s,
            fuel_consumed_kg=fuel_consumed_kg,
            final_altitude_m=final.altitude_m,
            final_velocity_ms=final.velocity_ms,
        )
