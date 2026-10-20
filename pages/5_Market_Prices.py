import streamlit as st
import pandas as pd
from market_data import (
    get_market_prices,
    get_crop_district_comparison,
    get_market_summary_metrics
)
from crop_recommendation import get_all_crop_names, get_all_districts, get_all_categories, get_district_default_crop

st.set_page_config(
    page_title="Market Prices | AgriNirnay",
    page_icon="📈",
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
    content: "📈";
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
    background: #4ade80;
    border-radius: 50%;
    box-shadow: 0 0 8px #4ade80;
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

/* KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 24px;
}

.kpi-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 18px;
    padding: 22px 20px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    height: 100%;
}

.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(35, 131, 75, 0.1);
}

.kpi-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    opacity: 0.75;
    margin-bottom: 6px;
}

.kpi-num {
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #124B2A;
    margin-bottom: 4px;
}

.kpi-sub {
    font-size: 12px;
    opacity: 0.8;
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
    <div class="hero-eyebrow"><span class="live-dot"></span> &nbsp; LIVE APMC COMMODITY TERMINAL · KARNATAKA</div>
    <div class="hero-title">Karnataka Mandi Market Rates</div>
    <div class="hero-sub">Direct daily price quotes, modal benchmarks, and price trends across all primary APMC agricultural markets in Karnataka.</div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD AND FILTER CONTEXT
# --------------------------------------------------
farm_details = st.session_state.get("farm_details", {})
default_district = farm_details.get("district", "Mandya")

# Target crop: strictly syncs with user's selected/recommended crop, never defaulting to Arecanut
active_crop_name = (
    st.session_state.pop("market_filter_crop", None)
    or st.session_state.get("selected_crop")
    or get_district_default_crop(default_district)
)

all_districts = ["All Districts"] + get_all_districts()
all_crops = ["All Crops"] + get_all_crop_names()
all_categories = ["All Categories"] + get_all_categories()


# --------------------------------------------------
# SEARCH AND FILTERS
# --------------------------------------------------
st.markdown("### 🔍 Market Filter & Mandi Search")

f1, f2, f3 = st.columns([1.5, 1.5, 1.5])

with f1:
    dist_index = all_districts.index(default_district) if default_district in all_districts else 0
    selected_district = st.selectbox("📍 Select District / Mandi Region", all_districts, index=dist_index)

with f2:
    crop_index = all_crops.index(active_crop_name) if active_crop_name in all_crops else 0
    selected_crop = st.selectbox("🌾 Select Commodity / Crop", all_crops, index=crop_index)

with f3:
    selected_category = st.selectbox("🏷️ Filter Category", all_categories, index=0)

search_q = st.text_input("Quick Keyword Search", placeholder="e.g. Mandya, Ragi, Paddy, Mysore, Doddaballapur...")


# --------------------------------------------------
# SUMMARY KPI CARDS
# --------------------------------------------------
summary = get_market_summary_metrics(
    district=selected_district if selected_district != "All Districts" else None,
    target_crop=selected_crop if selected_crop != "All Crops" else active_crop_name
)

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Market Region</div>
        <div class="kpi-num">{selected_district}</div>
        <div class="kpi-sub"><b>{summary['total_commodities']} Active Produce</b> Traded</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-card" style="border: 2px solid #23834B; background: rgba(35, 131, 75, 0.08);">
        <div class="kpi-label" style="color:#124B2A; font-weight:800;">Modal Price: {summary['featured_crop']}</div>
        <div class="kpi-num" style="color:#155B32;">₹{summary['featured_price']:,}</div>
        <div class="kpi-sub">Per Quintal · Current Benchmark</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Primary APMC Mandi</div>
        <div class="kpi-num" style="font-size:20px;">{summary['featured_market']}</div>
        <div class="kpi-sub">Official Auction Platform</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Price Momentum</div>
        <div class="kpi-num" style="color:#155B32; font-size:22px;">▲ {summary.get('featured_trend', 'Stable')}</div>
        <div class="kpi-sub">Strong Market Demand</div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# FETCH AND DISPLAY FILTERED MARKET DATA
# --------------------------------------------------
st.markdown("---")
st.markdown(f"### 📋 Verified Mandi Quotes for {selected_district}")

market_df = get_market_prices(
    district=selected_district,
    crop=selected_crop,
    category=selected_category,
    search_query=search_q
)

if market_df.empty:
    st.info("No APMC price quotes found matching your filters. Try selecting 'All Districts' or 'All Crops'.")
else:
    display_df = market_df[[
        "crop", "category", "market_apmc", "district",
        "min_price_inr_quintal", "modal_price_inr_quintal", "max_price_inr_quintal",
        "msp_inr_quintal", "price_trend"
    ]].copy()

    display_df.rename(columns={
        "crop": "Commodity / Crop",
        "category": "Category",
        "market_apmc": "APMC Mandi",
        "district": "District",
        "min_price_inr_quintal": "Min (₹/Qtl)",
        "modal_price_inr_quintal": "Modal Price (₹/Qtl)",
        "max_price_inr_quintal": "Max (₹/Qtl)",
        "msp_inr_quintal": "Govt MSP (₹)",
        "price_trend": "Trend"
    }, inplace=True)

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )


# --------------------------------------------------
# CROSS-DISTRICT COMPARISON
# --------------------------------------------------
st.markdown("---")
st.markdown("## 📊 Inter-District Mandi Rate Comparison")
st.caption("Compare prices for your crop across different Karnataka APMC mandis to identify the highest realizing market destination.")

comparison_crop_default = selected_crop if selected_crop != "All Crops" else active_crop_name
crop_names_list = get_all_crop_names()
comp_idx = crop_names_list.index(comparison_crop_default) if comparison_crop_default in crop_names_list else 0

comp_crop = st.selectbox(
    "Choose Commodity to Compare Across Mandis:",
    crop_names_list,
    index=comp_idx
)

comparison_df = get_crop_district_comparison(comp_crop)

if not comparison_df.empty:
    chart_data = comparison_df[["district", "modal_price_inr_quintal"]].copy()
    chart_data.set_index("district", inplace=True)
    chart_data.rename(columns={"modal_price_inr_quintal": "Modal Price (₹/Qtl)"}, inplace=True)

    c_col1, c_col2 = st.columns([2, 1])
    with c_col1:
        st.bar_chart(chart_data, color="#23834B")

    with c_col2:
        top_mandi = comparison_df.iloc[0]
        min_mandi = comparison_df.iloc[-1]
        st.markdown(f"""
        <div class="kpi-card" style="margin-bottom:12px; border-left: 4px solid #1b6d3b;">
            <div class="kpi-label">Highest Realizing Market</div>
            <div class="kpi-num" style="font-size:22px; color:#1b6d3b;">₹{top_mandi['modal_price_inr_quintal']:,} / Qtl</div>
            <div class="kpi-sub"><b>{top_mandi['market_apmc']}</b> ({top_mandi['district']})</div>
        </div>
        <div class="kpi-card" style="border-left: 4px solid #b91c1c;">
            <div class="kpi-label">Lowest Market Rate</div>
            <div class="kpi-num" style="font-size:22px; color:#b91c1c;">₹{min_mandi['modal_price_inr_quintal']:,} / Qtl</div>
            <div class="kpi-sub"><b>{min_mandi['market_apmc']}</b> ({min_mandi['district']})</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
        if st.button(f"📊 Plan Farm Finances for {comp_crop} →", use_container_width=True):
            st.session_state["selected_crop"] = comp_crop
            st.switch_page("pages/6_Cost_and_Revenue.py")


# --------------------------------------------------
# NAVIGATION FOOTER
# --------------------------------------------------
st.markdown("---")
b1, b2 = st.columns(2)

with b1:
    if st.button("← Back to Crop Recommendation", use_container_width=True):
        st.switch_page("pages/3_Crop_Recommendations.py")

with b2:
    if st.button("Calculate Farm Cost and Revenue →", use_container_width=True):
        st.switch_page("pages/6_Cost_and_Revenue.py")

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)