import streamlit as st
from soil_reader import read_soil_report

st.set_page_config(
    page_title="Soil Report | AgriNirnay",
    page_icon="🧪",
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
    content: "🧪";
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

/* Context Pills */
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
}

.context-pill b {
    color: #1a6338;
}

/* Cards */
.custom-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03);
}

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
# HERO BANNER
# --------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">🧪 &nbsp; STEP 2 · SOIL HEALTH & NUTRIENT PROFILE</div>
    <div class="hero-title">Soil Nutrient Analysis</div>
    <div class="hero-sub">Upload your Soil Health Card or configure soil texture and macronutrients (N, P, K, pH) to ensure precise crop matching.</div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# PROGRESS INDICATOR
# --------------------------------------------------
st.markdown("""
<div class="stepper-container">
    <div class="step-card">
        <div class="step-num">STEP 1</div>
        <div class="step-title">✓ Farm Details</div>
    </div>
    <div class="step-card-active">
        <div class="step-num" style="color:#124B2A;">STEP 2 · ACTIVE</div>
        <div class="step-title" style="color:#124B2A;">② Soil Report</div>
    </div>
    <div class="step-card">
        <div class="step-num">STEP 3</div>
        <div class="step-title">③ Recommended Crop</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FARM SUMMARY
# --------------------------------------------------
details = st.session_state.get("farm_details")

if details:
    st.markdown(f"""
    <div style="background: #FFFFFF; border: 2px solid #23834B; border-radius: 18px; padding: 18px 24px; margin: 18px 0 24px; box-shadow: 0 6px 20px rgba(27, 101, 59, 0.08);">
        <div style="font-size: 11px; font-weight: 800; letter-spacing: 2px; color: #155B32; text-transform: uppercase; margin-bottom: 12px;">
            🚜 SAVED FARM PARAMETERS
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 12px;">
            <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600;">
                📍 District: <span style="color: #155B32; font-weight: 800;">{details['district']}</span>
            </div>
            <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600;">
                🚜 Farm Size: <span style="color: #155B32; font-weight: 800;">{details['land_area']} Acres</span>
            </div>
            <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600;">
                🗓️ Season: <span style="color: #155B32; font-weight: 800;">{details['season']}</span>
            </div>
            <div style="background: #F4F9F5; border: 1.5px solid #D2E7D7; border-radius: 12px; padding: 10px 18px; color: #123821; font-size: 14px; font-weight: 600;">
                💧 Water: <span style="color: #155B32; font-weight: 800;">{details['water_availability']}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No farm details saved yet. Setting baseline location to Mandya.")
    if st.button("← Go to Farm Details"):
        st.switch_page("pages/1_Farm_Details.py")


# --------------------------------------------------
# SOIL REPORT UPLOAD
# --------------------------------------------------
st.markdown("### 📄 Soil Health Card Upload (Optional)")

st.markdown("""
<div class="custom-card">
    <h4 style="margin:0 0 8px; color:#185433; font-family:'Outfit',sans-serif;">Smart OCR Document Extractor</h4>
    <p style="margin:0 0 6px; font-size:14px; opacity:0.85;">Upload an official laboratory soil report or smartphone photo of your Soil Health Card. Our scanner automatically extracts pH and N-P-K nutrient values.</p>
    <span style="font-size:12px; opacity:0.7;">Supported formats: PDF, PNG, JPG, and JPEG</span>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose a soil test file from your device",
    type=["pdf", "jpg", "jpeg", "png"],
    key="soil_report_uploader"
)

extracted_values = {}
if uploaded_file is not None:
    st.session_state["soil_report_file"] = uploaded_file
    st.success(f"Loaded: **{uploaded_file.name}**")

    if uploaded_file.type.startswith("image/"):
        with st.expander("🖼️ View Uploaded Document Preview", expanded=False):
            st.image(uploaded_file, caption="Soil Health Card Scan", use_container_width=True)

    with st.spinner("Analyzing soil document with OCR extractor..."):
        report_result = read_soil_report(uploaded_file)
        if "error" in report_result and report_result["error"]:
            st.info(f"Document registered. {report_result['error']}")
        else:
            extracted_values = report_result.get("values", {})
            st.success("Successfully analyzed document! Soil parameters pre-filled below.")
else:
    st.session_state.pop("soil_report_file", None)
    st.markdown("""
    <div class="tip-callout">
        🌱 <b>No laboratory soil report handy?</b><br>
        Standard regional soil parameters for your district are pre-configured below. You can also adjust them directly.
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# SOIL PARAMETERS & NUTRIENT FORM
# --------------------------------------------------
st.markdown("---")
st.markdown("### 🌾 Soil Classification & Nutrient Status")

district_name = details.get("district", "") if details else ""

# Regional smart default soil type
default_soil_index = 0
if district_name in ["Vijayapura", "Kalaburagi", "Bagalkot", "Dharwad", "Gadag", "Raichur", "Ballari", "Yadgir"]:
    default_soil_index = 1  # Black Soil
elif district_name in ["Kodagu", "Chikkamagaluru", "Dakshina Kannada", "Udupi", "Uttara Kannada"]:
    default_soil_index = 4  # Laterite
elif district_name in ["Mandya", "Mysuru", "Bengaluru Rural", "Bengaluru Urban", "Tumakuru", "Kolar", "Hassan", "Ramanagara"]:
    default_soil_index = 0  # Red Loam

soil_options = [
    "Red Loam / Red Soil",
    "Deep Black Cotton Soil",
    "Sandy Loam / Light Soil",
    "Clay Loam / Alluvial",
    "Laterite Soil (Coastal / Malnad)",
    "Mixed Loamy Soil"
]

current_soil = st.session_state.get("soil_details", {})

col_s1, col_s2 = st.columns(2)

with col_s1:
    selected_soil = st.selectbox(
        "Soil Texture Classification",
        soil_options,
        index=default_soil_index,
        key="selected_soil_type_input"
    )

with col_s2:
    ph_val = extracted_values.get("pH")
    default_ph = float(ph_val) if ph_val is not None else float(current_soil.get("ph", 6.8))
    selected_ph = st.number_input(
        "Soil pH Level (Acidity / Alkalinity)",
        min_value=3.5,
        max_value=10.0,
        value=default_ph,
        step=0.1,
        help="Optimal soil pH for most crops is between 6.0 and 7.5"
    )

st.markdown("#### 🧪 Available Macronutrient Levels (kg / ha)")
col_n, col_p, col_k = st.columns(3)

with col_n:
    n_val = extracted_values.get("nitrogen")
    def_n = float(n_val) if n_val is not None else float(current_soil.get("nitrogen", 280.0))
    selected_n = st.number_input(
        "Available Nitrogen (N)",
        min_value=0.0,
        max_value=1200.0,
        value=def_n,
        step=10.0,
        help="Low: <280, Medium: 280-560, High: >560 kg/ha"
    )

with col_p:
    p_val = extracted_values.get("phosphorus")
    def_p = float(p_val) if p_val is not None else float(current_soil.get("phosphorus", 35.0))
    selected_p = st.number_input(
        "Available Phosphorus (P)",
        min_value=0.0,
        max_value=300.0,
        value=def_p,
        step=5.0,
        help="Low: <23, Medium: 23-56, High: >56 kg/ha"
    )

with col_k:
    k_val = extracted_values.get("potassium")
    def_k = float(k_val) if k_val is not None else float(current_soil.get("potassium", 240.0))
    selected_k = st.number_input(
        "Available Potassium (K)",
        min_value=0.0,
        max_value=800.0,
        value=def_k,
        step=10.0,
        help="Low: <145, Medium: 145-337, High: >337 kg/ha"
    )

# Save soil details
st.session_state["soil_details"] = {
    "soil_type": selected_soil,
    "ph": selected_ph,
    "nitrogen": selected_n,
    "phosphorus": selected_p,
    "potassium": selected_k
}

# Navigation buttons
st.markdown("---")
btn_left, btn_right = st.columns(2)

with btn_left:
    if st.button("← Back to Farm Details", use_container_width=True):
        st.switch_page("pages/1_Farm_Details.py")

with btn_right:
    if st.button("Explore Recommended Crop →", use_container_width=True):
        st.switch_page("pages/3_Crop_Recommendations.py")


# Footer
st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)
