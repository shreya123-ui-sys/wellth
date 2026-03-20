
import random

EXERCISES = {
    "lower": [
        {
            "exercise": "Walking Lunges",
            "variant": "Bodyweight",
            "sets": 3,
            "reps": 12,
            "instructions": "Controlled steps.",
            "beginner": "Reverse lunges",
            "no_equipment": "Stationary lunges"
        },
        {
            "exercise": "Squats",
            "variant": "Slow tempo",
            "sets": 3,
            "reps": 10,
            "instructions": "Chest up.",
            "beginner": "Box squats",
            "no_equipment": "Chair squats"
        }
    ],
    "upper": [
        {
            "exercise": "Push-Ups",
            "variant": "Standard",
            "sets": 3,
            "reps": 8,
            "instructions": "Core tight.",
            "beginner": "Incline push-ups",
            "no_equipment": "Knee push-ups"
        }
    ],
    "recovery": [
        {
            "exercise": "Yoga Flow",
            "variant": "Mobility",
            "sets": 1,
            "reps": 10,
            "instructions": "Gentle movement.",
            "beginner": "Seated stretching",
            "no_equipment": "Breathing work"
        }
    ]
}


def normalize_readiness(readiness):
    if isinstance(readiness, dict):
        return readiness.get("energy", 3), readiness.get("recovery", 60)

    if readiness == "build":
        return 4, 70
    if readiness == "recover":
        return 2, 30
    return 3, 60  # maintain


def assemble_workout(readiness, day_index=0):
    energy, recovery = normalize_readiness(readiness)

    if energy <= 2 or recovery < 40:
        pool = EXERCISES["recovery"]
        return random.sample(pool, 1)

    pool = EXERCISES["upper"] if day_index % 2 else EXERCISES["lower"]
    return random.sample(pool, min(2, len(pool)))
