import json
from dataclasses import asdict
from pathlib import Path
from enum import Enum


def export_json(results, filepath: str | Path) -> None:
    """Export dataclass result records to JSON, creating parent directories if needed."""
    if results is None:
        raise ValueError(
            "results must be an iterable of dataclass result records; got None"
        )

    rows = []
    for index, result in enumerate(results):
        try:
            row = asdict(result)
        except TypeError as error:
            raise ValueError(
                f"results[{index}] must be a dataclass result record; got {type(result).__name__}"
            ) from error

        def _make_serializable(value):
            if isinstance(value, Enum):
                return value.value
            if isinstance(value, dict):
                return {k: _make_serializable(v) for k, v in value.items()}
            if isinstance(value, list):
                return [_make_serializable(v) for v in value]
            return value

        rows.append(_make_serializable(row))

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(rows, file, indent=4)
    except (OSError, TypeError) as error:
        raise ValueError(f"Unable to write JSON export to {path}: {error}") from error
