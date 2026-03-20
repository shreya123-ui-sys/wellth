from database import get_connection
from datetime import date
import random


WORKOUT_LIBRARY = {
    "low": [
        {
            "name": "Gentle Yoga",
            "duration": 30,
            "exercises": [
                {"exercise": "Child's Pose",        "sets": 1, "reps": "60 sec",           "instructions": "Breathe deeply, relax hips to heels."},
                {"exercise": "Cat-Cow Stretch",      "sets": 2, "reps": "10 reps",          "instructions": "Slow and controlled, follow your breath."},
                {"exercise": "Seated Forward Fold",  "sets": 2, "reps": "30 sec",           "instructions": "Keep spine long, don't force it."},
                {"exercise": "Supine Twist",         "sets": 2, "reps": "30 sec each side", "instructions": "Let gravity do the work."},
            ]
        },
        {
            "name": "Light Walking + Stretching",
            "duration": 30,
            "exercises": [
                {"exercise": "Brisk Walk",            "sets": 1, "reps": "20 min",        "instructions": "Comfortable pace, focus on breathing."},
                {"exercise": "Standing Quad Stretch", "sets": 2, "reps": "30 sec each",   "instructions": "Hold wall for balance if needed."},
                {"exercise": "Hip Flexor Stretch",    "sets": 2, "reps": "30 sec each",   "instructions": "Keep torso upright."},
            ]
        }
    ],
    "moderate": [
        {
            "name": "Full Body Strength",
            "duration": 45,
            "exercises": [
                {"exercise": "Bodyweight Squats", "sets": 3, "reps": "12",          "instructions": "Chest up, knees over toes."},
                {"exercise": "Push-Ups",          "sets": 3, "reps": "10",          "instructions": "Core tight, full range of motion."},
                {"exercise": "Glute Bridges",     "sets": 3, "reps": "15",          "instructions": "Squeeze glutes at the top."},
                {"exercise": "Plank",             "sets": 3, "reps": "30 sec",      "instructions": "Straight line from head to heels."},
                {"exercise": "Lunges",            "sets": 3, "reps": "10 each leg", "instructions": "Step forward, knee behind toe."},
            ]
        },
        {
            "name": "Pilates Core",
            "duration": 40,
            "exercises": [
                {"exercise": "Hundred",              "sets": 1, "reps": "100 pumps",    "instructions": "Keep lower back pressed to mat."},
                {"exercise": "Single Leg Stretch",   "sets": 3, "reps": "10 each",      "instructions": "Controlled breathing throughout."},
                {"exercise": "Scissor Kicks",        "sets": 3, "reps": "15 each",      "instructions": "Keep core engaged, lower back flat."},
                {"exercise": "Side-Lying Leg Lifts", "sets": 3, "reps": "15 each side", "instructions": "Slow and controlled movement."},
            ]
        }
    ],
    "moderate-high": [
        {
            "name": "Strength + Cardio Mix",
            "duration": 50,
            "exercises": [
                {"exercise": "Jump Squats",           "sets": 3, "reps": "12",      "instructions": "Land softly, absorb with knees."},
                {"exercise": "Push-Up to T Rotation", "sets": 3, "reps": "8 each",  "instructions": "Control the rotation."},
                {"exercise": "Romanian Deadlift",     "sets": 3, "reps": "12",      "instructions": "Hinge at hips, slight knee bend."},
                {"exercise": "Mountain Climbers",     "sets": 3, "reps": "20 each", "instructions": "Keep hips level, drive knees fast."},
                {"exercise": "Dumbbell Rows",         "sets": 3, "reps": "12 each", "instructions": "Elbow close to body, squeeze back."},
            ]
        }
    ],
    "high": [
        {
            "name": "HIIT Power Session",
            "duration": 45,
            "exercises": [
                {"exercise": "Burpees",          "sets": 4, "reps": "10",                    "instructions": "Full extension at top, chest to floor."},
                {"exercise": "Box Jumps",        "sets": 4, "reps": "8",                     "instructions": "Land with soft knees."},
                {"exercise": "Kettlebell Swings","sets": 4, "reps": "15",                    "instructions": "Hip hinge power, not arms."},
                {"exercise": "Sprint Intervals", "sets": 6, "reps": "30 sec on / 30 sec off","instructions": "Max effort on sprints."},
                {"exercise": "Plank to Push-Up", "sets": 3, "reps": "10",                    "instructions": "Controlled transition each rep."},
            ]
        },
        {
            "name": "Heavy Strength Day",
            "duration": 55,
            "exercises": [
                {"exercise": "Barbell Squats",  "sets": 4, "reps": "8",  "instructions": "Below parallel, back straight."},
                {"exercise": "Bench Press",     "sets": 4, "reps": "8",  "instructions": "Controlled descent, full press."},
                {"exercise": "Deadlifts",       "sets": 4, "reps": "6",  "instructions": "Neutral spine throughout."},
                {"exercise": "Pull-Ups",        "sets": 3, "reps": "6",  "instructions": "Full hang to chin over bar."},
                {"exercise": "Overhead Press",  "sets": 3, "reps": "10", "instructions": "Core tight, no arching back."},
            ]
        }
    ]
}

