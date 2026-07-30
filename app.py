import streamlit as st

from config import APP_NAME, VERSION
from styles import load_css
from market import search_quote, format_price, format_volume


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📈",
    layout="wide",
)

load_css()


# -------------------------------------------------
# Session State
# -------------------------------------------------

if "quote" not in st.session_state:
    st.session_state.quote = None


# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(f"<div class='main-title'>{APP_NAME}</div>", unsafe_allow_html=True)

st.markdown(
    f"<div class='subtitle'>Professional ASX Momentum Scanner &nbsp;&nbsp; v{VERSION}</div>",
    unsafe_allow_html=True,
)

st.divider()


# -------------------------------------------------
# Search
# -------------------------------------------------

st.markdown("## 🔎 Ticker Search")

col1, col2 = st.columns([4, 1])

with col1:
    ticker = st.text_input(
        "ASX Code",
        placeholder="Example: BHP",
        label_visibility="collapsed",
    )

with col2:

    get_quote = st.button(
        "Get Quote",
        use_container_width=True,
    )


if get_quote:

    if ticker.strip() == "":
        st.warning("Please enter an ASX ticker.")
    else:

        with st.spinner("Retrieving market data..."):

            quote = search_quote(ticker)

            if quote:
                st.session_state.quote = quote
            else:
                st.error("Unable to retrieve market data.")


st.divider()


# -------------------------------------------------
# Market Snapshot
# -------------------------------------------------

st.markdown("## 📊 Market Snapshot")

quote = st.session_state.quote

if quote is None:

    st.info("Search for an ASX company to begin.")

else:

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Price",
            format_price(quote["price"]),
        )

    with c2:
        st.metric(
            "Change",
            quote["change"],
            quote["percent"],
        )

    with c3:
        st.metric(
            "Volume",
            format_volume(quote["volume"]),
        )

    with c4:
        st.metric(
            "Previous Close",
            format_price(quote["previous_close"]),
        )


st.divider()


# -------------------------------------------------
# Momentum Score
# -------------------------------------------------

st.markdown("## ⚡ Momentum Score")

left, middle, right = st.columns(3)

announcement_score = 0
technical_score = 0
overall_score = announcement_score + technical_score

with left:
    st.metric(
        "Announcement Score",
        announcement_score,
    )

with middle:
    st.metric(
        "Technical Score",
        technical_score,
    )

with right:
    st.metric(
        "Overall Score",
        overall_score,
    )


# -------------------------------------------------
# Recommendation
# -------------------------------------------------

if overall_score >= 60:

    recommendation = "🟢 BUY"

elif overall_score >= 30:

    recommendation = "🟡 WATCH"

else:

    recommendation = "🔴 IGNORE"

st.markdown("### Recommendation")

st.success(recommendation)


st.divider()


# -------------------------------------------------
# Latest Announcements
# -------------------------------------------------

st.markdown("## 📢 Latest Announcements")

st.info(
    "Live ASX announcements will appear here in the next sprint."
)


st.divider()


# -------------------------------------------------
# Watchlist
# -------------------------------------------------

st.markdown("## ⭐ Watchlist")

watchlist = [
    "BHP",
    "FMG",
    "RIO",
    "CBA",
    "NST",
]

st.dataframe(
    watchlist,
    use_container_width=True,
    hide_index=True,
)


# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    f"{APP_NAME} • Version {VERSION}"
)