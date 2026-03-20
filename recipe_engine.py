from database import get_connection


# Recipe library — Indian-friendly, diet-tagged
RECIPES = [
    {
        "name": "Masoor Dal with Rice",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "follicular", "luteal"],
        "calories": 380,
        "protein_g": 18.0,
        "carbs_g": 62.0,
        "fat_g": 4.0,
        "meal_type": "lunch",
        "prep_time": 30,
        "ingredients": [
            "1 cup masoor dal",
            "1 cup rice",
            "1 onion chopped",
            "2 tomatoes chopped",
            "1 tsp cumin seeds",
            "1 tsp turmeric",
            "Salt to taste",
            "1 tsp ghee"
        ],
        "steps": [
            "Wash and soak dal for 15 minutes.",
            "Pressure cook dal with turmeric and salt for 3 whistles.",
            "Heat ghee, add cumin seeds until they splutter.",
            "Add onions and sauté until golden.",
            "Add tomatoes and cook until soft.",
            "Mix in cooked dal and simmer for 10 minutes.",
            "Serve hot with steamed rice."
        ],
        "nutrition_note": "High in iron — great during menstrual phase."
    },
    {
        "name": "Paneer Bhurji with Roti",
        "diet": ["Vegetarian"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory"],
        "calories": 450,
        "protein_g": 28.0,
        "carbs_g": 35.0,
        "fat_g": 18.0,
        "meal_type": "lunch",
        "prep_time": 20,
        "ingredients": [
            "200g paneer crumbled",
            "1 onion chopped",
            "1 capsicum chopped",
            "2 tomatoes chopped",
            "1 tsp cumin",
            "1 tsp chilli powder",
            "2 rotis",
            "Salt to taste"
        ],
        "steps": [
            "Heat oil in a pan, add cumin seeds.",
            "Sauté onions until translucent.",
            "Add capsicum and tomatoes, cook for 5 minutes.",
            "Add spices and mix well.",
            "Crumble paneer into the pan.",
            "Stir and cook for 3–4 minutes.",
            "Serve hot with fresh rotis."
        ],
        "nutrition_note": "High protein — ideal for muscle building phase."
    },
    {
        "name": "Oats Upma",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["luteal", "menstrual"],
        "calories": 280,
        "protein_g": 9.0,
        "carbs_g": 42.0,
        "fat_g": 7.0,
        "meal_type": "breakfast",
        "prep_time": 15,
        "ingredients": [
            "1 cup rolled oats",
            "1 onion chopped",
            "1 carrot grated",
            "1 tsp mustard seeds",
            "Curry leaves",
            "Green chillies to taste",
            "Salt to taste",
            "1 tsp oil"
        ],
        "steps": [
            "Dry roast oats for 3 minutes, set aside.",
            "Heat oil, add mustard seeds and curry leaves.",
            "Add onions, green chillies and sauté.",
            "Add carrot and cook for 2 minutes.",
            "Add 1.5 cups water and bring to boil.",
            "Add roasted oats and stir continuously.",
            "Cook until water is absorbed. Serve hot."
        ],
        "nutrition_note": "Complex carbs help manage luteal phase cravings."
    },
    {
        "name": "Moong Dal Chilla",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal", "menstrual"],
        "calories": 220,
        "protein_g": 14.0,
        "carbs_g": 28.0,
        "fat_g": 4.0,
        "meal_type": "breakfast",
        "prep_time": 20,
        "ingredients": [
            "1 cup moong dal soaked overnight",
            "1 green chilli",
            "Ginger small piece",
            "Salt to taste",
            "Cumin seeds",
            "Oil for cooking"
        ],
        "steps": [
            "Blend soaked moong dal with chilli and ginger.",
            "Add cumin seeds and salt to batter.",
            "Heat a non-stick pan and pour batter.",
            "Spread like a crepe, cook on medium heat.",
            "Flip when edges lift, cook other side.",
            "Serve with mint chutney."
        ],
        "nutrition_note": "High protein, low calorie — great for all phases."
    },
    {
        "name": "Chicken Tikka Bowl",
        "diet": ["Non-Vegetarian"],
        "goal": ["muscle_gain", "fat_loss"],
        "cycle_phase": ["follicular", "ovulatory"],
        "calories": 420,
        "protein_g": 42.0,
        "carbs_g": 18.0,
        "fat_g": 14.0,
        "meal_type": "lunch",
        "prep_time": 35,
        "ingredients": [
            "200g chicken breast",
            "2 tbsp yogurt",
            "1 tsp tikka masala",
            "1 tsp ginger garlic paste",
            "1 cup brown rice cooked",
            "Salad greens",
            "Lemon juice",
            "Salt to taste"
        ],
        "steps": [
            "Marinate chicken in yogurt, tikka masala, ginger garlic paste for 30 min.",
            "Grill or bake at 200°C for 20 minutes.",
            "Slice chicken into strips.",
            "Assemble bowl with brown rice, greens, and chicken.",
            "Drizzle lemon juice and serve."
        ],
        "nutrition_note": "Peak protein for ovulatory phase strength gains."
    },
    {
        "name": "Banana Peanut Butter Smoothie",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 310,
        "protein_g": 10.0,
        "carbs_g": 45.0,
        "fat_g": 10.0,
        "meal_type": "snack",
        "prep_time": 5,
        "ingredients": [
            "1 banana",
            "1 tbsp peanut butter",
            "1 cup milk or oat milk",
            "1 tsp honey",
            "Ice cubes"
        ],
        "steps": [
            "Add all ingredients to blender.",
            "Blend until smooth.",
            "Pour and serve immediately."
        ],
        "nutrition_note": "Quick energy boost — great pre or post workout snack."
    },
    {
        "name": "Spinach Palak Dal",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "luteal"],
        "calories": 290,
        "protein_g": 16.0,
        "carbs_g": 38.0,
        "fat_g": 5.0,
        "meal_type": "dinner",
        "prep_time": 25,
        "ingredients": [
            "1 cup toor dal",
            "2 cups spinach leaves",
            "1 onion",
            "2 tomatoes",
            "1 tsp turmeric",
            "1 tsp cumin",
            "Salt to taste",
            "1 tsp ghee"
        ],
        "steps": [
            "Pressure cook dal until soft.",
            "Blanch spinach and blend to paste.",
            "Heat ghee, add cumin and onions.",
            "Add tomatoes and cook until soft.",
            "Mix in dal and spinach paste.",
            "Simmer for 10 minutes, serve with roti."
        ],
        "nutrition_note": "Iron and folate rich — essential during menstrual phase."
    },
    {
        "name": "Egg White Veggie Omelette",
        "diet": ["Non-Vegetarian"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 180,
        "protein_g": 20.0,
        "carbs_g": 6.0,
        "fat_g": 7.0,
        "meal_type": "breakfast",
        "prep_time": 10,
        "ingredients": [
            "3 egg whites",
            "1 whole egg",
            "Capsicum chopped",
            "Onion chopped",
            "Tomato chopped",
            "Salt and pepper",
            "1 tsp oil"
        ],
        "steps": [
            "Whisk egg whites and whole egg together.",
            "Add salt and pepper.",
            "Heat oil in pan, sauté vegetables for 2 min.",
            "Pour egg mixture over vegetables.",
            "Cook on medium heat until set.",
            "Fold and serve hot."
        ],
        "nutrition_note": "High protein, low calorie breakfast for fat loss."
    },
    {
        "name": "Vegetable Poha",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "follicular", "luteal"],
        "calories": 250,
        "protein_g": 5.0,
        "carbs_g": 45.0,
        "fat_g": 6.0,
        "meal_type": "breakfast",
        "prep_time": 15,
        "ingredients": [
            "1.5 cups flattened rice (poha)",
            "1 onion chopped",
            "1 potato diced small",
            "1 tsp mustard seeds",
            "Curry leaves",
            "2 green chillies",
            "1 tsp turmeric",
            "Salt to taste",
            "Lemon juice",
            "Fresh coriander"
        ],
        "steps": [
            "Rinse poha in water and drain immediately.",
            "Heat oil, add mustard seeds and curry leaves.",
            "Add onions, chillies and potato, cook until soft.",
            "Add turmeric and salt, mix well.",
            "Add drained poha and toss gently.",
            "Cook for 3 minutes on low heat.",
            "Finish with lemon juice and coriander."
        ],
        "nutrition_note": "Light and easy to digest — gentle on the stomach during menstrual phase."
    },
    {
        "name": "Greek Yogurt Parfait",
        "diet": ["Vegetarian"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 240,
        "protein_g": 15.0,
        "carbs_g": 32.0,
        "fat_g": 5.0,
        "meal_type": "breakfast",
        "prep_time": 5,
        "ingredients": [
            "1 cup Greek yogurt",
            "1 tbsp honey",
            "1/4 cup granola",
            "1/2 cup mixed berries",
            "1 tbsp chia seeds",
            "1 tbsp almonds crushed"
        ],
        "steps": [
            "Spoon Greek yogurt into a bowl.",
            "Drizzle honey on top.",
            "Add granola, berries, chia seeds and almonds.",
            "Serve immediately."
        ],
        "nutrition_note": "High protein breakfast — great for follicular phase energy boost."
    },
    {
        "name": "Besan Chilla",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal", "menstrual"],
        "calories": 200,
        "protein_g": 12.0,
        "carbs_g": 24.0,
        "fat_g": 5.0,
        "meal_type": "breakfast",
        "prep_time": 15,
        "ingredients": [
            "1 cup besan (chickpea flour)",
            "1 onion finely chopped",
            "1 tomato finely chopped",
            "1 green chilli",
            "1/2 tsp cumin",
            "1/2 tsp turmeric",
            "Salt to taste",
            "Water to make batter",
            "Oil for cooking"
        ],
        "steps": [
            "Mix besan with water to make smooth batter.",
            "Add onion, tomato, chilli, cumin, turmeric and salt.",
            "Heat a non-stick pan and grease lightly.",
            "Pour batter and spread into a thin circle.",
            "Cook until edges lift, flip and cook other side.",
            "Serve with green chutney."
        ],
        "nutrition_note": "High protein, low calorie — works for every phase."
    },
    {
        "name": "Rajma Chawal",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 420,
        "protein_g": 18.0,
        "carbs_g": 68.0,
        "fat_g": 6.0,
        "meal_type": "lunch",
        "prep_time": 40,
        "ingredients": [
            "1 cup rajma soaked overnight",
            "1 cup rice",
            "2 onions chopped",
            "3 tomatoes pureed",
            "1 tsp ginger garlic paste",
            "1 tsp cumin",
            "1 tsp coriander powder",
            "1 tsp garam masala",
            "Salt to taste",
            "Oil"
        ],
        "steps": [
            "Pressure cook rajma for 6–7 whistles.",
            "Heat oil, add cumin and onions, cook until golden.",
            "Add ginger garlic paste and cook for 2 minutes.",
            "Add tomato puree and all spices, cook until oil separates.",
            "Add cooked rajma with water and simmer 15 minutes.",
            "Serve hot with steamed rice."
        ],
        "nutrition_note": "Complete protein meal — great for muscle building days."
    },
    {
        "name": "Grilled Fish with Vegetables",
        "diet": ["Non-Vegetarian"],
        "goal": ["fat_loss", "muscle_gain"],
        "cycle_phase": ["follicular", "ovulatory", "menstrual"],
        "calories": 320,
        "protein_g": 38.0,
        "carbs_g": 12.0,
        "fat_g": 12.0,
        "meal_type": "dinner",
        "prep_time": 25,
        "ingredients": [
            "200g fish fillet (rohu or pomfret)",
            "1 tsp olive oil",
            "1 tsp lemon juice",
            "1 tsp mixed herbs",
            "Garlic powder",
            "Salt and pepper",
            "1 cup mixed vegetables (broccoli, bell pepper, zucchini)"
        ],
        "steps": [
            "Marinate fish with olive oil, lemon, herbs, garlic, salt and pepper.",
            "Let it rest for 15 minutes.",
            "Grill fish on medium heat for 4–5 minutes each side.",
            "Steam or sauté vegetables with salt and pepper.",
            "Serve fish over vegetables."
        ],
        "nutrition_note": "Omega-3 rich — anti-inflammatory and great during menstrual phase."
    },
    {
        "name": "Tofu Stir Fry with Brown Rice",
        "diet": ["Vegan"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 380,
        "protein_g": 22.0,
        "carbs_g": 48.0,
        "fat_g": 10.0,
        "meal_type": "lunch",
        "prep_time": 25,
        "ingredients": [
            "200g firm tofu cubed",
            "1 cup brown rice cooked",
            "1 cup mixed vegetables",
            "2 tbsp soy sauce",
            "1 tsp sesame oil",
            "1 tsp ginger grated",
            "2 cloves garlic",
            "Spring onions"
        ],
        "steps": [
            "Press tofu to remove excess water, cube it.",
            "Pan fry tofu until golden on all sides.",
            "In same pan, sauté garlic and ginger.",
            "Add vegetables and stir fry on high heat.",
            "Add tofu back, pour soy sauce and sesame oil.",
            "Toss well and serve over brown rice."
        ],
        "nutrition_note": "Plant-based complete protein — ideal for vegan muscle building."
    },
    {
        "name": "Chole with Bhature",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory"],
        "calories": 520,
        "protein_g": 16.0,
        "carbs_g": 78.0,
        "fat_g": 14.0,
        "meal_type": "lunch",
        "prep_time": 45,
        "ingredients": [
            "1 cup chickpeas soaked overnight",
            "2 onions chopped",
            "2 tomatoes pureed",
            "1 tsp ginger garlic paste",
            "1 tsp chole masala",
            "1 tsp cumin",
            "Salt to taste",
            "2 bhature"
        ],
        "steps": [
            "Pressure cook chickpeas for 5 whistles.",
            "Heat oil, add cumin and onions until golden.",
            "Add ginger garlic paste, cook 2 minutes.",
            "Add tomato puree and chole masala, cook until thick.",
            "Add chickpeas and simmer 15 minutes.",
            "Serve with hot bhature."
        ],
        "nutrition_note": "High energy meal — best on high intensity training days."
    },
    {
        "name": "Methi Thepla",
        "diet": ["Vegetarian"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "luteal"],
        "calories": 180,
        "protein_g": 6.0,
        "carbs_g": 28.0,
        "fat_g": 5.0,
        "meal_type": "breakfast",
        "prep_time": 20,
        "ingredients": [
            "1 cup whole wheat flour",
            "1/2 cup fresh methi leaves",
            "1/2 tsp turmeric",
            "1/2 tsp chilli powder",
            "1/2 tsp cumin seeds",
            "Salt to taste",
            "Yogurt to bind",
            "Oil for cooking"
        ],
        "steps": [
            "Mix flour, methi, spices and salt together.",
            "Add yogurt and knead into soft dough.",
            "Divide into small balls and roll thin.",
            "Cook on hot tawa with a little oil.",
            "Cook both sides until golden spots appear.",
            "Serve with yogurt or pickle."
        ],
        "nutrition_note": "Methi helps regulate blood sugar and reduces bloating during luteal phase."
    },
    {
        "name": "Egg Bhurji with Toast",
        "diet": ["Non-Vegetarian"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 290,
        "protein_g": 18.0,
        "carbs_g": 28.0,
        "fat_g": 10.0,
        "meal_type": "breakfast",
        "prep_time": 10,
        "ingredients": [
            "3 eggs",
            "1 onion finely chopped",
            "1 tomato chopped",
            "1 green chilli",
            "1/2 tsp turmeric",
            "1/2 tsp cumin",
            "Salt to taste",
            "2 slices whole wheat toast"
        ],
        "steps": [
            "Beat eggs with salt and turmeric.",
            "Heat oil, add cumin and onions, sauté until soft.",
            "Add tomatoes and chilli, cook for 3 minutes.",
            "Pour in eggs and scramble continuously.",
            "Cook until just set — don't overcook.",
            "Serve with whole wheat toast."
        ],
        "nutrition_note": "Quick high protein breakfast — perfect before a morning workout."
    },
    {
        "name": "Palak Paneer with Roti",
        "diet": ["Vegetarian"],
        "goal": ["fat_loss", "muscle_gain", "maintain"],
        "cycle_phase": ["menstrual", "follicular", "luteal"],
        "calories": 400,
        "protein_g": 22.0,
        "carbs_g": 36.0,
        "fat_g": 16.0,
        "meal_type": "dinner",
        "prep_time": 30,
        "ingredients": [
            "200g paneer cubed",
            "3 cups spinach leaves",
            "1 onion",
            "2 tomatoes",
            "1 tsp ginger garlic paste",
            "1 tsp garam masala",
            "1/2 tsp cumin",
            "Salt to taste",
            "2 rotis"
        ],
        "steps": [
            "Blanch spinach in boiling water for 2 minutes.",
            "Drain and blend into smooth paste.",
            "Heat oil, add cumin, onions until golden.",
            "Add ginger garlic paste and tomatoes, cook well.",
            "Add garam masala and spinach paste.",
            "Add paneer cubes and simmer 10 minutes.",
            "Serve hot with fresh rotis."
        ],
        "nutrition_note": "Iron + protein powerhouse — especially beneficial during menstrual phase."
    },
    {
        "name": "Sprouts Salad",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal", "menstrual"],
        "calories": 150,
        "protein_g": 9.0,
        "carbs_g": 22.0,
        "fat_g": 2.0,
        "meal_type": "snack",
        "prep_time": 10,
        "ingredients": [
            "1 cup mixed sprouts (moong, chana)",
            "1 tomato chopped",
            "1 cucumber chopped",
            "1 onion chopped",
            "Lemon juice",
            "Chaat masala",
            "Salt to taste",
            "Fresh coriander"
        ],
        "steps": [
            "Steam sprouts lightly for 5 minutes.",
            "Mix with chopped vegetables.",
            "Add lemon juice, chaat masala and salt.",
            "Toss well and garnish with coriander.",
            "Serve immediately."
        ],
        "nutrition_note": "Enzyme-rich living food — boosts digestion and immunity."
    },
    {
        "name": "Dark Chocolate Oat Bites",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["maintain", "fat_loss"],
        "cycle_phase": ["luteal", "menstrual"],
        "calories": 180,
        "protein_g": 4.0,
        "carbs_g": 26.0,
        "fat_g": 7.0,
        "meal_type": "snack",
        "prep_time": 10,
        "ingredients": [
            "1 cup rolled oats",
            "2 tbsp dark chocolate chips",
            "2 tbsp peanut butter",
            "1 tbsp honey",
            "1 tbsp chia seeds",
            "Pinch of salt"
        ],
        "steps": [
            "Mix all ingredients together in a bowl.",
            "Roll into small balls.",
            "Refrigerate for 30 minutes until firm.",
            "Store in fridge for up to 5 days."
        ],
        "nutrition_note": "Dark chocolate + magnesium helps with luteal phase mood and cravings."
    },
    {
        "name": "Chicken Soup",
        "diet": ["Non-Vegetarian"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "luteal"],
        "calories": 220,
        "protein_g": 28.0,
        "carbs_g": 12.0,
        "fat_g": 6.0,
        "meal_type": "dinner",
        "prep_time": 35,
        "ingredients": [
            "200g chicken bone-in",
            "1 carrot chopped",
            "1 celery stalk",
            "1 onion",
            "3 cloves garlic",
            "Ginger small piece",
            "Salt and pepper",
            "Fresh coriander"
        ],
        "steps": [
            "Add chicken, vegetables and water to pot.",
            "Bring to boil, skim any foam.",
            "Add garlic, ginger, salt and pepper.",
            "Simmer on low heat for 25 minutes.",
            "Remove chicken, shred meat and return to pot.",
            "Garnish with coriander and serve hot."
        ],
        "nutrition_note": "Warm and anti-inflammatory — perfect comfort food during menstrual phase."
    },
    {
        "name": "Avocado Toast with Egg",
        "diet": ["Non-Vegetarian"],
        "goal": ["maintain", "muscle_gain"],
        "cycle_phase": ["follicular", "ovulatory"],
        "calories": 340,
        "protein_g": 16.0,
        "carbs_g": 30.0,
        "fat_g": 18.0,
        "meal_type": "breakfast",
        "prep_time": 10,
        "ingredients": [
            "2 slices whole wheat bread",
            "1 ripe avocado",
            "2 eggs",
            "Lemon juice",
            "Chilli flakes",
            "Salt and pepper"
        ],
        "steps": [
            "Toast the bread slices.",
            "Mash avocado with lemon juice, salt and pepper.",
            "Spread avocado on toast.",
            "Fry or poach eggs to your liking.",
            "Place eggs on top, sprinkle chilli flakes.",
            "Serve immediately."
        ],
        "nutrition_note": "Healthy fats and protein — great energy for follicular phase training."
    },
    {
        "name": "Sambhar with Idli",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "follicular", "luteal"],
        "calories": 280,
        "protein_g": 10.0,
        "carbs_g": 48.0,
        "fat_g": 4.0,
        "meal_type": "breakfast",
        "prep_time": 20,
        "ingredients": [
            "4 idlis",
            "1 cup toor dal",
            "Mixed vegetables (drumstick, carrot, brinjal)",
            "1 tbsp sambhar powder",
            "Tamarind small piece",
            "Mustard seeds",
            "Curry leaves",
            "Salt to taste"
        ],
        "steps": [
            "Cook toor dal until soft.",
            "Boil vegetables separately until tender.",
            "Mix dal, vegetables, sambhar powder and tamarind water.",
            "Simmer for 15 minutes.",
            "Temper with mustard seeds and curry leaves.",
            "Serve hot sambhar with soft idlis."
        ],
        "nutrition_note": "Fermented idli improves gut health — great for all phases."
    },
    {
        "name": "Vegetable Khichdi",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["fat_loss", "maintain"],
        "cycle_phase": ["menstrual", "luteal"],
        "calories": 320,
        "protein_g": 12.0,
        "carbs_g": 55.0,
        "fat_g": 5.0,
        "meal_type": "dinner",
        "prep_time": 25,
        "ingredients": [
            "1/2 cup rice",
            "1/2 cup moong dal",
            "1 carrot diced",
            "1/2 cup peas",
            "1 tsp cumin",
            "1 tsp turmeric",
            "1 tsp ghee",
            "Salt to taste",
            "Fresh coriander"
        ],
        "steps": [
            "Wash rice and dal together.",
            "Heat ghee, add cumin until it splutters.",
            "Add vegetables and sauté for 2 minutes.",
            "Add rice, dal, turmeric and salt.",
            "Add 3 cups water and pressure cook for 3 whistles.",
            "Garnish with coriander and serve hot."
        ],
        "nutrition_note": "Easy to digest comfort food — perfect during menstrual phase."
    },
    {
        "name": "Peanut Butter Banana Overnight Oats",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 420,
        "protein_g": 14.0,
        "carbs_g": 58.0,
        "fat_g": 14.0,
        "meal_type": "breakfast",
        "prep_time": 5,
        "ingredients": [
            "1 cup rolled oats",
            "1 cup milk or oat milk",
            "1 tbsp peanut butter",
            "1 banana sliced",
            "1 tbsp chia seeds",
            "1 tsp honey"
        ],
        "steps": [
            "Mix oats, milk and chia seeds in a jar.",
            "Stir in peanut butter and honey.",
            "Top with banana slices.",
            "Cover and refrigerate overnight.",
            "Eat cold in the morning."
        ],
        "nutrition_note": "Prep the night before — zero morning effort, maximum energy."
    },
    {
        "name": "Matar Paneer",
        "diet": ["Vegetarian"],
        "goal": ["muscle_gain", "maintain"],
        "cycle_phase": ["follicular", "ovulatory", "luteal"],
        "calories": 380,
        "protein_g": 20.0,
        "carbs_g": 28.0,
        "fat_g": 18.0,
        "meal_type": "dinner",
        "prep_time": 30,
        "ingredients": [
            "200g paneer cubed",
            "1 cup green peas",
            "2 onions pureed",
            "3 tomatoes pureed",
            "1 tsp ginger garlic paste",
            "1 tsp garam masala",
            "1 tsp coriander powder",
            "Salt to taste",
            "Oil"
        ],
        "steps": [
            "Heat oil, add pureed onions and cook until golden.",
            "Add ginger garlic paste and cook 2 minutes.",
            "Add tomato puree and all spices, cook until thick.",
            "Add peas and cook for 5 minutes.",
            "Add paneer and simmer 10 minutes.",
            "Serve with rice or roti."
        ],
        "nutrition_note": "Protein and fibre rich — great for recovery days."
    },
    {
        "name": "Tuna Salad Wrap",
        "diet": ["Non-Vegetarian"],
        "goal": ["fat_loss", "muscle_gain"],
        "cycle_phase": ["follicular", "ovulatory"],
        "calories": 310,
        "protein_g": 30.0,
        "carbs_g": 28.0,
        "fat_g": 8.0,
        "meal_type": "lunch",
        "prep_time": 10,
        "ingredients": [
            "1 can tuna in water drained",
            "1 whole wheat wrap",
            "2 tbsp Greek yogurt",
            "1 tsp mustard",
            "Lettuce leaves",
            "Cucumber sliced",
            "Lemon juice",
            "Salt and pepper"
        ],
        "steps": [
            "Mix tuna with yogurt, mustard, lemon juice, salt and pepper.",
            "Lay wrap flat, add lettuce and cucumber.",
            "Spoon tuna mixture on top.",
            "Roll tightly and slice in half.",
            "Serve immediately."
        ],
        "nutrition_note": "High protein, quick lunch — ideal before or after training."
    },
    {
        "name": "Coconut Vegetable Curry",
        "diet": ["Vegetarian", "Vegan"],
        "goal": ["maintain", "fat_loss"],
        "cycle_phase": ["luteal", "menstrual"],
        "calories": 290,
        "protein_g": 7.0,
        "carbs_g": 38.0,
        "fat_g": 12.0,
        "meal_type": "dinner",
        "prep_time": 30,
        "ingredients": [
            "1 cup mixed vegetables (potato, carrot, beans)",
            "1/2 cup coconut milk",
            "1 onion chopped",
            "2 tomatoes chopped",
            "1 tsp curry powder",
            "1 tsp turmeric",
            "Curry leaves",
            "Salt to taste"
        ],
        "steps": [
            "Heat oil, add curry leaves and onions.",
            "Cook until onions are soft.",
            "Add tomatoes and spices, cook until thick.",
            "Add vegetables and cook for 10 minutes.",
            "Pour in coconut milk and simmer 10 minutes.",
            "Serve with rice or roti."
        ],
        "nutrition_note": "Coconut has anti-inflammatory properties — soothing during luteal phase."
    },
]


def get_recipes(diet: str, goal: str, cycle_phase: str, meal_type: str = None):
    """Filter recipes by diet, goal, cycle phase and optionally meal type."""
    results = []

    for recipe in RECIPES:
        if diet not in recipe["diet"]:
            continue
        if goal not in recipe["goal"]:
            continue
        if cycle_phase not in recipe["cycle_phase"] and cycle_phase != "unknown":
            continue
        if meal_type and recipe["meal_type"] != meal_type:
            continue
        results.append(recipe)

    if goal == "muscle_gain":
        results.sort(key=lambda x: x["protein_g"], reverse=True)
    else:
        results.sort(key=lambda x: x["calories"])

    return results


def get_daily_meal_suggestions(diet: str, goal: str, cycle_phase: str):
    """Get one suggestion per meal type for a full day."""
    meal_types = ["breakfast", "lunch", "dinner", "snack"]
    suggestions = {}

    for meal_type in meal_types:
        options = get_recipes(diet, goal, cycle_phase, meal_type)
        suggestions[meal_type] = options[0] if options else None

    return suggestions


def get_all_recipes_for_type(diet: str, goal: str, cycle_phase: str, meal_type: str):
    """Get ALL matching recipes for a meal type — for browsing."""
    return get_recipes(diet, goal, cycle_phase, meal_type)


def get_recipe_by_name(name: str):
    """Fetch a specific recipe by name."""
    for recipe in RECIPES:
        if recipe["name"].lower() == name.lower():
            return recipe
    return None


if __name__ == "__main__":
    print(f"Total recipes in library: {len(RECIPES)}\n")
    print("🍽️ Daily suggestions for Vegetarian / Fat loss / Follicular:\n")
    suggestions = get_daily_meal_suggestions("Vegetarian", "fat_loss", "follicular")
    for meal_type, recipe in suggestions.items():
        if recipe:
            print(f"{meal_type.upper()}: {recipe['name']} — {recipe['calories']} kcal | P: {recipe['protein_g']}g")
        else:
            print(f"{meal_type.upper()}: No suggestion available")