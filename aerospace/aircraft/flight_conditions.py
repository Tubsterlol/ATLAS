import math


def speed_of_sound(temperature_k: float) -> float:
    """
    a = sqrt(gamma * R * T)
    """
    gamma = 1.4
    gas_constant = 287.05
    return math.sqrt(gamma * gas_constant * temperature_k)


def mach_number(velocity_ms: float, temperature_k: float) -> float:
    a = speed_of_sound(temperature_k)
    return velocity_ms / a


def reynolds_number(
    density: float,
    velocity_ms: float,
    characteristic_length_m: float,
    dynamic_viscosity: float = 1.81e-5,
) -> float:
    return (density * velocity_ms * characteristic_length_m) / dynamic_viscosity
