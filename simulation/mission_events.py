from abc import ABC, abstractmethod

from mission_profile import MissionPhase


class MissionEvent(ABC):
    @abstractmethod
    def check(self, state) -> bool: ...

    @abstractmethod
    def execute(self, state): ...


class GearUpEvent(MissionEvent):
    def check(self, state):
        return (
            not self.completed
            and state.phase == MissionPhase.CLIMB
            and state.altitude_m >= 100.0
        )

    def execute(self, state):
        state.gear_up = True
        self.completed = True


class FlapsRetractEvent(MissionEvent):
    def check(self, state):
        return not self.completed and state.velocity_ms >= 90.0 and state.flaps_deg > 0

    def execute(self, state):
        state.flaps_deg = 0.0
        self.completed = True
