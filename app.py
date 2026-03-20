import streamlit as st
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

# ======================================
# CUSTOM CSS
# ======================================
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* Global font */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Background */
    .stApp {
        background-color: #f8faf8;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e8f0e8;
    }

    /* Sidebar ALL text — force dark */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] *,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] small,
    [data-testid="stSidebar"] caption {
        color: #1a2e1a !important;
    }

    /* All general text */
    p, span, label, div {
        color: #2d4a2d;
    }

    /* Input text */
    input, textarea, select {
        color: #2d4a2d !important;
        background-color: #ffffff !important;
    }

    /* Selectbox text */
    [data-testid="stSelectbox"] div,
    [data-testid="stSelectbox"] span {
        color: #2d4a2d !important;
    }

    /* Number input */
    [data-testid="stNumberInput"] input {
        color: #2d4a2d !important;
    }

    /* Text input */
    [data-testid="stTextInput"] input {
        color: #2d4a2d !important;
    }

    /* Dropdown options */
    [data-baseweb="select"] * {
        color: #2d4a2d !important;
    }

    /* Slider */
    [data-testid="stSlider"] label,
    [data-testid="stSlider"] div {
        color: #2d4a2d !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e0ece0;
        border-radius: 12px;
        padding: 16px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.75rem !important;
        color: #6b7c6b !important;
        font-weight: 500 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #2d4a2d !important;
    }

    [data-testid="stMetricDelta"] {
        font-size: 0.8rem !important;
        color: #5a8a5a !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #5a8a5a;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #4a7a4a;
        box-shadow: 0 4px 12px rgba(90,138,90,0.3);
        transform: translateY(-1px);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 4px;
        border: 1px solid #e0ece0;
        gap: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: #6b7c6b;
        font-weight: 500;
        font-size: 0.85rem;
        padding: 8px 16px;
    }

    .stTabs [aria-selected="true"] {
        background-color: #5a8a5a !important;
        color: white !important;
    }

    /* Expanders */
    [data-testid="stExpander"] {
        background-color: #ffffff;
        border: 1px solid #e0ece0;
        border-radius: 12px;
        margin-bottom: 8px;
    }

    /* Info / Success / Warning boxes */
    [data-testid="stAlert"] {
        border-radius: 12px;
        border: none;
    }

    /* Text inputs */
    [data-testid="stTextInput"] input {
        border-radius: 8px;
        border: 1px solid #d0e4d0;
        background-color: #ffffff;
    }

    /* Select boxes */
    [data-testid="stSelectbox"] > div {
        border-radius: 8px;
    }

    /* Progress bar */
    [data-testid="stProgressBar"] > div {
        background-color: #5a8a5a !important;
        border-radius: 8px;
    }

    /* Divider */
    hr {
        border-color: #e0ece0;
        margin: 1.5rem 0;
    }

    /* Headers */
    h1 {
        color: #2d4a2d !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
    }

    h2 {
        color: #3a5a3a !important;
        font-weight: 600 !important;
    }

    h3 {
        color: #4a6a4a !important;
        font-weight: 600 !important;
    }

    /* Dataframe */
    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e0ece0;
    }

    /* Forms */
    [data-testid="stForm"] {
        background-color: #ffffff;
        border: 1px solid #e0ece0;
        border-radius: 12px;
        padding: 20px;
    }

    /* Sidebar text */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #2d4a2d !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

from database import init_db
from user_engine import create_user, get_user, user_exists, calculate_bmi, calculate_tdee
from cycle_engine import log_period, get_cycle_phase, get_phase_recommendations
from meal_engine import log_meal, get_meals_by_date, get_daily_totals, get_meal_history, FOOD_DATABASE
from workout_engine import generate_weekly_plan, log_workout, get_workout_history
from recipe_engine import get_daily_meal_suggestions, get_all_recipes_for_type
from ai_engine import generate_recipe, generate_workout_tip, explain_cycle_phase, generate_weekly_nutrition_insight

init_db()

