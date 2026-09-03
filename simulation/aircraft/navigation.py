from dataclasses import dataclass
from math import atan2, cos, pi, radians, sin, sqrt

EARTH_RADIUS_M = 6_371_000.0


@dataclass(frozen=True)
class Waypoint:
    latitude_deg: float
    longitude_deg: float
    altitude_m: float


class NavigationCalculator:
    @staticmethod
    def distance_to_waypoint(
        latitude_deg: float,
        longitude_deg: float,
        waypoint: Waypoint,
    ) -> float:
        lat1 = radians(latitude_deg)
        lat2 = radians(waypoint.latitude_deg)

        delta_lat = radians(waypoint.latitude_deg - latitude_deg)
        delta_lon = radians(waypoint.longitude_deg - longitude_deg)

        a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return EARTH_RADIUS_M * c

    @staticmethod
    def bearing_to_waypoint(
        latitude_deg: float,
        longitude_deg: float,
        waypoint: Waypoint,
    ) -> float:
        lat1 = radians(latitude_deg)
        lat2 = radians(waypoint.latitude_deg)

        delta_lon = radians(waypoint.longitude_deg - longitude_deg)

        x = sin(delta_lon) * cos(lat2)
        y = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(delta_lon)

        bearing = atan2(x, y)

        return (bearing * 180.0 / pi + 360.0) % 360.0
