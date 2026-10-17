
import streamlit as st

st.set_page_config(
    page_title="AgriNirnay | Smart Crop Planning",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Register all application pages
home_page = st.Page(
    "home.py",
    title="Home",
    icon="🏠",
    default=True
)

farm_page = st.Page(
    "pages/1_Farm_Details.py",
    title="Farm Details",
    icon="🚜"
)

soil_page = st.Page(
    "pages/2_Soil_Report.py",
    title="Soil Report",
    icon="🧪"
)

crop_page = st.Page(
    "pages/3_Crop_Recommendations.py",
    title="Crop Recommendations",
    icon="🌾"
)

weather_page = st.Page(
    "pages/4_Weather.py",
    title="Weather",
    icon="🌦️"
)

market_page = st.Page(
    "pages/5_Market_Prices.py",
    title="Market Prices",
    icon="📈"
)

estimates_page = st.Page(
    "pages/6_Cost_and_Revenue.py",
    title="Cost and Revenue",
    icon="💰"
)

# Application navigation
navigation = st.navigation(
    {
        "Main": [
            home_page,
            farm_page,
            soil_page,
            crop_page
        ],
        "Farm Information": [
            weather_page,
            market_page,
            estimates_page
        ]
    }
)

# Run the selected page
navigation.run()
