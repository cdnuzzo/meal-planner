PRODUCE = "Produce"
MEATS = "Meats"
FROZEN = "Frozen"
OTHER = "Other"

MEALS = [
    {
        "name": "Taco Salad",
        "ingredients": [
            {"name": "ground beef", "category": MEATS},
            {"name": "SouthWest salad", "category": PRODUCE},
            {"name": "mexican cheese", "category": OTHER},
            {"name": "Doritos", "category": OTHER},
            {"name": "shredded iceberg lettuce", "category": PRODUCE},
        ]
    },
    {
        "name": "Caesar Salad",
        "ingredients": [
            {"name": "Caesar Salad mix", "category": PRODUCE},
            {"name": "Chicken or Steak", "category": MEATS},
            {"name": "Croutons", "category": OTHER},
        ]
    },
    {
        "name": "Ribs",
        "ingredients": [
            {"name": "ribs", "category": MEATS},
            {"name": "carrots", "category": PRODUCE},
            {"name": "fries", "category": FROZEN},
            {"name": "BBQ sauce", "category": OTHER},
        ]
    }
]
