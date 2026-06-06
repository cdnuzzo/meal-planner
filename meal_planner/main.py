import typer

from meal_planner.planner import (
    generate_plan,
    build_shopping_list,
)

app = typer.Typer()

@app.callback()
def main():
    """
    Meal planner CLI
    """
    pass

@app.command()
def week():
    meals = generate_plan()

    typer.echo("Meal Plan")
    typer.echo("=========\n")

    for meal in meals:
        typer.echo(f"- {meal['name']}")

    typer.echo("\nShopping List")
    typer.echo("=============\n")

    for item in build_shopping_list(meals):
        typer.echo(f"- {item}")


if __name__ == "__main__":
    app()
