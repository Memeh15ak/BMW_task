import streamlit as st
from datetime import datetime
from model.forcast import predict_buy_or_wait

st.set_page_config(page_title="Buy or Wait Advisor", page_icon="📈")

st.title("📦 BMW Part Price Advisor")

price = st.number_input("Current Price (INR)", value=3500)
month = datetime.now().month

if st.button("Should I Buy or Wait?"):
    result = predict_buy_or_wait(price, month)
    st.success(f"📢 Recommendation: **{result}**")
