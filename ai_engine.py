import os


try:
    from google import genai
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False

_client = None


def _get_client():
    global _client
    if _client is not None:
        return _client
    if not GENAI_AVAILABLE:
        return None
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        _client = genai.Client(api_key=api_key)
        return _client
    except Exception:
        return None


def _ask(prompt: str, fallback: str) -> str:
    client = _get_client()
    if not client:
        return fallback
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        return fallback


def generate_recipe(diet: str, goal: str, cycle_phase: str, meal_type: str) -> str:
    prompt = f"""
You are a nutritionist and chef specialising in women's health and Indian cuisine.

Generate ONE {meal_type} recipe for a woman with these needs:
- Diet: {diet}
- Fitness goal: {goal.replace('_', ' ')}
- Menstrual cycle phase: {cycle_phase}

The recipe must:
- Use Indian or Indian-fusion ingredients
- Be practical and easy to make at home
- Support her cycle phase nutritionally
- Be appropriate for her fitness goal

Format your response EXACTLY like this:

RECIPE NAME: [name]
CALORIES: [number]
PROTEIN: [number]g
CARBS: [number]g
FAT: [number]g
PREP TIME: [number] minutes

INGREDIENTS:
- [ingredient 1]
- [ingredient 2]
- [ingredient 3]

STEPS:
1. [step 1]
2. [step 2]
3. [step 3]

NUTRITION NOTE: [one sentence about why this is good for her phase]
"""
    fallback = f"""RECIPE NAME: Balanced {meal_type.title()} Bowl
CALORIES: 350
PROTEIN: 15g
CARBS: 45g
FAT: 10g
PREP TIME: 20 minutes

INGREDIENTS:
- 1 cup whole grains
- 1 cup vegetables
- 1 serving protein of choice
- Spices to taste

STEPS:
1. Cook grains as per package instructions.
2. Sauté vegetables with spices.
3. Combine and serve hot.

NUTRITION NOTE: A balanced meal supporting your current phase and goal."""
    return _ask(prompt, fallback)


def generate_workout_tip(phase: str, workout_name: str, intensity: str) -> str:
    prompt = f"""
You are a women's fitness coach who understands cycle-syncing.

Give a short motivating tip (3-4 sentences max) for a woman who is:
- In her {phase} phase
- About to do: {workout_name}
- Intensity level: {intensity}

Be specific, practical and encouraging.
"""
    fallback = "Listen to your body today. Focus on form over speed, and remember that showing up is the hardest part. You've got this! 💪"
    return _ask(prompt, fallback)


def generate_meal_swap(food_name: str, diet: str, reason: str) -> str:
    prompt = f"""
You are a nutritionist specialising in Indian women's health.

Suggest 2-3 healthy swaps for "{food_name}" for someone who is:
- Diet: {diet}
- Reason for swap: {reason}

Keep suggestions practical, Indian-friendly, and brief.
Format as a simple list.
"""
    fallback = f"Try replacing {food_name} with a lighter, protein-rich alternative that suits your diet."
    return _ask(prompt, fallback)


def generate_weekly_nutrition_insight(diet: str, goal: str, phase: str,
                                       avg_calories: float, avg_protein: float) -> str:
    prompt = f"""
You are a nutritionist reviewing a woman's weekly eating habits.

Her stats this week:
- Diet: {diet}
- Goal: {goal.replace('_', ' ')}
- Cycle phase: {phase}
- Average daily calories: {avg_calories} kcal
- Average daily protein: {avg_protein}g

Give a 3-4 sentence personalised insight covering:
- How her intake compares to her goal
- One thing she's doing well
- One specific improvement for next week

Be warm, encouraging and specific.
"""
    fallback = "You're building great habits! Focus on hitting your protein target consistently this week, and make sure to stay hydrated especially during your current cycle phase."
    return _ask(prompt, fallback)


def explain_cycle_phase(phase: str) -> str:
    prompt = f"""
Explain the {phase} phase of the menstrual cycle to a young woman in simple, friendly language.

Cover:
- What's happening hormonally (keep it simple)
- How she might feel physically and emotionally
- Why certain workouts and foods work better now

Keep it under 5 sentences. Be warm and informative, not clinical.
"""
    fallback = f"The {phase} phase brings unique hormonal shifts that affect your energy, mood and recovery. Tuning your workouts and meals to this phase can make a big difference in how you feel and perform."
    return _ask(prompt, fallback)