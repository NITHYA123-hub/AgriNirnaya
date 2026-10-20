"""Crop recommendation engine for AgriNirnay."""

from pathlib import Path
from typing import Any, Dict, List, Optional
import pandas as pd

DATA_PATH = Path("data") / "crop_dataset.csv"

_CACHED_DF: Optional[pd.DataFrame] = None


def load_dataset() -> pd.DataFrame:
    """Load and return the master crop dataset."""
    global _CACHED_DF
    if _CACHED_DF is not None:
        return _CACHED_DF

    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Master dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH, encoding="utf-8")
    _CACHED_DF = df
    return df


def get_all_crop_names() -> List[str]:
    """Return a sorted list of unique crop names."""
    df = load_dataset()
    return sorted(df["crop"].unique().tolist())


def get_all_districts() -> List[str]:
    """Return a list of all Karnataka districts present in the dataset."""
    df = load_dataset()
    districts = [d for d in df["district"].unique().tolist() if d != "All Districts"]
    return sorted(districts)


def get_all_categories() -> List[str]:
    """Return a sorted list of crop categories."""
    df = load_dataset()
    return sorted(df["category"].unique().tolist())


def get_district_default_crop(district: str) -> str:
    """Return the most culturally and agronomically signature staple crop for a district."""
    d = (district or "").strip().lower()

    # Major district staple associations
    if d in ["mandya", "mysuru", "raichur", "ballari", "koppal", "udupi", "dakshina kannada", "uttara kannada", "yadgir"]:
        return "Paddy (Rice)"
    elif d in ["bengaluru rural", "bengaluru urban", "tumakuru", "kolar", "chikkaballapur", "ramanagara"]:
        return "Ragi (Finger Millet)"
    elif d in ["davanagere", "haveri", "belagavi", "chitradurga"]:
        return "Maize (Corn)"
    elif d in ["kalaburagi", "bidar"]:
        return "Red Gram (Tur / Pigeon Pea)"
    elif d in ["vijayapura", "bagalkot", "gadag"]:
        return "Jowar (Sorghum)"
    elif d in ["dharwad"]:
        return "Bengal Gram (Chickpea / Chana)"
    elif d in ["shivamogga"]:
        return "Paddy (Rice)"
    elif d in ["hassan"]:
        return "Potato"
    elif d in ["chamarajanagar"]:
        return "Turmeric"
    elif d in ["kodagu", "chikkamagaluru"]:
        return "Coffee (Arabica / Robusta)"
    elif d in ["vijayanagara"]:
        return "Cotton"

    return "Ragi (Finger Millet)"


