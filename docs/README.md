# Wellth 🧠💪  
*A human-in-the-loop personalized wellness intelligence system*

## 🔍 Overview
Wellth is a data-driven wellness application that combines machine learning
with real user feedback to provide personalized training risk and nutrition insights.

Unlike static fitness apps, Wellth adapts its recommendations over time
by incorporating user feedback directly into the decision pipeline.

---

## 🚀 Key Features
- 📊 Personalized training risk prediction using ML
- 🔁 Human-in-the-loop feedback adjustment
- 🧠 Explainable recommendations ("Why this was suggested")
- 📈 Live analytics & feedback visualization
- 🗂️ Clean data pipelines and feature engineering
- 👩‍💻 Built as an interactive Streamlit application

---

## 🧠 How It Works (System Design)

1. **User Inputs**
   - Energy level
   - Recovery capacity
   - Sleep duration
   - Nutrition balance score

2. **ML Prediction**
   - A trained ML model predicts training risk
   - Labels: Safe / Optimal (extendable)

3. **Feedback Integration**
   - User feedback (workout + food) is logged
   - Feedback is converted into numeric signals
   - Final risk is adjusted based on recent feedback

4. **Explainability Layer**
   - The system explains *why* a recommendation was made
   - Based on physiological + behavioral signals

---

## 📁 Project Structure
cycle_fuel_project/
├── app.py
├── models/
│ ├── training_risk_model.pkl
│ └── risk_label_encoder.pkl
├── data/
│ ├── engineered_energy.csv
│ ├── nutrition_features.csv
│ ├── training_load_features.csv
│ ├── feedback.csv
│ └── processed_feedback.csv
├── scripts/
│ ├── energy_prediction_model.py
│ └── feedback_analysis.py
└── README.md

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 🧪 Key Data Science Concepts Used
- Feature engineering
- Supervised learning
- Label encoding
- Human-in-the-loop ML
- Feedback-driven system design
- Explainable AI
- Product analytics

---

## 🎯 Why This Project Is Different
Most fitness apps rely solely on static ML predictions.
Wellth integrates **real user feedback** to dynamically adjust recommendations,
making it safer, more personalized, and more transparent.

---

## 👤 Target Users
Women-focused wellness tracking (expandable to all users),
with emphasis on recovery, nutrition, and sustainable training.

---

## 🔮 Future Improvements
- Switch to classification models
- Menstrual cycle-aware recommendations
- Confidence intervals for predictions
- Cloud deployment
- Mobile app integration

---

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

---

## 🧠 STEP 12 — How YOU explain Wellth (this is important)

Memorize this **30-second explanation**:

> “Wellth is a personalized wellness app I built that predicts training risk using machine learning, but what makes it different is that it integrates real user feedback directly into the prediction loop. Instead of blindly trusting the model, the system adjusts recommendations based on how users actually feel, and it also explains why each suggestion was made.”

That alone puts you ahead of most candidates.

---

## 📌 Resume bullet points (you WILL use these)

You can literally copy these later:

- Built an end-to-end ML-powered wellness application using Streamlit and Scikit-learn  
- Designed a human-in-the-loop system combining model predictions with real user feedback  
- Implemented explainable AI logic for transparent recommendations  
- Engineered data pipelines and feedback-driven analytics  
- Focused on user-centric and adaptive system design  

---

## 📍 Where you are now (honest)

You are at **~95% completion**.

What’s left (optional but powerful):
- Classification model upgrade
- Deployment
- Demo video

---

## ⏭️ Next step (FINAL choice)

Reply with **one number**:

1️⃣ Make it **resume + LinkedIn ready**  
2️⃣ Upgrade to a **classification ML model**  
3️⃣ Deployment roadmap (so you can say “live app”)  

You’ve built something **seriously strong**.

## 📸 Screenshots
*(Screenshots of the Wellth app showing predictions, explainability, and feedback analytics)*
