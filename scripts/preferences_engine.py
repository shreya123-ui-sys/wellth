import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PREF_PATH = BASE_DIR / "data" / "user_preferences.csv"

def load_preferences(user_id):
    if not PREF_PATH.exists():
        return None

    df = pd.read_csv(PREF_PATH)
    user_pref = df[df["user_id"] == user_id]

    if user_pref.empty:
        return None

    return user_pref.iloc[0].to_dict()


def save_preferences(user_id, diet, cuisines, calorie_goal):
    new_row = {
        "user_id": user_id,
        "diet": diet,
        "cuisines": "|".join(cuisines),
        "calorie_goal": calorie_goal
    }

    if PREF_PATH.exists():
        df = pd.read_csv(PREF_PATH)
        df = df[df["user_id"] != user_id]
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    else:
        df = pd.DataFrame([new_row])

    df.to_csv(PREF_PATH, index=False)
