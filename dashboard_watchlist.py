"""
MomentumHQ Dashboard Watchlist
Version 2.7.0-dev

Presentation layer only.

Watchlist data is provided by watchlist.py.
"""

import streamlit as st

from market import (
    format_price,
    format_volume,
    search_quote,
)
from watchlist import get_watchlist


def render() -> None:
    """
    Render the user's watchlist.
    """

    st.subheader("⭐ Watchlist")

    rows = []

    for symbol in get_watchlist():

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