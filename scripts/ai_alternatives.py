# scripts/ai_alternatives.py

def suggest_alternatives(day, model=None):
    """
    AI-generated alternatives for a single day.
    Does NOT modify the original plan.
    """

    # Safe fallback (no AI / model missing)
    if model is None:
        return {
            "workout": "Full-body bodyweight circuit (same intensity)",
            "meals": {
                "breakfast": "Greek yogurt with fruits",
                "lunch": "Grilled paneer with rice",
                "dinner": "Dal, roti, and vegetables"
            }
        }

    prompt = f"""
    Suggest alternatives for the following fitness plan.
    Keep difficulty and calories similar.

    Workout:
    {day.get('workout', {})}

    Meals:
    {day.get('meals', {})}

    Respond briefly and clearly.
    """

    try:
        response = model.generate_content(prompt)
        return {
            "ai_text": response.text.strip()
        }
    except Exception as e:
        return {
            "ai_text": f"AI unavailable right now: {e}"
        }
