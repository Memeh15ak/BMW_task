import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load("model/pricing_model.pkl")

def explain_prediction(price: float, month: int):
    df = pd.DataFrame([[price, month]], columns=["price_inr", "month"])
    explainer = shap.Explainer(model)
    shap_values = explainer(df)

    # Show explanation plot
    shap.plots.waterfall(shap_values[0], show=True)
