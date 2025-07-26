from part4_repair_estimator.estimator import estimate_repair

def estimate_cost(parts: list, region: str) -> str:
    result = estimate_repair(parts, region)
    return f"Estimated cost: ₹{result['final_cost']} ({result['labor_hours']} hrs + parts)"
