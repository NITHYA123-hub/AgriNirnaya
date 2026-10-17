
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
    font-size: 32px;
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

.panel {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.25);
    border-radius: 18px;
    padding: 22px;
    margin: 14px 0;
    box-shadow: 0 5px 22px rgba(25, 65, 38, 0.04);
}

.panel h4 {
    color: #329454;
}

.panel p {
    color: var(--text-color);
}

.tip {
    background: rgba(46, 139, 87, 0.12);
    border-left: 4px solid #329454;
    padding: 15px;
    border-radius: 8px;
    color: var(--text-color);
    margin: 12px 0;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stWidgetLabel"] p {
    color: var(--text-color);
}

[data-testid="stFileUploader"] {
    background: var(--secondary-background-color);
    border: 1px dashed #79a984;
    border-radius: 14px;
    padding: 16px;
}

div.stButton > button {
    background: #207744;
    color: #ffffff !important;
    border: none;
    border-radius: 10px;
    min-height: 46px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #155b32;
    color: #ffffff !important;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<div class="hero">
    <div style="font-size:38px;">🧪</div>
    <div class="eyebrow">AGRINIRNAY · SOIL ANALYSIS</div>
    <h1>Understand Your Soil</h1>
    <p>Upload a soil health report to support informed crop planning.</p>
</div>
""", unsafe_allow_html=True)


# Progress indicator
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="step">
        ✓ Farm Details<br>
        <small>Completed step</small>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="step-active">
        ② Soil Report<br>
        <small>Current step</small>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="step">
        ③ Crop Options<br>
        <small>Next step</small>
    </div>
    """, unsafe_allow_html=True)


# Farm summary
st.markdown("## 🚜 Farm Summary")

details = st.session_state.get("farm_details")

if details:
    a, b, c, d = st.columns(4)

    a.metric("📍 District", details["district"])
    b.metric("🌾 Land", f'{details["land_area"]} acres')
    c.metric("🗓️ Season", details["season"])
    d.metric("💧 Water", details["water_availability"])
else:
    st.warning(
        "No farm details saved yet. Go back to the Farm Details page "
        "and save your information."
    )


# Soil report upload
st.markdown("## 📄 Soil Health Report")

st.markdown("""
<div class="panel">
    <h4>Upload your soil report</h4>
    <p>Choose a PDF or image of your laboratory soil report.</p>
    <p style="font-size:13px;opacity:0.75;">
        Supported formats: PDF, JPG, JPEG and PNG
    </p>
</div>
""", unsafe_allow_html=True)


uploaded_file = st.file_uploader(
    "Select a file from your device",
    type=["pdf", "jpg", "jpeg", "png"],
    key="soil_report_uploader"
)


if uploaded_file is not None:
    st.session_state["soil_report_file"] = uploaded_file

    st.success(f"Selected: {uploaded_file.name}")

    if uploaded_file.type.startswith("image/"):
        st.image(
            uploaded_file,
            caption="Soil report preview",
            use_container_width=True
        )

    elif uploaded_file.type == "application/pdf":
        st.info(
            "PDF uploaded successfully. Automatic soil-value extraction "
            "will be connected through soil_reader.py."
        )

    if st.button("Remove selected report"):
        st.session_state.pop("soil_report_file", None)
        st.rerun()

else:
    st.session_state.pop("soil_report_file", None)

    st.markdown("""
    <div class="tip">
        🌱 <b>No soil report?</b>
        You can continue without uploading one.
    </div>
    """, unsafe_allow_html=True)


# Navigation
st.markdown("---")

left, right = st.columns(2)

with left:
    if st.button(
        "← Back to Farm Details",
        use_container_width=True
    ):
        st.switch_page("pages/1_Farm_Details.py")

with right:
    if st.button(
        "Explore Crop Options →",
        use_container_width=True
    ):
        st.switch_page("pages/3_Crop_Recommendations.py")


# Footer
st.markdown("""
<div style="text-align:center;opacity:0.75;padding:22px 0;">
    AGRINIRNAY · DATA-DRIVEN AGRICULTURE
</div>
""", unsafe_allow_html=True)
