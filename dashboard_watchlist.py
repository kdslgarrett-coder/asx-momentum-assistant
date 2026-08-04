"""
MomentumHQ Dashboard Watchlist
Version 2.7.0-dev

Presentation layer only.

Watchlist data is provided by watchlist.py.
Analysis data is provided by analysis_engine.py.
"""

import streamlit as st

from analysis_engine import analyse_stock
from market import format_price
from watchlist import (
    get_watchlist,
    validate_and_add_ticker,
)


def render() -> None:
    """
    Render the user's opportunity watchlist.
    """

    st.subheader("⭐ My Opportunities")

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

        analysis = analyse_stock(symbol)

        if analysis is None:
            continue

        quote = analysis["quote"]

        rows.append(
            {
                "Ticker": symbol.replace(".AX", ""),
                "Score": analysis["opportunity_score"],
                "Rating": analysis["rating"],
                "Price": format_price(quote["price"]),
                "Change": quote["percent"],
                "Announcement": analysis["announcement_category"],
            }
        )

    rows.sort(
        key=lambda row: row["Score"],
        reverse=True,
    )

    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )