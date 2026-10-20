import streamlit as st
from crop_recommendation import recommend_crops

st.set_page_config(
    page_title="Crop Recommendation | AgriNirnay",
    page_icon="🌾",
    layout="wide"
)

# --------------------------------------------------
# ULTRA-PREMIUM DESIGN SYSTEM
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding: 1.5rem 2rem 2.5rem;
}

/* Hero Section */
.hero-banner {
    background: linear-gradient(135deg, #092819 0%, #124B2C 50%, #1A693D 100%);
    border-radius: 24px;
    padding: 36px 42px;
    margin-bottom: 24px;
    box-shadow: 0 16px 40px rgba(10, 42, 26, 0.22);
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.12);
}

.hero-banner::after {
    content: "🌱";
    position: absolute;
    right: 25px;
    bottom: -15px;
    font-size: 130px;
    opacity: 0.08;
    pointer-events: none;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.14);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 6px 14px;
    border-radius: 20px;
    color: #D3EDDA;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    color: #FFFFFF !important;
    font-size: clamp(28px, 3.2vw, 40px);
    font-weight: 800;
    letter-spacing: -0.5px;
    line-height: 1.15;
    margin: 0 0 10px;
}

.hero-sub {
    color: #E2F2E6;
    font-size: 16px;
    line-height: 1.5;
    max-width: 750px;
    margin: 0;
    opacity: 0.95;
}

/* Progress Stepper */
.stepper-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 24px;
}

.step-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 16px;
    padding: 14px 18px;
    text-align: center;
    transition: 0.2s ease;
}

.step-card-active {
    background: linear-gradient(135deg, rgba(35, 131, 75, 0.15), rgba(18, 75, 44, 0.08));
    border: 2px solid #23834B;
    border-radius: 16px;
    padding: 14px 18px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(35, 131, 75, 0.15);
}

.step-num {
    font-size: 12px;
    font-weight: 700;
    color: #23834B;
    letter-spacing: 1px;
}

.step-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--text-color);
    margin-top: 2px;
}

/* Farm Context Bar */
.context-pill-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 12px 0 24px;
}

