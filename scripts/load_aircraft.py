import csv

from aerospace.aircraft.aircraft import Aircraft
from aerospace.aircraft.geometry import AircraftGeometry
from aerospace.aircraft.geometry_calculations import aspect_ratio


def load_aircraft_dataset(filepath: str):

    aircraft = {}

    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
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

            aircraft_obj = Aircraft(
                name=row["name"],
                manufacturer=row["manufacturer"],
                mass_kg=float(row["mass_kg"]),
                drag_coefficient=float(row["drag_coefficient"]),
                thrust_n=float(row["thrust_n"]),
                max_speed_ms=float(row["max_speed_ms"]),
                fuel_burn_kg_s=float(row["fuel_burn_kg_s"]),
                geometry=geometry,
            )

            aircraft[aircraft_obj.name] = aircraft_obj

    return aircraft
