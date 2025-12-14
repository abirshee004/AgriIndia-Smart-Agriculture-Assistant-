# 🌱 AgriIndia – Smart Agriculture Assistant 🇮🇳


<p align="center">
  <img src="https://img.icons8.com/color/96/plant-under-sun.png" width="80"/>
  <img src="https://img.icons8.com/color/96/artificial-intelligence.png" width="80"/>
  <img src="https://img.icons8.com/color/96/india.png" width="80"/>
</p>

AgriGuru is an **AI-powered smart agriculture assistant** designed to help **Indian farmers** make better farming decisions using **Machine Learning and Data Analytics**.

The project currently focuses on **Crop Recommendation**, with future extensions for **Crop Disease Prediction, Weather Forecasting, Market Price Analysis**, and a **multilingual chatbot** for farmers.

---

## 📌 Project Overview

| Field | Details |
|------|--------|
| **Project Name** | AgriIndia – Smart Agriculture Assistant |
| **Domain** | Artificial Intelligence & Agriculture |
| **Project Type** | Final Year Academic Project |
| **Developed For** | Indian Agriculture |
| **Tech Stack** | Python, Machine Learning, Streamlit |

---

## 🎯 Objectives

- 🌱 Improve crop productivity using data-driven decisions  
- 🧪 Help farmers select the most suitable crop based on soil & climate  
- 👨‍🌾 Provide a simple, user-friendly interface (farmer-friendly UI)  
- 🤖 Promote smart agriculture using AI  
- 🚀 Build a scalable platform for future agriculture services  

---

## 🧠 Technologies Used
- Python
- Streamlit
- Machine Learning (LightGBM)
- Pandas, NumPy
- Plotly, Matplotlib
- Joblib

## ⚙️ Features Implemented

### ✅ Crop Recommendation System (Working)

#### 🔢 Inputs
- Nitrogen (N)  
- Phosphorus (P)  
- Potassium (K)  
- Soil pH  
- Rainfall  
- Temperature  

#### 📈 Outputs
- 🌾 **Best Recommended Crop**
- 🥇 **Top 3 Crop Suggestions** with confidence (%)

---

## 🚧 Under Development (UI Available)

- 🦠 Crop Disease Prediction  
- 🌦 Weather Forecasting  
- 💰 Market Price Analysis  
- 💬 Multilingual AI Chatbot for Farmers  

---

## 🧠 Machine Learning Model

- **Algorithm Used:** LightGBM Classifier  
- **Training Data:** Agricultural soil & climate dataset  
- **Output:** Crop label prediction  

### 📦 Model Files
- `crop_model.pkl` – Trained ML model  
- `label_encoder.pkl` – Crop label encoder  

Models are loaded using **Joblib** and integrated into the **Streamlit web app**.

---

## 📊 Dataset Information

The dataset contains:
- Soil nutrient values  
- Climate conditions  
- Corresponding crop labels  

🔗 **Dataset Download (Google Drive):**  
👉 **(https://drive.google.com/file/d/1BIBSD_W6sVnX5G04a6VOUjss_FCOvGGZ/view?usp=sharing)**

> ⚠️ Note: Dataset is hosted externally due to GitHub size limitations.

---

## 🗂 Project Folder Structure

```text
AgriGuru/
│
├── app.py                     # Main Streamlit app
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── pages/                     # Streamlit multi-pages
│   ├── 1_🏠_Home.py
│   ├── 2_🌾_Models.py
│   ├── 3_🛒_Products.py
│   ├── 4_ℹ️_About.py
│
├── assets/                    # Images & static files
│   ├── team images
│   ├── product images
│   ├── logos
│
├── models/                    # Trained ML models
│   ├── crop_model.pkl
│   ├── label_encoder.pkl

```

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AgriGuru.git
cd AgriGuru
```


## OPEN CMD in your system, then copy paste this: 
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 👥 Team
- **Team Leader:** ABIR SHEE
- **Project Mentor:** SOUMI TAKDAR
**Members**
- Diptam Kundu
- Amritash Banarjee
- Kaushiki Mandal
- Debanjan Gangully

## 🏫 Institute
B.P. Poddar Institute of Management and Technology  
Kolkata, India

# Batch (2022 - 2026), CSE

## 🇮🇳 Made in India

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg" width="120"/>
</p>

This project is developed as a **Final Year Academic Project** to support **Indian farmers**
through **AI-driven smart agriculture solutions**.



### 🔮 Future Enhancements

- 🌦 Real-time weather API integration

- 🦠 Image-based crop disease detection

- 💰 Market price prediction using time-series analysis

- 🎤 Voice-based chatbot in regional Indian languages 
