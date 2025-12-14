import streamlit as st

st.markdown("""
<style>
.project-card {
    background: linear-gradient(135deg, rgba(34,197,94,0.18), rgba(59,130,246,0.18));
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    margin-bottom: 20px;
}

.project-title {
    font-size: 22px;
    font-weight: 700;
    color: #22c55e;
    margin-bottom: 14px;
}

.project-row {
    font-size: 16px;
    margin: 8px 0;
}

.project-row span {
    color: #93c5fd;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.skill-badge {
    display: inline-block;
    background-color: #1f2937;
    color: #e5e7eb;
    padding: 5px 12px;
    border-radius: 14px;
    font-size: 12px;
    margin: 3px 4px 3px 0;
}
.member-card {
    background-color: rgba(255,255,255,0.03);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)



# ---------------- PAGE CONTENT ----------------
st.title("ℹ️ About AgriGuru")

# ---------------- PROJECT DETAILS ----------------
st.subheader("📌 Project Details")

st.markdown(
"""<div class="project-card">
<div class="project-title">🌱 AgriIndia – Smart Agriculture Assistant</div>

<div class="project-row">🏫 <span>College:</span> B.P. Poddar Institute of Management and Technology</div>
<div class="project-row">📍 <span>Address:</span> Poddar Vihar, Kaikhali, Kolkata – 700053</div>
<div class="project-row">📞 <span>Contact:</span> +91-XXXXXX3011</div>
<div class="project-row">🤖 <span>Domain:</span> Artificial Intelligence & Agriculture</div>
<div class="project-row">🇮🇳 <span>Made in India:</span> Final Year Academic Project</div>
</div>""",
unsafe_allow_html=True
)




# ---------------- TEAM SECTION ----------------
st.subheader("👥 Our Team")

st.markdown("### 🌟 Team Leader")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/abir.jpg", use_container_width=True)

with col2:
    st.markdown("**ABIR SHEE**")
    st.markdown("Team Leader & ML Developer")

    st.markdown("""
    <span class="skill-badge">Data Analyst</span>
    <span class="skill-badge">Python, SQL, Excel, PowerBI</span>
    <span class="skill-badge">Analysis</span>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <a href="https://www.linkedin.com/in/abir-shee-7bb4bb255/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="32">
        </a>
        """,
        unsafe_allow_html=True
    )



# TEAM MEMBERS
st.markdown("### 👨‍💻 Team Members")

col1, col2, col3, col4 = st.columns(4)

# Diptam
st.markdown("### 👤 Diptam Kundu")
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/diptam.jpg", use_container_width=True)

with col2:
    st.markdown("**Role:** Backend Developer & AI Developer")
    st.markdown("""
    <span class="skill-badge">Python</span>
    <span class="skill-badge">Flask</span>
    <span class="skill-badge">Machine Learning</span>
    """, unsafe_allow_html=True)

    st.markdown(
        '<a href="https://www.linkedin.com/in/diptam-kundu-7525b5267/" target="_blank">'
        '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="28"></a>',
        unsafe_allow_html=True
    )

st.markdown("---")


# Kaushiki
st.markdown("### 👤 Kaushiki Mandal")
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/kaushiki.jpg", use_container_width=True)

with col2:
    st.markdown("**Role:** Research & Documentation | ML Developer")
    st.markdown("""
    <span class="skill-badge">Research</span>
    <span class="skill-badge">Documentation</span>
    <span class="skill-badge">Machine Learning</span>
    """, unsafe_allow_html=True)

    st.markdown(
        '<a href="https://www.linkedin.com/in/kaushiki-mandal-832793267/" target="_blank">'
        '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="28"></a>',
        unsafe_allow_html=True
    )

st.markdown("---")


    # Amritash
st.markdown("### 👤 Amritash Banarjee")
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/amritash.jpg", use_container_width=True)

with col2:
    st.markdown("**Role:** UI / Frontend Developer")
    st.markdown("""
    <span class="skill-badge">HTML</span>
    <span class="skill-badge">CSS</span>
    <span class="skill-badge">UI Design</span>
    """, unsafe_allow_html=True)

    st.markdown(
        '<a href="https://www.linkedin.com/in/amritash-banerjee-2a2511341/" target="_blank">'
        '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="28"></a>',
        unsafe_allow_html=True
    )

st.markdown("---")

# Debanjan
st.markdown("### 👤 Debanjan Ganguly")
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/debanjan.jpg", use_container_width=True)

with col2:
    st.markdown("**Role:** Data Collection & Testing | Web Developer")
    st.markdown("""
    <span class="skill-badge">Data Collection</span>
    <span class="skill-badge">Testing</span>
    <span class="skill-badge">Web Development</span>
    """, unsafe_allow_html=True)

    st.markdown(
        '<a href="https://www.linkedin.com/" target="_blank">'
        '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="28"></a>',
        unsafe_allow_html=True
    )
