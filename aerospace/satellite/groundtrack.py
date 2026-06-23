from math import asin, degrees, radians, sin


def groundtrack_position(
    true_anomaly_deg: float,
    inclination_deg: float,
):

    anomaly_rad = radians(true_anomaly_deg)

    inclination_rad = radians(inclination_deg)

    latitude_deg = degrees(asin(sin(inclination_rad) * sin(anomaly_rad)))

    longitude_deg = true_anomaly_deg % 360.0

    return (
        latitude_deg,
        longitude_deg,
    )
