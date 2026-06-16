import math


class WaypointMission:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.current_index = 0

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
