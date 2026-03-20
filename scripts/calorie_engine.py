def adjust_calories(base_calories: int, goal: str, training_day: str):
    calories = base_calories

    # Goal adjustment
    if goal == "fat_loss":
        calories -= 300
    elif goal == "muscle_gain":
        calories += 300

    # Training day adjustment
    if training_day == "intense":
        calories += 200
    elif training_day == "rest":
        calories -= 150

    return max(calories, 1200)
