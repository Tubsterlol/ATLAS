from dataclasses import dataclass


@dataclass
class Waypoint:
    name: str
    x_m: float
    y_m: float

    @property
    def id(self) -> str:
        return self.name


__all__ = ["Waypoint"]
