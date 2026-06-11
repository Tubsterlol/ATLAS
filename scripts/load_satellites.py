import csv

from aerospace.satellite.satellite import Satellite


def load_satellite_dataset(filepath: str):

    satellites = {}

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            satellite_obj = Satellite(
                name=row["name"],
                mass_kg=float(row["mass_kg"]),
                cross_sectional_area_m2=float(row["cross_sectional_area_m2"]),
                drag_coefficient=float(row["drag_coefficient"]),
                altitude_m=float(row["altitude_m"]),
            )

            satellites[satellite_obj.name] = satellite_obj

    return satellites
