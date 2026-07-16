# Satellite Model

## Inputs and units

A satellite definition contains mass (kg), altitude (m), drag coefficient, and cross-sectional area (m²). `SatelliteState` holds altitude, velocity, inclination, eccentricity, true anomaly, and ground-track fields.

## Per-step calculation

1. Calculate circular-orbit speed from altitude.
2. Estimate atmospheric density and drag force.
3. Convert the simplified drag acceleration into altitude loss.
4. Apply scheduled orbit raises or station keeping.
5. Advance time and true anomaly; derive latitude and longitude.
6. Return period, energy, semi-major axis, apsides, and ground-track fields.

## Assumptions

- Circular-orbit quantities are used even when the state records an eccentricity.
- Decay is a simplified drag-to-altitude relationship, not numerical orbital integration.
- Ground-track longitude is anomaly-based and does not model Earth rotation.
- J2, solar radiation pressure, third-body effects, and ephemeris propagation are out of scope.

The model is useful for studying trends and workflow, not prediction of an operational satellite trajectory.
