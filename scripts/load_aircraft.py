import csv

from aerospace.aircraft.aircraft import Aircraft


def load_aircraft_dataset(filepath: str):

    aircraft = {}

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            aircraft_obj = Aircraft(
                name=row["name"],
                manufacturer=row["manufacturer"],
                mass_kg=float(row["mass_kg"]),
                wing_area_m2=float(row["wing_area_m2"]),
                wingspan_m=float(row["wingspan_m"]),
                drag_coefficient=float(row["drag_coefficient"]),
                lift_coefficient=float(row["lift_coefficient"]),
                thrust_n=float(row["thrust_n"]),
                max_speed_ms=float(row["max_speed_ms"]),
                fuel_burn_kg_s=float(row["fuel_burn_kg_s"]),
            )

            aircraft[aircraft_obj.name] = aircraft_obj

    return aircraft
