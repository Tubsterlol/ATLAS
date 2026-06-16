from simulation.flight_profiles import (
    ClimbProfile,
    CruiseProfile,
    DescentProfile,
)


class MissionProfile:
    def __init__(
        self,
        cruise_altitude_m: float,
        climb_rate_ms: float,
        descent_rate_ms: float,
        reserve_fuel_kg: float,
    ):
        self.climb = ClimbProfile(climb_rate_ms)
        self.cruise = CruiseProfile()
        self.descent = DescentProfile(descent_rate_ms)

        self.cruise_altitude_m = cruise_altitude_m
        self.reserve_fuel_kg = reserve_fuel_kg

    def update(self, state):

        if state.phase == "climb":
            self.climb.update(state)

            if state.altitude_m >= self.cruise_altitude_m:
                state.phase = "cruise"

        elif state.phase == "cruise":
            self.cruise.update(state)

            if state.fuel_kg <= self.reserve_fuel_kg:
                state.phase = "descent"

        elif state.phase == "descent":
            self.descent.update(state)
