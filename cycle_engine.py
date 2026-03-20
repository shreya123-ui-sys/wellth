from datetime import date
from database import get_connection

def log_period(user_id: str, period_start: str, cycle_length: int = 28, period_length: int = 5):
    conn = get_connection()
    conn.execute("""
        INSERT INTO cycle_logs (user_id, period_start, cycle_length, period_length)
        VALUES (?, ?, ?, ?)
    """, (user_id, period_start, cycle_length, period_length))
    conn.commit()
    conn.close()

def get_latest_cycle(user_id: str):
    conn = get_connection()
    row = conn.execute("""
        SELECT * FROM cycle_logs
        WHERE user_id = ?
        ORDER BY period_start DESC
        LIMIT 1
    """, (user_id,)).fetchone()
    conn.close()
    return row

def get_cycle_phase(user_id: str, today: str = None):
    if today is None:
        today = date.today().isoformat()

    row = get_latest_cycle(user_id)

    if not row:
        return {
            "phase": "unknown",
            "day": None,
            "description": "No cycle data logged yet.",
            "emoji": "❓"
        }

    period_start  = date.fromisoformat(row["period_start"])
    cycle_length  = row["cycle_length"]
    period_length = row["period_length"]
    today_date    = date.fromisoformat(today)

    day_of_cycle = (today_date - period_start).days % cycle_length + 1

    if day_of_cycle <= period_length:
        phase       = "menstrual"
        description = "Your body needs rest and gentle movement. Focus on recovery and iron-rich foods."
        emoji       = "🌑"
    elif day_of_cycle <= 13:
        phase       = "follicular"
        description = "Energy is rising! Great time to build strength and try new workouts."
        emoji       = "🌒"
    elif day_of_cycle <= 16:
        phase       = "ovulatory"
        description = "Peak energy and strength. Push harder today — your body is ready."
        emoji       = "🌕"
    else:
        phase       = "luteal"
        description = "Energy is dipping. Focus on moderate exercise, rest, and comfort foods."
        emoji       = "🌘"

    return {
        "phase":        phase,
        "day":          day_of_cycle,
        "description":  description,
        "emoji":        emoji,
        "cycle_length": cycle_length
    }

def get_phase_recommendations(phase: str):
    recommendations = {
        "menstrual": {
            "workout_type":      "Rest / Light yoga / Walking",
            "intensity":         "low",
            "nutrition_focus":   "Iron-rich foods, anti-inflammatory, warm meals",
            "foods_to_eat":      ["Spinach", "Lentils", "Dark chocolate", "Ginger tea", "Bananas"],
            "foods_to_avoid":    ["Caffeine", "Salty snacks", "Alcohol"],
            "calorie_adjustment": -100,
        },
        "follicular": {
            "workout_type":      "Strength training / Cardio / HIIT",
            "intensity":         "moderate-high",
            "nutrition_focus":   "High protein, complex carbs for energy",
            "foods_to_eat":      ["Eggs", "Quinoa", "Broccoli", "Berries", "Chicken"],
            "foods_to_avoid":    ["Processed sugar", "Heavy fried foods"],
            "calorie_adjustment": 0,
        },
        "ovulatory": {
            "workout_type":      "HIIT / Heavy lifting / Group classes",
            "intensity":         "high",
            "nutrition_focus":   "Antioxidant-rich, light and energising meals",
            "foods_to_eat":      ["Salmon", "Flaxseeds", "Fruits", "Leafy greens", "Almonds"],
            "foods_to_avoid":    ["Heavy carbs", "Excess dairy"],
            "calorie_adjustment": +100,
        },
        "luteal": {
            "workout_type":      "Moderate cardio / Pilates / Walking",
            "intensity":         "moderate",
            "nutrition_focus":   "Magnesium-rich foods, complex carbs to manage cravings",
            "foods_to_eat":      ["Sweet potato", "Dark chocolate", "Oats", "Pumpkin seeds", "Chamomile tea"],
            "foods_to_avoid":    ["Caffeine", "Refined sugar", "Alcohol"],
            "calorie_adjustment": +150,
        },
        "unknown": {
            "workout_type":      "Balanced full-body workout",
            "intensity":         "moderate",
            "nutrition_focus":   "Balanced macros",
            "foods_to_eat":      ["Whole grains", "Vegetables", "Lean protein"],
            "foods_to_avoid":    [],
            "calorie_adjustment": 0,
        }
    }
    return recommendations.get(phase, recommendations["unknown"])