import typer

from meal_planner.planner import (
    generate_plan,
    build_shopping_list,
)

app = typer.Typer()


@app.callback()
def main():
    """Meal Planner CLI"""
    pass


@app.command()
def week(days: int = 5):
    
    """
    Generate a meal and shopping list for the week.
    """

    meals = generate_plan(days)

    typer.echo("Meal Plan")
    typer.echo("=========\n")

    for meal in meals:
        typer.echo(f"- {meal['name']}")

    shopping_list = build_shopping_list(meals)

    typer.echo("\nShopping List")
    typer.echo("=============\n")

    category_order = [
        "Meats",
        "Produce",
        "Other",
        "Frozen"
    ]

    for category in category_order:
        if category not in shopping_list:
            continue

        typer.echo(f"{category}:")

        for item in sorted(shopping_list[category]):
            typer.echo(f"  - {item}")

        typer.echo("")


if __name__ == "__main__":
    app()