# ======================================
# PAGE CONFIG
# ======================================
st.set_page_config(
    page_title="Wellth",
    page_icon="🧠",
    layout="wide"
)

# ======================================
# SESSION STATE
# ======================================
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user" not in st.session_state:
    st.session_state.user = None

# ======================================
# ONBOARDING
# ======================================
if st.session_state.user_id is None:
    st.title("🧠 Welcome to Wellth")
    st.subheader("Your personalised fitness & nutrition companion")
    st.markdown("---")

    tab_login, tab_signup = st.tabs(["Login", "Sign Up"])

    with tab_login:
        st.subheader("Login")
        login_id = st.text_input("Enter your User ID", key="login_id")
        if st.button("Login", key="login_btn"):
            if user_exists(login_id):
                st.session_state.user_id = login_id
                st.session_state.user = get_user(login_id)
                st.rerun()
            else:
                st.error("User not found. Please sign up first.")

    with tab_signup:
        st.subheader("Create your profile")
        col1, col2 = st.columns(2)

        with col1:
            new_id   = st.text_input("Choose a User ID (no spaces)", key="new_id")
            name     = st.text_input("Your name")
            age      = st.number_input("Age", 10, 80, 20)
            weight   = st.number_input("Weight (kg)", 30.0, 200.0, 55.0, step=0.5)

        with col2:
            height   = st.number_input("Height (cm)", 100.0, 220.0, 162.0, step=0.5)
            goal     = st.selectbox("Goal", ["fat_loss", "maintain", "muscle_gain"],
                                    format_func=lambda x: x.replace("_", " ").title())
            diet     = st.selectbox("Diet", ["Vegetarian", "Non-Vegetarian", "Vegan"])
            activity = st.selectbox("Activity Level",
                                    ["sedentary", "light", "moderate", "active", "very_active"],
                                    index=2,
                                    format_func=lambda x: x.replace("_", " ").title())

        if st.button("Create Profile ✅"):
            if not new_id or not name:
                st.error("Please fill in all fields.")
            elif user_exists(new_id):
                st.error("User ID already taken. Try another.")
            else:
                create_user(new_id, name, age, weight, height, goal, diet, activity)
                st.session_state.user_id = new_id
                st.session_state.user = get_user(new_id)
                st.success(f"Welcome, {name}! 🎉")
                st.rerun()

