"""
MomentumHQ Dashboard
Version 2.5.3 Stable
"""

import streamlit as st

from config import APP_NAME, DEFAULT_TICKER, VERSION
from dashboard_home import render as render_home
from dashboard_insights import render as render_insights
from dashboard_news import render as render_news
from dashboard_watchlist import render as render_watchlist


def render() -> None:
    """
    Render the main MomentumHQ dashboard.
    """

    st.set_page_config(
        page_title=APP_NAME,
        layout="wide",
    )

    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    st.divider()

    st.session_state.setdefault("ticker", DEFAULT_TICKER)

    ticker = (
        st.text_input(
            "ASX Code",
            value=st.session_state.ticker,
            help="Enter an ASX ticker symbol (e.g. BHP, FMG, CBA).",
        )
        .strip()
        .upper()
    )

    st.session_state.ticker = ticker

    (
        dashboard_tab,
        announcements_tab,
        insights_tab,
        watchlist_tab,
    ) = st.tabs(
        [
            "📊 Dashboard",
            "📢 Announcements",
            "💡 Insights",
            "⭐ Watchlist",
        ]
    )

    with dashboard_tab:
        render_home(ticker)

    with announcements_tab:
        render_news(ticker)

    with insights_tab:
        render_insights(ticker)

    with watchlist_tab:
        render_watchlist()

    st.divider()
    st.caption(f"{APP_NAME} • Version {VERSION}")