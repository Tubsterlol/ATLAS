from aerospace.physics.constants import *

# Distance


def km_to_meters(km: float) -> float:
    return km * KM_TO_M


def meters_to_km(meters: float) -> float:
    return meters * M_TO_KM


def feet_to_meters(feet: float) -> float:
    return feet * FT_TO_M


def meters_to_feet(meters: float) -> float:
    return meters * M_TO_FT


def miles_to_km(miles: float) -> float:
    return miles * MILES_TO_KM


# Speed


def kmh_to_ms(speed_kmh: float) -> float:
    return speed_kmh * KMH_TO_MS


def ms_to_kmh(speed_ms: float) -> float:
    return speed_ms * MS_TO_KMH


def mph_to_ms(speed_mph: float) -> float:
    return speed_mph * MPH_TO_MS


def ms_to_mph(speed_ms: float) -> float:
    return speed_ms * MS_TO_MPH


# Angles


def degrees_to_radians(degrees: float) -> float:
    return degrees * DEG_TO_RAD


def radians_to_degrees(radians: float) -> float:
    return radians * RAD_TO_DEG


# Mass


def kg_to_lbs(kg: float) -> float:
    return kg * KG_TO_LBS


def lbs_to_kg(lbs: float) -> float:
    return lbs * LBS_TO_KG
