import streamlit as st
from datetime import datetime

# Set up the app UI
st.set_page_config(page_title="KrishiMitra", layout="wide")

st.markdown("""
<style>
    .title {
        font-size:40px;
        font-weight:bold;
        color:#2E8B57;
    }
    .subtitle {
        font-size:20px;
        color:#555;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🌾 KrishiMitra</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Powered Daily Companion for Farmers</div>", unsafe_allow_html=True)

st.success("Use the sidebar to navigate through different features of KrishiMitra!")
