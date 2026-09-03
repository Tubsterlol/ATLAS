from abc import ABC, abstractmethod


class FlightPhaseProfile(ABC):
    @abstractmethod
    def update(self, state):
        pass


class TakeoffProfile(FlightPhaseProfile):
    def update(self, state):
        state.climb_rate_ms = 12
        state.alpha_deg = 10


class ClimbProfile(FlightPhaseProfile):
    def __init__(self, climb_rate_ms: float):
        self.climb_rate_ms = climb_rate_ms

    def update(self, state):
        state.climb_rate_ms = self.climb_rate_ms
        state.alpha_deg = 6


class CruiseProfile(FlightPhaseProfile):
    def update(self, state):
        state.climb_rate_ms = 0
        state.alpha_deg = 2


class DescentProfile(FlightPhaseProfile):
    def __init__(self, descent_rate_ms: float):
        self.descent_rate_ms = descent_rate_ms

    def update(self, state):
        state.climb_rate_ms = -self.descent_rate_ms
        state.alpha_deg = 1


class LandingProfile(FlightPhaseProfile):
    def update(self, state):
        state.climb_rate_ms = -3
        state.alpha_deg = 8
