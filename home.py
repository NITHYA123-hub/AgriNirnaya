import streamlit as st

st.set_page_config(
    page_title="AgriNirnay | Smart Crop Planning",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

#MainMenu, footer, [data-testid="stHeader"] {
    visibility: hidden;
}

.stApp {
    background: #FAF9F3;
    color: #173D2B;
}

.block-container {
    max-width: 1350px;
    padding: 1.2rem 2.5rem 2rem;
}

/* Header & Brand */
.brand {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 6px 0 20px;
    border-bottom: 1px solid #E2E8D8;
    margin-bottom: 24px;
}

.brand-icon {
    font-size: 40px;
    filter: drop-shadow(0 4px 10px rgba(35, 131, 75, 0.25));
}

.brand-name {
    font-family: 'Outfit', sans-serif;
    font-size: 32px;
    font-weight: 900;
    color: #104026;
    letter-spacing: -1px;
    line-height: 1;
}

.brand-tag {
    color: #627A68;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    margin-top: 3px;
}

/* Hero Section */
.hero-wrapper {
    background: linear-gradient(135deg, #092819 0%, #124B2C 55%, #1B6D3E 100%);
    border-radius: 28px;
    padding: 44px 48px;
    margin-bottom: 30px;
    box-shadow: 0 20px 50px rgba(9, 40, 25, 0.22);
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: white;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 6px 16px;
    border-radius: 30px;
    color: #D3EDDA;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.hero-heading {
    font-family: 'Outfit', sans-serif;
    color: #FFFFFF !important;
    font-size: clamp(34px, 4.2vw, 54px);
    font-weight: 900;
    line-height: 1.08;
    letter-spacing: -1px;
    margin: 0 0 16px;
}

.hero-subheading {
    color: #E2F2E6;
    font-size: 18px;
    line-height: 1.6;
    max-width: 650px;
    margin-bottom: 24px;
    opacity: 0.95;
}

.hero-stats-row {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    margin-top: 24px;
    padding-top: 22px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
}

.hero-stat-item {
    font-size: 14px;
    color: #E2F2E6;
    display: flex;
    align-items: center;
    gap: 8px;
}

.hero-stat-item b {
    color: #FFFFFF;
    font-size: 16px;
}

/* Feature Cards */
.section-heading {
    font-family: 'Outfit', sans-serif;
    color: #124027;
    font-size: 26px;
    font-weight: 800;
    margin: 28px 0 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.feature-box {
    background: #FFFFFF;
    border: 1px solid #E1E9DD;
    border-radius: 20px;
    padding: 24px 20px;
    box-shadow: 0 8px 24px rgba(18, 63, 42, 0.04);
    transition: all 0.25s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.feature-box:hover {
    transform: translateY(-5px);
    border-color: #23834B;
    box-shadow: 0 14px 34px rgba(35, 131, 75, 0.12);
}

.feature-icon-wrapper {
    background: linear-gradient(135deg, #EDF6EE 0%, #DFF0E1 100%);
    width: 58px;
    height: 58px;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    margin-bottom: 16px;
    border: 1px solid rgba(35, 131, 75, 0.15);
}

.feature-title {
    font-family: 'Outfit', sans-serif;
    color: #14492B;
    font-size: 18px;
    font-weight: 800;
    margin: 0 0 8px;
}

.feature-desc {
    color: #5D7264;
    font-size: 13.5px;
    line-height: 1.5;
    margin: 0;
}

/* Styled Action Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #1B653B 0%, #278C53 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px;
    min-height: 48px;
    font-size: 15px;
    font-weight: 700;
    box-shadow: 0 6px 20px rgba(27, 101, 59, 0.26);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(27, 101, 59, 0.38);
}

.footer-banner {
    background: #103322;
    color: #D3EDDA;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin-top: 35px;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BRAND HEADER
# --------------------------------------------------
st.markdown("""
<div class="brand">
    <div class="brand-icon">🌿</div>
    <div>
        <div class="brand-name">AgriNirnay</div>
        <div class="brand-tag">SMART CROP PLANNING & FINANCIAL INTELLIGENCE</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO BANNER
# --------------------------------------------------
h_left, h_right = st.columns([1.2, 0.8], gap="large")

with h_left:
    st.markdown("""
    <div class="hero-wrapper">
        <div class="hero-eyebrow">🌱 &nbsp; DATA-DRIVEN AGRICULTURE FOR KARNATAKA</div>
        <div class="hero-heading">
            Make Smarter,<br>Higher-Yield Crop Decisions.
        </div>
        <div class="hero-subheading">
            Scientific soil matching, live APMC mandi prices, weather forecasts, and revenue modeling designed specifically for farmers across Karnataka.
        </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Start Crop Planning Workflow →", key="hero_start_btn", use_container_width=True):
        st.switch_page("pages/1_Farm_Details.py")
with h_right:
    st.markdown("""
    <div style="padding-top: 10px;">
        <img style="width:100%; height:370px; object-fit:cover; border-radius:28px; box-shadow: 0 16px 40px rgba(18,63,42,0.18);"
             src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
             alt="Lush green Karnataka crop fields at sunrise">
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FEATURE SECTION
# --------------------------------------------------
st.markdown('<div class="section-heading">🌟 Explore AgriNirnay Features</div>', unsafe_allow_html=True)

features = [
    ("🧪", "Soil Health",
     "Lab test card OCR reader for pH & N-P-K nutrient status.",
     "pages/2_Soil_Report.py", "Soil Insights"),
    ("🌾", "AI Crop Match",
     "Scientific single-crop recommendations tailored to your land.",
     "pages/3_Crop_Recommendations.py", "Recommended Crop"),
    ("🌦️", "Weather Forecast",
     "Hyper-local weather conditions and 3-day rainfall updates.",
     "pages/4_Weather.py", "Live Weather"),
    ("📈", "APMC Mandis",
     "Real-time benchmark modal prices across all 31 districts.",
     "pages/5_Market_Prices.py", "Mandi Rates"),
    ("💰", "ROI & Profit",
     "Interactive cost breakdown, yield sliders, and revenue modeling.",
     "pages/6_Cost_and_Revenue.py", "Plan Finances")
]

cols = st.columns(5, gap="medium")

for col, (icon, title, description, target_page, btn_text) in zip(cols, features):
    with col:
        st.markdown(f"""
        <div class="feature-box">
            <div>
                <div class="feature-icon-wrapper">{icon}</div>
                <div class="feature-title">{title}</div>
                <p class="feature-desc">{description}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        if st.button(f"{btn_text} →", key=f"home_feat_{target_page}", use_container_width=True):
            st.switch_page(target_page)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer-banner">
    AGRINIRNAY &nbsp; · &nbsp; DATA-DRIVEN AGRICULTURE &nbsp; · &nbsp; SFIC 2026
</div>
""", unsafe_allow_html=True)
