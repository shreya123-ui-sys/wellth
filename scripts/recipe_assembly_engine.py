def assemble_daily_meals(diet, calories_target, day_index):
    """
    Returns breakfast, lunch, dinner
    """

    breakfast = {
        "name": "Oats with Fruits",
        "ingredients": ["Oats", "Milk", "Banana"],
        "calories": 400,
        "steps": ["Boil oats", "Add fruits", "Serve"]
    }

    lunch = {
        "name": "Balanced Rice Bowl",
        "ingredients": ["Rice", "Vegetables", "Protein"],
        "calories": 700,
        "steps": ["Cook rice", "Add veggies", "Add protein"]
    }

    dinner = {
        "name": "Light Dinner Plate",
        "ingredients": ["Soup", "Salad"],
        "calories": 500,
        "steps": ["Prepare soup", "Mix salad"]
    }

    return {
        "breakfast": breakfast,
        "lunch": lunch,
        "dinner": dinner
    }
