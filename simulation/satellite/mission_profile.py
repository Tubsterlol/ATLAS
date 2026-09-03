from dataclasses import dataclass

from aerospace.satellite.maneuvers.maneuvers import orbit_raise
from aerospace.satellite.orbital.vis_viva import orbital_velocity
from simulation.satellite.maneuvers import (
    HohmannTransferManeuver,
    OrbitRaiseManeuver,
    StationKeepingManeuver,
)
from simulation.satellite.mission_phase import SatelliteMissionPhase
from simulation.satellite.station_keeping import station_keep


@dataclass(frozen=True)
class SatelliteMissionTargets:
    phase: SatelliteMissionPhase
    target_altitude_m: float
    target_velocity_ms: float


class SatelliteMissionProfile:
    def __init__(self, maneuvers=None):
        self.maneuvers = maneuvers or []
        self.executed_maneuvers = set()
        self.current_phase = SatelliteMissionPhase.COAST
        self.mission_targets = SatelliteMissionTargets(
            phase=self.current_phase,
            target_altitude_m=0.0,
            target_velocity_ms=0.0,
        )

    def _set_targets(self, phase, target_altitude_m: float):
        self.current_phase = phase
        self.mission_targets = SatelliteMissionTargets(
            phase=phase,
            target_altitude_m=target_altitude_m,
            target_velocity_ms=orbital_velocity(target_altitude_m),
        )

    def update(self, state):
        phase = SatelliteMissionPhase.COAST
        target_altitude_m = state.altitude_m

        for index, maneuver in enumerate(self.maneuvers):
            if isinstance(maneuver, OrbitRaiseManeuver):
                if (
                    index not in self.executed_maneuvers
                    and state.time_s >= maneuver.time_s
                ):
                    state.altitude_m = orbit_raise(
                        altitude_m=state.altitude_m,
                        delta_v_ms=maneuver.delta_v_ms,
                    )
                    self.executed_maneuvers.add(index)
                    phase = SatelliteMissionPhase.TRANSFER
                    target_altitude_m = state.altitude_m

            elif isinstance(maneuver, HohmannTransferManeuver):
                if (
                    index not in self.executed_maneuvers
                    and state.time_s >= maneuver.time_s
                ):
                    delta_v_ms = max(
                        0.0,
                        (maneuver.target_altitude_m - state.altitude_m) / 1000.0,
                    )
                    state.altitude_m = orbit_raise(
                        altitude_m=state.altitude_m,
                        delta_v_ms=delta_v_ms,
                    )
                    self.executed_maneuvers.add(index)
                    phase = SatelliteMissionPhase.TRANSFER
                    target_altitude_m = maneuver.target_altitude_m

            elif isinstance(maneuver, StationKeepingManeuver):
                state.altitude_m = station_keep(
                    current_altitude_m=state.altitude_m,
                    target_altitude_m=maneuver.target_altitude_m,
                    tolerance_m=maneuver.tolerance_m,
                )
                phase = SatelliteMissionPhase.STATION_KEEPING
                target_altitude_m = maneuver.target_altitude_m

        state.phase = phase
        self._set_targets(phase, target_altitude_m)
