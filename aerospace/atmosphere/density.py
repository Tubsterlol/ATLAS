import math

from aerospace.physics.constants import SCALE_HEIGHT_M, SEA_LEVEL_AIR_DENSITY

# Exponential Atmosphere Model
# rho = rho0 * exp(-h / H)


def atmospheric_density(altitude_m: float) -> float:

    return SEA_LEVEL_AIR_DENSITY * math.exp(-altitude_m / SCALE_HEIGHT_M)
