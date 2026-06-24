from dataclasses import dataclass


@dataclass
class OrbitRaiseManeuver:
    time_s: float
    delta_v_ms: float


@dataclass
class StationKeepingManeuver:
    target_altitude_m: float
    tolerance_m: float


@dataclass
class HohmannTransferManeuver:
    time_s: float
    target_altitude_m: float
