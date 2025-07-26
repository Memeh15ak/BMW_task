import pandas as pd
import numpy as np

labor_df = pd.read_csv("data/labor_standards.csv")
parts_df = pd.read_csv("data/part_prices.csv")
rates_df = pd.read_csv("data/region_rates.csv")

def convert_numpy_types(obj):
    """Convert numpy types to native Python types"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

def estimate_repair(parts: list, region: str, markup_percent: float = 10):
    # Calculate values and convert NumPy types to native Python types
    total_labor = labor_df[labor_df["part_id"].isin(parts)]["labor_hours"].sum()
    total_labor = convert_numpy_types(total_labor)
    
    labor_rate = rates_df[rates_df["region"] == region]["rate_per_hour"].values[0]
    labor_rate = convert_numpy_types(labor_rate)
    
    labor_cost = total_labor * labor_rate
    
    part_cost = parts_df[parts_df["part_id"].isin(parts)]["price_inr"].sum()
    part_cost = convert_numpy_types(part_cost)
    
    subtotal = labor_cost + part_cost
    total_cost = subtotal + (markup_percent / 100) * subtotal

    return {
        "region": str(region),
        "labor_hours": convert_numpy_types(total_labor),
        "labor_cost": convert_numpy_types(labor_cost),
        "part_cost": convert_numpy_types(part_cost),
        "markup_percent": convert_numpy_types(markup_percent),
        "final_cost": convert_numpy_types(round(total_cost, 2)),
        "currency": "INR" if region == "India" else "USD"
    }