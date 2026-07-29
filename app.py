import streamlit as st

# Configure the page
st.set_page_config(
    page_title="MomentumHQ",
    page_icon="📈",
    layout="wide"
)

# Header
st.title("📈 MomentumHQ")
st.subheader("AI-powered ASX Momentum Trading Assistant")

# Welcome message
st.success("🎉 Congratulations! Your first Streamlit application is running.")

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Market Status", value="Ready")

with col2:
    st.metric(label="High Priority Alerts", value="0")

with col3:
    st.metric(label="Trade Candidates", value="0")

st.divider()

st.header("Project Roadmap")

tasks = [
    "Live ASX Announcements",
    "AI News Summaries",
    "Momentum Scoring",
    "Watchlists",
    "Telegram Alerts",
    "Trading Journal",
]

for task in tasks:
    st.checkbox(task, value=False)

st.info("Version 0.1 - Welcome to MomentumHQ")