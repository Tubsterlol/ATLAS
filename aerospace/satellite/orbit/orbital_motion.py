def advance_true_anomaly(
    true_anomaly_deg: float,
    orbital_period_s: float,
    timestep_s: float,
) -> float:

    if orbital_period_s <= 0:
        return true_anomaly_deg

    degrees_per_second = 360.0 / orbital_period_s

    true_anomaly_deg += degrees_per_second * timestep_s

    return true_anomaly_deg % 360.0
