import math

SEA_LEVEL_TEMPERATURE = 288.15
SEA_LEVEL_PRESSURE = 101325

TEMPERATURE_LAPSE_RATE = 0.0065

GAS_CONSTANT_AIR = 287.05

GRAVITY = 9.80665


def isa_temperature(altitude_m: float) -> float:

    return SEA_LEVEL_TEMPERATURE - TEMPERATURE_LAPSE_RATE * altitude_m


def isa_pressure(altitude_m: float) -> float:

    temperature = isa_temperature(altitude_m)

    exponent = GRAVITY / (GAS_CONSTANT_AIR * TEMPERATURE_LAPSE_RATE)

    return SEA_LEVEL_PRESSURE * (temperature / SEA_LEVEL_TEMPERATURE) ** exponent


def isa_density(altitude_m: float) -> float:

    pressure = isa_pressure(altitude_m)

    temperature = isa_temperature(altitude_m)

    return pressure / (GAS_CONSTANT_AIR * temperature)
