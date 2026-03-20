import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")
else:
    model = None


def ai_coach_response(readiness, exercises, meal_summary):
    if not model:
        return (
            "You're doing great! 💪 Stay consistent, focus on good form, and recover well."
        )

    prompt = f"""
You are a friendly gym buddy and wellness coach.

User readiness: {readiness}
Planned exercises: {exercises}
Meals: {meal_summary}

Give:
- Motivation
- Why this plan fits
- One small improvement tip
"""

    try:
        return model.generate_content(prompt).text
    except Exception:
        return "Nice work showing up! Consistency beats perfection."


def ai_answer_question(question, context):
    if not model:
        return "Great question! Focus on consistency and listening to your body."

    prompt = f"""
You are a friendly fitness and nutrition coach.

Context:
{context}

User question:
{question}

Answer clearly and positively.
"""

    try:
        return model.generate_content(prompt).text
    except Exception:
        return "You're on the right track — keep it simple and consistent."


def ai_explain_exercise(exercise_name):
    """
    Explain an exercise clearly for beginners.
    """

    if not model:
        return (
            f"{exercise_name} works multiple muscle groups. "
            "Focus on controlled movement, proper posture, and breathing."
        )

    prompt = f"""
Explain the exercise "{exercise_name}" in a friendly way.

Include:
- What muscles it works
- How to do it correctly
- 1–2 form tips
Keep it short and beginner-friendly.
"""

    try:
        return model.generate_content(prompt).text
    except Exception:
        return (
            f"{exercise_name} is effective when done with good form. "
            "Move slowly and stay controlled."
        )
