import math

from aerospace.physics.aerodynamics import thrust_to_weight_ratio, wing_loading
from aerospace.physics.constants import EARTH_STANDARD_GRAVITY, SEA_LEVEL_AIR_DENSITY

# Aircraft Weight
# W = m * g


def aircraft_weight(mass_kg: float) -> float:

    return mass_kg * EARTH_STANDARD_GRAVITY


# Wing Loading
# WL = W / A


def aircraft_wing_loading(mass_kg: float, wing_area_m2: float) -> float:

    weight = aircraft_weight(mass_kg)

    return wing_loading(weight, wing_area_m2)


# Stall Speed
# Vs = sqrt((2W)/(rho * Cl * A))


def stall_speed(mass_kg: float, wing_area_m2: float, lift_coefficient: float) -> float:

    weight = aircraft_weight(mass_kg)

    return math.sqrt(
        (2 * weight) / (SEA_LEVEL_AIR_DENSITY * lift_coefficient * wing_area_m2)
    )


# Thrust-to-Weight Ratio
# TWR = T / W


def aircraft_thrust_to_weight(thrust_n: float, mass_kg: float) -> float:

    weight = aircraft_weight(mass_kg)

    return thrust_to_weight_ratio(thrust_n, weight)


# Simplified Climb Rate
# ROC = (T - D) * V / W


def climb_rate(
    thrust_n: float, drag_n: float, velocity_ms: float, mass_kg: float
) -> float:

    weight = aircraft_weight(mass_kg)

    excess_thrust = thrust_n - drag_n

    return (excess_thrust * velocity_ms) / weight
