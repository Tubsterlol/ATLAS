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

    def update(self, state):
        if self.completed:
            return

        target = self.current_waypoint

        dx = target.x_m - state.x_m
        dy = target.y_m - state.y_m

        distance = math.sqrt(dx**2 + dy**2)

        if distance < self.reach_radius_m:
            self.current_index += 1
            return

        state.heading_deg = math.degrees(math.atan2(dx, dy))


__all__ = ["WaypointMission"]
