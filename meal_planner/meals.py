import json
from pathlib import Path

_MEALS_PATH = Path(__file__).parent / "meals.json"

with open(_MEALS_PATH) as f:
    MEALS = json.load(f)


def save_meals(meals: list) -> None:
    with open(_MEALS_PATH, "w") as f:
        json.dump(meals, f, indent=4)