def get_crop_profile(crop_name: str, district: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Return detailed agronomic and economic profile for a specific crop."""
    df = load_dataset()
    crop_df = df[df["crop"] == crop_name]

    if crop_df.empty:
        return None

    # District specific row if available
    if district and district != "All Districts":
        dist_row = crop_df[crop_df["district"].str.lower() == district.lower()]
        if not dist_row.empty:
            return dist_row.iloc[0].to_dict()

    # Fallback to All Districts or first row
    all_dist = crop_df[crop_df["district"] == "All Districts"]
    if not all_dist.empty:
        return all_dist.iloc[0].to_dict()

    return crop_df.iloc[0].to_dict()


def recommend_crops(
    district: str,
    season: str,
    water_availability: str,
    soil_type: Optional[str] = None,
    ph: Optional[float] = None,
    nitrogen: Optional[float] = None,
    phosphorus: Optional[float] = None,
    potassium: Optional[float] = None,
    category_filter: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Evaluate and rank crops strictly based on district adaptation, season, water, and soil."""
    df = load_dataset()

    unique_crops = df["crop"].unique()
    recommendations = []

    district_clean = (district or "Mandya").strip().lower()
    season_clean = (season or "Kharif").strip().lower()
    water_clean = (water_availability or "Moderate").strip().lower()

    for crop_name in unique_crops:
        crop_rows = df[df["crop"] == crop_name]
        # Match specific district row
        match_district_row = crop_rows[crop_rows["district"].str.lower() == district_clean]
        is_district_native = not match_district_row.empty

        if is_district_native:
            crop_info = match_district_row.iloc[0].to_dict()
        else:
            state_row = crop_rows[crop_rows["district"] == "All Districts"]
            crop_info = state_row.iloc[0].to_dict() if not state_row.empty else crop_rows.iloc[0].to_dict()

        if category_filter and category_filter != "All" and crop_info["category"] != category_filter:
            continue

        crop_season = str(crop_info["season"]).strip().lower()
        crop_category = str(crop_info["category"]).strip().lower()
        crop_water = str(crop_info["water_requirement"]).strip().lower()

        # Strict eligibility: Plantation crops (Arecanut, Coffee, Coconut) are multi-year trees
        # They should NOT be recommended for a seasonal Kharif/Rabi field crop request unless in their specific home plantation belt
        is_plantation = crop_category in ["plantation"]
        if is_plantation and season_clean in ["kharif", "rabi", "summer"] and not is_district_native:
            continue

        score = 0
        reasons = []

        # 1. District Adaptation (0 to 40 pts)
        if is_district_native:
            score += 40
            reasons.append(f"Major proven crop historically cultivated in {district}")
        else:
            # If not grown in this district, heavy penalty for regional crops
            if is_plantation:
                score -= 30
            else:
                score += 10
                reasons.append(f"Adaptable to Southern/Northern Karnataka plains")

        # 2. Season Compatibility (0 to 30 pts)
        if crop_season == season_clean:
            score += 30
            reasons.append(f"Optimal {crop_info['season']} sowing and growing window")
        elif crop_season in ["annual", "all seasons", "multi-season"]:
            if is_district_native:
                score += 20
                reasons.append("Annual/Multi-season crop suitable for planting")
            else:
                score += 5
        else:
            # Opposite season (e.g. Rabi crop requested during Kharif)
            score -= 25
            reasons.append(f"Off-season: Primarily a {crop_info['season']} crop")

        # 3. Water Availability Match (0 to 20 pts)
        if water_clean == "high":
            if crop_water == "high":
                score += 20
                reasons.append("Ample water availability matches high water requirement")
            elif crop_water == "moderate":
                score += 18
                reasons.append("Adequate water supply for optimal vegetative growth")
            else:
                score += 15
                reasons.append("Hardy crop; will thrive with available water")
        elif water_clean == "moderate":
            if crop_water == "moderate":
                score += 20
                reasons.append("Matches moderate irrigation availability perfectly")
            elif crop_water == "low":
                score += 18
                reasons.append("Drought tolerant; low water stress risk")
            else:
                score -= 15
                reasons.append("High water demand: Requires assured irrigation")
        elif water_clean == "low":
            if crop_water == "low":
                score += 20
                reasons.append("Highly drought-hardy; thrives under rainfed / low moisture")
            elif crop_water == "moderate":
                score += 5
                reasons.append("Can yield reasonably with protective irrigation")
            else:
                score -= 35
                reasons.append("High water crop NOT recommended under low water availability")

        # 4. Soil Type Match (0 to 10 pts)
        if soil_type:
            soil_norm = soil_type.lower()
            crop_soils = str(crop_info["soil_type"]).lower()
            if any(term in crop_soils for term in soil_norm.split()):
                score += 10
                reasons.append(f"Well-suited to {soil_type} soil texture")
            else:
                score += 3

        # 5. Soil pH Match (0 to 5 pts)
        if ph is not None and ph > 0:
            min_ph = float(crop_info.get("min_ph", 5.5))
            max_ph = float(crop_info.get("max_ph", 7.5))
            if min_ph <= ph <= max_ph:
                score += 5
                reasons.append(f"Soil pH ({ph:.1f}) is within ideal range ({min_ph}-{max_ph})")
            else:
                score -= 5

        # Clamp score between 15 and 98
        final_score = max(15, min(98, score))

        # Only qualify if season and district compatibility are reasonable
        if final_score >= 80:
            badge = "Highly Recommended"
            badge_color = "#1b6d3b"
        elif final_score >= 65:
            badge = "Recommended"
            badge_color = "#2e7d32"
        elif final_score >= 50:
            badge = "Moderately Suitable"
            badge_color = "#d97706"
        else:
            badge = "Marginally Feasible"
            badge_color = "#dc2626"

        recommendations.append({
            "crop": crop_name,
            "category": crop_info["category"],
            "score": final_score,
            "badge": badge,
            "badge_color": badge_color,
            "reasons": reasons,
            "is_native": is_district_native,
            "season": crop_info["season"],
            "duration": crop_info["duration_display"],
            "water_requirement": crop_info["water_requirement"],
            "soil_type": crop_info["soil_type"],
            "cultivation_cost_per_acre": crop_info["cultivation_cost_per_acre"],
            "expected_yield": crop_info["expected_yield_quintal_per_acre"],
            "modal_price": crop_info["modal_price_inr_quintal"],
            "gross_revenue_per_acre": crop_info["expected_gross_revenue_per_acre"],
            "net_profit_per_acre": crop_info["expected_net_profit_per_acre"],
            "roi": crop_info["roi_percentage"],
            "market_apmc": crop_info["market_apmc"],
            "risk_level": crop_info["risk_level"],
            "notes": crop_info["notes"],
        })

    # Strict sorting: First by match score (descending), then native status, then ROI
    recommendations.sort(
        key=lambda x: (x["score"], 1 if x["is_native"] else 0, x["roi"]),
        reverse=True
    )
    return recommendations
