import streamlit as st

st.set_page_config(
    page_title="Farm Details | AgriNirnay",
    page_icon="🌱",
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
    max-width: 1150px;
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
    content: "🚜";
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

/* Form card */
[data-testid="stForm"] {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.25);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 30px rgba(25, 65, 38, 0.05);
}

/* Tip box */
.tip-callout {
    background: rgba(46, 139, 87, 0.12);
    border-left: 4px solid #23834B;
    padding: 16px 20px;
    border-radius: 12px;
    color: var(--text-color);
    margin: 16px 0;
    line-height: 1.6;
}

/* Styled Action Buttons */
div.stButton > button,
div.stFormSubmitButton > button {
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

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(27, 101, 59, 0.38);
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO BANNER
# --------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">🚜 &nbsp; STEP 1 · FARM BASELINE PARAMETERS</div>
    <div class="hero-title">Tell Us About Your Farm</div>
    <div class="hero-sub">Enter your land size, agro-climatic district, and seasonal water availability to discover tailored crop recommendations.</div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROGRESS INDICATOR
# --------------------------------------------------
st.markdown("""
<div class="stepper-container">
    <div class="step-card-active">
        <div class="step-num" style="color:#124B2A;">STEP 1 · ACTIVE</div>
        <div class="step-title" style="color:#124B2A;">① Farm Details</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 2</div>
        <div class="step-title">② Soil Report</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 3</div>
        <div class="step-title">③ Recommended Crop</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FARM INFORMATION FORM
# --------------------------------------------------
st.markdown("## 🚜 Farm Information Form")

with st.form("farm_details_form"):

    st.markdown("### 📍 Location & Geography")

    district = st.selectbox(
        "Karnataka District",
        [
            "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban",
            "Bidar", "Chamarajanagar", "Chikkaballapur", "Chikkamagaluru", "Chitradurga",
            "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Hassan",
            "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal",
            "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga",
            "Tumakuru", "Udupi", "Uttara Kannada", "Vijayanagara", "Vijayapura", "Yadgir"
        ],
        index=20,  # Mandya default
        key="farm_district_input"
    )

    st.markdown("### 🌾 Farm Size & Sowing Season")

    col1, col2 = st.columns(2)

    with col1:
        land_area = st.number_input(
            "Farm Land Size (Acres)",
            min_value=0.1,
            max_value=10000.0,
            value=1.0,
            step=0.5,
            key="farm_land_area_input"
        )

    with col2:
        season = st.selectbox(
            "Target Growing Season",
            ["Kharif", "Rabi", "Summer"],
            index=0,
            key="farm_season_input"
        )

    st.markdown("### 💧 Irrigation & Water Supply")

    water_availability = st.radio(
        "Available Irrigation Water Level",
        ["Low", "Moderate", "High"],
        index=1,
        horizontal=True,
        key="farm_water_input"
    )

    st.markdown("""
    <div class="tip-callout">
        💡 <b>Have a soil laboratory report?</b><br>
        You can upload a photo or PDF of your Soil Health Card on the next step. You can also proceed with standard regional soil values.
    </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "Save Farm Details & Continue to Soil Report →",
        use_container_width=True
    )


# --------------------------------------------------
# SAVE DETAILS AND NAVIGATE
# --------------------------------------------------
if submitted:
    st.session_state["farm_details"] = {
        "district": district,
        "land_area": land_area,
        "season": season,
        "water_availability": water_availability
    }

    # Clear previous upload when starting new submission
    st.session_state.pop("soil_report_file", None)
    st.switch_page("pages/2_Soil_Report.py")


if "farm_details" in st.session_state:
    details = st.session_state["farm_details"]
    st.caption(
        f"✓ Saved farm profile: **{details['district']}** · "
        f"**{details['land_area']} acres** · "
        f"**{details['season']}** season · "
        f"Water: **{details['water_availability']}**"
    )

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)
