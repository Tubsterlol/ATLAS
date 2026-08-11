import math

from simulation.mission_phase import MissionPhase


class WaypointMission:
    def __init__(
        self,
        waypoints,
        cruise_altitude_m: float | None = None,
        max_climb_rate_ms: float = 15.0,
    ):
        self.waypoints = waypoints
        self.current_index = 0
        self.cruise_altitude_m = cruise_altitude_m
        self.max_climb_rate_ms = max_climb_rate_ms

    def update(self, state):

        if self.current_index >= len(self.waypoints):
            return

        target = self.waypoints[self.current_index]

        dx = target.x_m - state.x_m
        dy = target.y_m - state.y_m

        distance = math.sqrt(dx**2 + dy**2)

        if distance < 1000:
            self.current_index += 1
            return

        state.heading_deg = math.degrees(math.atan2(dx, dy))

        if self.cruise_altitude_m is None:
            return

        if state.altitude_m < self.cruise_altitude_m:
            climb_fraction = 1.0 - state.altitude_m / self.cruise_altitude_m
            state.climb_rate_ms = max(0.0, self.max_climb_rate_ms * climb_fraction)
            state.phase = MissionPhase.CLIMB
        else:
            state.climb_rate_ms = 0.0
            state.phase = MissionPhase.CRUISE
