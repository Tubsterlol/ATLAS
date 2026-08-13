# Aircraft Model

## Inputs and units

Aircraft definitions contain mass (kg), thrust (N), maximum speed (m/s), fuel burn (kg/s), a base drag coefficient, and `AircraftGeometry`. State holds altitude (m), speed (m/s), fuel (kg), climb rate (m/s), heading (degrees), and planar position (m).

The aircraft side uses two layers:

- `MissionProfile` chooses the phase and target behavior.
- `AircraftSimulation` applies the physics and updates the state.

## Per-step calculation

`AircraftSimulation.step()` performs these operations:

1. Applies the active `MissionProfile`, which owns phase transitions and phase targets.
2. Applies optional waypoint navigation under the mission profile.
3. Looks up ISA density and temperature at the current altitude.
4. Calculates trim angle of attack for weight support.
5. Calculates lift coefficient, induced drag, Mach number, wave drag, lift, and drag.
6. Applies a simplified thrust-minus-drag-minus-climb-force acceleration.
7. Burns fuel, updates altitude, advances time, and updates planar position.

Core relationships include:

```text
Lift = ½ ρ V² S CL
Drag = ½ ρ V² S CD
CDi = CL² / (π e AR)
Vs = √(2W / (ρ S CL))
```

## Mission profile

`MissionProfile` is the main controller for aircraft missions.

- It starts in `TAKEOFF`.
- It moves to `CLIMB` when altitude passes the takeoff threshold.
- It moves to `CRUISE` when altitude reaches cruise altitude.
- It moves to `DESCENT` when fuel reaches the reserve limit.
- It moves to `LANDING` when altitude drops to the landing threshold.

`WaypointMission` does not choose the phase. It only updates route progress and heading.

## Assumptions

- Point-mass performance propagation; no rotational dynamics or control-surface model.
- Configured thrust is constant; there is no engine lapse or propulsion transient model.
- Heading is a north-referenced planar angle: 0° moves +Y and 90° moves +X.
- Heading is normalized to the range 0° to <360° after navigation updates.
- Stall and wave drag are deliberately simple coefficient models.
- The stall-speed utility assumes sea-level density.

See [validation.md](validation.md) for reference cases and limits.
