"""
MomentumHQ Dashboard Watchlist
Version 2.3.0
"""

import streamlit as st

from config import DEFAULT_WATCHLIST

from market import (
    search_quote,
    format_price,
    format_volume,
)


def render():

    st.subheader("⭐ Watchlist")

    rows = []

    for symbol in DEFAULT_WATCHLIST:

        quote = search_quote(symbol)

        if quote:

            rows.append(
                {
                    "Ticker": symbol.replace(".AX", ""),
                    "Price": format_price(quote["price"]),
                    "Change": quote["percent"],
                    "Volume": format_volume(quote["volume"]),
                }
            )

    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )