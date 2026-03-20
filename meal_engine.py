from database import get_connection
from datetime import date


def log_meal(user_id: str, meal_type: str, food_name: str,
             calories: float, protein_g: float, carbs_g: float, fat_g: float,
             log_date: str = None):
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    conn.execute("""
        INSERT INTO meal_logs (user_id, date, meal_type, food_name, calories, protein_g, carbs_g, fat_g)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, log_date, meal_type, food_name, calories, protein_g, carbs_g, fat_g))
    conn.commit()
    conn.close()


def get_meals_by_date(user_id: str, log_date: str = None):
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM meal_logs
        WHERE user_id = ? AND date = ?
        ORDER BY meal_type
    """, (user_id, log_date)).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_daily_totals(user_id: str, log_date: str = None):
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    row = conn.execute("""
        SELECT
            ROUND(SUM(calories), 1)  AS total_calories,
            ROUND(SUM(protein_g), 1) AS total_protein,
            ROUND(SUM(carbs_g), 1)   AS total_carbs,
            ROUND(SUM(fat_g), 1)     AS total_fat,
            COUNT(*)                 AS total_entries
        FROM meal_logs
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date)).fetchone()
    conn.close()
    return dict(row) if row else {}


def get_meal_history(user_id: str, days: int = 7):
    conn = get_connection()
    rows = conn.execute("""
        SELECT date,
               ROUND(SUM(calories), 1)  AS total_calories,
               ROUND(SUM(protein_g), 1) AS total_protein,
               ROUND(SUM(carbs_g), 1)   AS total_carbs,
               ROUND(SUM(fat_g), 1)     AS total_fat
        FROM meal_logs
        WHERE user_id = ?
        AND date >= date('now', ?)
        GROUP BY date
        ORDER BY date DESC
    """, (user_id, f'-{days} days')).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def delete_meal(meal_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM meal_logs WHERE id = ?", (meal_id,))
    conn.commit()
    conn.close()


FOOD_DATABASE = {
    "Rice (cooked)":         {"calories": 130, "protein_g": 2.7,  "carbs_g": 28.0, "fat_g": 0.3},
    "Roti (1 piece)":        {"calories": 100, "protein_g": 3.0,  "carbs_g": 18.0, "fat_g": 2.5},
    "Dal (cooked)":          {"calories": 116, "protein_g": 9.0,  "carbs_g": 20.0, "fat_g": 0.4},
    "Paneer (100g)":         {"calories": 265, "protein_g": 18.0, "carbs_g": 1.2,  "fat_g": 20.0},
    "Chicken breast (100g)": {"calories": 165, "protein_g": 31.0, "carbs_g": 0.0,  "fat_g": 3.6},
    "Egg (1 whole)":         {"calories": 70,  "protein_g": 6.0,  "carbs_g": 0.6,  "fat_g": 5.0},
    "Oats (100g)":           {"calories": 389, "protein_g": 17.0, "carbs_g": 66.0, "fat_g": 7.0},
    "Banana (1 medium)":     {"calories": 89,  "protein_g": 1.1,  "carbs_g": 23.0, "fat_g": 0.3},
    "Curd (100g)":           {"calories": 61,  "protein_g": 3.5,  "carbs_g": 4.7,  "fat_g": 3.3},
    "Chapati (1 piece)":     {"calories": 104, "protein_g": 3.1,  "carbs_g": 18.0, "fat_g": 2.8},
    "Sambar (100ml)":        {"calories": 50,  "protein_g": 2.5,  "carbs_g": 8.0,  "fat_g": 1.0},
    "Idli (1 piece)":        {"calories": 39,  "protein_g": 2.0,  "carbs_g": 8.0,  "fat_g": 0.2},
    "Dosa (1 piece)":        {"calories": 133, "protein_g": 3.5,  "carbs_g": 22.0, "fat_g": 3.7},
    "Upma (100g)":           {"calories": 145, "protein_g": 3.0,  "carbs_g": 22.0, "fat_g": 5.0},
    "Poha (100g)":           {"calories": 130, "protein_g": 2.5,  "carbs_g": 28.0, "fat_g": 1.0},
    "Rajma (cooked 100g)":   {"calories": 127, "protein_g": 8.7,  "carbs_g": 22.0, "fat_g": 0.5},
    "Chole (cooked 100g)":   {"calories": 164, "protein_g": 8.9,  "carbs_g": 27.0, "fat_g": 2.6},
    "Milk (200ml)":          {"calories": 122, "protein_g": 6.4,  "carbs_g": 9.6,  "fat_g": 6.6},
    "Apple (1 medium)":      {"calories": 95,  "protein_g": 0.5,  "carbs_g": 25.0, "fat_g": 0.3},
    "Almonds (10 pieces)":   {"calories": 70,  "protein_g": 2.5,  "carbs_g": 2.5,  "fat_g": 6.0},
}