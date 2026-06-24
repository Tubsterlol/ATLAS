from dataclasses import dataclass


@dataclass
class OrbitRaiseManeuver:
    time_s: float
    delta_v_ms: float
