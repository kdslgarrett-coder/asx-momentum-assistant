import streamlit as st

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
    st.metric("High Priority Alerts", "0")

with col3:
    st.metric("Trade Candidates", "0")

with col4:
    st.metric("Watchlist", "0")

st.divider()

left, right = st.columns([2,1])

with left:

    st.subheader("🔥 High Priority Alerts")

    st.info("No high priority announcements.")

    st.subheader("⭐ Momentum Candidates")

    st.dataframe(
        {
            "Ticker": [],
            "Score": [],
            "Action": []
        },
        use_container_width=True
    )

    st.subheader("📰 Latest ASX Announcements")

    st.info("Waiting for live announcement feed...")

with right:

    st.subheader("📊 Market Movers")

    st.info("Coming soon")

    st.subheader("👀 Watchlist")

    st.info("No watchlist yet.")

st.divider()

st.success("MomentumHQ Version 0.2")