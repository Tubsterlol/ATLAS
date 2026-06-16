class ClimbProfile:
    def __init__(self, climb_rate_ms: float):
        self.climb_rate_ms = climb_rate_ms

    def update(self, state):
        state.climb_rate_ms = self.climb_rate_ms


class CruiseProfile:
    def update(self, state):
        state.climb_rate_ms = 0.0


class DescentProfile:
    def __init__(self, descent_rate_ms: float):
        self.descent_rate_ms = descent_rate_ms

    def update(self, state):
        state.climb_rate_ms = -self.descent_rate_ms
