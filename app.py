import streamlit as st
import feedparser
import pandas as pd

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="MomentumHQ",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("📈 MomentumHQ")
st.caption("AI-powered ASX Momentum Trading Assistant")

st.divider()

# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------

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

# -------------------------------------------------------
# Sample Data
# -------------------------------------------------------

alerts = pd.DataFrame(
    [
        ["09:18", "CNB", "Trading Halt Lifted", "🔴 High"],
        ["09:41", "MLX", "Resource Upgrade", "🟠 Medium"],
        ["10:12", "VEA", "Broker Upgrade", "🟡 Low"],
        ["10:35", "CAY", "Exploration Results", "🟠 Medium"],
    ],
    columns=["Time", "Ticker", "Announcement", "Priority"],
)

candidates = pd.DataFrame(
    [
        ["CNB", 96, "BUY"],
        ["MLX", 91, "WATCH"],
        ["VEA", 88, "WATCH"],
    ],
    columns=["Ticker", "Score", "Action"],
)

left, right = st.columns([2, 1])

# =======================================================
# LEFT COLUMN
# =======================================================

with left:

    st.subheader("🔥 High Priority Alerts")
    st.dataframe(alerts, use_container_width=True, hide_index=True)

    st.subheader("⭐ Momentum Candidates")
    st.dataframe(candidates, use_container_width=True, hide_index=True)

    st.subheader("📰 Latest ASX Announcements")

announcement_df = pd.DataFrame(
    columns=[
        "Time",
        "Ticker",
        "Headline",
        "Momentum",
        "Recommendation",
    ]
)

st.dataframe(
    announcement_df,
    use_container_width=True,
    hide_index=True,
)
    # ---------------------------------------------------
    # Momentum Scoring Engine
    # ---------------------------------------------------

    def score_announcement(
        announcement,
        price_above_ema9,
        ema9_above_ema20,
        above_vwap,
        volume_ratio,
        turnover,
    ):

        score = 0
        reasons = []

        announcement_scores = {
            "Trading Halt Lifted": 40,
            "Major Acquisition": 35,
            "Major Contract": 35,
            "Resource Upgrade": 30,
            "Drill Results": 30,
            "Quarterly": 20,
            "Broker Upgrade": 15,
            "Capital Raising": -30,
            "Director Selling": -20,
            "Suspension": -40,
        }

        if announcement in announcement_scores:
            pts = announcement_scores[announcement]
            score += pts
            reasons.append((announcement, pts))

        if price_above_ema9:
            score += 10
            reasons.append(("Above EMA9", 10))

        if ema9_above_ema20:
            score += 10
            reasons.append(("EMA9 above EMA20", 10))

        if above_vwap:
            score += 10
            reasons.append(("Above VWAP", 10))

        if volume_ratio >= 3:
            score += 10
            reasons.append(("High Volume Ratio", 10))

        if turnover >= 5:
            score += 10
            reasons.append(("Turnover > $5M", 10))

        return score, reasons

    score, reasons = score_announcement(
        announcement="Trading Halt Lifted",
        price_above_ema9=True,
        ema9_above_ema20=True,
        above_vwap=True,
        volume_ratio=5,
        turnover=12,
    )

    st.divider()

    st.subheader("🧠 Momentum Score Test")

    st.metric("Score", score)

    for reason, pts in reasons:
        st.write(f"✅ {reason}: +{pts}")

    st.divider()

    st.subheader("📰 RSS Feed Test")

    feed = feedparser.parse(
        "https://www.afr.com/rss/markets"
    )

    if feed.entries:
        for article in feed.entries[:5]:
            st.write(f"• {article.title}")
    else:
        st.error("No RSS feed found.")

# =======================================================
# RIGHT COLUMN
# =======================================================

with right:

    st.subheader("📊 Market Movers")

    st.metric("Top Gainer", "CNB +18.4%")
    st.metric("Top Volume", "MLX")

    st.subheader("👀 Watchlist")

    st.write("• CNB")
    st.write("• MLX")
    st.write("• VEA")
    st.write("• CAY")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.divider()

st.success("MomentumHQ Version 0.2.2")