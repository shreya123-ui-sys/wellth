import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PLAN_PATH = BASE_DIR / "data" / "weekly_plans.csv"

def load_plan_history(user_id):
    if not PLAN_PATH.exists():
        return pd.DataFrame()

    df = pd.read_csv(PLAN_PATH)
    return df[df["user_id"] == user_id]
