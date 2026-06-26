# Meal Planner

A CLI tool for generating weekly meal plans and shopping lists. Meals and ingredients are stored locally in a JSON file and managed entirely from the terminal.

## Installation

```bash
pip install -e .
```

## Commands

### `week`

Generate a random meal plan and grouped shopping list for the week.

```bash
meal-planner week          # 5-day plan (default)
meal-planner week --days 3 # 3-day plan
```

**Example output:**
```
Meal Plan
=========

- Taco Salad
- Ribs
- Beef Stew

Shopping List
=============

Meats:
  - ground beef
  - ribs
  - stew meat

Produce:
  - carrots
  - peppers
  - potatoes
  - shredded iceberg lettuce
  - SouthWest salad

Other:
  - BBQ sauce
  - beef broth
  - Doritos
  - mexican cheese

Frozen:
  - fries
```

---

### `list`

Show all saved meals and their ingredients.

```bash
meal-planner list
```

---

### `add`

Add a new meal. Ingredients are optional at creation time and use the format `name:Category`.

```bash
meal-planner add "Chicken Stir Fry"
meal-planner add "Chicken Stir Fry" -i "chicken breast:Meats" -i "broccoli:Produce" -i "soy sauce:Other"
```

Valid categories: `Produce`, `Meats`, `Frozen`, `Other`

---

### `remove`

Remove a meal by name. Prompts for confirmation unless `--yes` is passed.

```bash
meal-planner remove "Chicken Stir Fry"
meal-planner remove "Chicken Stir Fry" --yes
```

---

## Project Structure

```
meal_planner/
├── main.py      # CLI commands (Typer)
├── planner.py   # meal plan generation and shopping list logic
├── meals.py     # JSON loader and save function
└── meals.json   # meal and ingredient data
```

## Stack

- Python 3.9+
- [Typer](https://typer.tiangolo.com/) for the CLI
