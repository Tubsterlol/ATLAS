from simulation.flight_profiles import (
    ClimbProfile,
    CruiseProfile,
    DescentProfile,
    LandingProfile,
    TakeoffProfile,
)

from .mission_events import FlapsRetractEvent, GearUpEvent
from .mission_phase import MissionPhase


class MissionProfile:
    def __init__(
        self,
        cruise_altitude_m: float,
        climb_rate_ms: float,
        descent_rate_ms: float,
        reserve_fuel_kg: float,
        takeoff_transition_altitude_m: float = 150.0,
        landing_transition_altitude_m: float = 1000.0,
    ):
        ...
        self.phase_profiles = {
            MissionPhase.TAKEOFF: TakeoffProfile(),
            MissionPhase.CLIMB: ClimbProfile(climb_rate_ms),
            MissionPhase.CRUISE: CruiseProfile(),
            MissionPhase.DESCENT: DescentProfile(descent_rate_ms),
            MissionPhase.LANDING: LandingProfile(),
        }

        self.events = [
            GearUpEvent(),
            FlapsRetractEvent(),
        ]
        self.cruise_altitude_m = cruise_altitude_m
        self.reserve_fuel_kg = reserve_fuel_kg

        self.takeoff_transition_altitude_m = takeoff_transition_altitude_m

        self.landing_transition_altitude_m = landing_transition_altitude_m

        self.current_phase = MissionPhase.TAKEOFF

        self.phase_profiles = {
            MissionPhase.TAKEOFF: TakeoffProfile(),
            MissionPhase.CLIMB: ClimbProfile(climb_rate_ms),
            MissionPhase.CRUISE: CruiseProfile(),
            MissionPhase.DESCENT: DescentProfile(descent_rate_ms),
            MissionPhase.LANDING: LandingProfile(),
        }

    def set_phase(
        self,
        phase: MissionPhase,
        state,
    ):
        self.current_phase = phase
        state.phase = phase

    def transition(
        self,
        state,
    ):
        if (
            self.current_phase == MissionPhase.TAKEOFF
            and state.altitude_m >= self.takeoff_transition_altitude_m
        ):
            self.set_phase(
                MissionPhase.CLIMB,
                state,
            )

        elif (
            self.current_phase == MissionPhase.CLIMB
            and state.altitude_m >= self.cruise_altitude_m
        ):
            self.set_phase(
                MissionPhase.CRUISE,
                state,
            )

        elif (
            self.current_phase == MissionPhase.CRUISE
            and state.fuel_kg <= self.reserve_fuel_kg
        ):
            self.set_phase(
                MissionPhase.DESCENT,
                state,
            )

        elif (
            self.current_phase == MissionPhase.DESCENT
            and state.altitude_m <= self.landing_transition_altitude_m
        ):
            self.set_phase(
                MissionPhase.LANDING,
                state,
            )

    def update(
        self,
        state,
    ):
        self.transition(state)
        profile = self.phase_profiles[self.current_phase]
        profile.update(state)

        for event in self.events:
            if event.check(state):
                event.execute(state)
