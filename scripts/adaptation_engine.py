def adapt_plan(calorie_goal, readiness, feedback):
    """
    Adjusts calorie goal and workout readiness based on feedback
    """

    # Default = no change
    new_calorie_goal = calorie_goal
    new_readiness = readiness

    if feedback == "Too light":
        if calorie_goal == "fat_loss":
            new_calorie_goal = "maintain"
        elif calorie_goal == "maintain":
            new_calorie_goal = "muscle_gain"

        if readiness == "low":
            new_readiness = "maintain"
        elif readiness == "maintain":
            new_readiness = "high"

    elif feedback == "Too heavy":
        if calorie_goal == "muscle_gain":
            new_calorie_goal = "maintain"
        elif calorie_goal == "maintain":
            new_calorie_goal = "fat_loss"

        if readiness == "high":
            new_readiness = "maintain"
        elif readiness == "maintain":
            new_readiness = "low"

    return new_calorie_goal, new_readiness
