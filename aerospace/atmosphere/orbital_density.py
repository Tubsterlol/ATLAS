def orbital_density(altitude_m: float) -> float:

    altitude_km = altitude_m / 1000

    if altitude_km < 150:
        return 2e-9

    elif altitude_km < 200:
        return 2e-10

    elif altitude_km < 300:
        return 3e-11

    elif altitude_km < 400:
        return 5e-12

    elif altitude_km < 500:
        return 1e-12

    elif altitude_km < 600:
        return 3e-13

    elif altitude_km < 700:
        return 1e-13

    return 1e-14
