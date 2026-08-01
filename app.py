"""
MomentumHQ
Version 2.0.0
"""

import streamlit as st

from config import APP_NAME
from styles import load_css
from dashboard import render


st.set_page_config(
    page_title=APP_NAME,
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_css()

render()