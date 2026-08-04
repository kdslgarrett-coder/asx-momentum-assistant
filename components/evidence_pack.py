"""
MomentumHQ Evidence Pack
Version 3.0.0-dev

Displays the supporting evidence behind the Analyst's conclusion.
"""

import streamlit as st

from market import format_price


def _yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def render_evidence_pack(analysis: dict) -> None:
    """
    Render the MomentumHQ Evidence Pack.
    """

    indicators = analysis["indicators"]
    quote = analysis["quote"]
    analyst = analysis["analyst"]

    st.markdown("## 📁 Evidence Pack")

    #
    # Market Confirmation
    #

    st.markdown("### 📈 Market Confirmation")

    c1, c2 = st.columns(2)

    c1.metric("Trend", indicators["trend"])
    c2.metric("RVOL", f"{indicators['rvol']:.2f}x")

    c1, c2 = st.columns(2)

    c1.metric(
        "Above VWAP",
        _yes_no(quote["price"] > indicators["vwap"]),
    )

    c2.metric(
        "Breakout",
        _yes_no(quote["price"] > indicators["ema20"]),
    )

    st.divider()

    #
    # Technical Health
    #

    st.markdown("### 📊 Technical Health")

    c1, c2 = st.columns(2)

    c1.metric(
        "RSI",
        f"{indicators['rsi']:.1f}",
    )

    c2.metric(
        "VWAP",
        format_price(indicators["vwap"]),
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "EMA 9",
        format_price(indicators["ema9"]),
    )

    c2.metric(
        "EMA 20",
        format_price(indicators["ema20"]),
    )

    st.divider()

    #
    # Analyst Assessment
    #

    st.markdown("### 🧠 Analyst Assessment")

    st.write(analyst["summary"])

    st.info(
        analyst["confidence"]["reason"]
    )