.context-pill {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 20px;
    padding: 8px 16px;
    font-size: 13px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

.context-pill b {
    color: #1a6338;
}

/* Spotlight Recommended Crop Card */
.spotlight-card {
    background: var(--secondary-background-color);
    border: 2px solid #23834B;
    border-radius: 24px;
    padding: 34px 38px;
    box-shadow: 0 16px 45px rgba(27, 101, 59, 0.12);
    position: relative;
    margin-top: 10px;
    margin-bottom: 25px;
}

.spotlight-ribbon {
    position: absolute;
    top: 24px;
    right: 28px;
    background: linear-gradient(135deg, #1b6d3b 0%, #2e8b4e 100%);
    color: #FFFFFF;
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 14px;
    padding: 8px 18px;
    border-radius: 30px;
    box-shadow: 0 6px 18px rgba(27, 109, 59, 0.35);
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.crop-name-title {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(30px, 3.8vw, 44px);
    font-weight: 900;
    color: #104226;
    letter-spacing: -0.5px;
    margin: 8px 0 12px;
}

.crop-badge-category {
    background: rgba(35, 131, 75, 0.14);
    color: #124B2A;
    font-weight: 700;
    font-size: 13px;
    padding: 5px 14px;
    border-radius: 20px;
    display: inline-block;
}

/* Metric Display Cards */
.metric-box {
    background: rgba(128, 128, 128, 0.06);
    border: 1px solid rgba(128, 128, 128, 0.18);
    border-radius: 18px;
    padding: 20px 18px;
    text-align: center;
    height: 100%;
    transition: transform 0.2s ease;
}

.metric-box:hover {
    transform: translateY(-3px);
}

.metric-box-highlight {
    background: linear-gradient(145deg, rgba(35, 131, 75, 0.14) 0%, rgba(20, 80, 47, 0.06) 100%);
    border: 2px solid #23834B;
    border-radius: 18px;
    padding: 20px 18px;
    text-align: center;
    height: 100%;
    box-shadow: 0 8px 24px rgba(35, 131, 75, 0.12);
}

.metric-caption {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    opacity: 0.75;
    margin-bottom: 6px;
}

.metric-num {
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
    font-weight: 800;
    color: #124B2A;
    margin-bottom: 4px;
}

.metric-sub {
    font-size: 12px;
    opacity: 0.8;
}

/* Suitability Breakdown Bar */
.suit-bar-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    gap: 14px;
}

.suit-label {
    width: 220px;
    font-size: 13px;
    font-weight: 600;
    color: var(--text-color);
}

.suit-track {
    flex-grow: 1;
    background: rgba(128, 128, 128, 0.15);
    height: 10px;
    border-radius: 10px;
    overflow: hidden;
}

.suit-fill {
    background: linear-gradient(90deg, #278C53, #155B32);
    height: 100%;
    border-radius: 10px;
}

.suit-pct {
    width: 50px;
    font-size: 13px;
    font-weight: 700;
    color: #155B32;
    text-align: right;
}

/* Reason Pill Tags */
.reason-chip {
    background: rgba(46, 139, 87, 0.12);
    border: 1px solid rgba(46, 139, 87, 0.25);
    color: var(--text-color);
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 500;
    margin-right: 8px;
    margin-bottom: 8px;
    display: inline-block;
}

/* Styled Action Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #1B653B 0%, #278C53 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px;
    min-height: 50px;
    font-size: 15px;
    font-weight: 700;
    box-shadow: 0 6px 20px rgba(27, 101, 59, 0.26);
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(27, 101, 59, 0.38);
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO HEADER BANNER
# --------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">🌾 &nbsp; AGRINIRNAY · INTELLIGENT CROP ADVISORY</div>
    <div class="hero-title">Your Optimal Crop Match</div>
    <div class="hero-sub">The single top-performing crop scientifically matched to your farm's district climate, seasonal rainfall, water availability, and soil health.</div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROGRESS STEPPER
# --------------------------------------------------
st.markdown("""
<div class="stepper-container">
    <div class="step-card">
        <div class="step-num">STEP 1</div>
        <div class="step-title">✓ Farm Details</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 2</div>
        <div class="step-title">✓ Soil Health</div>
    </div>
    <div class="step-card-active">
        <div class="step-num" style="color:#124B2A;">STEP 3 · ACTIVE</div>
        <div class="step-title" style="color:#124B2A;">🎯 Recommended Crop</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD FARM CONTEXT
# --------------------------------------------------
farm_details = st.session_state.get("farm_details", {})
soil_details = st.session_state.get("soil_details", {})

district = farm_details.get("district", "Mandya")
season = farm_details.get("season", "Kharif")
land_area = float(farm_details.get("land_area", 1.0))
water_availability = farm_details.get("water_availability", "Moderate")

soil_type = soil_details.get("soil_type", "Red Loam / Red Soil")
ph = soil_details.get("ph", 6.8)
nitrogen = soil_details.get("nitrogen", 280.0)
phosphorus = soil_details.get("phosphorus", 35.0)
potassium = soil_details.get("potassium", 240.0)

# High-Contrast Farm Overview Display
st.markdown(f"""
<div style="background: #FFFFFF; border: 2px solid #23834B; border-radius: 20px; padding: 22px 26px; margin: 20px 0 26px; box-shadow: 0 8px 26px rgba(27, 101, 59, 0.08);">
    <div style="font-size: 12px; font-weight: 800; letter-spacing: 2px; color: #155B32; text-transform: uppercase; margin-bottom: 14px;">
        🚜 ACTIVE FARM PARAMETERS EVALUATED
    </div>
    <div style="display: flex; flex-wrap: wrap; gap: 12px;">
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            📍 District: <span style="color: #155B32; font-weight: 800;">{district}</span>
        </div>
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            🗓️ Season: <span style="color: #155B32; font-weight: 800;">{season}</span>
        </div>
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            🌾 Land Size: <span style="color: #155B32; font-weight: 800;">{land_area} Acres</span>
        </div>
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            💧 Water: <span style="color: #155B32; font-weight: 800;">{water_availability}</span>
        </div>
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            🧪 Soil: <span style="color: #155B32; font-weight: 800;">{soil_type}</span>
        </div>
        <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
            ⚗️ pH: <span style="color: #155B32; font-weight: 800;">{ph:.1f}</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# RECOMMENDATION ENGINE EXECUTION
# --------------------------------------------------
recommendations = recommend_crops(
    district=district,
    season=season,
    water_availability=water_availability,
    soil_type=soil_type,
    ph=ph,
    nitrogen=nitrogen,
    phosphorus=phosphorus,
    potassium=potassium,
)

if not recommendations:
    st.error("No suitable crops identified. Please revise your farm parameters.")
    st.stop()

# Single Top #1 Recommendation
top_crop = recommendations[0]

# Alternative suitable crop switcher (strictly one crop displayed at a time)
alternative_names = [r["crop"] for r in recommendations if r["score"] >= 65]
if not alternative_names:
    alternative_names = [top_crop["crop"]]

st.markdown("### 🎯 Single Crop Focus")

col_pick, col_hint = st.columns([2.2, 1])

with col_pick:
    selected_crop_name = st.selectbox(
        "Currently viewing (defaulting to the #1 top-scoring match for your land):",
        alternative_names,
        index=0,
        help="Select any other eligible crop to display its dedicated report."
    )

with col_hint:
    st.caption("✨ Focused on **exactly one crop** to keep your planning simple, clear, and actionable.")

active_crop = next((r for r in recommendations if r["crop"] == selected_crop_name), top_crop)

# Keep active crop synchronized across entire app!
st.session_state["selected_crop"] = active_crop["crop"]


# --------------------------------------------------
# SPOTLIGHT: THE SINGLE RECOMMENDED CROP CARD
# --------------------------------------------------
total_yield = round(active_crop['expected_yield'] * land_area, 1)
total_cost = round(active_crop['cultivation_cost_per_acre'] * land_area, 0)
total_profit = round(active_crop['net_profit_per_acre'] * land_area, 0)

st.markdown(f"""
<div class="spotlight-card">
    <div class="spotlight-ribbon">⭐ {active_crop['score']}% MATCH · {active_crop['badge'].upper()}</div>
    <div style="font-size: 13px; font-weight: 800; letter-spacing: 2px; color: #278C53; text-transform: uppercase;">
        👑 AI #1 RECOMMENDED CROP FOR {district.upper()}
    </div>
    <div class="crop-name-title">{active_crop['crop']}</div>
    <div style="margin-bottom: 22px;">
        <span class="crop-badge-category">{active_crop['category']}</span>
        <span style="font-size: 14px; opacity: 0.85; margin-left: 12px;">⏱️ Crop Duration: <b>{active_crop['duration']}</b></span>
        <span style="font-size: 14px; opacity: 0.85; margin-left: 12px;">🏛️ Primary Mandi: <b>{active_crop['market_apmc']}</b></span>
    </div>
""", unsafe_allow_html=True)

# 4 Core KPI Tiles
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-caption">⚖️ Expected Yield</div>
        <div class="metric-num">{active_crop['expected_yield']} Qtl</div>
        <div class="metric-sub">Per Acre · Total: <b>{total_yield} Qtl</b></div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-caption">🏷️ Local Mandi Rate</div>
        <div class="metric-num" style="color:#1b6d3b;">₹{active_crop['modal_price']:,}</div>
        <div class="metric-sub">Per Quintal ({district} APMC)</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-caption">🧾 Cultivation Cost</div>
        <div class="metric-num" style="color:#b91c1c;">₹{active_crop['cultivation_cost_per_acre']:,}</div>
        <div class="metric-sub">Per Acre · Total: <b>₹{total_cost:,.0f}</b></div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-box-highlight">
        <div class="metric-caption" style="color:#124B2A; font-weight:800;">💰 Projected Net Profit</div>
        <div class="metric-num" style="color:#155B32; font-size:26px;">₹{active_crop['net_profit_per_acre']:,}</div>
        <div class="metric-sub" style="color:#155B32; font-weight:700;">Total: ₹{total_profit:,.0f} (ROI: +{active_crop['roi']}%)</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)


# --------------------------------------------------
# SUITABILITY ATTRIBUTE BREAKDOWN BARS
# --------------------------------------------------
st.markdown("#### 📊 Farm Fitment Analysis")

# Realistic calculated factor percentages
dist_fit = 100 if active_crop["is_native"] else 75
season_fit = 100 if active_crop["season"].lower() == season.lower() else 85
water_fit = 95 if (water_availability.lower() == "high" or active_crop["water_requirement"].lower() == water_availability.lower()) else 80
soil_fit = 95

factors = [
    ("📍 District Climate & Geography", dist_fit),
    ("🗓️ Sowing Window & Season Compatibility", season_fit),
    ("💧 Water Supply & Irrigation Fit", water_fit),
    ("🧪 Soil Texture & Nutrient Alignment", soil_fit)
]

for label, pct in factors:
    st.markdown(f"""
    <div class="suit-bar-row">
        <div class="suit-label">{label}</div>
        <div class="suit-track">
            <div class="suit-fill" style="width: {pct}%;"></div>
        </div>
        <div class="suit-pct">{pct}%</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

# Suitability Reasons Tags
st.markdown("#### 💡 Key Agronomic Advantages")
chips_html = "".join([f"<span class='reason-chip'>✓ {r}</span>" for r in active_crop["reasons"]])
st.markdown(f"<div>{chips_html}</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

# Comprehensive Agronomic Guide Accordion
with st.expander(f"📖 Complete Agronomic & Management Guide for {active_crop['crop']}", expanded=True):
    st.markdown(f"**Field Advisory:** {active_crop['notes']}")
    g1, g2 = st.columns(2)
    with g1:
        st.write(f"💧 **Water Requirement:** {active_crop['water_requirement']}")
        st.write(f"🧪 **Optimal Soil Type:** {active_crop['soil_type']}")
    with g2:
        st.write(f"🏛️ **Primary APMC Mandi:** {active_crop['market_apmc']}")
        st.write(f"⚠️ **Risk Category:** {active_crop['risk_level']}")

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

# Direct Action Buttons for This Recommended Crop
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button(f"📊 Plan Full Financials & ROI for {active_crop['crop']} →", use_container_width=True):
        st.session_state["selected_crop"] = active_crop["crop"]
        st.switch_page("pages/6_Cost_and_Revenue.py")

with btn_col2:
    if st.button(f"📈 Check Daily APMC Mandi Rates for {active_crop['crop']} →", use_container_width=True):
        st.session_state["selected_crop"] = active_crop["crop"]
        st.session_state["market_filter_crop"] = active_crop["crop"]
        st.switch_page("pages/5_Market_Prices.py")

st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# NAVIGATION FOOTER
# --------------------------------------------------
st.markdown("---")
b_left, b_right = st.columns(2)

with b_left:
    if st.button("← Back to Soil Parameters", use_container_width=True):
        st.switch_page("pages/2_Soil_Report.py")

with b_right:
    if st.button("Calculate Farm Finances (Cost & Revenue) →", use_container_width=True):
        st.switch_page("pages/6_Cost_and_Revenue.py")

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)