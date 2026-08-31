import math

from aerospace.core.validation import require_positive


class WaypointMission:
    def __init__(self, waypoints, reach_radius_m: float = 1000.0):
        require_positive(reach_radius_m, "reach_radius_m")

        self.waypoints = list(waypoints)
        self.reach_radius_m = reach_radius_m
        self.current_index = 0

    @property
    def waypoint_count(self) -> int:
        return len(self.waypoints)

    @property
    def completed(self) -> bool:
        return self.current_index >= len(self.waypoints)

    @property
    def current_waypoint(self):
        if self.completed:
            return None

        return self.waypoints[self.current_index]

    @property
    def previous_waypoint(self):
        if self.current_index <= 0 or not self.waypoints:
            return None

        previous_index = min(self.current_index, len(self.waypoints)) - 1
        return self.waypoints[previous_index]

    @property
    def remaining_waypoints(self):
        if self.completed:
            return []

        return self.waypoints[self.current_index + 1 :]

    @property
    def is_final_waypoint(self) -> bool:
        return not self.completed and self.current_index == len(self.waypoints) - 1

    def status(self, state):
        if self.completed:
            return {
                "current_waypoint_id": None,
                "distance_to_waypoint_m": 0.0,
                "heading_error_deg": 0.0,
                "remaining_waypoint_count": 0,
                "mission_completed": True,
            }

        target = self.current_waypoint
        dx = target.x_m - state.x_m
        dy = target.y_m - state.y_m
        distance = math.hypot(dx, dy)
        desired_heading = math.degrees(math.atan2(dx, dy))
        heading_error = (desired_heading - state.heading_deg + 180.0) % 360.0 - 180.0

        return {
            "current_waypoint_id": target.id,
            "distance_to_waypoint_m": float(distance),
            "heading_error_deg": float(abs(heading_error)),
            "remaining_waypoint_count": len(self.remaining_waypoints),
            "mission_completed": False,
        }

    def update(self, state):
        if self.completed:
            state.navigation_status = self.status(state)
            return

        target = self.current_waypoint

        dx = target.x_m - state.x_m
        dy = target.y_m - state.y_m

        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.reach_radius_m:
            self.current_index += 1
            state.navigation_status = self.status(state)
            return

        state.heading_deg = math.degrees(math.atan2(dx, dy))
        state.navigation_status = self.status(state)


__all__ = ["WaypointMission"]
