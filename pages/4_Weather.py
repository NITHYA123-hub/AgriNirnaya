import streamlit as st
from weather import get_weather

st.set_page_config(
    page_title="Weather | AgriNirnay",
    page_icon="🌦️",
    layout="wide",
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
    content: "🌦️";
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

.live-dot {
    width: 8px;
    height: 8px;
    background: #38bdf8;
    border-radius: 50%;
    box-shadow: 0 0 8px #38bdf8;
    display: inline-block;
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

/* Weather Metric Card */
.weather-card {
    background: var(--secondary-background-color);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(128, 128, 128, 0.2);
    margin-bottom: 14px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
}

.weather-label {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    opacity: 0.8;
}

.weather-value {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #124B2A;
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
    <div class="hero-eyebrow"><span class="live-dot"></span> &nbsp; SATELLITE METEOROLOGY · OPEN-METEO</div>
    <div class="hero-title">Live Farm Weather & Rain Forecast</div>
    <div class="hero-sub">Real-time localized temperature, relative humidity, wind velocity, and multi-day precipitation forecasts for crop scheduling.</div>
</div>
""", unsafe_allow_html=True)


# Automatically use the saved district or allow selection
farm_details = st.session_state.get("farm_details", {})
saved_district = farm_details.get("district")

all_karnataka_districts = [
    "Bagalkot", "Ballari", "Belagavi", "Bengaluru Rural", "Bengaluru Urban",
    "Bidar", "Chamarajanagar", "Chikkaballapur", "Chikkamagaluru", "Chitradurga",
    "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Hassan",
    "Haveri", "Kalaburagi", "Kodagu", "Kolar", "Koppal",
    "Mandya", "Mysuru", "Raichur", "Ramanagara", "Shivamogga",
    "Tumakuru", "Udupi", "Uttara Kannada", "Vijayanagara", "Vijayapura", "Yadgir"
]

default_idx = all_karnataka_districts.index(saved_district) if saved_district in all_karnataka_districts else 20  # Mandya

col_w1, col_w2 = st.columns([2, 1])
with col_w1:
    district = st.selectbox("📍 Select District for Weather Forecast", all_karnataka_districts, index=default_idx)
with col_w2:
    if saved_district:
        st.caption(f"✓ Using saved farm district: **{saved_district}**")
    else:
        st.caption("Tip: Save farm details to automatically sync district.")

st.caption(
    "Weather data is processed via Open-Meteo API. "
    "Conditions reflect nearby meteorological observation stations."
)

cache_key = f"agrinirnay_weather_{district}"

if cache_key not in st.session_state:
    with st.spinner(f"Fetching current weather and rainfall forecast for {district}..."):
        st.session_state[cache_key] = get_weather(district)

weather = st.session_state[cache_key]

if weather.get("error"):
    st.error(weather["error"])

    if st.button("🔄 Try Again"):
        st.session_state.pop(cache_key, None)
        st.rerun()

    st.stop()

st.success(
    f"📍 Weather Observation: **{weather.get('city', district)}, {weather.get('country', 'India')}**"
)

# Current conditions
st.markdown("### 🌤️ Current Atmospheric Conditions")

col1, col2, col3 = st.columns(3)

temperature = weather.get("temperature")
humidity = weather.get("humidity")
wind = weather.get("wind_speed")
feels_like = weather.get("apparent_temperature")
condition = weather.get("condition", "🌤️ Partly Cloudy")
current_rain = weather.get("rain", 0.0)
today_rain = weather.get("today_rainfall_forecast", 0.0)
today_prob = weather.get("today_rain_probability", 0)

with col1:
    st.metric(
        "🌡️ Temperature",
        f"{temperature} °C" if temperature is not None else "N/A",
        f"Feels like {feels_like} °C" if feels_like is not None else None,
    )

with col2:
    st.metric(
        "🌤️ Sky Condition",
        condition,
        f"Wind: {wind} km/h" if wind is not None else None,
    )

with col3:
    st.metric(
        "💧 Relative Humidity",
        f"{humidity}%" if humidity is not None else "N/A",
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "🌧️ Today's Expected Rain",
        f"{today_rain} mm" if today_rain is not None else "0.0 mm",
        f"{today_prob}% Rain Chance" if today_prob is not None else None,
        help="Total forecasted precipitation accumulation for today across your farm region.",
    )

with col5:
    st.metric(
        "☔ Current Rainfall Now",
        "0.0 mm (Currently Dry)" if (current_rain is None or current_rain == 0.0) else f"{current_rain} mm (Active Rain)",
        help="0.0 mm indicates that no active rainfall is falling from the sky at this exact moment.",
    )

with col6:
    st.metric(
        "💨 Wind Velocity",
        f"{wind} km/h" if wind is not None else "N/A",
    )

st.markdown(f"""
<div style="background: #FFFFFF; border: 1px solid #D2E7D7; border-left: 5px solid #23834B; border-radius: 12px; padding: 14px 18px; margin: 16px 0; color: #123821; font-size: 13.5px; line-height: 1.6; box-shadow: 0 4px 14px rgba(0,0,0,0.03);">
    💡 <b>Understanding Rainfall Metrics:</b><br>
    <b>Current Rainfall is {current_rain if current_rain is not None else 0.0} mm</b> because real-time radar confirms it is currently dry at your farm at this exact second.<br>
    <b>Today's Forecast Total is {today_rain if today_rain is not None else 0.0} mm</b> with a <b>{today_prob if today_prob is not None else 0}% likelihood of showers</b> throughout the day. Check the 3-day agricultural outlook below for upcoming weather patterns.
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# MULTI-DAY RAINFALL FORECAST
# --------------------------------------------------
daily = weather.get("daily", {})
if daily and daily.get("precipitation_sum"):
    st.markdown("---")
    st.markdown("### 📅 3-Day Agricultural Rainfall Outlook")

    dates = daily.get("time", ["Day 1", "Day 2", "Day 3"])
    rain_sums = daily.get("precipitation_sum", [0, 0, 0])
    rain_probs = daily.get("precipitation_probability_max", [0, 0, 0])
    temp_maxs = daily.get("temperature_2m_max", [0, 0, 0])
    temp_mins = daily.get("temperature_2m_min", [0, 0, 0])

    fc_cols = st.columns(min(3, len(dates)))
    for idx, col in enumerate(fc_cols):
        with col:
            st.markdown(f"""
            <div class="weather-card">
                <div class="weather-label">Forecast: {dates[idx]}</div>
                <div class="weather-value" style="font-size:22px; margin: 6px 0;">🌧️ {rain_sums[idx]} mm Rain</div>
                <div style="font-size:13px; opacity:0.85;">Probability: <b>{rain_probs[idx]}%</b></div>
                <div style="font-size:13px; opacity:0.85; margin-top:4px;">Temp: {temp_mins[idx]}°C - {temp_maxs[idx]}°C</div>
            </div>
            """, unsafe_allow_html=True)


# Navigation
st.markdown("---")
w_left, w_right = st.columns(2)

with w_left:
    if st.button("← Back to Recommended Crop", use_container_width=True):
        st.switch_page("pages/3_Crop_Recommendations.py")

with w_right:
    if st.button("Check APMC Mandi Market Prices →", use_container_width=True):
        st.switch_page("pages/5_Market_Prices.py")

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)
