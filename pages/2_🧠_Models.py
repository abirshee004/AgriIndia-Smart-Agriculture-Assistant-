import streamlit as st
import pandas as pd
import joblib

st.title("🧠 AgriGuru – AI Models")

model = joblib.load("models/crop_model.pkl")
le = joblib.load("models/label_encoder.pkl")

tab1, tab2, tab3, tab4 = st.tabs([
    "🌾 Crop Recommendation",
    "🦠 Crop Disease Prediction",
    "🌦 Weather Forecasting",
    "💰 Market Price Analysis"
])

# ---------------- CROP RECOMMENDATION ----------------
with tab1:
    st.subheader("🌾 Crop Recommendation System")
    st.image("assets/logo.png", width=100)

    col1, col2, col3 = st.columns(3)
    N = col1.number_input("Nitrogen (N)", 0, 200, 90)
    P = col2.number_input("Phosphorus (P)", 0, 200, 42)
    K = col3.number_input("Potassium (K)", 0, 300, 40)

    col4, col5, col6 = st.columns(3)
    pH = col4.number_input("Soil pH", 0.0, 14.0, 5.3)
    rainfall = col5.number_input("Rainfall (mm)", 0, 1500, 800)
    temperature = col6.number_input("Temperature (°C)", 0.0, 50.0, 32.6)

    if st.button("🌱 Predict Now"):
        sample = pd.DataFrame([[N, P, K, pH, rainfall, temperature]],
            columns=['N','P','K','pH','rainfall','temperature'])

        probs = model.predict_proba(sample)[0]
        top3_idx = probs.argsort()[-3:][::-1]
        crops = le.inverse_transform(top3_idx)
        probs = probs[top3_idx]

        st.success(f"✅ Best Crop: **{crops[0]}** ({probs[0]*100:.2f}%)")

        st.write("### 🌾 Top 3 Recommended Crops")
        for c, p in zip(crops, probs):
            st.write(f"- **{c}** → {p*100:.2f}%")

# ---------------- OTHER MODELS ----------------
with tab2:
    st.warning("🛠 Crop Disease Prediction model is under maintenance")

with tab3:
    st.warning("🛠 Weather Forecasting model is under maintenance")

with tab4:
    st.warning("🛠 Market Price Analysis model is under maintenance")

# ---------------- CHATBOT PLACEHOLDER ----------------
st.markdown("---")
st.info("💬 Chatbot (Coming Soon): Farmers can chat in local languages")

