def wave_drag_coefficient(
    mach: float,
) -> float:
    """
    Simple wave drag model.

    Returns the additional drag coefficient caused
    by compressibility effects.
    """

    if mach < 0.80:
        return 0.0

    elif mach < 1.00:
        return 0.15 * (mach - 0.80) / 0.20

    elif mach < 1.20:
        return 0.15 + 0.10 * (mach - 1.00) / 0.20

    else:
        return 0.25
