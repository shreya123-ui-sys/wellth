import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
PROGRESS_PATH = BASE_DIR / "data" / "progress_log.csv"


def log_week(user_id, readiness, calorie_goal, feedback):
    row = {
        "user_id": user_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "readiness": readiness,
        "calorie_goal": calorie_goal,
        "feedback": feedback
    }

    if PROGRESS_PATH.exists():
        df = pd.read_csv(PROGRESS_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(PROGRESS_PATH, index=False)


def load_progress(user_id):
    if not PROGRESS_PATH.exists():
        return pd.DataFrame()

    df = pd.read_csv(PROGRESS_PATH)
    return df[df["user_id"] == user_id]
