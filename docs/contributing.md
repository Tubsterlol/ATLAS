# Contributing

## Development principles

- Keep calculations small, named, and unit-explicit.
- State assumptions and fidelity limits in docstrings and the relevant model document.
- Add a focused test for each equation, boundary, or bug fix.
- Add a validation case when a change affects physical behavior.

## Adding a model

1. Place reusable equations and domain models under `aerospace/aircraft/`, `aerospace/satellite/`, or the relevant shared package.
2. Keep integration, mutable state, results, and telemetry under `simulation/core/`.
3. Keep aircraft and satellite propagation logic under their matching `simulation` subpackage.
4. Define explicit SI units in parameter names.
5. Add unit tests plus a documented validation reference where possible.
6. Update the README and the relevant document in `docs/`.

Prefer imports from the owning subpackage, such as `simulation.core.state` or `simulation.satellite.simulator`. Keep the top-level exports stable when changing a public type's implementation location.

## Before opening a change

```bash
python -m pip install .
python -m pip install pytest
python -m pytest -q
```

Review generated output and keep data artifacts, caches, and local environment files out of version control.