WEEKLY_STRUCTURE = {
    "fat_loss": {
        "menstrual":  ["low",           "rest", "low",           "rest",     "moderate",      "low",      "rest"],
        "follicular": ["moderate",      "moderate-high", "moderate", "rest", "moderate-high", "moderate", "rest"],
        "ovulatory":  ["high",          "moderate-high", "high",  "moderate", "high",         "moderate", "rest"],
        "luteal":     ["moderate",      "low",  "moderate",      "low",      "moderate",      "low",      "rest"],
    },
    "muscle_gain": {
        "menstrual":  ["low",           "rest", "low",           "rest",     "moderate",      "low",      "rest"],
        "follicular": ["moderate-high", "moderate", "moderate-high", "rest", "moderate-high", "moderate", "rest"],
        "ovulatory":  ["high",          "high", "moderate-high", "rest",     "high",          "moderate", "rest"],
        "luteal":     ["moderate",      "moderate", "low",       "moderate", "moderate",      "low",      "rest"],
    },
    "maintain": {
        "menstrual":  ["low",           "rest", "low",           "low",      "moderate",      "low",      "rest"],
        "follicular": ["moderate",      "moderate", "rest",      "moderate", "moderate",      "low",      "rest"],
        "ovulatory":  ["moderate-high", "moderate", "high",      "rest",     "moderate-high", "moderate", "rest"],
        "luteal":     ["moderate",      "low",  "moderate",      "rest",     "moderate",      "low",      "rest"],
    }
}

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def generate_weekly_plan(user_id: str, goal: str, cycle_phase: str):
    phase = cycle_phase if cycle_phase in WEEKLY_STRUCTURE.get(goal, {}) else "unknown"
    if phase == "unknown":
        intensities = ["moderate", "moderate", "rest", "moderate", "moderate-high", "low", "rest"]
    else:
        intensities = WEEKLY_STRUCTURE[goal][phase]

    weekly_plan = []

    for i, day in enumerate(DAYS):
        intensity = intensities[i]

        if intensity == "rest":
            weekly_plan.append({
                "day":          day,
                "intensity":    "rest",
                "workout_name": "Rest Day 🛌",
                "duration":     0,
                "exercises":    [],
                "note":         "Recovery is part of training. Sleep well and stay hydrated."
            })
        else:
            options = WORKOUT_LIBRARY.get(intensity, WORKOUT_LIBRARY["moderate"])
            chosen  = random.choice(options)
            weekly_plan.append({
                "day":          day,
                "intensity":    intensity,
                "workout_name": chosen["name"],
                "duration":     chosen["duration"],
                "exercises":    chosen["exercises"],
                "note":         ""
            })

    return weekly_plan


def log_workout(user_id: str, workout: str, duration: int,
                intensity: str, feedback: str = "", log_date: str = None):
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    conn.execute("""
        INSERT INTO workout_logs (user_id, date, workout, duration, intensity, feedback)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (user_id, log_date, workout, duration, intensity, feedback))
    conn.commit()
    conn.close()


def get_workout_history(user_id: str, days: int = 7):
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM workout_logs
        WHERE user_id = ?
        AND date >= date('now', ?)
        ORDER BY date DESC
    """, (user_id, f'-{days} days')).fetchall()
    conn.close()
    return [dict(row) for row in rows]