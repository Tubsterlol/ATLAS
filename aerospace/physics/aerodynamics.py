# Dynamic Pressure
# q = 0.5 * rho * v^2


def dynamic_pressure(density: float, velocity: float) -> float:

    return 0.5 * density * (velocity**2)


# Lift Equation
# L = 0.5 * rho * v^2 * Cl * A


def lift_force(
    density: float, velocity: float, lift_coefficient: float, wing_area: float
) -> float:

    return 0.5 * density * (velocity**2) * lift_coefficient * wing_area


# Drag Equation
# D = 0.5 * rho * v^2 * Cd * A


def drag_force(
    density: float, velocity: float, drag_coefficient: float, reference_area: float
) -> float:

    return 0.5 * density * (velocity**2) * drag_coefficient * reference_area


# Wing Loading
# WL = Weight / Wing Area


def wing_loading(weight: float, wing_area: float) -> float:

    return weight / wing_area


# Thrust-to-Weight Ratio
# TWR = Thrust / Weight


def thrust_to_weight_ratio(thrust: float, weight: float) -> float:

    return thrust / weight
