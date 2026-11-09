import json
from pathlib import Path

from app.config import Settings
from app.main import create_app

destination = Path(__file__).resolve().parents[2] / "docs" / "openapi.json"
destination.write_text(
    json.dumps(create_app(Settings()).openapi(), indent=2) + "\n", encoding="utf-8"
)
print(destination)
