# Satellite Model

## Inputs and units

A satellite definition contains mass (kg), altitude (m), drag coefficient, and cross-sectional area (m²). `SatelliteState` holds altitude, velocity, inclination, eccentricity, mission phase, true anomaly, and ground-track fields.

The satellite side also uses two layers:

- `SatelliteMissionProfile` chooses the mission mode and maneuver policy.
- `SatelliteSimulation` applies decay, time advance, and orbital bookkeeping.

## Per-step calculation

1. Let `SatelliteMissionProfile` own maneuver timing, mission phase, and phase targets.
2. Calculate circular-orbit speed from altitude.
3. Estimate atmospheric density and drag force.
4. Convert the simplified drag acceleration into altitude loss.
5. Apply scheduled orbit raises or station keeping through the mission profile.
6. Advance time and true anomaly; derive latitude and longitude.
7. Return period, energy, semi-major axis, apsides, phase, and ground-track fields.

## Mission profile

`SatelliteMissionProfile` is the main controller for satellite runs.

- `COAST` means no active maneuver is happening.
- `TRANSFER` means an orbit raise or transfer maneuver is active.
- `STATION_KEEPING` means the profile is holding a target altitude.

The profile owns maneuver timing and target choice. The simulator does not decide those things by itself.

## Assumptions

- Circular-orbit quantities are used even when the state records an eccentricity.
- Decay is a simplified drag-to-altitude relationship, not numerical orbital integration.
- Ground-track longitude is anomaly-based and does not model Earth rotation.
- `SatelliteMissionProfile` is the authoritative control layer for maneuver state; `SatelliteSimulation` performs propagation and bookkeeping.
- J2, solar radiation pressure, third-body effects, and ephemeris propagation are out of scope.

The model is useful for studying trends and workflow, not prediction of an operational satellite trajectory.
