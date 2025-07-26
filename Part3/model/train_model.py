import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("Part3/data/part_prices.csv")
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month
df['price_change'] = df['price_inr'].diff()
df['target'] = (df['price_inr'].shift(-1) > df['price_inr']).astype(int)

df.dropna(inplace=True)
X = df[['price_inr', 'month']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = XGBClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "Part3/model/pricing_model.pkl")
print("Model trained and saved.")
