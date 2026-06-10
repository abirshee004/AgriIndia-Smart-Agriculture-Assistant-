import streamlit as st
import pandas as pd
import joblib
import numpy as np
import cv2
from PIL import Image
import pyttsx3 
import tensorflow as tf
import pickle
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AgriGuru AI", layout="wide")

# ---------------- TITLE ----------------
st.title("🧠 AgriGuru – AI Models")

# ---------------- LOAD MODELS ----------------
# Crop Recommendation
crop_model = joblib.load("models/crop_model.pkl")
crop_le = joblib.load("models/label_encoder.pkl")

# Disease Model (CNN)
disease_model = tf.keras.models.load_model("models/disease_model.h5")

with open("models/class_names.pkl", "rb") as f:
    class_names = pickle.load(f)

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4 = st.tabs([
    "🌾 Crop Recommendation",
    "🦠 Crop Disease Prediction",
    "🌦 Weather Forecasting",
    "💰 Market Price Analysis"
])

# =====================================================
# 🌾 CROP RECOMMENDATION
# =====================================================
with tab1:
    st.subheader("🌾 Crop Recommendation System")

    col1, col2, col3 = st.columns(3)
    N = col1.number_input("Nitrogen (N)", 0, 200, 90)
    P = col2.number_input("Phosphorus (P)", 0, 200, 42)
    K = col3.number_input("Potassium (K)", 0, 300, 40)

    col4, col5, col6 = st.columns(3)
    pH = col4.number_input("Soil pH", 0.0, 14.0, 5.5)
    rainfall = col5.number_input("Rainfall (mm)", 0, 1500, 800)
    temperature = col6.number_input("Temperature (°C)", 0.0, 50.0, 30.0)

    if st.button("🌱 Predict Crop"):
        sample = pd.DataFrame([[N, P, K, pH, rainfall, temperature]],
            columns=['N','P','K','pH','rainfall','temperature'])

        probs = crop_model.predict_proba(sample)[0]
        top3_idx = probs.argsort()[-3:][::-1]

        crops = crop_le.inverse_transform(top3_idx)
        probs = probs[top3_idx]

        st.success(f"✅ Best Crop: **{crops[0]}** ({probs[0]*100:.2f}%)")

        st.write("### 🌾 Top 3 Recommendations")
        for c, p in zip(crops, probs):
            st.write(f"- {c} → {p*100:.2f}%")

# =====================================================
# 🦠 DISEASE DETECTION
# =====================================================
with tab2:
    st.subheader("🦠 Crop Disease Detection")

    # -------- TEXT TO SPEECH --------
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    # -------- SOLUTIONS --------
    disease_solutions = {
        "Tomato___Late_blight": "Remove infected leaves. Use fungicide like Mancozeb.",
        "Potato___Early_blight": "Use crop rotation and fungicide.",
        "Healthy": "Your plant is healthy 🌱"
    }

    # -------- IMAGE PREPROCESS --------
    def preprocess(img):
        img = img.resize((224, 224))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)
        return img

    # -------- INPUT --------
    option = st.radio("Choose Input Method", ["📷 Camera", "📁 Upload"])

    image = None

    if option == "📷 Camera":
        image = st.camera_input("Take a photo")

    elif option == "📁 Upload":
        image = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    # -------- PREDICTION --------
    if image is not None:
        img = Image.open(image)
        st.image(img, caption="Selected Image", use_column_width=True)

        processed = preprocess(img)

        pred = disease_model.predict(processed)
        class_idx = np.argmax(pred)

        label = class_names[class_idx]
        confidence = np.max(pred) * 100

        st.success(f"🦠 Disease: **{label}**")
        st.write(f"📊 Confidence: {confidence:.2f}%")

        solution = disease_solutions.get(label, "Consult agricultural expert.")
        st.info(f"💊 Solution: {solution}")

        # -------- VOICE --------
        if st.button("🔊 Read Report"):
            speak(f"Disease detected is {label}. Solution is {solution}")

# =====================================================
# 🌦 WEATHER
# =====================================================
import requests
from datetime import datetime

with tab3:
    st.subheader("🌦 14-Day Weather Forecast")

    city = st.text_input("Enter City Name", "Kolkata")

    API_KEY = "62d1ef50af73da8bff0933870e68c634"   # 🔴 replace this

    if st.button("Get Weather Forecast"):

        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            st.error("❌ City not found or API issue")
        else:
            data = response.json()

            st.success(f"📍 Weather Forecast for {city}")

            # ---------------- GROUP BY DATE ----------------
            forecast = {}

            for item in data['list']:
                date = item['dt_txt'].split(" ")[0]

                temp = item['main']['temp']
                humidity = item['main']['humidity']
                weather = item['weather'][0]['main']

                if date not in forecast:
                    forecast[date] = {
                        "temp": [],
                        "humidity": [],
                        "weather": weather
                    }

                forecast[date]["temp"].append(temp)
                forecast[date]["humidity"].append(humidity)

            # ---------------- DISPLAY ----------------
            days = list(forecast.keys())[:14]

            cols = st.columns(3)

            for i, day in enumerate(days):
                avg_temp = sum(forecast[day]["temp"]) / len(forecast[day]["temp"])
                avg_humidity = sum(forecast[day]["humidity"]) / len(forecast[day]["humidity"])
                weather = forecast[day]["weather"]

                # -------- ICONS --------
                if "Rain" in weather:
                    icon = "🌧️"
                elif "Cloud" in weather:
                    icon = "☁️"
                elif "Clear" in weather:
                    icon = "☀️"
                else:
                    icon = "🌩️"

                with cols[i % 3]:
                    st.markdown(f"""
                    ### {icon} {day}
                    🌡 Temp: {avg_temp:.1f}°C  
                    💧 Humidity: {avg_humidity:.0f}%  
                    🌤 Condition: {weather}
                    """)

# =====================================================
# 💰 MARKET
# =====================================================
with tab4:
    st.warning("💰 Market Price Analysis coming soon...")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.info("💬 AgriGuru Chatbot (Coming Soon)")