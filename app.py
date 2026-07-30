import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MomentumHQ",
    page_icon="📈",
    layout="wide"
)

st.title("📈 MomentumHQ")
st.caption("AI-powered ASX Momentum Trading Assistant")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Market Status", "🟢 Ready")

with col2:
    st.metric("High Priority Alerts", "4")

with col3:
    st.metric("Trade Candidates", "3")

with col4:
    st.metric("Watchlist", "12")

st.divider()

alerts = pd.DataFrame(
    [
        ["09:18", "CNB", "Trading Halt Lifted", "🔴 High"],
        ["09:41", "MLX", "Resource Upgrade", "🟠 Medium"],
        ["10:12", "VEA", "Broker Upgrade", "🟡 Low"],
        ["10:35", "CAY", "Exploration Results", "🟠 Medium"],
    ],
    columns=["Time", "Ticker", "Announcement", "Priority"]
)

candidates = pd.DataFrame(
    [
        ["CNB", 96, "BUY"],
        ["MLX", 91, "WATCH"],
        ["VEA", 88, "WATCH"],
    ],
    columns=["Ticker", "Score", "Action"]
)

left, right = st.columns([2,1])

with left:

    st.subheader("🔥 High Priority Alerts")
    st.dataframe(alerts, use_container_width=True, hide_index=True)

    st.subheader("⭐ Momentum Candidates")
    st.dataframe(candidates, use_container_width=True, hide_index=True)

    st.subheader("📰 Latest ASX Announcements")
    st.info("Live announcement feed coming in Version 0.3")

with right:

    st.subheader("📊 Market Movers")

    st.metric("Top Gainer", "CNB +18.4%")
    st.metric("Top Volume", "MLX")

    st.subheader("👀 Watchlist")

    st.write("• CNB")
    st.write("• MLX")
    st.write("• VEA")
    st.write("• CAY")

st.divider()

st.success("MomentumHQ Version 0.2.1")