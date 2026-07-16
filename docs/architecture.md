# Architecture

## Data flow

```text
CSV dataset or benchmark → Aircraft/Satellite model → State + configuration
→ AircraftSimulation/SatelliteSimulation → Result records → CSV/JSON/graphs
```

## Packages

| Package | Responsibility |
| --- | --- |
| `aerospace` | Physics, atmosphere, navigation, aircraft, and satellite calculations. |
| `simulation` | Mutable state, time stepping, profiles, maneuvers, scenario runners, and simulators. |
| `analytics` | Result export and visualization helpers. |
| `scripts` | CSV dataset loading. |
| `datasets` | Example aircraft and satellite input records. |
| `tests` | Physics reference checks and unit tests. |

`api`, `database`, and `tui` are reserved for future product interfaces and are not active application layers.

## Simulation lifecycle

1. Construct a vehicle model and initial state directly, or load one from a dataset.
2. Construct the corresponding simulator with a timestep.
3. Call `step()` once or `run_step_count()` for a fixed number of steps.
4. Export or analyze the returned dataclass result records.

The simulator owns simulation time. Vehicle state is mutable and reflects the latest completed step.
