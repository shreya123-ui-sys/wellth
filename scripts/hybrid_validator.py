# scripts/hybrid_validator.py

def validate_and_merge_plan(
    context: dict,
    base_plan: dict,
    ai_draft: dict
) -> dict:
    """
    Hybrid validator:
    - base_plan = deterministic (safe)
    - ai_draft = AI-generated suggestions
    - output = validated final plan
    """

    final_plan = {
        "workout": [],
        "meal": {},
        "notes": []
    }

    energy = context.get("energy", 3)
    recovery = context.get("recovery", 50)
    equipment = context.get("equipment", [])
    diet = context.get("diet")

    # -------------------------
    # WORKOUT VALIDATION
    # -------------------------
    base_workout = base_plan["workout"]["exercises"]
    ai_workout = ai_draft.get("workout", [])

    # Rule: low energy or recovery → limit volume
    max_exercises = 1 if energy <= 2 or recovery < 40 else len(base_workout)

    approved_workout = []

    for ex in ai_workout:
        if len(approved_workout) >= max_exercises:
            break

        # Rule: equipment check
        if ex.get("equipment", "none") != "none" and ex.get("equipment") not in equipment:
            final_plan["notes"].append(
                f"Skipped {ex['name']} (equipment unavailable)"
            )
            continue

        approved_workout.append(ex["name"])

    # Fallback to base plan if AI unsuitable
    if not approved_workout:
        approved_workout = base_workout[:max_exercises]
        final_plan["notes"].append("Used safe fallback workout")

    final_plan["workout"] = approved_workout

    # -------------------------
    # MEAL VALIDATION
    # -------------------------
    base_meal = base_plan["meal"]
    ai_meal = ai_draft.get("meal", {})

    # Rule: diet compliance
    if ai_meal and ai_meal.get("diet") == diet:
        final_plan["meal"] = ai_meal
    else:
        final_plan["meal"] = base_meal
        final_plan["notes"].append("Used safe fallback meal")

    return final_plan
