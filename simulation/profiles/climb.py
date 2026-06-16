from simulation.profiles.base import FlightProfile


class ClimbProfile(FlightProfile):
    def __init__(
        self,
        target_altitude_m,
        climb_rate_ms,
    ):
        self.target_altitude_m = target_altitude_m
        self.climb_rate_ms = climb_rate_ms

    def update(self, state):

        if state.altitude_m < self.target_altitude_m:
            state.climb_rate_ms = self.climb_rate_ms
        else:
            state.climb_rate_ms = 0.0
