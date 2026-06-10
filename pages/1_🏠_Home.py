import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Full-page background with Indian flag */
.main {
    background: 
        linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)),
        url("assets/india_flag.png");
    background-size: cover;
    background-attachment: fixed;
    color: white;
}

/* Title */
.hero-title {
    font-size: 64px;
    font-weight: 800;
    color: #f4f4f4;
}
.hero-sub {
    font-size: 22px;
    color: #cccccc;
}

/* Section titles */
.section-title {
    font-size: 36px;
    font-weight: 700;
    margin-top: 40px;
    color: #f5c518;
}

/* Cards */
.card {
    background-color: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 0px 20px rgba(0,0,0,0.4);
}

/* Objective bullets */
.obj {
    font-size: 18px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero-title">🌾 AgriIndia</div>
<div class="hero-sub">
AI-Powered Agriculture Platform for India 🇮🇳<br>
Empowering Farmers • Enhancing Productivity • Made in India
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- VIDEO + HISTORY ----------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.video("assets/intro_video.mp4")

with col2:
    st.markdown("""
    <div class="card">
    <div class="section-title">📜 History of Agriculture in India</div>
    <p>
    India has one of the world's oldest agricultural civilizations, dating back
    over <b>10,000 years</b>. From the Indus Valley Civilization to modern smart
    farming, agriculture has remained the backbone of the Indian economy.
    </p>
    <p>
    Today, Artificial Intelligence, Machine Learning, and Data Science are
    transforming traditional farming into <b>smart, efficient, and sustainable
    agriculture</b>.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- IMAGE GALLERY ----------------
st.markdown("<div class='section-title'>🌱 Indian Agriculture in Action</div>", unsafe_allow_html=True)

img1, img2, img3, img4 = st.columns(4)
img1.image("assets/farmer1.jpg", use_container_width=True)
img2.image("assets/farming.jpg", use_container_width=True)
img3.image("assets/farmer2.jpg", use_container_width=True)
img4.image("assets/farmer3.jpg", use_container_width=True)

# ---------------- OBJECTIVES ----------------
st.markdown("""
<div class="section-title">🎯 Objectives of AgriGuru</div>
<div class="card">
<div class="obj">✅ Improve crop productivity using AI</div>
<div class="obj">✅ Assist illiterate farmers with smart recommendations</div>
<div class="obj">✅ Predict best crops based on soil & climate</div>
<div class="obj">✅ Early crop disease awareness</div>
<div class="obj">✅ Market price & weather intelligence</div>
</div>
""", unsafe_allow_html=True)

# ---------------- CALL TO ACTION ----------------
st.markdown("""
<br>
<div class="card" style="text-align:center;">
<h2>🚜 Empowering Indian Farmers with Technology 🇮🇳</h2>
<p>Explore AI models, crop recommendations, and smart farming tools.</p>
</div>
""", unsafe_allow_html=True)
