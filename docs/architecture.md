# Architecture

## Data flow

```text
CSV dataset or benchmark → Aircraft/Satellite model → State + mission profile
→ AircraftSimulation/SatelliteSimulation → Result records → CSV/JSON/graphs
```

## Repository structure

```text
aerospace/
	aircraft/      Aircraft models, aerodynamics, geometry, and propulsion
	satellite/     Satellite models, orbital mechanics, maneuvers, and perturbations
	atmosphere/    Atmospheric models
	physics/       Shared constants and physical calculations
	navigation/    Navigation calculations
simulation/
	core/          State, results, telemetry, integration, and time stepping
	aircraft/      Aircraft simulator, profiles, and waypoint navigation
	satellite/     Satellite simulator, profiles, and maneuvers
	scenarios/     Scenario definitions, runners, and constellation execution
analytics/       Metrics, graphs, exports, and reports
datasets/        Input aircraft and satellite records
examples/        Runnable examples grouped by domain
tests/           Unit, integration, and validation tests
rust/            Optional Rust simulation engine crates
```

## Packages

| Package | Responsibility |
| --- | --- |
| `aerospace` | Aircraft, satellite, atmosphere, navigation, and shared physics calculations. |
| `simulation.core` | Mutable state, time stepping, integration, results, and telemetry. |
| `simulation.aircraft` | Aircraft propagation, flight profiles, and waypoint navigation. |
| `simulation.satellite` | Satellite propagation, mission profiles, and maneuvers. |
| `simulation.scenarios` | Scenario definitions, runners, and constellation simulation. |
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
