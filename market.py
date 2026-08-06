"""
MomentumHQ Market Data
Version 2.1.0

Provides live market data for MomentumHQ.

The Market Provider supplies factual market
information only.

It does not analyse securities.
It does not generate signals.
It does not score opportunities.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

import streamlit as st
import yfinance as yf


@st.cache_data(ttl=300)
def get_quote(symbol: str) -> dict[str, Any] | None:
    """
    Retrieve a live ASX quote from Yahoo Finance.
    """

    symbol = symbol.strip().upper()

    if not symbol.endswith(".AX"):
        symbol += ".AX"

    try:

        ticker = yf.Ticker(symbol)

        info = ticker.info
        history = ticker.history(period="2d")

        if history.empty:
            return None

        latest = history.iloc[-1]

        previous_close = (
            float(history.iloc[-2]["Close"])
            if len(history) > 1
            else float(latest["Close"])
        )

        price = float(latest["Close"])
        change = price - previous_close

        change_percent = (
            (change / previous_close) * 100
            if previous_close
            else 0.0
        )

        return {

            "symbol": symbol,

            "company": info.get(
                "longName",
                symbol,
            ),

            "price": price,

            "change": change,

            #
            # Numeric value for Scouts
            #

            "change_percent": change_percent,

            #
            # Formatted value for UI
            #

            "percent": (
                f"{change_percent:+.2f}%"
            ),

            "volume": int(latest["Volume"]),

            "previous_close": previous_close,

            "high": float(latest["High"]),

            "low": float(latest["Low"]),

            "market_cap": info.get(
                "marketCap"
            ),

            #
            # Retrieval metadata
            #

            "retrieved_at": datetime.now(),

        }

    except Exception as ex:

        st.error(
            f"Market Data Error:\n\n{ex}"
        )

        return None


def search_quote(
    symbol: str,
) -> dict[str, Any] | None:
    """
    Convenience wrapper.
    """

    return get_quote(symbol)


def format_price(
    value: float | None,
) -> str:

    if value is None:
        return "-"

    return (
        f"${value:,.3f}"
        if value < 1
        else f"${value:,.2f}"
    )


def format_volume(
    value: int | None,
) -> str:

    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return (
            f"{value / 1_000_000_000:.2f}B"
        )

    if value >= 1_000_000:
        return (
            f"{value / 1_000_000:.2f}M"
        )

    if value >= 1_000:
        return (
            f"{value / 1_000:.1f}K"
        )

    return str(value)


def format_market_cap(
    value: int | None,
) -> str:

    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return (
            f"${value / 1_000_000_000:.2f}B"
        )

    return (
        f"${value / 1_000_000:.1f}M"
    )