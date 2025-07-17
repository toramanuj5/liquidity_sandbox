import streamlit as st

st.set_page_config(page_title="Agentic AI Sandbox", layout="wide")
st.title("🚀 Agentic AI Sandbox for Liquidity Risk")

st.markdown("""
Welcome to your Liquidity Risk Sandbox.

Upload policy documents or balance sheets below, and run regulatory compliance or liquidity metrics.
""")

uploaded_file = st.file_uploader("📄 Upload a regulatory PDF or balance sheet CSV", type=["pdf", "csv"])
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
    # Placeholder for logic to process PDF/CSV
