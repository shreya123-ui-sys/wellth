import os

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False


def generate_ai_plan(context: dict) -> dict:
    """
    AI as a GENERATOR (optional).
    Falls back safely if no API key or package.
    """

    if not GENAI_AVAILABLE or not os.getenv("GOOGLE_API_KEY"):
        # Safe fallback
        return {
            "summary": "AI unavailable — fallback plan",
            "workout": "Full-body moderate session",
            "meals": "Balanced high-protein meals",
        }

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Create a 1-day fitness and meal plan.

    Context:
    {context}

    Return JSON with keys:
    - workout
    - meals
    - focus
    """

    response = model.generate_content(prompt)

    return {
        "ai_text": response.text
    }
