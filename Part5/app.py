import streamlit as st
from agent import agent

st.title("🔧 BMW Dealer AI Assistant")

query = st.text_input("Ask something (e.g., Estimate cost for VIN X1X52023DM...)")

if query:
    with st.spinner("Thinking..."):
        response = agent.run(query)
        st.success(response)
