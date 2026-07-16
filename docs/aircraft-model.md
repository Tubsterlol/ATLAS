# Aircraft Model

## Inputs and units

Aircraft definitions contain mass (kg), thrust (N), maximum speed (m/s), fuel burn (kg/s), a base drag coefficient, and `AircraftGeometry`. State holds altitude (m), speed (m/s), fuel (kg), climb rate (m/s), heading (degrees), and planar position (m).

## Per-step calculation

`AircraftSimulation.step()` performs these operations:

1. Applies an optional mission or waypoint profile.
2. Looks up ISA density and temperature at the current altitude.
3. Calculates trim angle of attack for weight support.
4. Calculates lift coefficient, induced drag, Mach number, wave drag, lift, and drag.
5. Applies a simplified thrust-minus-drag-minus-climb-force acceleration.
6. Burns fuel, updates altitude, advances time, and updates planar position.

Core relationships include:

```text
Lift = ½ ρ V² S CL
Drag = ½ ρ V² S CD
CDi = CL² / (π e AR)
Vs = √(2W / (ρ S CL))
```

## Assumptions

- Point-mass performance propagation; no rotational dynamics or control-surface model.
- Configured thrust is constant; there is no engine lapse or propulsion transient model.
- Heading is a north-referenced planar angle: 0° moves +Y and 90° moves +X.
- Stall and wave drag are deliberately simple coefficient models.
- The stall-speed utility assumes sea-level density.

See [validation.md](validation.md) for reference cases and limits.
