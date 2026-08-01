"""
MomentumHQ Dashboard
Version 2.0.0
"""

import streamlit as st

from config import (
    APP_NAME,
    VERSION,
    DEFAULT_TICKER,
    DEFAULT_WATCHLIST,
)

from market import (
    search_quote,
    format_price,
    format_volume,
    format_market_cap,
)


def render():

    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    st.divider()

    # -----------------------------
    # Search
    # -----------------------------

    if "quote" not in st.session_state:
        st.session_state.quote = None

    col1, col2 = st.columns([4, 1])

    with col1:

        ticker = st.text_input(
            "ASX Code",
            value=DEFAULT_TICKER,
        ).upper()

    with col2:

        st.write("")
        search = st.button(
            "Search",
            use_container_width=True,
        )

    if search:

        with st.spinner("Retrieving market data..."):

            st.session_state.quote = search_quote(ticker)

    quote = st.session_state.quote

    # -----------------------------
    # Quote
    # -----------------------------

    if quote:

        st.subheader(quote["company"])

        row1 = st.columns(4)

        with row1[0]:
            st.metric(
                "Price",
                format_price(quote["price"]),
            )

        with row1[1]:
            st.metric(
                "Change",
                quote["percent"],
            )

        with row1[2]:
            st.metric(
                "Volume",
                format_volume(quote["volume"]),
            )

        with row1[3]:
            st.metric(
                "Previous Close",
                format_price(
                    quote["previous_close"]
                ),
            )

        row2 = st.columns(3)

        with row2[0]:
            st.metric(
                "Day High",
                format_price(
                    quote["high"]
                ),
            )

        with row2[1]:
            st.metric(
                "Day Low",
                format_price(
                    quote["low"]
                ),
            )

        with row2[2]:
            st.metric(
                "Market Cap",
                format_market_cap(
                    quote["market_cap"]
                ),
            )

    else:

        st.info(
            "Search for an ASX stock to begin."
        )

    st.divider()

    # -----------------------------
    # Watchlist
    # -----------------------------

    st.subheader("Watchlist")

    table = []

    for symbol in DEFAULT_WATCHLIST:

        q = search_quote(symbol)

        if q:

            table.append(
                {
                    "Ticker": symbol.replace(".AX", ""),
                    "Price": format_price(q["price"]),
                    "Change": q["percent"],
                    "Volume": format_volume(
                        q["volume"]
                    ),
                }
            )

        else:

            table.append(
                {
                    "Ticker": symbol.replace(".AX", ""),
                    "Price": "-",
                    "Change": "-",
                    "Volume": "-",
                }
            )

    st.dataframe(
        table,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    st.caption(
        f"{APP_NAME} • Version {VERSION}"
    )