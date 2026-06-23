from aerospace.satellite.orbital_parameters import (
    orbital_energy,
    orbital_period,
    semi_major_axis,
)
from scripts.load_satellites import load_satellite_dataset

satellites = load_satellite_dataset("datasets/satellites/satellites.csv")

iss = satellites["ISS"]

print(f"Altitude: {iss.altitude_m:.0f} m")

print(f"Semi-major axis: {semi_major_axis(iss.altitude_m):.0f} m")

print(f"Orbital period: {orbital_period(iss.altitude_m) / 60:.2f} min")

print(f"Orbital energy: {orbital_energy(iss.altitude_m):.2f} J/kg")
