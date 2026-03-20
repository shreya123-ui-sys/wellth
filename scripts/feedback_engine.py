import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FEEDBACK_PATH = BASE_DIR / "data" / "feedback.csv"

def save_feedback(user_id, feedback):
    row = {
        "user_id": user_id,
        "feedback": feedback
    }

    if FEEDBACK_PATH.exists():
        df = pd.read_csv(FEEDBACK_PATH)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(FEEDBACK_PATH, index=False)


def get_latest_feedback(user_id):
    if not FEEDBACK_PATH.exists():
        return None

    df = pd.read_csv(FEEDBACK_PATH)
    user_df = df[df["user_id"] == user_id]

    if user_df.empty:
        return None

    return user_df.iloc[-1]["feedback"]
