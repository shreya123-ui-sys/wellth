import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
PLAN_PATH = BASE_DIR / "data" / "weekly_plans.csv"

def save_weekly_plan(user_id, readiness, workouts, meals):
    rows = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    for day in workouts:
        rows.append({
            "timestamp": timestamp,
            "user_id": user_id,
            "day": day,
            "readiness": readiness,
            "workout": workouts.get(day, "rest"),
            "meal": meals[day]["name"]
        })

    df_new = pd.DataFrame(rows)

    if PLAN_PATH.exists():
        df_old = pd.read_csv(PLAN_PATH)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_csv(PLAN_PATH, index=False)
