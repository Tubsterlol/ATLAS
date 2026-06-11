import math

from aerospace.physics.constants import (
    EARTH_STANDARD_GRAVITY,
    SEA_LEVEL_PRESSURE,
    STANDARD_TEMPERATURE_K,
    UNIVERSAL_GAS_CONSTANT,
)

# Barometric Formula


def atmospheric_pressure(altitude_m: float) -> float:

    lapse_rate = 0.0065

    return SEA_LEVEL_PRESSURE * (
        1 - (lapse_rate * altitude_m) / STANDARD_TEMPERATURE_K
    ) ** ((EARTH_STANDARD_GRAVITY * 0.0289644) / (UNIVERSAL_GAS_CONSTANT * lapse_rate))
