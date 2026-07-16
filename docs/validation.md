# ATLAS Model Validation

## Purpose

This document records reference checks for the simplified models implemented in ATLAS. A passing unit test confirms that code behaves as implemented; a validation case checks whether that implementation produces a physically reasonable result for a defined input.

ATLAS is an educational and exploratory framework. These checks do not qualify it for operational flight or mission analysis.

## Method

Each baseline case has a fixed input, an independent reference value or analytical equation, an ATLAS result, and an acceptance tolerance. Values are rounded to the precision useful for the current model fidelity.

| Status | Meaning |
| --- | --- |
| Baseline | Reference check implemented in the automated suite. |
| Planned | A useful case whose source data and acceptance tolerance have not yet been established. |

## Baseline checks

### Gravity

| Case | Input | Reference | ATLAS result | Tolerance | Status |
| --- | --- | --- | --- | --- | --- |
| Surface gravity | Altitude: 0 m | 9.81 m/s² | 9.82 m/s² | ±0.1 m/s² | Baseline |

The result is calculated from the Newtonian gravity equation using the Earth mass and radius constants in `aerospace.physics.constants`.

### Circular-orbit mechanics

| Case | Input | Reference | ATLAS result | Tolerance | Status |
| --- | --- | --- | --- | --- | --- |
| ISS-like orbital speed | Altitude: 400 km | 7.6–7.8 km/s | ~7.67 km/s | Within range | Baseline |
| ISS orbital period | Altitude: 408 km | ~92.6 min | 92.58 min | ±1 min | Baseline |

These values assume a circular orbit and use Earth’s standard gravitational parameter. They do not validate perturbation propagation.

### Standard atmosphere

| Case | Input | Reference | ATLAS result | Tolerance | Status |
| --- | --- | --- | --- | --- | --- |
| Sea-level density | 0 m | 1.225 kg/m³ | 1.225 kg/m³ | ±0.01 kg/m³ | Baseline |
| Density at 10 km | 10,000 m | ~0.41 kg/m³ | ~0.41 kg/m³ | ±0.03 kg/m³ | Baseline |

The implemented ISA calculation is a single lapse-rate layer. Do not use this validation beyond the altitude range supported by that approximation.

### Aircraft performance

| Case | Input | Reference | ATLAS result | Tolerance | Status |
| --- | --- | --- | --- | --- | --- |
| F-16 thrust-to-weight | 129,000 N thrust; 12,000 kg mass | ~1.10 | 1.096 | ±0.02 | Baseline |
| Generic stall speed | 10,000 kg; 30 m²; CL = 1.5 | Positive finite value | 59.66 m/s | Exact equation | Baseline |
| F-16 Reynolds number | 250 m/s at sea level; 2.8 m chord | Order of 10⁷–10⁸ | ~4.7 × 10⁷ | One order of magnitude | Baseline |

The stall-speed calculation assumes sea-level density and a specified lift coefficient. It is not a replacement for aircraft-specific flight-manual data.

## Model assumptions and exclusions

- Aircraft motion is a point-mass performance model, not a six-degree-of-freedom rigid-body simulation.
- The aerodynamic model uses configured coefficients and simple lift, induced-drag, stall, and wave-drag relationships.
- Satellite quantities are circular-orbit approximations; the decay calculation is a simplified drag-to-altitude relationship.
- No baseline currently covers winds, propulsion lapse, non-spherical gravity, J2, solar radiation pressure, or high-fidelity atmospheric density.

## Adding a validation case

1. State the model function and exact input values.
2. Cite an analytical derivation, standard, or authoritative reference dataset.
3. Define a tolerance that matches the model’s stated fidelity.
4. Add an automated test and add the result to the relevant table above.
5. Record any deliberate deviation from the reference and why it is acceptable.
