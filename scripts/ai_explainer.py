import os

def explain_day(day, model=None):
    if model is None:
        return "This plan balances training and nutrition for steady progress."

    prompt = f"""
    Explain this fitness day simply and clearly.

    Workout:
    {day['workout']['title']} - {day['workout'].get('description', '')}

    Meals:
    Breakfast: {day['meals']['breakfast']['name']}
    Lunch: {day['meals']['lunch']['name']}
    Dinner: {day['meals']['dinner']['name']}

    Keep it under 4 sentences.
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception:
        return "This plan supports balanced fitness and recovery."
