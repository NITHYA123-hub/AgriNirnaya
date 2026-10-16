
import streamlit as st

st.markdown("""
<style>
.block-container {
    max-width: 1150px;
    padding: 1.5rem 2rem 2.5rem;
}

.hero {
    background: linear-gradient(120deg, #123f2a, #23834b);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 22px;
}

.hero h1 {
    color: #ffffff !important;
    font-size: 35px;
    margin-bottom: 8px;
}

.hero p {
    color: #e4f4e8 !important;
    font-size: 16px;
}

.hero .eyebrow {
    color: #d3edda;
    font-size: 12px;
    letter-spacing: 2px;
}

.step, .step-active {
    border-radius: 14px;
    padding: 14px;
    text-align: center;
    min-height: 65px;
}

.step {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.25);
    color: var(--text-color);
}

.step-active {
    background: #e2f4e5;
    border: 1px solid #5aaf70;
    color: #185d31;
    font-weight: 700;
}

[data-testid="stForm"] {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.25);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 5px 22px rgba(25, 65, 38, 0.05);
}

[data-testid="stWidgetLabel"] p,
[data-testid="stRadio"] label,
[data-testid="stRadio"] p {
    color: var(--text-color);
}

div.stButton > button,
div.stFormSubmitButton > button {
    background: #207744;
    color: #ffffff !important;
    border: none;
    border-radius: 10px;
    min-height: 48px;
    font-weight: 600;
}

div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    background: #155b32;
    color: #ffffff !important;
}

.tip {
    background: rgba(46, 139, 87, 0.12);
    border-left: 4px solid #329454;
    padding: 15px;
    border-radius: 8px;
    margin: 12px 0;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Hero banner
st.markdown("""
<div class="hero">
    <div style="font-size:38px;">🌱</div>
    <div class="eyebrow">AGRINIRNAY · SMART CROP PLANNING</div>
    <h1>Tell us about your farm</h1>
    <p>Farm details in. Smarter crop planning starts here.</p>
</div>
""", unsafe_allow_html=True)

# Progress indicator
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="step-active">
        ① Farm Details<br><small>Current step</small>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="step">
        ② Soil Report<br><small>Optional upload</small>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="step">
        ③ Crop Options<br><small>Explore matches</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🚜 Farm information")

with st.form("farm_details_form"):
    st.markdown("### 📍 Farm location")

    district = st.selectbox(
        "District",
        [
            "Bengaluru Rural",
            "Mysuru",
            "Mandya",
            "Tumakuru",
            "Belagavi",
            "Dharwad"
        ]
    )

    st.markdown("### 🌾 Land and season")

    col1, col2 = st.columns(2)

    with col1:
        land_area = st.number_input(
            "Farm size (acres)",
            min_value=0.1,
            max_value=10000.0,
            value=1.0,
            step=0.5
        )

    with col2:
        season = st.selectbox(
            "Growing season",
            ["Kharif", "Rabi", "Summer"]
        )

    st.markdown("### 💧 Water availability")

    water_availability = st.radio(
        "Available irrigation water",
        ["Low", "Moderate", "High"],
        horizontal=True
    )

    st.markdown("""
    <div class="tip">
        💡 <b>Have a soil report?</b>
        Upload it on the next page. You can also continue without one.
    </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "Save Farm Details & Continue →",
        use_container_width=True
    )

if submitted:
    st.session_state["farm_details"] = {
        "district": district,
        "land_area": land_area,
        "season": season,
        "water_availability": water_availability
    }

    st.session_state["soil_report_file"] = None
    st.switch_page("pages/2_Soil_Report.py")

if "farm_details" in st.session_state:
    details = st.session_state["farm_details"]
    st.caption(
        f"Saved farm: {details['district']} · "
        f"{details['land_area']} acres · {details['season']}"
    )

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:22px 0;">
    AGRINIRNAY · DATA-DRIVEN AGRICULTURE
</div>
""", unsafe_allow_html=True)
