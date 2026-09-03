from dataclasses import dataclass

from .mission_phase import MissionPhase
from .telemetry import TelemetryRecord


@dataclass
class MissionResult:
    completed: bool
    failed: bool
    final_phase: MissionPhase
    flight_time_s: float
    fuel_consumed_kg: float
    final_altitude_m: float
    final_velocity_ms: float
    route_completed: bool = False
    current_waypoint_id: str | None = None
    distance_to_waypoint_m: float = 0.0
    heading_error_deg: float = 0.0
    remaining_waypoint_count: int = 0
    failure_reasons: list[str] | None = None
    final_waypoint: str | None = None
    waypoints_completed: int = 0
    total_time_s: float = 0.0
    fuel_remaining_kg: float = 0.0
    max_altitude_m: float = 0.0


class MissionEvaluator:
    def evaluate(
        self,
        telemetry: list[TelemetryRecord],
    ) -> MissionResult:
        if not telemetry:
            raise ValueError("Cannot evaluate mission without telemetry")

        first = telemetry[0]
        final = telemetry[-1]
        route_completed = bool(final.mission_completed)
        final_waypoint = next(
            (
                record.current_waypoint_id
                for record in reversed(telemetry)
                if record.current_waypoint_id is not None
            ),
            None,
        )
        waypoints_completed = max(
            0,
            first.remaining_waypoint_count - final.remaining_waypoint_count,
        )
        if route_completed and final_waypoint is not None:
            waypoints_completed += 1
        total_time_s = final.time_s - first.time_s

        fuel_consumed_kg = max(
            0.0,
            first.fuel_kg - final.fuel_kg,
        )

        completed = final.phase == MissionPhase.LANDING
        current_waypoint_id = final.current_waypoint_id
        distance_to_waypoint_m = float(final.distance_to_waypoint_m)
        heading_error_deg = float(final.heading_error_deg)
        remaining_waypoint_count = int(final.remaining_waypoint_count)

        failure_reasons: list[str] = []

        if not completed:
            failure_reasons.append("mission_not_landed")
        if not route_completed:
            failure_reasons.append("route_not_completed")
        if final.fuel_kg <= 0.0:
            failure_reasons.append("fuel_depleted")
        if final.altitude_m < 0.0:
            failure_reasons.append("negative_altitude")

        failed = bool(failure_reasons)

        return MissionResult(
            completed=completed,
            failed=failed,
            final_phase=final.phase,
            flight_time_s=final.time_s - first.time_s,
            fuel_consumed_kg=fuel_consumed_kg,
            final_altitude_m=final.altitude_m,
            final_velocity_ms=final.velocity_ms,
            route_completed=route_completed,
            current_waypoint_id=current_waypoint_id,
            distance_to_waypoint_m=distance_to_waypoint_m,
            heading_error_deg=heading_error_deg,
            remaining_waypoint_count=remaining_waypoint_count,
            failure_reasons=failure_reasons,
            final_waypoint=final_waypoint,
            waypoints_completed=waypoints_completed,
            total_time_s=total_time_s,
            fuel_remaining_kg=final.fuel_kg,
            max_altitude_m=max(record.altitude_m for record in telemetry),
        )
