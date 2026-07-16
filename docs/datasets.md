# Datasets

Dataset loaders live in `scripts/` and accept CSV files with a header row.

## Aircraft schema

```text
name, manufacturer, mass_kg, drag_coefficient, thrust_n, max_speed_ms,
fuel_burn_kg_s, wing_span_m, wing_area_m2, mean_chord_m, sweep_deg,
taper_ratio, fuselage_length_m, fuselage_diameter_m,
horizontal_tail_area_m2, vertical_tail_area_m2
```

All dimensions are SI units. Coefficients and taper ratio are dimensionless; sweep is in degrees.

## Satellite schema

```text
name, mass_kg, cross_sectional_area_m2, drag_coefficient, altitude_m
```

Altitude is height above Earth’s reference surface in metres.

## Adding a dataset

Keep units in the header names, add one vehicle per row, and use a unique `name` when the file is intended for dictionary-based lookup. Run a small scenario after adding data to check that the model is within its intended operating range.
