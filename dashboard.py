import streamlit as st

from config import APP_NAME, VERSION, DEFAULT_WATCHLIST
from market import search_quote, format_price, format_volume
from momentum import demo_score
from announcements import get_announcements


def render():

    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    if "quote" not in st.session_state:
        st.session_state.quote = None

    col1, col2 = st.columns([3, 1])

    with col1:
        ticker = st.text_input(
            "ASX Code",
            value="BHP"
        ).upper()

    with col2:
        st.write("")
        if st.button(
            "Get Quote",
            use_container_width=True,
        ):
            st.session_state.quote = search_quote(ticker)

    quote = st.session_state.quote

    if quote:

        st.subheader(quote.get("symbol", ""))

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Price",
            format_price(
                quote.get("price")
            ),
        )

        c2.metric(
            "Change",
            quote.get("percent", "-"),
        )

        c3.metric(
            "Volume",
            format_volume(
                quote.get("volume")
            ),
        )

        c4.metric(
            "Previous Close",
            format_price(
                quote.get("previous_close")
            ),
        )

    st.divider()

    st.subheader("Momentum")

    score = demo_score()

    st.progress(score["overall"] / 100)

    left, right = st.columns(2)

    with left:
        st.metric(
            "Announcement",
            score["announcement"],
        )

        st.metric(
            "Technical",
            score["technical"],
        )

    with right:
        st.metric(
            "Overall",
            score["overall"],
        )

        st.success(
            score["recommendation"]
        )

    st.divider()

    st.subheader("Latest ASX Announcements")

    announcements = get_announcements(10)

    if announcements:

        for item in announcements:

            category = item["category"]

            if category == "Major Contract":
                icon = "🟢"

            elif category == "Quarterly":
                icon = "🟡"

            elif category in [
                "Capital Raising",
                "Trading Halt",
                "Director Selling",
            ]:
                icon = "🔴"

            else:
                icon = "⚪"

            st.markdown(
                f"""
**{icon} {item['title']}**

*{item['published']}*

Category: **{category}**

---
"""
            )

    else:

        st.info(
            "No announcements available."
        )

    st.subheader("Watchlist")

    for code in DEFAULT_WATCHLIST:
        st.write(f"• {code}")

    st.caption(
        f"{APP_NAME} v{VERSION}"
    )