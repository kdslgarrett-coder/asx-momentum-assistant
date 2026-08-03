"""
MomentumHQ Market Data
Version 2.0.0
"""

from typing import Any, Dict, Optional

import streamlit as st
import yfinance as yf


@st.cache_data(ttl=300)
def get_quote(symbol: str) -> Optional[Dict[str, Any]]:
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
        percent = (change / previous_close) * 100 if previous_close else 0.0

        return {
            "symbol": symbol,
            "price": price,
            "change": change,
            "percent": f"{percent:+.2f}%",
            "volume": int(latest["Volume"]),
            "previous_close": previous_close,
            "high": float(latest["High"]),
            "low": float(latest["Low"]),
            "market_cap": info.get("marketCap"),
            "company": info.get("longName", symbol),
        }

    except Exception as ex:
        st.error(f"Market Data Error:\n\n{ex}")
        return None


def search_quote(symbol: str) -> Optional[Dict[str, Any]]:
    """
    Convenience wrapper.
    """
    return get_quote(symbol)


def format_price(value: Optional[float]) -> str:
    if value is None:
        return "-"

    return f"${value:,.3f}" if value < 1 else f"${value:,.2f}"


def format_volume(value: Optional[int]) -> str:
    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"

    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    if value >= 1_000:
        return f"{value / 1_000:.1f}K"

    return str(value)


def format_market_cap(value: Optional[int]) -> str:
    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"

    return f"${value / 1_000_000:.1f}M"