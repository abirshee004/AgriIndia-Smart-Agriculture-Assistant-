import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Farmer Business Hub",
    page_icon="🚜",
    layout="wide"
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
st.markdown("""
<style>

.main{
    background-color:#f5fff5;
}

.hero{
    background:linear-gradient(90deg,#2E7D32,#66BB6A);
    padding:30px;
    border-radius:20px;
    color:white;
    text-align:center;
}

.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,.15);
    margin-bottom:20px;
}

.section{
    color:#1B5E20;
}

</style>
""",unsafe_allow_html=True)

# ----------------------------------------------------
# HERO
# ----------------------------------------------------
st.markdown("""
<div class="hero">
<h1>🌾 Farmer Market Connect</h1>

<h3>
Sell Smarter • Earn More • Reduce Middlemen
</h3>

<p style="font-size:20px;">
Helping Indian Farmers Connect with Buyers,
Government Platforms,
Export Opportunities
and Modern Agricultural Markets.
</p>

</div>
""",unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# WHY FARMERS LOSE MONEY
# ----------------------------------------------------
st.markdown("<h2 class='section'>❓ Why Do Farmers Lose Profit?</h2>",unsafe_allow_html=True)

col1,col2=st.columns([2,1])

with col1:

    st.markdown("""
### Major Problems Faced by Farmers

- ❌ Dependence on middlemen
- ❌ No information about current market prices
- ❌ Lack of direct buyers
- ❌ High transportation costs
- ❌ Poor storage facilities
- ❌ No export awareness
- ❌ Limited digital knowledge
- ❌ Low bargaining power

These issues often force farmers to sell their crops
at prices lower than the actual market value.
""")

with col2:

    st.info("""
### Example

Farmer sells rice

₹2200 / Quintal

↓

Middleman sells

₹2800 / Quintal

↓

Farmer loses ₹600

per Quintal.
""")

st.divider()

# ----------------------------------------------------
# OUR SOLUTION
# ----------------------------------------------------
st.markdown("<h2 class='section'>✅ AgriIndia Solution</h2>",unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:
    st.success("""
### 📈 AI Prediction

✔ Crop Recommendation

✔ Disease Detection

✔ Weather Forecast

✔ Market Price Prediction
""")

with col2:
    st.success("""
### 🤝 Market Connect

✔ Direct Buyers

✔ eNAM

✔ FPO

✔ Wholesale Markets

✔ Retail Chains
""")

with col3:
    st.success("""
### 🌍 Future Goal

✔ Export Guidance

✔ Online Selling

✔ Digital Payments

✔ Farmer Marketplace
""")

st.divider()

# ----------------------------------------------------
# GOVERNMENT PLATFORMS
# ----------------------------------------------------
st.markdown("<h2 class='section'>🏛 Government Platforms</h2>",unsafe_allow_html=True)

c1,c2=st.columns(2)

with c1:

    st.markdown("""
### 🌾 eNAM

National Agriculture Market

• Sell through digital mandis

• Transparent pricing

• Nationwide buyers

🔗 https://enam.gov.in
""")

    st.link_button(
        "Open eNAM",
        "https://enam.gov.in"
    )

with c2:

    st.markdown("""
### 📊 AGMARKNET

Daily mandi prices

• Compare prices

• Check nearby markets

• Plan better selling

🔗 https://agmarknet.gov.in
""")

    st.link_button(
        "Open AGMARKNET",
        "https://agmarknet.gov.in"
    )

st.write("")

c3,c4=st.columns(2)

with c3:

    st.markdown("""
### 🌍 APEDA

Agricultural Export

• Export registration

• Export guidelines

• International buyers
""")

    st.link_button(
        "Open APEDA",
        "https://apeda.gov.in"
    )

with c4:

    st.markdown("""
### 👨‍🌾 PM-KISAN

Government Support

• Income support

• Farmer benefits

• Registration
""")

    st.link_button(
        "Open PM-KISAN",
        "https://pmkisan.gov.in"
    )

st.divider()


# =====================================================
# EXPORT GUIDE
# =====================================================

st.markdown("<h2 class='section'>🌍 Export Your Agricultural Products</h2>", unsafe_allow_html=True)

st.info("""
India exports rice, mango, spices, tea, coffee, vegetables,
fruits and many agricultural products worldwide.

AgriIndia encourages farmers to understand export opportunities
and connect with certified exporters.
""")

st.markdown("""
### 📋 Export Process

1️⃣ Produce high-quality crops

⬇️

2️⃣ Grade and package properly

⬇️

3️⃣ Register through APEDA

⬇️

4️⃣ Find Export Buyers

⬇️

5️⃣ Complete Documentation

⬇️

6️⃣ Export Internationally
""")

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🌍 APEDA Registration",
        "https://apeda.gov.in"
    )

with col2:
    st.link_button(
        "📑 DGFT Registration",
        "https://dgft.gov.in"
    )

st.divider()

# =====================================================
# FPO
# =====================================================

st.markdown("<h2 class='section'>🤝 Join Farmer Producer Organization (FPO)</h2>", unsafe_allow_html=True)

st.success("""
Farmer Producer Organizations help farmers sell products together.

Benefits:

✅ Better market prices

✅ Bulk selling

✅ Reduced transportation cost

✅ Better bargaining power

✅ Easy access to loans

✅ Government support
""")

st.link_button(
    "🔗 Learn About FPO",
    "https://sfacindia.com"
)

st.divider()

# =====================================================
# PACKAGING
# =====================================================

st.markdown("<h2 class='section'>📦 Packaging & Grading</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Good Packaging

✔ Clean bags

✔ Proper labels

✔ Moisture protection

✔ Strong packaging

✔ Fresh produce
""")

with col2:

    st.warning("""
### Avoid

❌ Torn bags

❌ Wet packaging

❌ Mixed quality

❌ Damaged vegetables

❌ Dirty containers
""")

st.divider()

# =====================================================
# TRANSPORT
# =====================================================

st.markdown("<h2 class='section'>🚚 Transportation Tips</h2>", unsafe_allow_html=True)

st.markdown("""

Before sending products to market:

✅ Compare transport costs

✅ Choose nearest mandi

✅ Use refrigerated transport for fruits

✅ Avoid overloading

✅ Pack carefully

✅ Check weather before transport

""")

st.divider()

# =====================================================
# DIGITAL PAYMENT
# =====================================================

st.markdown("<h2 class='section'>💳 Secure Digital Payments</h2>", unsafe_allow_html=True)

st.info("""

Receive payments safely through

✔ UPI

✔ Bank Transfer

✔ RuPay

✔ Digital Banking

Avoid cash transactions with unknown buyers.

""")

st.divider()

# =====================================================
# DIRECT SELLING
# =====================================================

st.markdown("<h2 class='section'>🏪 Sell Directly Without Middlemen</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 🛒 Retail Shops

Sell directly to

✔ Grocery Shops

✔ Vegetable Stores

✔ Fruit Markets
""")

with col2:
    st.success("""
### 🏨 Hotels

Supply directly to

✔ Hotels

✔ Restaurants

✔ Caterers

✔ Hostels
""")

with col3:
    st.success("""
### 🏭 Industries

Sell to

✔ Rice Mills

✔ Food Processing

✔ Juice Factory

✔ Export Companies
""")

st.divider()

# =====================================================
# LEARNING VIDEOS
# =====================================================

st.markdown("<h2 class='section'>🎥 Learn Through Videos</h2>", unsafe_allow_html=True)

st.write("### 📺 How eNAM Works")

st.video("https://www.youtube.com/watch?v=HqkKxPVj8oE")

st.write("### 📺 Agricultural Export Guide")

st.video("https://www.youtube.com/watch?v=VJx3htxpINo")

st.write("### 📺 Modern Farming Techniques")

st.video("https://www.youtube.com/watch?v=tKGSZrgVkoo")

st.divider()

# =====================================================
# USEFUL WEBSITES
# =====================================================

st.markdown("<h2 class='section'>🌐 Useful Agricultural Websites</h2>", unsafe_allow_html=True)

websites = {
    "🌾 eNAM":"https://enam.gov.in",
    "📈 AGMARKNET":"https://agmarknet.gov.in",
    "🌍 APEDA":"https://apeda.gov.in",
    "👨‍🌾 PM KISAN":"https://pmkisan.gov.in",
    "🤝 SFAC (FPO)":"https://sfacindia.com",
    "🏛 ICAR":"https://icar.org.in",
    "🌱 Ministry of Agriculture":"https://agriwelfare.gov.in"
}

for name, link in websites.items():
    st.link_button(name, link)

st.divider()

# =====================================================
# PROFIT CALCULATOR
# =====================================================

st.markdown("<h2 class='section'>💰 Farmer Profit Calculator</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    production_cost = st.number_input(
        "Production Cost (₹)",
        min_value=0.0,
        value=50000.0
    )

    transport_cost = st.number_input(
        "Transport Cost (₹)",
        min_value=0.0,
        value=5000.0
    )

with col2:
    quantity = st.number_input(
        "Quantity (Quintal)",
        min_value=1.0,
        value=100.0
    )

    selling_price = st.number_input(
        "Selling Price per Quintal (₹)",
        min_value=0.0,
        value=2500.0
    )

if st.button("Calculate Profit"):

    revenue = quantity * selling_price

    total_cost = production_cost + transport_cost

    profit = revenue - total_cost

    st.metric("Total Revenue", f"₹ {revenue:,.2f}")

    st.metric("Total Cost", f"₹ {total_cost:,.2f}")

    if profit >= 0:
        st.success(f"✅ Expected Profit : ₹ {profit:,.2f}")
    else:
        st.error(f"❌ Expected Loss : ₹ {abs(profit):,.2f}")

st.divider()

# =====================================================
# SMART SELLING TIPS
# =====================================================

st.markdown("<h2 class='section'>📈 Smart Selling Tips</h2>", unsafe_allow_html=True)

st.success("""
✔ Compare mandi prices before selling.

✔ Check weather before transportation.

✔ Sell through FPO whenever possible.

✔ Use digital payment.

✔ Grade products before selling.

✔ Store crops if prices are very low.

✔ Use AgriIndia Market Price Prediction.

✔ Compare nearby mandi prices.

✔ Keep invoices and payment receipts.

✔ Avoid distress selling.
""")

st.divider()

# =====================================================
# HELPLINE
# =====================================================

st.markdown("<h2 class='section'>☎ Farmer Helpline</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
📞 Kisan Call Centre

1800-180-1551
""")

with c2:
    st.info("""
🌱 PM Kisan

https://pmkisan.gov.in
""")

with c3:
    st.info("""
🌾 Agriculture Ministry

https://agriwelfare.gov.in
""")

st.divider()

# =====================================================
# FAQ
# =====================================================

st.markdown("<h2 class='section'>❓ Frequently Asked Questions</h2>", unsafe_allow_html=True)

with st.expander("How can I sell without middlemen?"):
    st.write("""
Register on eNAM, join an FPO, or connect directly with buyers,
retailers, hotels, supermarkets, and exporters.
""")

with st.expander("How do I know today's market price?"):
    st.write("""
Use AgriIndia Market Price Prediction and verify prices using AGMARKNET.
""")

with st.expander("Can small farmers export products?"):
    st.write("""
Yes. Farmers can export individually or through FPOs after completing
APEDA registration and quality requirements.
""")

with st.expander("Why should I join an FPO?"):
    st.write("""
FPOs improve bargaining power, reduce transport costs,
enable bulk selling, and increase access to government support.
""")

st.divider()

# =====================================================
# SUCCESS STORY
# =====================================================

st.markdown("<h2 class='section'>🌟 Success Story</h2>", unsafe_allow_html=True)

st.success("""
A farmer producing 100 quintals of rice sold directly through
an FPO instead of using a middleman.

Middleman Price:
₹2,100 per quintal

Direct Buyer Price:
₹2,550 per quintal

Additional Income:
₹45,000

This demonstrates how better market access can significantly
improve farmers' earnings.
""")

st.divider()

# =====================================================
# MOTIVATION
# =====================================================

st.markdown("""
<div style="
background:#2E7D32;
padding:25px;
border-radius:15px;
text-align:center;
color:white;
">

<h2>🌾 Empower Farmers • Strengthen Agriculture • Build India 🇮🇳</h2>

<p style="font-size:20px;">
AgriIndia is not just an AI platform.
It is a step toward helping farmers make informed decisions,
reduce losses, and improve income through technology.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption("""
Developed as part of the **AgriIndia – Smart Agriculture Platform**.

Modules Included:
- 🌾 Crop Recommendation
- 🦠 Crop Disease Detection
- 🌦 Weather Forecasting
- 💰 Market Price Prediction
- 🤝 Farmer Market Connect
- 🤖 AI Chatbot (Future Enhancement)

© 2026 AgriIndia Project
""")