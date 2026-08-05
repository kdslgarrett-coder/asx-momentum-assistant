"""
MomentumHQ Dashboard
Version 3.0.0-dev

Application workspace orchestration.
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_TAGLINE,
    DEFAULT_TICKER,
    FOOTER,
    VERSION,
)

from dashboard_research import render as render_research
from dashboard_insights import render as render_insights
from dashboard_news import render as render_news
from dashboard_watchlist import render as render_watchlist
from dashboard_morning_brief import render as render_morning_brief


TABS = (
    "🌅 Morning Brief",
    "🔎 Research",
    "📈 Opportunities",
    "💡 Insights",
    "📢 Announcements",
)


def render() -> None:
    """
    Render the MomentumHQ workspace.
    """

    st.title(APP_NAME)

    st.caption(APP_TAGLINE)

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
        morning_brief_tab,
        research_tab,
        opportunities_tab,
        insights_tab,
        announcements_tab,
    ) = st.tabs(TABS)

    with morning_brief_tab:
        render_morning_brief()

    with research_tab:
        render_research(ticker)

    with opportunities_tab:
        render_watchlist()

    with insights_tab:
        render_insights(ticker)

    with announcements_tab:
        render_news(ticker)

    st.divider()

    st.caption(FOOTER)