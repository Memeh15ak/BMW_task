import streamlit as st
from rag_qa import qa_chain

st.set_page_config(page_title="📄 BMW Document QA")

st.title("📄 Ask BMW Document")

query = st.text_input("Ask something from the PDF...")

if query:
    with st.spinner("Thinking..."):
        result = qa_chain.run(query)
        st.success(result)
