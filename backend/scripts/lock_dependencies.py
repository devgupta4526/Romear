"""Record the tested environment; run only after an intentional dependency update."""

from importlib.metadata import distributions
from pathlib import Path

pins = sorted(
    f"{distribution.metadata['Name']}=={distribution.version}"
    for distribution in distributions()
    if distribution.metadata["Name"].lower() not in {"pip", "setuptools", "romear-api"}
)
destination = Path(__file__).resolve().parents[1] / "requirements.lock"
destination.write_text(
    "# Python 3.14; exact tested runtime and check dependencies.\n" + "\n".join(pins) + "\n",
    encoding="utf-8",
)
