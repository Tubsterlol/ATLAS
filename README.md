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
- Ground-track latitude and longitude from inclination and true anomaly
- Orbit-raise and station-keeping maneuvers
- Multiple simulations through `ConstellationSimulation`

## Repository layout

```text
aerospace/       Reusable aircraft, satellite, atmosphere, physics, and navigation models
simulation/      State objects, time stepping, simulators, profiles, maneuvers, and scenarios
analytics/       CSV/JSON export and plotting helpers
datasets/        Aircraft and satellite CSV datasets used by the examples
examples/        Runnable simulations and orbital-parameter demonstrations
tests/           Physics validation and aircraft/satellite unit tests
```

## Quick start

ATLAS can be used directly on your host machine or inside the provided Docker container. Python 3.10+ is recommended for local runs; the Docker workflow uses Python 3.14 via the image defined in the Dockerfile.

### Local Python setup

```bash
git clone <repository-url>
cd ATLAS

# Optional but recommended
python -m venv .venv
source .venv/bin/activate

# Install the project and its runtime dependencies
python -m pip install .
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

To run the F-22 performance example and write a CSV to the outputs directory:

```bash
python examples/f22_performance.py
```

### Docker Compose workflow

The repository includes a simple Compose service named `atlas` in `docker-compose.yml`. It builds the image from the local Dockerfile, mounts the repository into `/app`, and starts an interactive shell by default.

```bash
docker compose build atlas
docker compose run --rm atlas
```

From inside the container, you can run the examples or tests directly:

```bash
python -m pip install .
python examples/scenario_demo.py
python examples/iss_orbital_parameters.py
python examples/f22_performance.py
pytest -q
```

Because the project root is bind-mounted into `/app`, changes made on the host are available immediately inside the container.

## Testing

Install the package and test dependencies first, then run the full suite from the repository root:

```bash
python -m pip install .
python -m pip install pytest
python -m pytest -q
```

The suite includes physics checks plus focused aircraft and satellite tests for mission profiles, aerodynamics, decay, maneuver handling, and simulation state updates.

## Documentation

- [Architecture](docs/architecture.md)
- [Aircraft model](docs/aircraft-model.md)
- [Satellite model](docs/satellite-model.md)
- [Datasets](docs/datasets.md)
- [Validation](docs/validation.md)
- [Contributing](docs/contributing.md)

## Current model boundaries

ATLAS favors transparent models over high-fidelity ones. In particular:

- The aircraft engine is a point-mass, time-stepped performance model; it does not solve full six-degree-of-freedom rigid-body dynamics or include a detailed propulsion model.
- The ISA model uses one simple formula for how temperature changes with altitude. It does not model all the different atmospheric layers separately.
- Satellite propagation assumes circular-orbit quantities and uses a simplified drag-to-altitude-decay relationship. It does not model a full perturbation environment, Earth rotation in longitude, other orbital disturbances, or highly accurate orbital data.
- Mission profiles own the control policy for aircraft and satellites. The simulators apply physics and advance time.
- API, database, and terminal UI directories are present as basic placeholders and are not yet product interfaces.

These limitations make the code suitable for teaching, experiments, and extension work, but results should be independently validated before any operational use.

## Next directions

Useful extensions include full flight-envelope and autopilot support, richer atmospheric and orbital perturbation models, orbital-element propagation, visualization, and a production API/UI layer.

## License

See [LICENSE](LICENSE).
