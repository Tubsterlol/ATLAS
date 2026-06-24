from dataclasses import dataclass


@dataclass
class OrbitalManeuver:
    time_s: float
    delta_v_ms: float
