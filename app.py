import streamlit as st
from styles import load_css
from dashboard import render

st.set_page_config(page_title="MomentumHQ", page_icon="📈", layout="wide")
load_css()
render()