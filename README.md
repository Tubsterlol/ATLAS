# ATLAS

**ATLAS** is a Python framework for exploring aircraft performance and low-Earth-orbit satellite dynamics. It combines reusable aerospace calculations with small, time-stepped simulation engines, scenario runners, sample datasets, and export utilities.

It is intended for engineering education, prototyping, and experimentation. The models are deliberately approachable; ATLAS is not a flight-certified or mission-certified analysis tool.

## What it can simulate

### Aircraft

- ISA temperature and density at the simulated altitude
- Lift, parasite drag, induced drag, wave drag, stall, trim, Mach number, and Reynolds number
- Thrust-driven acceleration, fuel burn, climb/descent, and two-dimensional position updates
- Flight profiles, mission phases, and waypoint steering

### Satellites

- Circular-orbit velocity, period, specific orbital energy, and semi-major axis
- Simplified atmospheric drag and altitude-decay propagation
- Ground-track latitude/longitude from inclination and true anomaly
- Orbit-raise and station-keeping maneuvers
- Multiple simulations through `ConstellationSimulation`

## Repository layout

```text
aerospace/       Reusable aircraft, satellite, atmosphere, physics, and navigation models
simulation/      State objects, time stepping, simulators, profiles, maneuvers, and scenarios
analytics/       CSV/JSON export and plotting helpers
datasets/        Aircraft and satellite CSV datasets used by the examples
examples/        Runnable simulations and orbital-parameter demonstrations
tests/           Physics validation and aircraft unit/integration-style tests
```

## Quick start

ATLAS currently has no runtime third-party dependency. Python 3.10+ is recommended.

```bash
git clone <repository-url>
cd ATLAS

# Optional but recommended
python -m venv .venv
source .venv/bin/activate

# Needed to run the tests
python -m pip install pytest
```

Run an aircraft scenario from the repository root:

```bash
python examples/scenario_demo.py
```

This loads the F-16 from `datasets/aircraft/military.csv`, simulates 1,000 one-second steps, and prints the first and last `AircraftResult`.

For a quick orbital calculation:

```bash
python examples/iss_orbital_parameters.py
```

## Using the library

The aircraft simulator takes an `Aircraft` definition plus a mutable `AircraftState`. Each call to `step()` advances the state and returns a record containing the quantities calculated during that step.

```python
from aerospace.aircraft.geometry.geometry import AircraftGeometry
from aerospace.aircraft.models.aircraft import Aircraft
from simulation.aircraft_simulator import AircraftSimulation
from simulation.state import AircraftState

aircraft = Aircraft(
    name="Demo aircraft",
    manufacturer="ATLAS",
    mass_kg=2_000,
    drag_coefficient=0.02,
    thrust_n=20_000,
    max_speed_ms=300,
    fuel_burn_kg_s=0.5,
    geometry=AircraftGeometry(
        wing_span_m=15.0,
        wing_area_m2=25.0,
        mean_chord_m=2.0,
        taper_ratio=0.5,
        sweep_deg=20.0,
        fuselage_length_m=12.0,
        fuselage_diameter_m=1.5,
        horizontal_tail_area_m2=5.0,
        vertical_tail_area_m2=3.0,
    ),
)

state = AircraftState(
    altitude_m=1_000,
    velocity_ms=100,
    fuel_kg=100,
    climb_rate_ms=5,
    heading_deg=90,
)

simulation = AircraftSimulation(aircraft, state, timestep_s=1.0)
results = simulation.run_step_count(60)

print(results[-1].altitude_m)
print(results[-1].velocity_ms)
```

For dataset-driven runs, use `simulation.scenario_runner.run_aircraft_scenario` or `run_satellite_scenario`. See [scenario_demo.py](examples/scenario_demo.py), [f16_performance.py](examples/f16_performance.py), and [iss_simulation.py](examples/iss_simulation.py).

## Results and exports

`AircraftSimulation` produces `AircraftResult` objects, including time, altitude, speed, forces, atmosphere, fuel, position, angle of attack, drag breakdown, and stall status. `SatelliteSimulation` returns equivalent `SatelliteResult` orbital and decay fields.

Export result lists with:

```python
from analytics.exports.csv_exporter import export_csv
from analytics.exports.json_exporter import export_json

export_csv(results, "outputs/run.csv")
export_json(results, "outputs/run.json")
```

The `outputs/` directory is included for generated files. Exporters expect their destination directory to exist.

## Dataset formats

Aircraft datasets contain the vehicle properties and planform/geometry values consumed by `scripts.load_aircraft_dataset`:

```text
name, manufacturer, mass_kg, drag_coefficient, thrust_n, max_speed_ms,
fuel_burn_kg_s, wing_span_m, wing_area_m2, mean_chord_m, sweep_deg,
taper_ratio, fuselage_length_m, fuselage_diameter_m,
horizontal_tail_area_m2, vertical_tail_area_m2
```

Satellite datasets are read by `scripts.load_satellite_dataset`:

```text
name, mass_kg, cross_sectional_area_m2, drag_coefficient, altitude_m
```

## Testing

Run the full suite from the repository root:

```bash
python -m pytest -q
```

The suite includes broad physics checks plus focused aircraft tests for aerodynamic equations, stall and wave-drag boundaries, trim, performance and geometry utilities, and simulation state updates.

## Current model boundaries

ATLAS favors transparent models over high-fidelity ones. In particular:

- The aircraft engine is a point-mass, time-stepped performance model; it does not solve full six-degree-of-freedom rigid-body dynamics or include a detailed propulsion model.
- The ISA implementation uses a single temperature lapse-rate formulation, not the full multi-layer standard atmosphere.
- Satellite propagation assumes circular-orbit quantities and uses a simplified drag-to-altitude-decay relationship. It does not model a full perturbation environment, Earth rotation in longitude, or ephemeris-grade orbital propagation.
- API, database, and terminal UI directories are present as scaffolding and are not yet product-facing interfaces.

These limitations make the code suitable for teaching, experiments, and extension work, but results should be independently validated before any operational use.

## Next directions

Useful extensions include full flight-envelope and autopilot support, richer atmospheric and orbital perturbation models, orbital-element propagation, visualization, and a production API/UI layer.

## License

See [LICENSE](LICENSE).
