def assemble_daily_plan(diet, readiness, equipment, day_index):
    """
    Builds a single day's plan using rule-based logic.
    AI layers can override this later.
    """

    # ---- Workout logic (simple baseline) ----
    workout = {
        "title": "Full Body Conditioning",
        "description": f"Readiness level {readiness}. Focus on form and recovery."
    }

    # ---- Meals logic (diet-aware placeholder) ----
    meals = {
        "breakfast": {"name": f"{diet.title()} Breakfast"},
        "lunch": {"name": f"{diet.title()} Lunch"},
        "dinner": {"name": f"{diet.title()} Dinner"},
    }

    return {
        "day": day_index,
        "workout": workout,
        "meals": meals
    }
