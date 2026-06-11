# ISA Troposphere Approximation


def atmospheric_temperature(altitude_m: float) -> float:

    sea_level_temp = 288.15
    lapse_rate = 0.0065

    return sea_level_temp - (lapse_rate * altitude_m)
