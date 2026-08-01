"""
MomentumHQ Dashboard Home
Version 2.3.0
"""

import streamlit as st
import plotly.graph_objects as go

from market import (
    search_quote,
    format_price,
    format_volume,
    format_market_cap,
)

from history import get_history
from indicators import calculate_indicators


def render(ticker):

    quote = search_quote(ticker)

    if quote is None:
        st.error("Unable to retrieve market data.")
        return

    history = get_history(ticker)

    indicators = calculate_indicators(history)

    if indicators:
        history = indicators["history"]

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
            use_container_width=True,
        )

    st.divider()

    if indicators:

        st.subheader("Technical Analysis")

        score = 0

        if indicators["trend"] == "Bullish":
            score += 10

        if quote["price"] > indicators["ema20"]:
            score += 10

        if quote["price"] > indicators["vwap"]:
            score += 5

        if 50 <= indicators["rsi"] <= 70:
            score += 5

        if indicators["rvol"] >= 1.5:
            score += 10

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
            "Technical Score",
            f"{score}/40",
        )

        if score >= 35:
            st.success("🟢 STRONG BUY")
        elif score >= 25:
            st.success("🟢 BUY")
        elif score >= 15:
            st.warning("🟡 WATCH")
        else:
            st.error("🔴 AVOID")