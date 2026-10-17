
import streamlit as st
from weather import get_weather

st.set_page_config(
    page_title="Weather | AgriNirnay",
    page_icon="🌦️",
    layout="wide",
)

st.markdown("""
<style>
.hero {
    background: linear-gradient(120deg, #123F2A, #23834B);
    padding: 28px;
    border-radius: 20px;
    margin-bottom: 22px;
    color: white;
}
.hero h1, .hero p {
    color: white !important;
}
.weather-card {
    background: var(--secondary-background-color);
    padding: 18px;
    border-radius: 16px;
    border: 1px solid rgba(128, 128, 128, 0.2);
    margin-bottom: 12px;
}
.weather-label {
    font-size: 14px;
    opacity: 0.8;
}
.weather-value {
    font-size: 26px;
    font-weight: 700;
}
.stButton > button {
    background: #207744;
    color: white;
    border-radius: 10px;
    border: none;
    min-height: 42px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌦️ Farm Weather</h1>
    <p>Current conditions and rainfall forecasts for your farm area.</p>
</div>
""", unsafe_allow_html=True)

# Automatically use the saved district.
farm_details = st.session_state.get("farm_details", {})
district = farm_details.get("district")

if not district:
    st.warning(
        "Please save your farm details first to load the weather."
    )

    if st.button("Enter Farm Details"):
        st.switch_page("pages/1_Farm_Details.py")

    st.stop()

st.markdown(f"### 📍 Farm district: {district}")

st.caption(
    "Weather is estimated for a nearby town. "
    "Conditions may differ at your exact farm location."
)

cache_key = f"agrinirnay_weather_{district}"

if cache_key not in st.session_state:
    with st.spinner("Fetching current weather and rainfall forecast..."):
        st.session_state[cache_key] = get_weather(district)

weather = st.session_state[cache_key]

if weather.get("error"):
    st.error(weather["error"])

    if st.button("🔄 Try Again"):
        st.session_state.pop(cache_key, None)
        st.rerun()

    st.stop()

st.success(
    f"Weather location: {weather.get('city', district)}, "
    f"{weather.get('country', 'India')}"
)

# Current conditions.
st.markdown("### 🌤️ Current Conditions")

col1, col2, col3 = st.columns(3)

temperature = weather.get("temperature")
humidity = weather.get("humidity")
current_rain = weather.get("rain")
precipitation = weather.get("precipitation")
wind = weather.get("wind_speed")
feels_like = weather.get("apparent_temperature")

with col1:
    st.metric(
        "🌡️ Temperature",
        f"{temperature} °C" if temperature is not None else "N/A",
    )

with col2:
    st.metric(
        "💧 Humidity",
        f"{humidity}%" if humidity is not None else "N/A",
    )

with col3:
    st.metric(
        "💨 Wind Speed",
        f"{wind} km/h" if wind is not None else "N/A",
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "🌧️ Current Rain",
        f"{current_rain} mm"
        if current_rain is not None
        else "N/A",
        help="Rain during the current weather interval.",
    )

with col5:
    st.metric(
        "☔ Current Precipitation",
        f"{precipitation} mm"
        if precipitation is not None
        else "N/A",
        help="Total precipitation during the current weather interval.",
    )

with col6:
    st.metric(
        "🌡️ Feels Like",
        f"{feels_like} °C"
        if feels_like is not None
        else "N/A",
    )

st.caption(
    f"Weather data time: {weather.get('time', 'Unavailable')} "
    f"({weather.get('timezone', 'local time')})"
)

# Today's forecast.
st.markdown("---")
st.markdown("### 🌧️ Today's Rainfall Forecast")

today_rainfall = weather.get("today_rainfall_forecast")
today_probability = weather.get("today_rain_probability")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Expected Rainfall Today",
        f"{today_rainfall} mm"
        if today_rainfall is not None
        else "Unavailable",
        help="Forecast total precipitation for today.",
    )

with col2:
    st.metric(
        "Chance of Rain Today",
        f"{today_probability}%"
        if today_probability is not None
        else "Unavailable",
        help="Maximum forecast precipitation probability for today.",
    )

# Three-day forecast.
st.markdown("---")
st.markdown("### 📅 Three-Day Forecast")

daily = weather.get("daily", {})
dates = daily.get("time", [])
max_temps = daily.get("temperature_2m_max", [])
min_temps = daily.get("temperature_2m_min", [])
rainfall = daily.get("precipitation_sum", [])
rain_probs = daily.get("precipitation_probability_max", [])

if dates:
    forecast_cols = st.columns(len(dates))

    for i, col in enumerate(forecast_cols):
        with col:
            st.markdown(
                '<div class="weather-card">',
                unsafe_allow_html=True,
            )

            st.markdown(f"**{dates[i]}**")

            if i < len(max_temps) and max_temps[i] is not None:
                st.write(f"🌡️ Maximum: {max_temps[i]} °C")

            if i < len(min_temps) and min_temps[i] is not None:
                st.write(f"❄️ Minimum: {min_temps[i]} °C")

            if i < len(rainfall) and rainfall[i] is not None:
                st.write(f"🌧️ Expected rainfall: {rainfall[i]} mm")

            if i < len(rain_probs) and rain_probs[i] is not None:
                st.write(f"☔ Chance of rain: {rain_probs[i]}%")

            st.markdown(
                "</div>",
                unsafe_allow_html=True,
            )
else:
    st.info("The three-day forecast is currently unavailable.")

# Farming guidance.
st.markdown("---")
st.markdown("### 🌱 Weather Guidance")

if today_probability is not None and today_probability >= 60:
    st.info(
        "Rain is reasonably likely according to the forecast. "
        "Check local conditions before irrigation or sowing."
    )
elif today_probability is not None and today_probability <= 20:
    st.info(
        "The forecast indicates a low chance of rain. "
        "Check soil moisture and crop requirements before irrigation."
    )
else:
    st.info(
        "Check the rainfall forecast and your soil moisture before "
        "making irrigation or sowing decisions."
    )

st.caption(
    "Forecasts are estimates, not guarantees. "
    "Verify local conditions before making important farming decisions."
)

if st.button("🔄 Refresh Weather", use_container_width=True):
    st.session_state.pop(cache_key, None)
    st.rerun()
