from dataclasses import dataclass


@dataclass(frozen=True)
class Waypoint:
    latitude_deg: float
    longitude_deg: float
    altitude_m: float
