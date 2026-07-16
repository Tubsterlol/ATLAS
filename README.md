# ATLAS

ATLAS is a Python framework for exploring aircraft performance and low-Earth-orbit satellite dynamics. It combines reusable aerospace calculations with time-stepped simulators, scenarios, datasets, and result exporters.

It is designed for education, prototyping, and experimentation—not flight- or mission-certified analysis.

## Capabilities

- **Aircraft:** atmosphere, lift and drag, trim, stall, Mach/Reynolds numbers, fuel burn, altitude, and two-dimensional navigation.
- **Satellites:** circular-orbit properties, simplified atmospheric drag/decay, ground tracks, orbit raises, and station keeping.
- **Workflow:** CSV datasets → model objects → simulator state → result records → CSV/JSON exports.

## Quick start

From the repository root, run an included scenario:

```bash
python examples/scenario_demo.py
python examples/iss_orbital_parameters.py
```

Run the test suite with:

```bash
pytest -q
```

## Documentation

- [Architecture](docs/architecture.md)
- [Aircraft model](docs/aircraft-model.md)
- [Satellite model](docs/satellite-model.md)
- [Datasets](docs/datasets.md)
- [Validation](docs/validation.md)
- [Contributing](docs/contributing.md)

## Limitations

ATLAS uses transparent, simplified models. Aircraft propagation is not six-degree-of-freedom dynamics; atmospheric calculations use a limited ISA formulation; and satellite propagation is circular-orbit and drag-decay oriented. Independently validate results before any operational use.

## License

See [LICENSE](LICENSE).
