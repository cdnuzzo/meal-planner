import random

from meal_planner.meals import MEALS


def generate_plan(days: int = 5):
    return random.sample(MEALS, k=min(days, len(MEALS)))

def build_shopping_list(meals):
    ingredients = set()

    for meal in meals:
        ingredients.update(meal["ingredients"])

    return sorted(ingredients)


