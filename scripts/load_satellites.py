import csv
from pathlib import Path

from aerospace.satellite.models.satellite import Satellite


REQUIRED_SATELLITE_COLUMNS = {
    "name",
    "mass_kg",
    "cross_sectional_area_m2",
    "drag_coefficient",
    "altitude_m",
}


def load_satellite_dataset(filepath: str | Path) -> dict[str, Satellite]:
    """Load satellite records and report dataset problems with row-level context."""
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Satellite dataset was not found: {path}")

    try:
        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            available_columns = set(reader.fieldnames or [])
            missing_columns = sorted(REQUIRED_SATELLITE_COLUMNS - available_columns)
            if missing_columns:
                raise ValueError(
                    f"Satellite dataset is missing required columns in {path}: "
                    f"{', '.join(missing_columns)}"
                )

            satellites = {}
            for row_number, row in enumerate(reader, start=2):
                try:
                    satellite = Satellite(
                        name=row["name"],
                        mass_kg=float(row["mass_kg"]),
                        cross_sectional_area_m2=float(row["cross_sectional_area_m2"]),
                        drag_coefficient=float(row["drag_coefficient"]),
                        altitude_m=float(row["altitude_m"]),
                    )
                except (KeyError, TypeError, ValueError) as error:
                    raise ValueError(
                        f"Invalid satellite record at row {row_number} in {path}: {error}"
                    ) from error
                satellites[satellite.name] = satellite
            return satellites
    except csv.Error as error:
        raise ValueError(
            f"Satellite dataset is not valid CSV: {path}: {error}"
        ) from error
