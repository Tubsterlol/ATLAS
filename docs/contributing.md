# Contributing

## Development principles

- Keep calculations small, named, and unit-explicit.
- State assumptions and fidelity limits in docstrings and the relevant model document.
- Add a focused test for each equation, boundary, or bug fix.
- Add a validation case when a change affects physical behavior.

## Adding a model

1. Place reusable equations under `aerospace/`.
2. Keep time integration and state mutation under `simulation/`.
3. Define explicit SI units in parameter names.
4. Add unit tests plus a documented validation reference where possible.
5. Update the README and the relevant document in `docs/`.

## Before opening a change

```bash
python -m pip install .
python -m pip install pytest
python -m pytest -q
```

Review generated output and keep data artifacts, caches, and local environment files out of version control.
