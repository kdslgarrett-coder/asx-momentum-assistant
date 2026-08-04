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
from watchlist import (
    get_watchlist,
    validate_and_add_ticker,
)


def render() -> None:
    """
    Render the user's watchlist.
    """

    st.subheader("⭐ Watchlist")

    st.markdown("### Add ASX Ticker")

    col1, col2 = st.columns([3, 1])

    with col1:
        ticker = st.text_input(
            "ASX Code",
            placeholder="e.g. KRR",
            label_visibility="collapsed",
        )

    with col2:
        add_clicked = st.button(
            "Add to Watchlist",
            use_container_width=True,
        )

    if add_clicked:

        status, message = validate_and_add_ticker(ticker)

        if status == "success":
            st.success(message)
            st.rerun()

        elif status == "warning":
            st.warning(message)

        else:
            st.error(message)

    st.divider()

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