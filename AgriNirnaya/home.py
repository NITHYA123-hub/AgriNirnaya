
import streamlit as st

st.markdown("""
<style>
#MainMenu, footer, [data-testid="stHeader"] {
    visibility: hidden;
}
.stApp {
    background: #faf9f3;
    color: #173d2b;
}
.block-container {
    max-width: 1400px;
    padding: 1rem 2.5rem 1.5rem;
}
.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 0 18px;
    border-bottom: 1px solid #e5e8dc;
    margin-bottom: 22px;
}
.brand-icon { font-size: 38px; }
.brand-name {
    font-size: 29px;
    font-weight: 800;
    color: #17452e;
    letter-spacing: -1px;
}
.brand-tag {
    color: #71816e;
    font-size: 10px;
    letter-spacing: 3px;
}
.hero-copy {
    padding: 40px 15px 30px 5px;
}
.eyebrow {
    color: #277445;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 3px;
}
.hero-title {
    font-size: clamp(38px, 4.5vw, 62px);
    font-weight: 800;
    line-height: 1.04;
    letter-spacing: -2px;
    color: #153c29;
    margin: 20px 0;
}
.hero-subtitle {
    font-size: 18px;
    line-height: 1.6;
    color: #617268;
    margin-bottom: 22px;
}
.hero-image {
    width: 100%;
    height: 365px;
    object-fit: cover;
    border-radius: 110px 22px 100px 22px;
    box-shadow: 0 14px 35px #193e291a;
}
.location-note {
    color: #53705c;
    font-size: 13px;
    margin-top: 18px;
}
.section-title {
    color: #183f2c;
    font-size: 24px;
    font-weight: 750;
    margin: 12px 0 17px;
}
.feature {
    background: #fff;
    border: 1px solid #e0e8dc;
    border-radius: 17px;
    padding: 22px 20px;
    min-height: 175px;
    transition: 0.2s;
}
.feature-icon {
    background: #edf4e9;
    width: 54px;
    height: 54px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 27px;
    margin-bottom: 14px;
}
.feature h3 {
    color: #1a5034;
    font-size: 18px;
    margin: 0 0 8px;
}
.feature p {
    color: #68776c;
    font-size: 14px;
    line-height: 1.5;
    margin: 0;
}
.notice {
    background: #edf3e9;
    border-radius: 12px;
    padding: 14px;
    text-align: center;
    color: #49634e;
    font-size: 13px;
    margin-top: 18px;
}
.footer {
    background: #173e2d;
    color: #e8f0e7;
    text-align: center;
    padding: 17px;
    border-radius: 12px;
    margin-top: 18px;
    font-size: 11px;
    letter-spacing: 2px;
}
div.stButton > button {
    background: #1d603a;
    color: white;
    border: 1px solid #1d603a;
    border-radius: 28px;
    min-height: 48px;
    font-weight: 700;
    padding: 0 25px;
}
div.stButton > button:hover {
    background: #12452a;
    border-color: #12452a;
    color: white;
}
@media (max-width: 700px) {
    .block-container { padding: 1rem; }
    .hero-copy { padding: 15px 0; }
    .hero-image { height: 240px; border-radius: 35px 12px; }
    .brand-name { font-size: 24px; }
}
</style>
""", unsafe_allow_html=True)

# Brand header
st.markdown("""
<div class="brand">
    <div class="brand-icon">🌿</div>
    <div>
        <div class="brand-name">AgriNirnay</div>
        <div class="brand-tag">SMART CROP PLANNING</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero section
left, right = st.columns([0.9, 1.1], gap="large")

with left:
    st.markdown("""
    <div class="hero-copy">
        <div class="eyebrow">DATA-DRIVEN AGRICULTURE</div>
        <div class="hero-title">
            Make smarter<br>crop decisions.
        </div>
        <div class="hero-subtitle">
            Soil, weather and market insights for your farm.
        </div>
        <div class="location-note">
            📍 Designed for farmers across Karnataka
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start Crop Planning  →", use_container_width=True):
        st.switch_page("pages/1_Farm_Details.py")

with right:
    st.markdown("""
    <img class="hero-image"
    src="https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=1200&q=85"
    alt="Green agricultural fields at sunrise">
    """, unsafe_allow_html=True)

# Feature section
st.markdown('<div class="section-title">Explore AgriNirnay</div>',
            unsafe_allow_html=True)

features = [
    ("🧪", "Soil Insights",
     "Use soil reports to support crop planning."),
    ("🌾", "Crop Recommendations",
     "Explore crops suited to your farm details."),
    ("🌦️", "Weather Updates",
     "View weather information for your region."),
    ("📊", "Cost & Revenue",
     "Review estimated costs and crop revenue.")
]

cols = st.columns(4, gap="medium")

for col, (icon, title, description) in zip(cols, features):
    with col:
        st.markdown(f"""
        <div class="feature">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="notice">
    🌱 &nbsp; Estimates are indicative, not guaranteed.
</div>
<div class="footer">
    AGRINIRNAY &nbsp; · &nbsp; SFIC 2026
</div>
""", unsafe_allow_html=True)
