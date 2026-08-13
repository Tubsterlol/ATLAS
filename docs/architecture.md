# Architecture

## Data flow

```text
CSV dataset or benchmark → Aircraft/Satellite model → State + mission profile
→ AircraftSimulation/SatelliteSimulation → Result records → CSV/JSON/graphs
```

## Packages

| Package | Responsibility |
| --- | --- |
| `aerospace` | Physics, atmosphere, navigation, aircraft, and satellite calculations. |
| `simulation` | Mutable state, time stepping, mission profiles, maneuvers, scenario runners, and simulators. |
| `analytics` | Result export and visualization helpers. |
| `scripts` | CSV dataset loading. |
| `datasets` | Example aircraft and satellite input records. |
| `tests` | Physics reference checks and unit tests. |

`api`, `database`, and `tui` are reserved for future product interfaces and are not active application layers.

## Simulation lifecycle

1. Construct a vehicle model and initial state directly, or load one from a dataset.
2. Construct the mission profile that owns phase, target, and maneuver policy.
3. Construct the corresponding simulator with a timestep.
4. Call `step()` once or `run_step_count()` for a fixed number of steps.
5. Export or analyze the returned dataclass result records.

The simulator owns simulation time and physics propagation. Mission profiles own the control policy. Vehicle state is mutable and reflects the latest completed step.

## Aircraft flow

1. `MissionProfile` reads the current aircraft state.
2. It sets the current phase, target altitude, and target climb rate.
3. Optional waypoint navigation updates heading only.
4. `AircraftSimulation` applies the flight model and moves the state forward one step.

## Satellite flow

1. `SatelliteMissionProfile` reads the current satellite state.
2. It decides whether the mission is in coast, transfer, or station keeping.
3. It applies scheduled orbit changes or station keeping policy.
4. `SatelliteSimulation` applies drag decay, advances time, and updates orbit fields.
