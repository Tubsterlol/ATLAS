from enum import Enum


class SatelliteMissionPhase(Enum):
    COAST = "coast"
    TRANSFER = "transfer"
    STATION_KEEPING = "station_keeping"
