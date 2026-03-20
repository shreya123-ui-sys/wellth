import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "data" / "wellth.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     TEXT PRIMARY KEY,
            name        TEXT,
            age         INTEGER,
            weight_kg   REAL,
            height_cm   REAL,
            goal        TEXT,
            diet        TEXT,
            activity    TEXT,
            created_at  TEXT DEFAULT (date('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cycle_logs (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id         TEXT,
            period_start    TEXT,
            cycle_length    INTEGER DEFAULT 28,
            period_length   INTEGER DEFAULT 5,
            logged_at       TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meal_logs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     TEXT,
            date        TEXT,
            meal_type   TEXT,
            food_name   TEXT,
            calories    REAL,
            protein_g   REAL,
            carbs_g     REAL,
            fat_g       REAL,
            logged_at   TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_logs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     TEXT,
            date        TEXT,
            workout     TEXT,
            duration    INTEGER,
            intensity   TEXT,
            feedback    TEXT,
            logged_at   TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weekly_plans (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     TEXT,
            week_start  TEXT,
            day         TEXT,
            workout     TEXT,
            meals       TEXT,
            cycle_phase TEXT,
            logged_at   TEXT DEFAULT (datetime('now'))
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_logs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     TEXT,
            date        TEXT,
            glasses     INTEGER,
            logged_at   TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sleep_logs (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id       TEXT,
            date          TEXT,
            hours         REAL,
            quality       TEXT,
            notes         TEXT,
            logged_at     TEXT DEFAULT (datetime('now'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id          TEXT,
            date             TEXT,
            workout_feedback TEXT,
            meal_feedback    TEXT,
            notes            TEXT,
            logged_at        TEXT DEFAULT (datetime('now'))
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialised!")

if __name__ == "__main__":
    init_db()