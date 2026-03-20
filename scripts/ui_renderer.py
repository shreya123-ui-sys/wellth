import streamlit as st

def render_workout(workout):
    for i, ex in enumerate(workout, 1):
        st.subheader(f"{i}. {ex['exercise']}")
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(ex["image"], use_container_width=True)

        with col2:
            st.markdown(f"**Sets × Reps:** {ex['sets']} × {ex['reps']}")
            st.write(ex["instructions"])
            st.success(f"Beginner: {ex['beginner']}")
            st.info(f"No equipment: {ex['no_equipment']}")

        st.divider()

def render_meal(title, meal):
    st.markdown(f"### 🍽️ {title}: {meal['name']}")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(meal["image"], use_container_width=True)

    with col2:
        st.caption(meal["calories"])
        st.write(
            f"**Protein:** {meal['protein']} | "
            f"**Carbs:** {meal['carbs']} | "
            f"**Fat:** {meal['fat']}"
        )

        st.markdown("**Ingredients:**")
        for i in meal["ingredients"]:
            st.write(f"- {i}")

        st.markdown("**Steps:**")
        for s in meal["steps"]:
            st.write(f"- {s}")

def render_daily_meals(meals):
    render_meal("Breakfast", meals["breakfast"])
    render_meal("Lunch", meals["lunch"])
    render_meal("Dinner", meals["dinner"])
