import streamlit as st

st.title("📰 Agriculture News & Articles")

st.markdown(
    "Latest updates, innovations, and awareness articles related to **Indian Agriculture** 🌾"
)

st.markdown("---")

# ================= ARTICLE 1 =================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "assets/smart_farming.jpg",
        use_container_width=True
    )

with col2:
    st.subheader("🌱 Smart Farming: The Future of Indian Agriculture")
    st.write(
        """
        Smart farming uses modern technologies like AI, IoT, and data analytics
        to improve crop productivity and reduce farming risks.

        With tools like crop recommendation systems and weather forecasting,
        farmers can make informed decisions and increase yield.
        """
    )
    st.markdown("📅 *Published: July 2025*")

st.markdown("---")


# ================= ARTICLE 2 =================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1586773860418-d37222d8fce3",
        use_container_width=True
    )

with col2:
    st.subheader("🚜 Government Initiatives for Farmers in India")
    st.write(
        """
        The Indian government has launched multiple schemes to support farmers,
        including soil health cards, crop insurance, and digital agriculture platforms.

        These initiatives aim to increase farmer income and promote sustainable agriculture.
        """
    )
    st.markdown("📅 *Published: July 2025*")

st.markdown("---")

# ================= ARTICLE 3 =================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
        use_container_width=True
    )

with col2:
    st.subheader("🌦 Climate Change and Its Impact on Crops")
    st.write(
        """
        Climate change is affecting rainfall patterns, soil quality, and crop cycles.
        Farmers need climate-aware tools such as weather forecasting models
        and resilient crop planning to overcome these challenges.
        """
    )
    st.markdown("📅 *Published: July 2025*")

st.markdown("---")

import streamlit as st

st.markdown("---")

# ================= ARTICLE 4 =================

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "assets/women_farmers.jpg",   # put the image in assets folder
        use_container_width=True
    )

with col2:
    st.subheader("👩‍🌾 Not Just Farmers’ Wives: The Rising Role of Women Farmers in India")

    st.write(
        """
        For many years, women working in Indian agriculture were seen only as helpers
        or farmers’ wives. However, the reality is very different. Women play a vital role
        in almost every agricultural activity, including sowing, transplanting, weeding,
        harvesting, and post-harvest processing.

        Despite contributing significantly to food production, women farmers often lack
        land ownership, access to credit, fair wages, and decision-making power. Their work
        remains largely unrecognized in official records and policies.

        Today, awareness programs, self-help groups, and technology-driven solutions are
        slowly empowering women in agriculture. Tools like AI-based crop recommendation
        systems, soil health analysis, and weather forecasting can help women farmers make
        informed decisions, reduce risk, and improve productivity.

        Recognizing women as farmers is essential for building an inclusive, sustainable,
        and future-ready Indian agricultural system.
        """
    )

    st.markdown("📅 *Published: July 2025*")

st.markdown("---")


st.info("📰 More agriculture-related articles will be added soon.")
