from simulation.flight_profiles import (
    ClimbProfile,
    CruiseProfile,
    DescentProfile,
    LandingProfile,
    TakeoffProfile,
)
from simulation.mission_phase import MissionPhase


class MissionProfile:
    def __init__(
        self,
        cruise_altitude_m: float,
        climb_rate_ms: float,
        descent_rate_ms: float,
        reserve_fuel_kg: float,
    ):
        self.cruise_altitude_m = cruise_altitude_m
        self.reserve_fuel_kg = reserve_fuel_kg

        self.current_phase = MissionPhase.TAKEOFF

        self.phase_profiles = {
            MissionPhase.TAKEOFF: TakeoffProfile(),
            MissionPhase.CLIMB: ClimbProfile(climb_rate_ms),
            MissionPhase.CRUISE: CruiseProfile(),
            MissionPhase.DESCENT: DescentProfile(descent_rate_ms),
            MissionPhase.LANDING: LandingProfile(),
        }

    def transition(self, state):

        if self.current_phase == MissionPhase.TAKEOFF and state.altitude_m >= 150:
            self.current_phase = MissionPhase.CLIMB

        elif (
            self.current_phase == MissionPhase.CLIMB
            and state.altitude_m >= self.cruise_altitude_m
        ):
            self.current_phase = MissionPhase.CRUISE

        elif (
            self.current_phase == MissionPhase.CRUISE
            and state.fuel_kg <= self.reserve_fuel_kg
        ):
            self.current_phase = MissionPhase.DESCENT

        elif self.current_phase == MissionPhase.DESCENT and state.altitude_m <= 1000:
            self.current_phase = MissionPhase.LANDING

    def update(self, state):
        self.transition(state)
        state.phase = self.current_phase
        self.phase_profiles[self.current_phase].update(state)
