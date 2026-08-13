from dataclasses import dataclass

from simulation.flight_profiles import (
    ClimbProfile,
    CruiseProfile,
    DescentProfile,
    LandingProfile,
    TakeoffProfile,
)

from .mission_events import FlapsRetractEvent, GearUpEvent
from .mission_phase import MissionPhase


@dataclass(frozen=True)
class MissionTargets:
    phase: MissionPhase
    target_altitude_m: float
    target_climb_rate_ms: float


class MissionProfile:
    def __init__(
        self,
        cruise_altitude_m: float,
        climb_rate_ms: float,
        descent_rate_ms: float,
        reserve_fuel_kg: float,
        takeoff_transition_altitude_m: float = 150.0,
        landing_transition_altitude_m: float = 1000.0,
        navigation=None,
    ):
        self.events = [
            GearUpEvent(),
            FlapsRetractEvent(),
        ]
        self.navigation = navigation
        self.cruise_altitude_m = cruise_altitude_m
        self.reserve_fuel_kg = reserve_fuel_kg

        self.takeoff_transition_altitude_m = takeoff_transition_altitude_m

        self.landing_transition_altitude_m = landing_transition_altitude_m

        self.current_phase = MissionPhase.TAKEOFF
        self.takeoff_climb_rate_ms = 12.0
        self.landing_climb_rate_ms = -3.0

        self.phase_profiles = {
            MissionPhase.TAKEOFF: TakeoffProfile(),
            MissionPhase.CLIMB: ClimbProfile(climb_rate_ms),
            MissionPhase.CRUISE: CruiseProfile(),
            MissionPhase.DESCENT: DescentProfile(descent_rate_ms),
            MissionPhase.LANDING: LandingProfile(),
        }
        self.mission_targets = self._targets_for_phase(self.current_phase)

    def _targets_for_phase(self, phase: MissionPhase) -> MissionTargets:
        if phase == MissionPhase.TAKEOFF:
            return MissionTargets(
                phase=phase,
                target_altitude_m=self.takeoff_transition_altitude_m,
                target_climb_rate_ms=self.takeoff_climb_rate_ms,
            )

        if phase == MissionPhase.CLIMB:
            return MissionTargets(
                phase=phase,
                target_altitude_m=self.cruise_altitude_m,
                target_climb_rate_ms=self.phase_profiles[MissionPhase.CLIMB].climb_rate_ms,
            )

        if phase == MissionPhase.CRUISE:
            return MissionTargets(
                phase=phase,
                target_altitude_m=self.cruise_altitude_m,
                target_climb_rate_ms=0.0,
            )

        if phase == MissionPhase.DESCENT:
            return MissionTargets(
                phase=phase,
                target_altitude_m=self.landing_transition_altitude_m,
                target_climb_rate_ms=-self.phase_profiles[MissionPhase.DESCENT].descent_rate_ms,
            )

        if phase == MissionPhase.LANDING:
            return MissionTargets(
                phase=phase,
                target_altitude_m=0.0,
                target_climb_rate_ms=self.landing_climb_rate_ms,
            )

        raise ValueError(f"Unsupported mission phase: {phase}")

    def set_phase(
        self,
        phase: MissionPhase,
        state,
    ):
        self.current_phase = phase
        state.phase = phase
        self.mission_targets = self._targets_for_phase(phase)

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
        # Keep state phase synchronized even when no boundary was crossed.
        state.phase = self.current_phase
        profile = self.phase_profiles[self.current_phase]
        profile.update(state)

        for event in self.events:
            if event.check(state):
                event.execute(state)

        # Navigation supplies horizontal guidance only. MissionProfile remains
        # authoritative for phase, altitude, and climb/descent behavior.
        if self.navigation is not None:
            self.navigation.update(state)
