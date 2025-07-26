import joblib
import pandas as pd

model = joblib.load("model/pricing_model.pkl")

def predict_buy_or_wait(price: float, month: int) -> str:
    df = pd.DataFrame([[price, month]], columns=["price_inr", "month"])
    pred = model.predict(df)[0]
    return "Buy Now" if pred == 1 else "Wait"
