"""Small, dependency-free validation helpers for public ATLAS inputs."""


def require_non_empty_string(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string; got {value!r}")


def require_positive(value: float, name: str) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero; got {value}")


def require_non_negative(value: float, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative; got {value}")


def require_in_range(value: float, name: str, minimum: float, maximum: float) -> None:
    if not minimum <= value <= maximum:
        raise ValueError(
            f"{name} must be between {minimum} and {maximum}; got {value}"
        )
