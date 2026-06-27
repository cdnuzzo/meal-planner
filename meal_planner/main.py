from typing import List, Optional

import typer

from meal_planner.meals import MEALS, save_meals
from meal_planner.planner import build_shopping_list

app = typer.Typer()

VALID_CATEGORIES = {"Produce", "Meats", "Frozen", "Other"}
CATEGORY_ORDER = ["Meats", "Produce", "Other", "Frozen"]


@app.callback()
def main():
    """Meal Planner CLI"""
    pass


@app.command()
def week(days: int = 5):
    """Interactively select meals for each day of the week."""
    if not MEALS:
        typer.echo("No meals saved. Use 'meal-planner add' to add some.")
        raise typer.Exit(1)

    typer.echo("Available meals:\n")
    for i, meal in enumerate(MEALS, 1):
        typer.echo(f"  {i}. {meal['name']}")
    typer.echo("")

    selected = []
    for day in range(1, days + 1):
        while True:
            raw = typer.prompt(f"Day {day}")
            try:
                choice = int(raw)
                if 1 <= choice <= len(MEALS):
                    selected.append(MEALS[choice - 1])
                    break
            except ValueError:
                pass
            typer.echo(f"  Enter a number between 1 and {len(MEALS)}.")

    typer.echo("\nMeal Plan")
    typer.echo("=========\n")
    for day, meal in enumerate(selected, 1):
        typer.echo(f"Day {day}: {meal['name']}")

    shopping_list = build_shopping_list(selected)

    typer.echo("\nShopping List")
    typer.echo("=============\n")

    for category in CATEGORY_ORDER:
        if category not in shopping_list:
            continue

        typer.echo(f"{category}:")

        for item in sorted(shopping_list[category]):
            typer.echo(f"  - {item}")

        typer.echo("")


@app.command("list")
def list_meals():
    """List all saved meals and their ingredients."""
    for meal in sorted(MEALS, key=lambda m: m["name"]):
        typer.echo(f"{meal['name']}")
        for ing in meal["ingredients"]:
            typer.echo(f"  - {ing['name']} ({ing['category']})")
        typer.echo("")


@app.command()
def add(
    name: str,
    ingredient: Optional[List[str]] = typer.Option(
        None, "--ingredient", "-i",
        help="Ingredient in 'name:Category' format. Repeat for multiple. "
             "Valid categories: Produce, Meats, Frozen, Other.",
    ),
):
    """Add a new meal. Optionally add ingredients with -i 'name:Category'."""
    if any(m["name"].lower() == name.lower() for m in MEALS):
        typer.echo(f"A meal named '{name}' already exists.")
        raise typer.Exit(1)

    ingredients = []
    for raw in (ingredient or []):
        parts = raw.rsplit(":", 1)
        if len(parts) != 2 or parts[1] not in VALID_CATEGORIES:
            typer.echo(
                f"Invalid format: '{raw}'. Use 'name:Category'.\n"
                f"Valid categories: {', '.join(sorted(VALID_CATEGORIES))}"
            )
            raise typer.Exit(1)
        ingredients.append({"name": parts[0].strip(), "category": parts[1].strip()})

    MEALS.append({"name": name, "ingredients": ingredients})
    save_meals(MEALS)
    typer.echo(f"Added '{name}' with {len(ingredients)} ingredient(s).")


@app.command()
def remove(
    name: str,
    yes: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation."),
):
    """Remove a meal by name."""
    match = next((m for m in MEALS if m["name"].lower() == name.lower()), None)
    if not match:
        typer.echo(f"No meal named '{name}'.")
        raise typer.Exit(1)

    if not yes:
        confirmed = typer.confirm(f"Remove '{match['name']}'?")
        if not confirmed:
            raise typer.Exit(0)

    MEALS.remove(match)
    save_meals(MEALS)
    typer.echo(f"Removed '{match['name']}'.")


if __name__ == "__main__":
    app()
