import csv
from pathlib import Path

from aerospace.aircraft.geometry.geometry import AircraftGeometry
from aerospace.aircraft.models.aircraft import Aircraft


REQUIRED_AIRCRAFT_COLUMNS = {
    "name",
    "manufacturer",
    "mass_kg",
    "drag_coefficient",
    "thrust_n",
    "max_speed_ms",
    "fuel_burn_kg_s",
    "wing_span_m",
    "wing_area_m2",
    "mean_chord_m",
    "sweep_deg",
    "taper_ratio",
    "fuselage_length_m",
    "fuselage_diameter_m",
    "horizontal_tail_area_m2",
    "vertical_tail_area_m2",
}


def load_aircraft_dataset(filepath: str | Path) -> dict[str, Aircraft]:
    """Load aircraft records and report dataset problems with row-level context."""
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Aircraft dataset was not found: {path}")

    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            _validate_columns(reader.fieldnames, REQUIRED_AIRCRAFT_COLUMNS, path)
            return {
                aircraft.name: aircraft
                for row_number, row in enumerate(reader, start=2)
                for aircraft in [_parse_aircraft_row(row, row_number, path)]
            }
    except csv.Error as error:
        raise ValueError(
            f"Aircraft dataset is not valid CSV: {path}: {error}"
        ) from error


def _validate_columns(columns, required_columns: set[str], path: Path) -> None:
    available_columns = set(columns or [])
    missing_columns = sorted(required_columns - available_columns)
    if missing_columns:
        raise ValueError(
            f"Aircraft dataset is missing required columns in {path}: "
            f"{', '.join(missing_columns)}"
        )


def _parse_aircraft_row(row: dict[str, str], row_number: int, path: Path) -> Aircraft:
    try:
        geometry = AircraftGeometry(
            wing_span_m=float(row["wing_span_m"]),
            wing_area_m2=float(row["wing_area_m2"]),
            mean_chord_m=float(row["mean_chord_m"]),
            sweep_deg=float(row["sweep_deg"]),
            taper_ratio=float(row["taper_ratio"]),
            fuselage_length_m=float(row["fuselage_length_m"]),
            fuselage_diameter_m=float(row["fuselage_diameter_m"]),
            horizontal_tail_area_m2=float(row["horizontal_tail_area_m2"]),
            vertical_tail_area_m2=float(row["vertical_tail_area_m2"]),
        )
        return Aircraft(
            name=row["name"],
            manufacturer=row["manufacturer"],
            mass_kg=float(row["mass_kg"]),
            drag_coefficient=float(row["drag_coefficient"]),
            thrust_n=float(row["thrust_n"]),
            max_speed_ms=float(row["max_speed_ms"]),
            fuel_burn_kg_s=float(row["fuel_burn_kg_s"]),
            geometry=geometry,
        )
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(
            f"Invalid aircraft record at row {row_number} in {path}: {error}"
        ) from error
