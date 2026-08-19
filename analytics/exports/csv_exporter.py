import csv
from dataclasses import asdict
from pathlib import Path


def export_csv(results, filepath: str | Path) -> None:
    """Export dataclass result records to CSV, creating parent directories if needed."""
    rows = _serialize_results(results)
    if not rows:
        return

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    except OSError as error:
        raise OSError(f"Unable to write CSV export to {path}: {error}") from error


def _serialize_results(results) -> list[dict]:
    if results is None:
        raise ValueError(
            "results must be an iterable of dataclass result records; got None"
        )

    rows = []
    for index, result in enumerate(results):
        try:
            rows.append(asdict(result))
        except TypeError as error:
            raise ValueError(
                f"results[{index}] must be a dataclass result record; got {type(result).__name__}"
            ) from error
    return rows
