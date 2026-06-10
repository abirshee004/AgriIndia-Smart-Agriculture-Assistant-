import streamlit as st

# ---------------- CSS ----------------
st.markdown("""
<style>
.state-card {
    border-radius: 16px;
    overflow: hidden;
    background-color: #111827;
    padding: 10px;
    text-align: center;
}
.state-title {
    font-size: 18px;
    font-weight: 700;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🗺️ Farming Across Indian States")
st.caption("Click on a state to explore its agricultural richness 🌾")

# ---------------- STATE DATA ----------------
states = {
    "Rajasthan": {
        "image": "assets/states/rajasthan/hero.jpg",
        "desc": """
        Rajasthan has a long history of agriculture adapted to arid and semi-arid climates.
        Farming mainly depends on monsoon rainfall and traditional water conservation methods.
        
        **Major Crops:** Bajra, Wheat, Barley, Mustard, Pulses  
        **Techniques:** Dry farming, drip irrigation, khadin system
        """,
        "crops": [
            "assets/states/rajasthan/crop1.jpg",
            "assets/states/rajasthan/crop2.jpg",
            "assets/states/rajasthan/crop3.jpg",
            "assets/states/rajasthan/crop4.jpg",
            "assets/states/rajasthan/crop5.jpg",
            "assets/states/rajasthan/crop6.jpg",
        ]
    },

    "Punjab": {
        "image": "assets/states/punjab/hero.jpg",
        "desc": """
        Punjab is known as the **Granary of India**.
        The Green Revolution transformed agriculture here with modern machinery and irrigation.
        
        **Major Crops:** Wheat, Rice, Sugarcane, Maize  
        **Techniques:** Mechanized farming, canal irrigation
        """,
        "crops": [
            "assets/states/punjab/crop1.jpg",
            "assets/states/punjab/crop2.jpg",
            "assets/states/punjab/crop3.jpg",
            "assets/states/punjab/crop4.jpg",
            "assets/states/punjab/crop5.jpg",
            "assets/states/punjab/crop6.jpg",
        ]
    },

    "Maharashtra": {
    "image": "assets/states/maharashtra/hero.jpg",
    "desc": """
    Maharashtra has a diverse agricultural system influenced by varied climate zones,
    from coastal Konkan to dry regions of Vidarbha and Marathwada.
    Agriculture here depends on both rainfall and modern irrigation methods.

    **Major Crops:** Sugarcane, Cotton, Soybean, Jowar, Bajra, Grapes  
    **Techniques:** Drip irrigation, rain-fed farming, horticulture, watershed management
    """,
    # "crops": [
    #     "assets/states/maharashtra/crop1.jpg",
    #     "assets/states/maharashtra/crop2.jpg",
    #     "assets/states/maharashtra/crop3.jpg",
    #     "assets/states/maharashtra/crop4.jpg",
    #     "assets/states/maharashtra/crop5.jpg",
    #     "assets/states/maharashtra/crop6.jpg",
    # ]
},


    "West Bengal": {
    "image": "assets/states/west_bengal/hero.jpg",
    "desc": """
    West Bengal has a rich agricultural heritage supported by fertile alluvial soil
    and abundant river systems like the Ganga and its tributaries.
    Agriculture is largely rain-fed and river-based.

    **Major Crops:** Rice, Jute, Tea, Potato, Sugarcane, Vegetables  
    **Techniques:** Monsoon-based farming, river irrigation, traditional paddy cultivation,
    terrace farming in hilly regions (Darjeeling)
    """,
    # "crops": [
    #     "assets/states/west_bengal/crop1.jpg",
    #     "assets/states/west_bengal/crop2.jpg",
    #     "assets/states/west_bengal/crop3.jpg",
    #     "assets/states/west_bengal/crop4.jpg",
    #     "assets/states/west_bengal/crop5.jpg",
    #     "assets/states/west_bengal/crop6.jpg",
    # ]
},


"Uttar Pradesh": {
    "image": "assets/states/uttar_pradesh/hero.jpg",
    "desc": """
    Uttar Pradesh is one of India's largest agricultural states,
    supported by fertile alluvial soil of the Indo-Gangetic plains.
    Agriculture here plays a vital role in India's food security.

    **Major Crops:** Wheat, Rice, Sugarcane, Potato, Pulses, Oilseeds  
    **Techniques:** Canal irrigation, tube-well irrigation, crop rotation,
    traditional and mechanized farming practices
    """,
    # "crops": [
    #     "assets/states/uttar_pradesh/crop1.jpg",
    #     "assets/states/uttar_pradesh/crop2.jpg",
    #     "assets/states/uttar_pradesh/crop3.jpg",
    #     "assets/states/uttar_pradesh/crop4.jpg",
    #     "assets/states/uttar_pradesh/crop5.jpg",
    #     "assets/states/uttar_pradesh/crop6.jpg",
    # ]
}


}

# ---------------- STATE GRID ----------------
cols = st.columns(4)

for i, (state, data) in enumerate(states.items()):
    with cols[i % 4]:
        if st.button(f"📍 {state}", key=state):
            st.session_state["selected_state"] = state

        st.markdown('<div class="state-card">', unsafe_allow_html=True)
        st.image(data["image"], use_container_width=True)
        # st.markdown(f'<div class="state-title">{state}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- STATE DETAIL VIEW ----------------
if "selected_state" in st.session_state:
    state = st.session_state["selected_state"]
    data = states[state]

    st.header(f"🌾 Agriculture in {state}")
    st.image(data["image"], use_container_width=True)

    st.write(data["desc"])

    st.subheader("🚜 Major Crop Farming Areas")

    crop_cols = st.columns(3)
    for i, img in enumerate(data["crops"]):
        with crop_cols[i % 3]:
            st.image(img, use_container_width=True)

    st.success("🇮🇳 Proudly showcasing Indian Agriculture")
