import math


def update_position(
    x_m: float,
    y_m: float,
    velocity_ms: float,
    heading_deg: float,
    timestep_s: float,
):
    distance = velocity_ms * timestep_s

    heading_rad = math.radians(heading_deg)

    x_m += distance * math.sin(heading_rad)
    y_m += distance * math.cos(heading_rad)

    return x_m, y_m
