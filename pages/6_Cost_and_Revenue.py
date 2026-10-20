import streamlit as st
import pandas as pd
from financial_estimates import calculate_financials
from crop_recommendation import get_all_crop_names, get_crop_profile, get_district_default_crop

st.set_page_config(
    page_title="Cost and Revenue | AgriNirnay",
    page_icon="💰",
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
    content: "💰";
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

/* Financial Metric Panels */
.fin-metric-card {
    background: var(--secondary-background-color);
    border: 1px solid rgba(128, 128, 128, 0.2);
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03);
    height: 100%;
    transition: transform 0.2s ease;
}

.fin-metric-card:hover {
    transform: translateY(-3px);
}

.fin-metric-highlight {
    background: linear-gradient(145deg, rgba(35, 131, 75, 0.15) 0%, rgba(20, 80, 47, 0.06) 100%);
    border: 2px solid #23834B;
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(35, 131, 75, 0.15);
    height: 100%;
}

.fin-caption {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    opacity: 0.75;
    margin-bottom: 6px;
}

.fin-num {
    font-family: 'Outfit', sans-serif;
    font-size: 28px;
    font-weight: 900;
    color: #124B2A;
    margin-bottom: 4px;
}

.fin-sub {
    font-size: 13px;
    opacity: 0.8;
}

