# 🌱 AgriNirnay
### *Data-Driven Smart Crop Planning, Applied AI Decision Support & Financial Intelligence for Karnataka Farmers*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agrinirnaya.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SFIC 2026](https://img.shields.io/badge/Initiative-SFIC%202026-darkgreen.svg)]()
[![Institution](https://img.shields.io/badge/Institution-S--VYASA%20University-orange.svg)]()

> **🚀 Live Web Deployment:** https://agrinirnaya.streamlit.app/ 
> **📄 Comprehensive Project Report:** **[PROJECT_REPORT.md](project_Report.txt)**

---

## 📌 Overview

**AgriNirnay** is an intelligent, localized agricultural decision-support platform engineered specifically for farmers, agricultural extension officers, and agribusiness planners across all **31 districts of Karnataka**. 

Farming decisions are historically vulnerable to fragmented information—unreliable weather forecasts, fluctuating APMC mandi auction prices, escalating cultivation costs, and uncertainty about which crop genuinely suits local soil nutrients. **AgriNirnay** unifies soil chemistry, agro-climatic district parameters, real-time satellite weather, APMC mandi economics, and financial modeling into a single, high-contrast, beautiful interface.

Developed under the **Smart Farming Innovation Challenge (SFIC 2026)** theme **"Samriddh Annadata, Samriddh Bharat"**, AgriNirnay bridges the gap between academic agronomy, data science, and grassroots farm planning.

---

## 👥 Project Team & Credentials

* **Institution:** S-VYASA Deemed to be University, Bengaluru, Karnataka
* **Project Team:**
  * **Nithya L** — Lead Developer, Application Architecture, Master Dataset Engineering & UX
  * **Mandara G.V** — Crop Recommendation Scoring Engine & Agronomic Rules
  * **Rishi M.S** — Satellite Weather Integration & Soil Report OCR
  * **Hiten** — APMC Mandi Intelligence & Financial Estimates

---

## ✨ Key Capabilities & Modules

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AgriNirnay Guided Workflow                           │
│                                                                                  │
│  1. Farm Details ──► 2. Soil Health ──► 3. AI Crop Spotlight                     │
│         ▲                                       │                                │
│         │                                       ▼                                │
│  6. Cost & ROI  ◄── 5. Market Mandi ◄── 4. Satellite Weather                     │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### 1. 🚜 Farm Profiling & Baseline Parameters ([pages/1_Farm_Details.py](pages/1_Farm_Details.py))
* **Full Geographic Coverage:** Complete coverage across all 31 districts of Karnataka.
* **Seasonal Sowing Windows:** Tailored options for **Kharif**, **Rabi**, and **Summer** seasons.
* **Hydrological Availability:** Configurable water access (*Low / Rainfed*, *Moderate*, *High / Assured Irrigation*).
* **Land Area Scaling:** Scalable land input from marginal holdings (0.5 acres) to commercial estates (100+ acres).

### 2. 🧪 Soil Health Card OCR & Nutrient Profiling ([pages/2_Soil_Report.py](pages/2_Soil_Report.py))
* **Automated Document OCR:** Upload smartphone photos or PDF laboratory soil health cards to extract **pH**, **Available Nitrogen (N)**, **Phosphorus (P)**, and **Potassium (K)**.
* **Graceful Fallback:** Farmers without a lab report can use smart regional soil defaults (*Red Loam*, *Black Cotton*, *Sandy Loam*, *Laterite*, *Alluvial*) pre-calibrated to their district.

### 3. 🌾 AI-Powered Single Crop Recommendation Spotlight ([pages/3_Crop_Recommendations.py](pages/3_Crop_Recommendations.py))
* **Single Best Match Focus:** Solves decision paralysis by spotlighting **only the #1 single best-matched crop** for the farm, complete with:
  * Suitability score (0–98%) with qualification badges (*Highly Recommended*, *Recommended*).
  * 4-factor suitability breakdown bars (District Climate, Season Window, Water Supply, Soil Nutrient Match).
  * Expected harvest yields, cultivation expenses, local mandi price, projected net profit, and ROI %.
* **Interactive Alternative Switcher:** Allows the farmer to inspect alternative high-scoring crops one at a time without cluttering the screen.
* **Authentic Regional Logic:** Strict agro-climatic validation ensures crops are agronomically proven in the farmer's district (e.g., Paddy in Mandya/Raichur, Ragi in Bengaluru/Tumakuru, Red Gram in Kalaburagi, Chilli in Haveri, Tomato in Kolar, Cotton in Ballari, Coffee in Kodagu).

### 4. 🌦️ Satellite Meteorology & Rainfall Forecasts ([pages/4_Weather.py](pages/4_Weather.py))
* **Hyper-Local API Integration:** Powered by the **Open-Meteo REST API** with automatic geocoding for all 31 Karnataka district headquarters.
* **Clear Rainfall Analytics:**
  * Displays **Today's Expected Rainfall Total** (mm) and **Precipitation Probability** (%).
  * Clear explanation of instantaneous radar readings (*0.0 mm indicates dry conditions right now*).
  * 3-day agricultural rainfall and temperature outlook with actionable field advisories.

### 5. 📈 APMC Mandi Market Intelligence ([pages/5_Market_Prices.py](pages/5_Market_Prices.py))
* **Live Benchmark Mandi Rates:** Real-time modal prices, daily min/max spreads, and government Minimum Support Price (MSP) benchmarks across Karnataka mandis.
* **District-Relevant Pricing:** Eliminates the bug where Arecanut prices (₹48,000/Qtl) appeared on cereal/pulse views. Prices synchronize directly with the farmer's selected crop.
* **Inter-District Price Spread:** Interactive comparison bar chart comparing produce prices across APMC mandis to help farmers choose the highest-realizing market destination.

### 6. 💰 Financial Planning, Cost Breakdown & ROI Simulator ([pages/6_Cost_and_Revenue.py](pages/6_Cost_and_Revenue.py))
* **Itemized Cultivation Cost Breakdown:**
  * Seeds & Planting Material
  * Fertilizers & Organic Manures
  * Irrigation & Plant Protection
  * Labor, Mechanization & Harvesting
* **Break-Even Analysis:** Calculates the exact break-even yield (Qtl/acre) and minimum selling price (₹/Qtl) needed to prevent operational loss.
* **Interactive Yield & Price Sliders:** Real-time recalculation of gross revenue, net profit, and ROI %.
* **3-Scenario Sensitivity Analysis:** Side-by-side risk comparison for *Conservative* (dry spell / price drop), *Expected* (normal modal), and *Optimistic* (bumper harvest / festive rates) seasons.

---

## 📊 Consolidated Master Dataset (`data/crop_dataset.csv`)

In compliance with project specifications, all legacy, partial, and Paddy-only datasets were consolidated into a single master dataset:

📁 `data/crop_dataset.csv`
* **Total Records:** 270 verified entries
* **Total Columns:** 33 agricultural and financial parameters
* **Distinct Crops:** 31 diverse Karnataka crops across 9 categories
* **Districts Covered:** All 31 Karnataka districts + Statewide baseline
* **Data Integrity:** 100% complete (0 null or missing values)

### Schema Overview:
| Column | Description |
| :--- | :--- |
| `crop_id` | Unique identifier (e.g. `CR_0001`) |
| `crop` | Commodity name (e.g. *Paddy, Ragi, Maize, Red Gram, Groundnut, Sugarcane, Cotton, Tomato, Chilli*) |
| `category` | Cereal, Millet, Pulse, Oilseed, Commercial, Vegetable, Fruit, Spice, Plantation |
| `district` | Karnataka district name (e.g. *Mandya, Kalaburagi, Haveri, Dharwad, Kolar*) |
| `season` | Kharif, Rabi, Summer, Annual |
| `soil_type` | Optimal soil classifications (*Red Loam, Black Cotton, Laterite, etc.*) |
| `min_ph` / `max_ph` | Optimal pH range |
| `nitrogen_req_kg_ha` | Recommended Nitrogen (kg/ha) |
| `phosphorus_req_kg_ha`| Recommended Phosphorus (kg/ha) |
| `potassium_req_kg_ha` | Recommended Potassium (kg/ha) |
| `water_requirement` | Low, Moderate, High |
| `duration_display` | Growing duration in days/months |
| `market_apmc` | Primary APMC trading market |
| `modal_price_inr_quintal` | Benchmark modal price (₹/Quintal) |
| `cultivation_cost_per_acre` | Total cost of cultivation per acre (₹) |
| `expected_yield_quintal_per_acre` | Average expected yield (Quintals/acre) |
| `expected_net_profit_per_acre` | Projected net profit per acre (₹) |
| `roi_percentage` | Expected Return on Investment (%) |
| `notes` | Field advisory, recommended seed varieties, and management notes |

---

## 🏗️ Project Architecture & File Hierarchy

```
AgriNirnaya/
├── app.py                      # Multi-page Streamlit application registry & navigation
├── home.py                     # Landing page with hero banner, stats & module cards
├── crop_recommendation.py      # Core AI crop matching & scoring engine
├── market_data.py              # APMC mandi pricing service & comparison tools
├── financial_estimates.py      # Financial modeling, cost breakdown & ROI engine
├── soil_reader.py              # PDF/image OCR extractor for soil health cards
├── weather.py                  # Open-Meteo live weather & rainfall forecast client
├── generate_dataset.py         # Generator script for the unified master dataset
├── inspect_data.py             # Data integrity validation and inspection tool
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this document)
├── PROJECT_REPORT.md           # Full engineering and academic project report
├── data/
│   └── crop_dataset.csv        # The single consolidated master dataset
└── pages/
    ├── 1_Farm_Details.py       # Step 1: Farm location, size, season, and water input
    ├── 2_Soil_Report.py        # Step 2: Soil report OCR upload & nutrient status
    ├── 3_Crop_Recommendations.py# Step 3: Spotlight #1 single crop recommendation
    ├── 4_Weather.py            # Step 4: Live farm weather & 3-day rainfall outlook
    ├── 5_Market_Prices.py      # Step 5: Real-time APMC mandi commodity rates & trends
    └── 6_Cost_and_Revenue.py   # Step 6: Crop financial calculator & sensitivity modeling
```

---

## 🚀 Quickstart & Local Installation

### Prerequisites
* Python 3.10 or higher
* `pip` package manager
* (Optional for OCR) Tesseract OCR engine

### 1. Clone the Repository
```bash
git clone https://github.com/NITHYA123-hub/AgriNirnaya.git
cd AgriNirnaya
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv

# On Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# On Linux / macOS
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 🎨 Design Philosophy & UX Standards

* **Aesthetic Palette:** Deep forest green (`#092819`, `#124B2C`), emerald accents (`#23834B`), and crisp high-contrast cards (`#FFFFFF`, `#F4F9F5`).
* **Typography:** Professional Google Fonts—**Outfit** for bold, clean headings and **Plus Jakarta Sans** for readable body and metric labels.
* **Decision Clarity:** Unlike generic recommendation tools that overwhelm users with 30+ simultaneous options, AgriNirnay spotlights **only one best-matched crop** while providing single-item inspection for alternative options.
* **Prominent Farm Context Card:** Replaced faint secondary background pills with a solid white overview card featuring `2px solid #23834B` borders and high-contrast green labels, ensuring farm parameters (District, Season, Area, Water, Soil, pH) remain clearly visible on all devices.

---

## 🧪 Validation & Regional Testing

| District | Season | Water Level | Soil Texture | #1 Spotlight Crop | Match | Benchmark Mandi Rate | Expected Net Profit / Acre |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mandya** | Kharif | High | Red Loam | **Paddy (Rice)** | 98% | Mandya APMC (₹2,450/Qtl) | ₹38,700 |
| **Mandya** | Kharif | Moderate | Red Loam | **Ragi (Finger Millet)**| 98% | Mandya APMC (₹3,850/Qtl) | ₹47,600 |
| **Kalaburagi** | Kharif | Moderate | Black Cotton| **Red Gram (Tur)** | 98% | Kalaburagi APMC (₹8,400/Qtl)| ₹51,200 |
| **Vijayapura** | Rabi | Low | Black Soil | **Jowar (Maldandi)** | 98% | Vijayapura APMC (₹3,350/Qtl) | ₹28,200 |
| **Haveri** | Kharif | Moderate | Black Soil | **Chilli (Byadgi)** | 98% | Byadgi APMC (₹31,500/Qtl) | ₹4,10,000 |
| **Davanagere** | Kharif | Moderate | Red Loam | **Maize (Corn)** | 98% | Davanagere APMC (₹2,280/Qtl) | ₹45,840 |
| **Kolar** | Kharif | Moderate | Red Loam | **Tomato** | 98% | Kolar APMC (₹1,850/Qtl) | ₹2,98,500 |
| **Kodagu** | Annual | High | Laterite | **Coffee (Arabica)** | 98% | Madikeri Mandi (₹28,500/Qtl) | ₹1,58,000 |

---

## 📄 Documentation

For full academic, architectural, mathematical, and econometric details, please refer to the formal project report:  
👉 **[PROJECT_REPORT.md](PROJECT_REPORT.md)**

---

## 👥 Acknowledgments & Hackathon Context

Developed for **SFIC 2026** (Smart Farming Innovation Challenge) under the national theme:  
🌾 **Samriddh Annadata, Samriddh Bharat** (Prosperous Farmer, Prosperous India)

*Institution: S-VYASA Deemed to be University, Bengaluru, Karnataka*

---
*AgriNirnay — Empowering Karnataka Agriculture Through Intelligent Data.*
