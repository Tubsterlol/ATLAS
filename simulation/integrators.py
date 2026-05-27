# Euler Integration
# x_new = x + v * dt

def euler_integrate(
    value: float,
    rate: float,
    timestep_s: float
) -> float:

    return value + (
        rate * timestep_s
    )
