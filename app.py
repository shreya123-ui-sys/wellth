import streamlit as st
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

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

    tab_home, tab_cycle, tab_workout, tab_meals, tab_recipes, tab_progress = st.tabs([
        "🏠 Home", "🌙 Cycle", "🏋️ Workout", "🍽️ Meals", "📖 Recipes", "📈 Progress"
    ])

    # --------------------------------------------------
    # TAB 1 — HOME
    # --------------------------------------------------
    with tab_home:
        st.title(f"🧠 Wellth — {date.today().strftime('%A, %d %B %Y')}")
        st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)
        bmi_data = calculate_bmi(user["weight_kg"], user["height_cm"])
        totals   = get_daily_totals(user_id)

        col1.metric("BMI",                bmi_data["bmi"], bmi_data["category"])
        col2.metric("Daily Calorie Target", f"{tdee} kcal")
        col3.metric("Calories Today",      f"{totals.get('total_calories', 0)} kcal")
        col4.metric("Cycle Phase",         f"{cycle_info['emoji']} {phase.title()}")

        st.markdown("---")
        st.subheader(f"{cycle_info['emoji']} Today's Insight")
        st.info(cycle_info["description"])

        recs   = get_phase_recommendations(phase)
        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("**💪 Recommended Workout**")
            st.write(recs["workout_type"])
            st.markdown("**🥗 Nutrition Focus**")
            st.write(recs["nutrition_focus"])

        with col_b:
            st.markdown("**✅ Foods to eat**")
            for f in recs["foods_to_eat"]:
                st.write(f"• {f}")
            if recs["foods_to_avoid"]:
                st.markdown("**❌ Foods to limit**")
                for f in recs["foods_to_avoid"]:
                    st.write(f"• {f}")

        st.markdown("---")
        st.subheader("🤖 AI Phase Explanation")
        if st.button("Explain my current phase"):
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