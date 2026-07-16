import json
from dataclasses import asdict
from pathlib import Path


def export_json(results, filepath: str | Path) -> None:
    """Export dataclass result records to JSON, creating parent directories if needed."""
    if results is None:
        raise ValueError("results must be an iterable of dataclass result records; got None")

    rows = []
    for index, result in enumerate(results):
        try:
            rows.append(asdict(result))
        except TypeError as error:
            raise ValueError(
                f"results[{index}] must be a dataclass result record; got {type(result).__name__}"
            ) from error

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(rows, file, indent=4)
    except (OSError, TypeError) as error:
        raise ValueError(f"Unable to write JSON export to {path}: {error}") from error