/* Tip Callout */
.tip-callout {
    background: rgba(46, 139, 87, 0.12);
    border-left: 4px solid #23834B;
    padding: 18px 22px;
    border-radius: 12px;
    color: var(--text-color);
    margin: 18px 0;
    line-height: 1.6;
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
    <div class="hero-eyebrow">💰 &nbsp; AGRINIRNAY · FINANCIAL PLANNING & ROI FORECAST</div>
    <div class="hero-title">Cost & Revenue Modeling</div>
    <div class="hero-sub">Detailed operational expense breakdown, projected harvest volumes, market revenues, and net profit projections tailored to your farm size.</div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# FARM & CROP SELECTION
# --------------------------------------------------
farm_details = st.session_state.get("farm_details", {})
district = farm_details.get("district", "Mandya")
default_acres = float(farm_details.get("land_area", 1.0))

all_crops = get_all_crop_names()
district_staple = get_district_default_crop(district)

# Sync with active recommended crop, never defaulting to Arecanut
preselected = st.session_state.get("selected_crop") or district_staple
crop_idx = all_crops.index(preselected) if preselected in all_crops else (all_crops.index(district_staple) if district_staple in all_crops else 0)

st.markdown("### 🚜 Farm & Commodity Configuration")

p_col1, p_col2 = st.columns([2, 1])

with p_col1:
    selected_crop = st.selectbox("🌾 Crop for Financial Modeling", all_crops, index=crop_idx)
    st.session_state["selected_crop"] = selected_crop

with p_col2:
    farm_acres = st.number_input(
        "🚜 Farm Area (Acres)",
        min_value=0.1,
        max_value=1000.0,
        value=default_acres,
        step=0.5
    )

# Load baseline crop profile
crop_profile = get_crop_profile(selected_crop, district=district)
if not crop_profile:
    st.error("Crop profile data not found.")
    st.stop()


# --------------------------------------------------
# INTERACTIVE SIMULATION SLIDERS
# --------------------------------------------------
st.markdown("---")
st.markdown("### 🎛️ Interactive Yield & Price Simulation")
st.caption("Adjust expected harvest yield and selling price to model your profits under varying seasonal conditions.")

base_yield = float(crop_profile["expected_yield_quintal_per_acre"])
min_yield = float(crop_profile["min_yield_quintal_per_acre"])
max_yield = float(crop_profile["max_yield_quintal_per_acre"])

base_price = float(crop_profile["modal_price_inr_quintal"])
min_price = float(crop_profile["min_price_inr_quintal"])
max_price = float(crop_profile["max_price_inr_quintal"])

slider_c1, slider_c2 = st.columns(2)

with slider_c1:
    sim_yield = st.slider(
        f"Expected Yield (Quintals / Acre) [Benchmark: {base_yield} Qtl]",
        min_value=max(1.0, float(round(min_yield * 0.7, 1))),
        max_value=float(round(max_yield * 1.3, 1)),
        value=base_yield,
        step=0.5
    )

with slider_c2:
    sim_price = st.slider(
        f"Expected Selling Price (₹ / Quintal) [Benchmark: ₹{base_price:,.0f}]",
        min_value=max(100.0, float(round(min_price * 0.7, 0))),
        max_value=float(round(max_price * 1.3, 0)),
        value=base_price,
        step=50.0
    )


# Calculate financials
fin = calculate_financials(
    crop_name=selected_crop,
    land_acres=farm_acres,
    custom_yield=sim_yield,
    custom_price=sim_price,
    district=district
)


# --------------------------------------------------
# FINANCIAL HEADLINE METRICS
# --------------------------------------------------
st.markdown("---")
st.markdown(f"## 📊 Financial Forecast: {selected_crop} ({farm_acres} Acres)")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="fin-metric-card">
        <div class="fin-caption">Total Cultivation Cost</div>
        <div class="fin-num" style="color:#b91c1c;">₹{fin['total_cost']:,}</div>
        <div class="fin-sub">₹{fin['per_acre_cost']:,} / acre</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="fin-metric-card">
        <div class="fin-caption">Total Farm Output</div>
        <div class="fin-num">{fin['total_production_quintals']} Qtl</div>
        <div class="fin-sub">{fin['yield_per_acre']} Qtl / acre</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="fin-metric-card">
        <div class="fin-caption">Gross Revenue</div>
        <div class="fin-num">₹{fin['gross_revenue']:,}</div>
        <div class="fin-sub">@ ₹{fin['selling_price_per_quintal']:,} / Qtl</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="fin-metric-highlight">
        <div class="fin-caption" style="color:#124B2A; font-weight:800;">Projected Net Profit</div>
        <div class="fin-num" style="color:#155B32;">₹{fin['net_profit']:,}</div>
        <div class="fin-sub" style="color:#155B32; font-weight:700;">₹{fin['net_profit_per_acre']:,} / acre · <b>+{fin['roi_percentage']}% ROI</b></div>
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# DETAILED COST BREAKDOWN
# --------------------------------------------------
st.markdown("---")
b_col1, b_col2 = st.columns([1.2, 1.8])

with b_col1:
    st.markdown("### 📋 Input Cost Breakdown")
    cost_data = fin["cost_breakdown"]
    cost_df = pd.DataFrame([
        {"Cost Component": k, "Total Amount (₹)": v, "Per Acre (₹)": round(v / farm_acres, 2)}
        for k, v in cost_data.items()
    ])
    st.dataframe(cost_df, use_container_width=True, hide_index=True)

    st.markdown(f"""
    <div style="background:var(--secondary-background-color); border:1px solid rgba(128,128,128,0.22); padding:16px; border-radius:14px; margin-top:12px;">
        <div style="margin-bottom:6px;"><b>⚖️ Break-Even Price:</b> <span style="color:#155B32; font-weight:700;">₹{fin['break_even_price']:,} / Quintal</span></div>
        <div style="font-size:12px; opacity:0.8; margin-bottom:10px;">Minimum market price required per quintal to cover all cultivation costs.</div>
        <div><b>🌾 Break-Even Yield:</b> <span style="color:#155B32; font-weight:700;">{fin['break_even_yield']:.2f} Qtl / Acre</span></div>
        <div style="font-size:12px; opacity:0.8;">Minimum harvest volume required per acre to avoid operational losses.</div>
    </div>
    """, unsafe_allow_html=True)

with b_col2:
    st.markdown("### 📊 Operational Expense Distribution")
    chart_df = pd.DataFrame(
        {"Amount (₹)": list(cost_data.values())},
        index=list(cost_data.keys())
    )
    st.bar_chart(chart_df, color="#23834B")


# --------------------------------------------------
# SCENARIO SENSITIVITY ANALYSIS
# --------------------------------------------------
st.markdown("---")
st.markdown("## 📈 Sensitivity & Risk Scenario Analysis")
st.caption("Compare how your farm net income performs across adverse vs. peak market seasons.")

scenarios = fin["scenarios"]
scen_rows = [
    {
        "Scenario": "📉 Conservative (Dry spell / 12% price dip)",
        "Yield / Acre": f"{scenarios['conservative']['yield_per_acre']} Qtl",
        "Selling Price": f"₹{scenarios['conservative']['price']:,}/Qtl",
        "Gross Revenue": f"₹{scenarios['conservative']['gross_revenue']:,}",
        "Net Profit": f"₹{scenarios['conservative']['net_profit']:,}",
        "ROI (%)": f"{scenarios['conservative']['roi']}%",
    },
    {
        "Scenario": "🎯 Expected (Normal season & modal APMC rate)",
        "Yield / Acre": f"{scenarios['expected']['yield_per_acre']} Qtl",
        "Selling Price": f"₹{scenarios['expected']['price']:,}/Qtl",
        "Gross Revenue": f"₹{scenarios['expected']['gross_revenue']:,}",
        "Net Profit": f"₹{scenarios['expected']['net_profit']:,}",
        "ROI (%)": f"{scenarios['expected']['roi']}%",
    },
    {
        "Scenario": "🚀 Optimistic (Peak yield & high festive market prices)",
        "Yield / Acre": f"{scenarios['optimistic']['yield_per_acre']} Qtl",
        "Selling Price": f"₹{scenarios['optimistic']['price']:,}/Qtl",
        "Gross Revenue": f"₹{scenarios['optimistic']['gross_revenue']:,}",
        "Net Profit": f"₹{scenarios['optimistic']['net_profit']:,}",
        "ROI (%)": f"{scenarios['optimistic']['roi']}%",
    },
]

st.dataframe(pd.DataFrame(scen_rows), use_container_width=True, hide_index=True)


# --------------------------------------------------
# MSP AND AGRONOMIC ADVISORY
# --------------------------------------------------
msp_val = fin.get("msp", 0)
msp_text = f"Government Minimum Support Price (MSP): **₹{msp_val:,} / Quintal**." if msp_val > 0 else "Commercial crop traded in open APMC mandis without statutory MSP."

st.markdown(f"""
<div class="tip-callout">
    💡 <b>Government Support & Risk Rating:</b><br>
    {msp_text} Risk Level is evaluated as <b>{fin['risk_level']}</b>.<br>
    <b>Advisory Note:</b> {fin['notes']}
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# NAVIGATION FOOTER
# --------------------------------------------------
st.markdown("---")
btn_l, btn_r = st.columns(2)

with btn_l:
    if st.button("← Back to Market Mandi Rates", use_container_width=True):
        st.switch_page("pages/5_Market_Prices.py")

with btn_r:
    if st.button("Explore Crop Recommendations →", use_container_width=True):
        st.switch_page("pages/3_Crop_Recommendations.py")

st.markdown("""
<div style="text-align:center;opacity:0.75;padding:26px 0;font-size:13px;letter-spacing:1px;">
    AGRINIRNAY · SMART CROP DECISIONS FOR KARNATAKA
</div>
""", unsafe_allow_html=True)