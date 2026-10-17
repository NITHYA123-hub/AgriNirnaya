
import streamlit as st

st.set_page_config(
    page_title="Farm Details | AgriNirnay",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DESIGN — STREAMLIT THEME AWARE
# --------------------------------------------------

st.markdown("""
<style>

/* Use Streamlit's default theme background and text */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Main content spacing */
.block-container {
    max-width: 1150px;
    padding: 1.5rem 2rem 2.5rem;
}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #123F2A, #23834B);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 22px;
    box-shadow: 0 6px 20px rgba(18, 63, 42, 0.12);
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 35px;
    margin-bottom: 8px;
}

.hero p {
    color: #E4F4E8 !important;
    font-size: 16px;
}

.hero .eyebrow {
    color: #D3EDDA !important;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 600;
}

/* Progress indicator */
.step,
.step-active {
    border-radius: 14px;
    padding: 14px 8px;
    text-align: center;
    min-height: 70px;
    line-height: 1.8;
    font-size: 15px;
}

.step {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.35);
    color: var(--text-color) !important;
}

.step small {
    color: var(--text-color) !important;
    opacity: 0.8;
    font-size: 12px;
}

.step-active {
    background-color: #DDF2E2 !important;
    border: 2px solid #23834B;
    color: #124B2A !important;
    font-weight: 700;
}

.step-active small {
    color: #23633A !important;
    opacity: 1;
}

/* Form card — follows the selected Streamlit theme */
[data-testid="stForm"] {
    background-color: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.3);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 5px 22px rgba(25, 65, 38, 0.05);
}

/* Theme-aware headings and labels */
h1, h2, h3, h4,
[data-testid="stWidgetLabel"] p,
[data-testid="stRadio"] label,
[data-testid="stRadio"] p {
    color: var(--text-color);
}

/* Select boxes */
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: var(--secondary-background-color);
    border-color: rgba(128, 128, 128, 0.4);
}

[data-testid="stSelectbox"] div[data-baseweb="select"] span {
    color: var(--text-color);
}

/* Number input */
[data-testid="stNumberInput"] input {
    background-color: var(--secondary-background-color);
    color: var(--text-color);
    border-color: rgba(128, 128, 128, 0.4);
}

/* Tip box */
.tip {
    background-color: rgba(46, 139, 87, 0.13);
    color: var(--text-color);
    border-left: 4px solid #329454;
    padding: 15px;
    border-radius: 8px;
    margin: 12px 0;
    line-height: 1.7;
}

.tip b {
    color: var(--text-color);
}

/* Buttons */
div.stButton > button,
div.stFormSubmitButton > button {
    background-color: #207744 !important;
    color: #FFFFFF !important;
    border: 1px solid #207744 !important;
    border-radius: 10px;
    min-height: 48px;
    font-weight: 600;
    transition: 0.2s ease;
}

div.stButton > button p,
div.stFormSubmitButton > button p {
    color: #FFFFFF !important;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background-color: #155B32 !important;
    border-color: #155B32 !important;
}

/* Saved details and footer */
[data-testid="stCaptionContainer"] {
    color: var(--text-color);
}

footer {
    visibility: hidden;
}

/* Mobile layout */
@media (max-width: 640px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 27px;
    }

    .step,
    .step-active {
        padding: 10px 4px;
        font-size: 12px;
    }

    [data-testid="stForm"] {
        padding: 16px;
    }
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HERO BANNER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <div style="font-size:38px;">🌱</div>
    <div class="eyebrow">AGRINIRNAY · SMART CROP PLANNING</div>
    <h1>Tell us about your farm</h1>
    <p>Farm details in. Smarter crop planning starts here.</p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROGRESS INDICATOR
# --------------------------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="step-active">
        ① Farm Details<br>
        <small>Current step</small>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="step">
        ② Soil Report<br>
        <small>Optional upload</small>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="step">
        ③ Crop Options<br>
        <small>Explore matches</small>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FARM INFORMATION FORM
# --------------------------------------------------

st.markdown("## 🚜 Farm information")

with st.form("farm_details_form"):

    st.markdown("### 📍 Farm location")

    district = st.selectbox(
        "District",
        [
            "Bagalkot",
            "Ballari",
            "Belagavi",
            "Bengaluru Rural",
            "Bengaluru Urban",
            "Bidar",
            "Chamarajanagar",
            "Chikkaballapur",
            "Chikkamagaluru",
            "Chitradurga",
            "Dakshina Kannada",
            "Davanagere",
            "Dharwad",
            "Gadag",
            "Hassan",
            "Haveri",
            "Kalaburagi",
            "Kodagu",
            "Kolar",
            "Koppal",
            "Mandya",
            "Mysuru",
            "Raichur",
            "Ramanagara",
            "Shivamogga",
            "Tumakuru",
            "Udupi",
            "Uttara Kannada",
            "Vijayanagara",
            "Vijayapura",
            "Yadgir"
        ],
        index=3,
        key="farm_district_input"
    )

    st.markdown("### 🌾 Land and season")

    col1, col2 = st.columns(2)

    with col1:
        land_area = st.number_input(
            "Farm size (acres)",
            min_value=0.1,
            max_value=10000.0,
            value=1.0,
            step=0.5,
            key="farm_land_area_input"
        )

    with col2:
        season = st.selectbox(
            "Growing season",
            ["Kharif", "Rabi", "Summer"],
            key="farm_season_input"
        )

    st.markdown("### 💧 Water availability")

    water_availability = st.radio(
        "Available irrigation water",
        ["Low", "Moderate", "High"],
        horizontal=True,
        key="farm_water_input"
    )

    st.markdown("""
    <div class="tip">
        💡 <b>Have a soil report?</b><br>
        Upload it on the next page. You can also continue without one.
    </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "Save Farm Details & Continue →",
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

    # Clear the previous upload when starting a new submission.
    st.session_state.pop("soil_report_file", None)

    st.switch_page("pages/2_Soil_Report.py")


# --------------------------------------------------
# SHOW SAVED FARM DETAILS
# --------------------------------------------------

if "farm_details" in st.session_state:
    details = st.session_state["farm_details"]

    st.caption(
        f"Saved farm: {details['district']} · "
        f"{details['land_area']} acres · "
        f"{details['season']} · "
        f"Water: {details['water_availability']}"
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    opacity:0.75;
    padding:22px 0;
    font-size:13px;
    letter-spacing:1px;
">
    AGRINIRNAY · DATA-DRIVEN AGRICULTURE
</div>
""", unsafe_allow_html=True)
