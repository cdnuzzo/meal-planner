import random

from meal_planner.meals import MEALS


def generate_plan(days: int = 5):
    return random.sample(MEALS, k=min(days, len(MEALS)))


def build_shopping_list(meals):
    shopping_list = {}

    for meal in meals:
        for ingredient in meal["ingredients"]:
            category = ingredient["category"]
            name = ingredient["name"]

            if category not in shopping_list:
                shopping_list[category] = set()

            shopping_list[category].add(name)

    return shopping_list
