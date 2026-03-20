from database import get_connection


def create_user(user_id: str, name: str, age: int, weight_kg: float,
                height_cm: float, goal: str, diet: str, activity: str):
    conn = get_connection()
    try:
        conn.execute("""
            INSERT INTO users (user_id, name, age, weight_kg, height_cm, goal, diet, activity)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (user_id, name, age, weight_kg, height_cm, goal, diet, activity))
        conn.commit()
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        conn.close()


def get_user(user_id: str):
    conn = get_connection()
    row = conn.execute("""
        SELECT * FROM users WHERE user_id = ?
    """, (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def update_user(user_id: str, **kwargs):
    if not kwargs:
        return
    fields = ", ".join(f"{k} = ?" for k in kwargs)
    values = list(kwargs.values()) + [user_id]
    conn = get_connection()
    conn.execute(f"UPDATE users SET {fields} WHERE user_id = ?", values)
    conn.commit()
    conn.close()


def user_exists(user_id: str) -> bool:
    return get_user(user_id) is not None


def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 1)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return {"bmi": bmi, "category": category}


def calculate_tdee(user: dict) -> int:
    weight   = user["weight_kg"]
    height   = user["height_cm"]
    age      = user["age"]
    activity = user["activity"]

    # Mifflin-St Jeor for women
    bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_multipliers = {
        "sedentary":   1.2,
        "light":       1.375,
        "moderate":    1.55,
        "active":      1.725,
        "very_active": 1.9
    }

    multiplier = activity_multipliers.get(activity, 1.55)
    tdee = int(bmr * multiplier)

    if user["goal"] == "fat_loss":
        tdee -= 300
    elif user["goal"] == "muscle_gain":
        tdee += 300

    return tdee