# ======================================
# MAIN APP
# ======================================
else:
    user    = st.session_state.user
    user_id = st.session_state.user_id

    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/heart-with-pulse.png", width=60)
        st.markdown(f"### Hi, {user['name']} 👋")
        st.caption(f"Goal: {user['goal'].replace('_', ' ').title()}")
        st.caption(f"Diet: {user['diet']}")
        st.markdown("---")

        cycle_info = get_cycle_phase(user_id)
        phase      = cycle_info["phase"]
        st.markdown(f"**Cycle Phase:** {cycle_info['emoji']} {phase.title()}")
        if cycle_info["day"]:
            st.caption(f"Day {cycle_info['day']} of {cycle_info.get('cycle_length', 28)}")
        st.markdown("---")

        if st.button("Logout"):
            st.session_state.user_id = None
            st.session_state.user    = None
            st.rerun()

    tdee = calculate_tdee(user)

    tab_home, tab_cycle, tab_workout, tab_meals, tab_recipes, tab_progress, tab_health = st.tabs([
        "🏠 Home", "🌙 Cycle", "🏋️ Workout", "🍽️ Meals", "📖 Recipes", "📈 Progress", "💧 Health"
    ])

    # --------------------------------------------------
    # TAB 1 — HOME
    # --------------------------------------------------
    with tab_home:
        # Hero section
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #e8f5e8 0%, #f0f7f0 50%, #e0efe0 100%);
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 24px;
            border: 1px solid #d0e8d0;
        ">
            <h1 style="margin:0; font-size:2rem; color:#2d4a2d;">
                Good {
                    'morning 🌅' if date.today().weekday() < 5 else 'weekend 🌿'
                }, {user['name']}!
            </h1>
            <p style="margin:8px 0 0 0; color:#5a7a5a; font-size:1rem;">
                {date.today().strftime('%A, %d %B %Y')} &nbsp;·&nbsp;
                {cycle_info['emoji']} {phase.title()} Phase
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Metrics row
        col1, col2, col3, col4 = st.columns(4)
        bmi_data = calculate_bmi(user["weight_kg"], user["height_cm"])
        totals   = get_daily_totals(user_id)

        from health_engine import get_water_today, get_sleep_today
        glasses_today = get_water_today(user_id)
        sleep_today   = get_sleep_today(user_id)

        col1.metric("🔥 Calories Today",    f"{totals.get('total_calories', 0)} kcal",
                    f"Target: {tdee} kcal")
        col2.metric("💧 Water",             f"{glasses_today} / 8 glasses")
        col3.metric("😴 Sleep",             f"{sleep_today['hours']}h" if sleep_today else "Not logged")
        col4.metric("⚖️ BMI",               bmi_data["bmi"], bmi_data["category"])

        st.markdown("---")

        # Phase insight card
        recs = get_phase_recommendations(phase)
        col_a, col_b = st.columns([1.2, 1])

        with col_a:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                border-radius: 16px;
                padding: 24px;
                border: 1px solid #e0ece0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
                height: 100%;
            ">
                <div style="font-size: 2rem; margin-bottom: 8px;">{cycle_info['emoji']}</div>
                <h3 style="margin: 0 0 8px 0; color: #2d4a2d;">
                    {phase.title()} Phase — Day {cycle_info['day'] or '?'}
                </h3>
                <p style="color: #5a7a5a; font-size: 0.9rem; line-height: 1.6; margin: 0;">
                    {cycle_info['description']}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col_b:
            st.markdown(f"""
            <div style="
                background: #ffffff;
                border-radius: 16px;
                padding: 24px;
                border: 1px solid #e0ece0;
                box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            ">
                <h3 style="margin: 0 0 16px 0; color: #2d4a2d;">Today's Focus</h3>
                <p style="margin: 0 0 8px 0; color: #4a6a4a;">
                    <strong>💪 Workout:</strong> {recs['workout_type']}
                </p>
                <p style="margin: 0 0 16px 0; color: #4a6a4a;">
                    <strong>🥗 Nutrition:</strong> {recs['nutrition_focus']}
                </p>
                <p style="margin: 0; color: #5a7a5a; font-size: 0.85rem;">
                    <strong>✅ Eat:</strong> {', '.join(recs['foods_to_eat'][:3])}
                </p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # AI explanation button
        st.subheader("🤖 AI Phase Explanation")
        if st.button("✨ Explain my current phase"):
            with st.spinner("Asking AI..."):
                explanation = explain_cycle_phase(phase)
            st.success(explanation)

    # --------------------------------------------------
    # TAB 2 — CYCLE
    # --------------------------------------------------
    with tab_cycle:
        st.title("🌙 Cycle Tracker")
        st.markdown("---")

        st.subheader("Log your period")
        col1, col2, col3 = st.columns(3)
        with col1:
            period_start  = st.date_input("Period start date", value=date.today())
        with col2:
            cycle_length  = st.number_input("Cycle length (days)", 21, 35, 28)
        with col3:
            period_length = st.number_input("Period length (days)", 2, 10, 5)

        if st.button("Log Period ✅"):
            log_period(user_id, period_start.isoformat(), cycle_length, period_length)
            st.success("Period logged!")
            st.rerun()

        st.markdown("---")
        st.subheader("Current Phase")
        cycle_info = get_cycle_phase(user_id)
        phase      = cycle_info["phase"]

        if phase == "unknown":
            st.warning("No cycle data yet. Log your period above to get phase-aware recommendations.")
        else:
            st.markdown(f"## {cycle_info['emoji']} {phase.title()} Phase — Day {cycle_info['day']}")
            st.write(cycle_info["description"])
            st.markdown("---")

            recs = get_phase_recommendations(phase)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 💪 Workout")
                st.write(f"**Type:** {recs['workout_type']}")
                st.write(f"**Intensity:** {recs['intensity'].title()}")
            with col2:
                st.markdown("### 🥗 Nutrition")
                st.write(f"**Focus:** {recs['nutrition_focus']}")
                st.write(f"**Calorie adjustment:** {recs['calorie_adjustment']:+d} kcal")

            col3, col4 = st.columns(2)
            with col3:
                st.markdown("**✅ Eat more of:**")
                for f in recs["foods_to_eat"]:
                    st.write(f"• {f}")
            with col4:
                if recs["foods_to_avoid"]:
                    st.markdown("**❌ Limit these:**")
                    for f in recs["foods_to_avoid"]:
                        st.write(f"• {f}")

    # --------------------------------------------------
    # TAB 3 — WORKOUT
    # --------------------------------------------------
    with tab_workout:
        st.title("🏋️ Weekly Workout Plan")
        st.markdown("---")

        cycle_info = get_cycle_phase(user_id)
        phase      = cycle_info["phase"] if cycle_info["phase"] != "unknown" else "follicular"

        if st.button("🔄 Generate This Week's Plan"):
            st.session_state["weekly_plan"] = generate_weekly_plan(user_id, user["goal"], phase)

        if "weekly_plan" in st.session_state:
            plan = st.session_state["weekly_plan"]
            for day_plan in plan:
                with st.expander(f"**{day_plan['day']}** — {day_plan['workout_name']} ({day_plan['duration']} min)"):
                    if day_plan["intensity"] == "rest":
                        st.info(day_plan["note"])
                    else:
                        st.caption(f"Intensity: {day_plan['intensity'].title()}")
                        for ex in day_plan["exercises"]:
                            st.markdown(f"**{ex['exercise']}** — {ex['sets']} sets × {ex['reps']}")
                            st.caption(f"💡 {ex['instructions']}")

                        if st.button(f"🤖 Get AI tip for {day_plan['day']}", key=f"tip_{day_plan['day']}"):
                            with st.spinner("Getting AI tip..."):
                                tip = generate_workout_tip(phase, day_plan["workout_name"], day_plan["intensity"])
                            st.success(tip)
        else:
            st.info("Click the button above to generate your personalised weekly plan.")

        st.markdown("---")
        st.subheader("✅ Log a Completed Workout")

        with st.form("workout_log_form"):
            workout_name = st.text_input("Workout name")
            col1, col2   = st.columns(2)
            with col1:
                duration  = st.number_input("Duration (minutes)", 5, 180, 30)
            with col2:
                intensity = st.selectbox("Intensity", ["low", "moderate", "moderate-high", "high"])
            feedback  = st.text_area("How did it feel? (optional)")
            submitted = st.form_submit_button("Log Workout ✅")

        if submitted and workout_name:
            log_workout(user_id, workout_name, duration, intensity, feedback)
            st.success("Workout logged!")

    # --------------------------------------------------
    # TAB 4 — MEALS
    # --------------------------------------------------
    with tab_meals:
        st.title("🍽️ Meal Logger")
        st.markdown("---")

        totals = get_daily_totals(user_id)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Calories",  f"{totals.get('total_calories', 0)} / {tdee} kcal")
        col2.metric("Protein",   f"{totals.get('total_protein', 0)}g")
        col3.metric("Carbs",     f"{totals.get('total_carbs', 0)}g")
        col4.metric("Fat",       f"{totals.get('total_fat', 0)}g")

        st.markdown("---")
        st.subheader("Log a meal")

        with st.form("meal_form"):
            col1, col2  = st.columns(2)
            with col1:
                meal_type   = st.selectbox("Meal type", ["breakfast", "lunch", "dinner", "snack"])
                food_choice = st.selectbox("Pick a food", ["Custom"] + list(FOOD_DATABASE.keys()))
            with col2:
                if food_choice != "Custom":
                    food_data = FOOD_DATABASE[food_choice]
                    st.info(f"Per serving: {food_data['calories']} kcal | P: {food_data['protein_g']}g | C: {food_data['carbs_g']}g | F: {food_data['fat_g']}g")

            if food_choice == "Custom":
                food_name = st.text_input("Food name")
                c1, c2, c3, c4 = st.columns(4)
                calories  = c1.number_input("Calories",   0.0, 2000.0, 0.0)
                protein   = c2.number_input("Protein (g)", 0.0, 200.0, 0.0)
                carbs     = c3.number_input("Carbs (g)",   0.0, 500.0, 0.0)
                fat       = c4.number_input("Fat (g)",     0.0, 200.0, 0.0)
            else:
                food_name = food_choice
                food_data = FOOD_DATABASE[food_choice]
                calories  = food_data["calories"]
                protein   = food_data["protein_g"]
                carbs     = food_data["carbs_g"]
                fat       = food_data["fat_g"]

            log_submitted = st.form_submit_button("Log Meal ✅")

        if log_submitted and food_name:
            log_meal(user_id, meal_type, food_name, calories, protein, carbs, fat)
            st.success(f"Logged {food_name}!")
            st.rerun()

        st.markdown("---")
        st.subheader("Today's meals")
        meals = get_meals_by_date(user_id)
        if meals:
            for m in meals:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"**{m['meal_type'].title()}** — {m['food_name']} | {m['calories']} kcal | P: {m['protein_g']}g | C: {m['carbs_g']}g | F: {m['fat_g']}g")
                with col2:
                    if st.button("🗑️ Delete", key=f"del_{m['id']}"):
                        from meal_engine import delete_meal
                        delete_meal(m["id"])
                        st.rerun()
        else:
            st.info("No meals logged today yet.")

    # --------------------------------------------------
    # TAB 5 — RECIPES
    # --------------------------------------------------
    with tab_recipes:
        st.title("📖 Recipe Suggestions")
        st.markdown("---")

        cycle_info = get_cycle_phase(user_id)
        phase      = cycle_info["phase"] if cycle_info["phase"] != "unknown" else "follicular"

        st.info(f"Showing recipes for your **{phase.title()} phase** · **{user['diet']}** · **{user['goal'].replace('_', ' ').title()}** goal")

        recipe_tab1, recipe_tab2 = st.tabs(["📋 Suggested Meals", "🤖 AI Generate Recipe"])

        with recipe_tab1:
            suggestions = get_daily_meal_suggestions(user["diet"], user["goal"], phase)
            for meal_type, recipe in suggestions.items():
                if recipe:
                    with st.expander(f"**{meal_type.upper()}** — {recipe['name']} ({recipe['calories']} kcal)"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("**🥗 Ingredients**")
                            for ing in recipe["ingredients"]:
                                st.write(f"• {ing}")
                        with col2:
                            st.markdown("**👩‍🍳 Steps**")
                            for i, step in enumerate(recipe["steps"], 1):
                                st.write(f"{i}. {step}")

                        st.markdown("---")
                        col3, col4, col5 = st.columns(3)
                        col3.metric("Protein", f"{recipe['protein_g']}g")
                        col4.metric("Carbs",   f"{recipe['carbs_g']}g")
                        col5.metric("Fat",     f"{recipe['fat_g']}g")

                        if recipe.get("nutrition_note"):
                            st.success(f"💡 {recipe['nutrition_note']}")

        with recipe_tab2:
            st.subheader("🤖 Generate a new recipe with AI")
            col1, col2 = st.columns(2)
            with col1:
                ai_meal_type = st.selectbox("Meal type", ["breakfast", "lunch", "dinner", "snack"], key="ai_meal_type")
            with col2:
                st.info(f"Will generate for: {user['diet']} · {phase.title()} phase · {user['goal'].replace('_',' ').title()}")

            if st.button("✨ Generate AI Recipe"):
                with st.spinner("AI is cooking up something special..."):
                    ai_recipe = generate_recipe(user["diet"], user["goal"], phase, ai_meal_type)
                st.markdown("### 🍽️ Your AI Recipe")
                st.markdown(ai_recipe)

    # --------------------------------------------------
    # TAB 6 — PROGRESS
    # --------------------------------------------------
    with tab_progress:
        st.title("📈 Progress")
        st.markdown("---")

        st.subheader("Calorie intake — last 7 days")
        history = get_meal_history(user_id, days=7)

        if history:
            import pandas as pd
            df = pd.DataFrame(history)
            df = df.set_index("date")
            st.bar_chart(df["total_calories"])

            st.markdown("---")
            st.subheader("Macro breakdown")
            st.dataframe(df[["total_protein", "total_carbs", "total_fat"]], use_container_width=True)

            st.markdown("---")
            st.subheader("🤖 AI Weekly Insight")
            if st.button("Get AI nutrition insight"):
                avg_calories = df["total_calories"].mean()
                avg_protein  = df["total_protein"].mean()
                with st.spinner("Analysing your week..."):
                    insight = generate_weekly_nutrition_insight(
                        user["diet"], user["goal"], phase,
                        round(avg_calories, 1), round(avg_protein, 1)
                    )
                st.success(insight)
        else:
            st.info("No meal history yet. Start logging meals to see your progress!")

        st.markdown("---")
        st.subheader("Workout history — last 7 days")
        workout_history = get_workout_history(user_id, days=7)

        if workout_history:
            for w in workout_history:
                st.markdown(f"**{w['date']}** — {w['workout']} | {w['duration']} min | {w['intensity'].title()} | {w['feedback'] or 'No feedback'}")
        else:
            st.info("No workouts logged yet. Complete a workout and log it!")

    # --------------------------------------------------
    # TAB 7 — HEALTH (Water & Sleep)
    # --------------------------------------------------
    with tab_health:
        st.title("💧 Water & Sleep Tracker")
        st.markdown("---")

        from health_engine import (
            log_water, get_water_today, get_water_history,
            get_water_message, reset_water, DAILY_WATER_GOAL,
            log_sleep, get_sleep_today, get_sleep_history,
            get_sleep_message, get_avg_sleep, SLEEP_GOAL
        )

        water_tab, sleep_tab = st.tabs(["💧 Water", "😴 Sleep"])

        # --------------------------------------------------
        # WATER TAB
        # --------------------------------------------------
        with water_tab:
            st.subheader("💧 Daily Water Intake")

            glasses_today = get_water_today(user_id)
            water_msg     = get_water_message(glasses_today)

            # Progress bar
            progress = min(glasses_today / DAILY_WATER_GOAL, 1.0)
            st.progress(progress)

            col1, col2, col3 = st.columns(3)
            col1.metric("Glasses Today",  f"{glasses_today} / {DAILY_WATER_GOAL}")
            col2.metric("Remaining",      f"{max(DAILY_WATER_GOAL - glasses_today, 0)} glasses")
            col3.metric("Goal",           f"{DAILY_WATER_GOAL} glasses")

            # Message
            if water_msg["color"] == "success":
                st.success(f"{water_msg['emoji']} {water_msg['message']}")
            elif water_msg["color"] == "warning":
                st.warning(f"{water_msg['emoji']} {water_msg['message']}")
            elif water_msg["color"] == "error":
                st.error(f"{water_msg['emoji']} {water_msg['message']}")
            else:
                st.info(f"{water_msg['emoji']} {water_msg['message']}")

            st.markdown("---")

            # Quick add buttons
            st.subheader("Quick Add")
            col1, col2, col3, col4 = st.columns(4)

            if col1.button("+ 1 glass 💧"):
                log_water(user_id, 1)
                st.rerun()
            if col2.button("+ 2 glasses 💧💧"):
                log_water(user_id, 2)
                st.rerun()
            if col3.button("+ 3 glasses 💧💧💧"):
                log_water(user_id, 3)
                st.rerun()
            if col4.button("Reset 🔄"):
                reset_water(user_id)
                st.rerun()

            st.markdown("---")

            # History
            st.subheader("Last 7 days")
            water_history = get_water_history(user_id, days=7)

            if water_history:
                import pandas as pd
                df_water = pd.DataFrame(water_history).set_index("date")
                st.bar_chart(df_water["glasses"])
            else:
                st.info("No water history yet. Start logging!")

            # Cycle-aware tip
            st.markdown("---")
            phase_water_tips = {
                "menstrual":  "🌑 Drink warm water with lemon during your period — it helps with cramps.",
                "follicular": "🌒 Stay hydrated to support rising energy levels this phase.",
                "ovulatory":  "🌕 Peak phase means peak sweat — drink more if you're training hard!",
                "luteal":     "🌘 Bloating is common in luteal phase. Consistent water helps reduce it.",
                "unknown":    "💧 Aim for 8 glasses a day for optimal health."
            }
            st.info(phase_water_tips.get(phase, phase_water_tips["unknown"]))

        # --------------------------------------------------
        # SLEEP TAB
        # --------------------------------------------------
        with sleep_tab:
            st.subheader("😴 Sleep Tracker")

            sleep_today = get_sleep_today(user_id)
            avg_sleep   = get_avg_sleep(user_id, days=7)

            col1, col2, col3 = st.columns(3)
            col1.metric("Last Night",    f"{sleep_today['hours']}h" if sleep_today else "Not logged")
            col2.metric("7-Day Average", f"{avg_sleep}h")
            col3.metric("Sleep Goal",    f"{SLEEP_GOAL}h")

            if sleep_today:
                sleep_msg = get_sleep_message(sleep_today["hours"], phase)
                if sleep_msg["color"] == "success":
                    st.success(f"{sleep_msg['emoji']} {sleep_msg['message']}")
                elif sleep_msg["color"] == "warning":
                    st.warning(f"{sleep_msg['emoji']} {sleep_msg['message']}")
                elif sleep_msg["color"] == "error":
                    st.error(f"{sleep_msg['emoji']} {sleep_msg['message']}")
                else:
                    st.info(f"{sleep_msg['emoji']} {sleep_msg['message']}")

            st.markdown("---")
            st.subheader("Log Last Night's Sleep")

            with st.form("sleep_form"):
                col1, col2 = st.columns(2)
                with col1:
                    sleep_hours   = st.slider("Hours slept", 0.0, 12.0, 7.0, step=0.5)
                with col2:
                    sleep_quality = st.selectbox("Sleep quality", ["Poor", "Fair", "Good", "Excellent"])
                sleep_notes   = st.text_input("Any notes? (optional)")
                sleep_submit  = st.form_submit_button("Log Sleep 😴")

            if sleep_submit:
                log_sleep(user_id, sleep_hours, sleep_quality, sleep_notes)
                st.success(f"Logged {sleep_hours}h of {sleep_quality} sleep!")
                st.rerun()

            st.markdown("---")
            st.subheader("Sleep history — last 7 days")
            sleep_history = get_sleep_history(user_id, days=7)

            if sleep_history:
                import pandas as pd
                df_sleep = pd.DataFrame(sleep_history).set_index("date")
                st.line_chart(df_sleep["hours"])

                st.markdown("**Detailed log:**")
                for s in sleep_history:
                    st.markdown(f"**{s['date']}** — {s['hours']}h | {s['quality']} | {s['notes'] or 'No notes'}")
            else:
                st.info("No sleep history yet. Log your sleep above!")

            # Cycle-aware tip
            st.markdown("---")
            phase_sleep_tips = {
                "menstrual":  "🌑 Your body needs more rest during menstruation. Don't fight the tiredness.",
                "follicular": "🌒 Sleep helps consolidate the energy gains of follicular phase.",
                "ovulatory":  "🌕 You may need less sleep now — but don't skip it!",
                "luteal":     "🌘 Progesterone rises in luteal phase — you may feel sleepier. Listen to your body.",
                "unknown":    "💤 Consistent sleep timing improves sleep quality over time."
            }
            st.info(phase_sleep_tips.get(phase, phase_sleep_tips["unknown"]))