from dataclasses import dataclass


@dataclass
class Waypoint:
    name: str
    x_m: float
    y_m: float
