"""
MomentumHQ Dashboard
Version 2.3.0
"""

import streamlit as st

from config import APP_NAME, VERSION, DEFAULT_TICKER
from dashboard_home import render as render_home
from dashboard_news import render as render_news
from dashboard_watchlist import render as render_watchlist


def render():

    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    st.divider()

    if "ticker" not in st.session_state:
        st.session_state.ticker = DEFAULT_TICKER

    ticker = st.text_input(
        "ASX Code",
        value=st.session_state.ticker,
    ).upper()

    st.session_state.ticker = ticker

    tab1, tab2, tab3 = st.tabs([
        "📊 Dashboard",
        "📢 Announcements",
        "⭐ Watchlist",
    ])

    with tab1:
        render_home(ticker)

    with tab2:
        render_news(ticker)

    with tab3:
        render_watchlist()

    st.divider()
    st.caption(f"{APP_NAME} • Version {VERSION}")
