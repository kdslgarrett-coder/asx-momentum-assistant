"""
MomentumHQ Dashboard Home
Version 2.6.0-dev
"""

import streamlit as st
import plotly.graph_objects as go

from analysis_engine import analyse_stock
from market import (
    format_market_cap,
    format_price,
    format_volume,
)


def render(ticker):
    """
    Render the main dashboard.

    Technical scoring is now provided by analysis_engine.py.
    Behaviour is intentionally unchanged.
    """

    analysis = analyse_stock(ticker)

    if analysis is None:
        st.error("Unable to retrieve market data.")
        return

    quote = analysis["quote"]
    history = analysis["history"]
    indicators = analysis["indicators"]

    st.subheader(quote["company"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Price", format_price(quote["price"]))
    c2.metric("Change", quote["percent"])
    c3.metric("Volume", format_volume(quote["volume"]))
    c4.metric(
        "Previous Close",
        format_price(quote["previous_close"]),
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Day High", format_price(quote["high"]))
    c2.metric("Day Low", format_price(quote["low"]))
    c3.metric(
        "Market Cap",
        format_market_cap(quote["market_cap"]),
    )

    st.divider()

    if history is not None:

        st.subheader("Price Chart")

        fig = go.Figure()

        fig.add_trace(
            go.Candlestick(
                x=history.index,
                open=history["Open"],
                high=history["High"],
                low=history["Low"],
                close=history["Close"],
                name="Price",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=history.index,
                y=history["EMA9"],
                name="EMA 9",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=history.index,
                y=history["EMA20"],
                name="EMA 20",
            )
        )

        fig.update_layout(
            height=650,
            xaxis_rangeslider_visible=False,
        )

        st.plotly_chart(
            fig,
            width="stretch",
        )

    st.divider()

    if indicators:

        st.subheader("Technical Analysis")

        c1, c2, c3 = st.columns(3)

        c1.metric("Trend", indicators["trend"])
        c2.metric("RSI", f"{indicators['rsi']:.1f}")
        c3.metric("RVOL", f"{indicators['rvol']:.2f}x")

        c1, c2 = st.columns(2)

        c1.metric(
            "EMA 9",
            format_price(indicators["ema9"]),
        )

        c2.metric(
            "EMA 20",
            format_price(indicators["ema20"]),
        )

        c1, c2 = st.columns(2)

        c1.metric(
            "VWAP",
            format_price(indicators["vwap"]),
        )

        c2.metric(
            "Opportunity Score",
            f"{analysis['opportunity_score']}/100",
        )

        st.success(f"⭐ {analysis['rating']}")