"""
MomentumHQ Dashboard Watchlist
Version 2.6.0-dev

Presentation layer only.

Uses analysis_engine.py as the single source of truth.
"""

import streamlit as st

from analysis_engine import analyse_stock
from config import DEFAULT_WATCHLIST
from market import (
    format_price,
    format_volume,
)


def render():
    """Render the MomentumHQ watchlist."""

    st.subheader("⭐ Watchlist")

    rows = []

    for symbol in DEFAULT_WATCHLIST:

        analysis = analyse_stock(symbol)

        if analysis is None:
            continue

        quote = analysis["quote"]

        rows.append(
            {
                "Ticker": symbol.replace(".AX", ""),
                "Price": format_price(quote["price"]),
                "Change": quote["percent"],
                "Volume": format_volume(quote["volume"]),
                "Score": analysis["opportunity_score"],
                "Rating": analysis["rating"],
            }
        )

    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )