from simulation.profiles.base import FlightProfile


class CruiseProfile(FlightProfile):
    def __init__(
        self,
        cruise_altitude_m,
        cruise_speed_ms,
    ):
        self.cruise_altitude_m = cruise_altitude_m
        self.cruise_speed_ms = cruise_speed_ms

    def update(self, state):

        state.climb_rate_ms = 0.0
