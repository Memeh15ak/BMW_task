import pandas as pd

labor_df = pd.read_csv("data/labor_standards.csv")
parts_df = pd.read_csv("data/part_prices.csv")
rates_df = pd.read_csv("data/region_rates.csv")

def estimate_repair(parts: list, region: str, markup_percent: float = 10):
    total_labor = labor_df[labor_df["part_id"].isin(parts)]["labor_hours"].sum()
    labor_rate = rates_df[rates_df["region"] == region]["rate_per_hour"].values[0]
    labor_cost = total_labor * labor_rate

    part_cost = parts_df[parts_df["part_id"].isin(parts)]["price_inr"].sum()
    subtotal = labor_cost + part_cost
    total_cost = subtotal + (markup_percent / 100) * subtotal

    return {
        "region": region,
        "labor_hours": total_labor,
        "labor_cost": labor_cost,
        "part_cost": part_cost,
        "markup_percent": markup_percent,
        "final_cost": round(total_cost, 2),
        "currency": "INR" if region == "India" else "USD"
    }
