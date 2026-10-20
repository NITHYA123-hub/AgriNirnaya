"""Market and APMC prices service for AgriNirnay."""

from pathlib import Path
from typing import Any, Dict, List, Optional
import pandas as pd

DATA_PATH = Path("data") / "crop_dataset.csv"


def load_market_data() -> pd.DataFrame:
    """Load the master dataset for market analysis."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Master dataset not found at {DATA_PATH}")
    return pd.read_csv(DATA_PATH, encoding="utf-8")


def get_market_prices(
    district: Optional[str] = None,
    crop: Optional[str] = None,
    category: Optional[str] = None,
    search_query: Optional[str] = None,
) -> pd.DataFrame:
    """Filter and return APMC market prices."""
    df = load_market_data()

    # Filter out state generic if a specific district is requested
    if district and district != "All Districts":
        df = df[df["district"].str.lower() == district.lower()]
    elif district == "All Districts":
        # show all individual district markets
        df = df[df["district"] != "All Districts"]

    if crop and crop != "All Crops":
        df = df[df["crop"] == crop]

    if category and category != "All Categories":
        df = df[df["category"] == category]

    if search_query:
        q = search_query.strip().lower()
        mask = (
            df["crop"].str.lower().str.contains(q, na=False)
            | df["market_apmc"].str.lower().str.contains(q, na=False)
            | df["district"].str.lower().str.contains(q, na=False)
        )
        df = df[mask]

    return df


def get_crop_district_comparison(crop_name: str) -> pd.DataFrame:
    """Compare prices for a single crop across all Karnataka APMC markets."""
    df = load_market_data()
    crop_df = df[(df["crop"] == crop_name) & (df["district"] != "All Districts")]
    return crop_df.sort_values(by="modal_price_inr_quintal", ascending=False)


def get_market_summary_metrics(district: Optional[str] = None, target_crop: Optional[str] = None) -> Dict[str, Any]:
    """Calculate key market highlight statistics tailored to the district and crop."""
    df = load_market_data()
    if district and district != "All Districts":
        subset = df[df["district"].str.lower() == district.lower()]
        if subset.empty:
            subset = df[df["district"] != "All Districts"]
    else:
        subset = df[df["district"] != "All Districts"]

    if subset.empty:
        return {
            "total_commodities": 0,
            "featured_crop": target_crop or "N/A",
            "featured_price": 0,
            "featured_market": "APMC Mandi",
            "rising_trends_count": 0,
            "avg_modal_price": 0,
        }

    # If target crop is provided and present in subset
    crop_match = subset[subset["crop"] == target_crop] if target_crop else pd.DataFrame()
    if not crop_match.empty:
        featured_row = crop_match.iloc[0]
    else:
        # Default to first staple in this district (usually Paddy, Ragi, or Maize)
        featured_row = subset.iloc[0]

    rising = subset[subset["price_trend"] == "Rising"].shape[0]

    return {
        "total_commodities": subset["crop"].nunique(),
        "featured_crop": featured_row["crop"],
        "featured_price": featured_row["modal_price_inr_quintal"],
        "featured_market": featured_row["market_apmc"],
        "featured_trend": featured_row["price_trend"],
        "rising_trends_count": rising,
        "avg_modal_price": round(subset["modal_price_inr_quintal"].mean(), 2),
    }
