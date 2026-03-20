from database import get_connection
from datetime import date


# ======================================
# WATER TRACKER
# ======================================

DAILY_WATER_GOAL = 8  # glasses


def log_water(user_id: str, glasses: int, log_date: str = None):
    """Log water intake for a day. Adds to existing count."""
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()

    # Check if entry exists for today
    existing = conn.execute("""
        SELECT id, glasses FROM water_logs
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date)).fetchone()

    if existing:
        new_total = existing["glasses"] + glasses
        conn.execute("""
            UPDATE water_logs SET glasses = ?
            WHERE id = ?
        """, (new_total, existing["id"]))
    else:
        conn.execute("""
            INSERT INTO water_logs (user_id, date, glasses)
            VALUES (?, ?, ?)
        """, (user_id, log_date, glasses))

    conn.commit()
    conn.close()


def get_water_today(user_id: str, log_date: str = None):
    """Get total glasses of water logged today."""
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    row = conn.execute("""
        SELECT glasses FROM water_logs
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date)).fetchone()
    conn.close()
    return row["glasses"] if row else 0


def reset_water(user_id: str, log_date: str = None):
    """Reset water count for a day."""
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    conn.execute("""
        UPDATE water_logs SET glasses = 0
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date))
    conn.commit()
    conn.close()


def get_water_history(user_id: str, days: int = 7):
    """Get water intake for the past N days."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT date, glasses FROM water_logs
        WHERE user_id = ?
        AND date >= date('now', ?)
        ORDER BY date DESC
    """, (user_id, f'-{days} days')).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_water_message(glasses: int) -> dict:
    """Return motivational message based on water intake."""
    goal = DAILY_WATER_GOAL
    percentage = (glasses / goal) * 100

    if glasses == 0:
        return {"emoji": "🏜️", "message": "Haven't had any water yet! Start now.", "color": "error"}
    elif glasses < goal * 0.4:
        return {"emoji": "💧", "message": f"{glasses}/{goal} glasses. Keep going!", "color": "warning"}
    elif glasses < goal * 0.7:
        return {"emoji": "💦", "message": f"{glasses}/{goal} glasses. Halfway there!", "color": "warning"}
    elif glasses < goal:
        return {"emoji": "🌊", "message": f"{glasses}/{goal} glasses. Almost there!", "color": "info"}
    else:
        return {"emoji": "✅", "message": f"Goal reached! {glasses} glasses today 🎉", "color": "success"}


# ======================================
# SLEEP TRACKER
# ======================================

SLEEP_GOAL = 8.0  # hours


def log_sleep(user_id: str, hours: float, quality: str, notes: str = "", log_date: str = None):
    """
    Log sleep for a night.
    quality: 'Poor', 'Fair', 'Good', 'Excellent'
    """
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()

    # Replace existing entry for same date
    existing = conn.execute("""
        SELECT id FROM sleep_logs
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date)).fetchone()

    if existing:
        conn.execute("""
            UPDATE sleep_logs SET hours = ?, quality = ?, notes = ?
            WHERE id = ?
        """, (hours, quality, notes, existing["id"]))
    else:
        conn.execute("""
            INSERT INTO sleep_logs (user_id, date, hours, quality, notes)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, log_date, hours, quality, notes))

    conn.commit()
    conn.close()


def get_sleep_today(user_id: str, log_date: str = None):
    """Get sleep log for today."""
    if log_date is None:
        log_date = date.today().isoformat()

    conn = get_connection()
    row = conn.execute("""
        SELECT * FROM sleep_logs
        WHERE user_id = ? AND date = ?
    """, (user_id, log_date)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_sleep_history(user_id: str, days: int = 7):
    """Get sleep logs for the past N days."""
    conn = get_connection()
    rows = conn.execute("""
        SELECT * FROM sleep_logs
        WHERE user_id = ?
        AND date >= date('now', ?)
        ORDER BY date DESC
    """, (user_id, f'-{days} days')).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_sleep_message(hours: float, phase: str) -> dict:
    """Return sleep quality message considering cycle phase."""
    phase_tips = {
        "menstrual":  "Extra sleep helps during your period. Rest is healing! 🌑",
        "follicular": "Good sleep fuels your rising energy this phase. 🌒",
        "ovulatory":  "Your peak phase needs quality sleep to sustain energy. 🌕",
        "luteal":     "Sleep issues are common in luteal phase. Wind down early. 🌘",
        "unknown":    "Consistent sleep is key to overall health. 💤"
    }

    if hours < 5:
        return {
            "emoji": "😴",
            "message": f"Only {hours}h — that's too little. {phase_tips.get(phase, '')}",
            "color": "error"
        }
    elif hours < 6.5:
        return {
            "emoji": "😐",
            "message": f"{hours}h sleep. Try to get closer to 8h. {phase_tips.get(phase, '')}",
            "color": "warning"
        }
    elif hours < 8:
        return {
            "emoji": "😊",
            "message": f"{hours}h — decent sleep! {phase_tips.get(phase, '')}",
            "color": "info"
        }
    else:
        return {
            "emoji": "🌟",
            "message": f"{hours}h — great sleep! {phase_tips.get(phase, '')}",
            "color": "success"
        }


def get_avg_sleep(user_id: str, days: int = 7) -> float:
    """Get average sleep hours over past N days."""
    history = get_sleep_history(user_id, days)
    if not history:
        return 0.0
    return round(sum(h["hours"] for h in history) / len(history), 1)


if __name__ == "__main__":
    # Test
    log_water("shreya", 3)
    log_water("shreya", 2)
    glasses = get_water_today("shreya")
    print(f"Water today: {glasses} glasses")
    print(get_water_message(glasses))

    log_sleep("shreya", 7.5, "Good", "Felt rested")
    sleep = get_sleep_today("shreya")
    print(f"\nSleep: {sleep}")
    print(get_sleep_message(7.5, "follicular"))