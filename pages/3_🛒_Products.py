import streamlit as st

st.title("🛒 AgriGuru Store – Smart Farming Products")

st.write("High-quality tools to help Indian farmers adopt smart agriculture 🇮🇳")
st.markdown("---")

# ---------------- PRODUCT 1 ----------------
col1, col2 = st.columns([1.4, 2])

with col1:
    st.image("assets/ph_meter.jpg",  use_container_width=True)

with col2:
    st.subheader("🌱 Digital Soil pH Meter")
    st.write("💰 **Price:** ₹799")
    st.markdown("""
    **Features:**
    - Instant soil pH testing  
    - No battery required  
    - Helps select the right crop  
    - Easy to use for farmers  
    """)
    st.markdown(
        "[🛒 Buy on Amazon](https://www.amazon.in/s?k=soil+ph+meter) | "
        "[🛍 Buy on Flipkart](https://www.flipkart.com/search?q=soil+ph+meter)"
    )

st.markdown("---")

# ---------------- PRODUCT 2 ----------------
col1, col2 = st.columns([1.4, 2])

with col1:
    st.image("assets/moisture_meter.jpg",  use_container_width=True)

with col2:
    st.subheader("💧 Soil Moisture Meter")
    st.write("💰 **Price:** ₹999")
    st.markdown("""
    **Features:**
    - Measures soil moisture level  
    - Prevents over-watering  
    - Improves irrigation efficiency  
    - Suitable for all crops  
    """)
    st.markdown(
        "[🛒 Buy on Amazon](https://www.amazon.in/s?k=soil+moisture+meter) | "
        "[🛍 Buy on Flipkart](https://www.flipkart.com/search?q=soil+moisture+meter)"
    )

st.markdown("---")

# ---------------- PRODUCT 3 ----------------
col1, col2 = st.columns([1.4, 2])

with col1:
    st.image("assets/compost_kit.jpg",  use_container_width=True)

with col2:
    st.subheader("🌿 Organic Compost Making Kit")
    st.write("💰 **Price:** ₹1,299")
    st.markdown("""
    **Features:**
    - Converts organic waste into natural compost  
    - Improves soil fertility and crop yield  
    - Eco-friendly and chemical-free  
    - Easy to use for farmers and households  
    """)
    st.markdown(
        "[🛒 Buy on Amazon](https://www.amazon.in/s?k=organic+compost+kit) | "
        "[🛍 Buy on Flipkart](https://www.flipkart.com/search?q=compost+kit)"
    )

st.markdown("---")



# ---------------- PRODUCT 4 ----------------
col1, col2 = st.columns([1.3, 2])

with col1:
    st.image("assets/sprayer.jpg",  use_container_width=True)

with col2:
    st.subheader("🚜 Battery Operated Sprayer")
    st.write("💰 **Price:** ₹3,999")
    st.markdown("""
    **Features:**
    - Reduces farmer effort  
    - Uniform pesticide spraying  
    - Rechargeable battery  
    - Suitable for large fields  
    """)
    st.markdown(
        "[🛒 Buy on Amazon](https://www.amazon.in/s?k=battery+sprayer+for+agriculture) | "
        "[🛍 Buy on Flipkart](https://www.flipkart.com/search?q=battery+sprayer)"
    )

st.markdown("---")

st.success("🌾 Smart tools for Smart Indian Farming 🇮🇳")
