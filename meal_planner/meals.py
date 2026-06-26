import json
from pathlib import Path

with open(Path(__file__).parent / "meals.json") as f:
    MEALS = json.load(f)
