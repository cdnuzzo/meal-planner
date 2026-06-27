# Meal Planner

A CLI tool for generating weekly meal plans and shopping lists. Meals and ingredients are stored locally in a JSON file and managed entirely from the terminal.

## Installation

```bash
pip install -e .
```

## Commands

### `week`

Interactively select a meal for each day, then displays the full meal plan and a deduplicated shopping list grouped by category.

```bash
meal-planner week          # 5-day plan (default)
meal-planner week --days 3 # 3-day plan
```

**Example session:**
```
Available meals:

  1. Taco Salad
  2. Caesar Salad
  3. Ribs
  4. Beef Stew
  5. Pesto Pasta

Day 1: 3
Day 2: 1
Day 3: 4
Day 4: 2
Day 5: 5

Meal Plan
=========

Day 1: Ribs
Day 2: Taco Salad
Day 3: Beef Stew
Day 4: Caesar Salad
Day 5: Pesto Pasta

Shopping List
=============

Meats:
  - fish or chicken
  - ground beef
  - ribs
  - stew meat
  ...
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
