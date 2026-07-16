from dataclasses import dataclass

from aerospace.core.validation import require_non_negative


@dataclass
class OrbitRaiseManeuver:
    time_s: float
    delta_v_ms: float

    def __post_init__(self) -> None:
        require_non_negative(self.time_s, "time_s")


@dataclass
class StationKeepingManeuver:
    target_altitude_m: float
    tolerance_m: float

    def __post_init__(self) -> None:
        require_non_negative(self.target_altitude_m, "target_altitude_m")
        require_non_negative(self.tolerance_m, "tolerance_m")


@dataclass
class HohmannTransferManeuver:
    time_s: float
    target_altitude_m: float

    def __post_init__(self) -> None:
        require_non_negative(self.time_s, "time_s")
        require_non_negative(self.target_altitude_m, "target_altitude_m")
