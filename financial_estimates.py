"""Financial estimates and economic forecasting module for AgriNirnay."""

from typing import Any, Dict, Optional
from crop_recommendation import get_crop_profile


def calculate_financials(
    crop_name: str,
    land_acres: float = 1.0,
    custom_yield: Optional[float] = None,
    custom_price: Optional[float] = None,
    district: Optional[str] = None,
) -> Dict[str, Any]:
    """Calculate detailed input costs, gross revenue, net profit, and ROI."""
    profile = get_crop_profile(crop_name, district=district)
    if not profile:
        raise ValueError(f"Crop '{crop_name}' profile not found.")

    land_acres = max(0.1, float(land_acres))

    # Base per-acre values
    seed_cost_acre = float(profile["seed_cost_per_acre"])
    fert_cost_acre = float(profile["fertilizer_cost_per_acre"])
    irrig_cost_acre = float(profile["irrigation_pest_cost_per_acre"])
    labour_cost_acre = float(profile["labour_harvest_cost_per_acre"])
    total_cost_acre = seed_cost_acre + fert_cost_acre + irrig_cost_acre + labour_cost_acre

    # Yield and Price
    yield_acre = float(custom_yield) if custom_yield is not None else float(profile["expected_yield_quintal_per_acre"])
    price_qtl = float(custom_price) if custom_price is not None else float(profile["modal_price_inr_quintal"])

    # Totals for farm size
    total_seed = round(seed_cost_acre * land_acres, 2)
    total_fertilizer = round(fert_cost_acre * land_acres, 2)
    total_irrigation_pest = round(irrig_cost_acre * land_acres, 2)
    total_labour = round(labour_cost_acre * land_acres, 2)
    total_cost = round(total_cost_acre * land_acres, 2)

    total_production_qtl = round(yield_acre * land_acres, 2)
    gross_revenue = round(total_production_qtl * price_qtl, 2)
    net_profit = round(gross_revenue - total_cost, 2)
    net_profit_acre = round(net_profit / land_acres, 2)
    roi = round((net_profit / total_cost) * 100, 1) if total_cost > 0 else 0.0

    # Break-even metrics
    break_even_price = round(total_cost / total_production_qtl, 2) if total_production_qtl > 0 else 0.0
    break_even_yield = round(total_cost_acre / price_qtl, 2) if price_qtl > 0 else 0.0

    # Sensitivity scenarios
    # 1. Conservative (Dry spell / Price dip)
    cons_yield = round(yield_acre * 0.80, 2)
    cons_price = round(price_qtl * 0.88, 2)
    cons_rev = round(cons_yield * land_acres * cons_price, 2)
    cons_profit = round(cons_rev - total_cost, 2)
    cons_roi = round((cons_profit / total_cost) * 100, 1) if total_cost > 0 else 0.0

    # 2. Optimistic (Favorable weather / Peak market rate)
    opt_yield = round(yield_acre * 1.15, 2)
    opt_price = round(price_qtl * 1.12, 2)
    opt_rev = round(opt_yield * land_acres * opt_price, 2)
    opt_profit = round(opt_rev - total_cost, 2)
    opt_roi = round((opt_profit / total_cost) * 100, 1) if total_cost > 0 else 0.0

    return {
        "crop": crop_name,
        "category": profile["category"],
        "district": profile.get("district", "Karnataka"),
        "land_acres": land_acres,
        "duration": profile["duration_display"],
        "risk_level": profile["risk_level"],
        "msp": profile.get("msp_inr_quintal", 0),
        "yield_per_acre": yield_acre,
        "min_yield": profile["min_yield_quintal_per_acre"],
        "max_yield": profile["max_yield_quintal_per_acre"],
        "selling_price_per_quintal": price_qtl,
        "min_price": profile["min_price_inr_quintal"],
        "max_price": profile["max_price_inr_quintal"],
        "cost_breakdown": {
            "Seeds & Planting": total_seed,
            "Fertilizers & Manure": total_fertilizer,
            "Irrigation & Plant Protection": total_irrigation_pest,
            "Labour & Harvesting": total_labour,
        },
        "per_acre_cost": round(total_cost_acre, 2),
        "total_cost": total_cost,
        "total_production_quintals": total_production_qtl,
        "gross_revenue": gross_revenue,
        "net_profit": net_profit,
        "net_profit_per_acre": net_profit_acre,
        "roi_percentage": roi,
        "break_even_price": break_even_price,
        "break_even_yield": break_even_yield,
        "scenarios": {
            "conservative": {
                "yield_per_acre": cons_yield,
                "price": cons_price,
                "gross_revenue": cons_rev,
                "net_profit": cons_profit,
                "roi": cons_roi,
            },
            "expected": {
                "yield_per_acre": yield_acre,
                "price": price_qtl,
                "gross_revenue": gross_revenue,
                "net_profit": net_profit,
                "roi": roi,
            },
            "optimistic": {
                "yield_per_acre": opt_yield,
                "price": opt_price,
                "gross_revenue": opt_rev,
                "net_profit": opt_profit,
                "roi": opt_roi,
            },
        },
        "notes": profile["notes"],
    }
