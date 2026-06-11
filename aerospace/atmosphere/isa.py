import math

SEA_LEVEL_TEMP = 288.15
SEA_LEVEL_PRESSURE = 101325

LAPSE_RATE = 0.0065
GAS_CONSTANT_AIR = 287.05
GRAVITY = 9.80665


def isa_temperature(altitude_m: float) -> float:
    """
    Valid for troposphere (0–11 km)
    """
    return SEA_LEVEL_TEMP - (LAPSE_RATE * altitude_m)


def isa_pressure(altitude_m: float) -> float:
    """
    Valid for troposphere (0–11 km)
    """

    return SEA_LEVEL_PRESSURE * (1 - (LAPSE_RATE * altitude_m) / SEA_LEVEL_TEMP) ** (
        GRAVITY / (GAS_CONSTANT_AIR * LAPSE_RATE)
    )


def isa_density(altitude_m: float) -> float:
    """
    rho = p / RT
    """

    pressure = isa_pressure(altitude_m)

    temperature = isa_temperature(altitude_m)

    return pressure / (GAS_CONSTANT_AIR * temperature)
