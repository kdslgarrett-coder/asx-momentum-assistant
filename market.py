"""
MomentumHQ Market Data
Version 2.1.0
"""

import streamlit as st
import yfinance as yf
import pandas as pd


@st.cache_data(ttl=300)
def get_quote(symbol: str):

    if not symbol.upper().endswith(".AX"):
        symbol = symbol.upper() + ".AX"

    try:

        ticker = yf.Ticker(symbol)

        info = ticker.info

        history = ticker.history(period="2d")

        if history.empty:
            return None

        latest = history.iloc[-1]

        if len(history) > 1:
            previous_close = float(history.iloc[-2]["Close"])
        else:
            previous_close = float(latest["Close"])

        price = float(latest["Close"])

        change = price - previous_close

        percent = (change / previous_close) * 100 if previous_close else 0

        return {
            "symbol": symbol,
            "company": info.get("longName", symbol),
            "price": price,
            "change": change,
            "percent": f"{percent:+.2f}%",
            "volume": int(latest["Volume"]),
            "previous_close": previous_close,
            "high": float(latest["High"]),
            "low": float(latest["Low"]),
            "market_cap": info.get("marketCap"),
        }

    except Exception as ex:

        st.error(f"Market Data Error\n\n{ex}")

        return None


@st.cache_data(ttl=300)
def get_history(symbol, period="6mo"):

    if not symbol.upper().endswith(".AX"):
        symbol = symbol.upper() + ".AX"

    df = yf.download(
        symbol,
        period=period,
        progress=False,
        auto_adjust=True,
    )

    if df.empty:
        return None

    df["EMA9"] = df["Close"].ewm(span=9).mean()
    df["EMA20"] = df["Close"].ewm(span=20).mean()

    return df


def search_quote(symbol):
    return get_quote(symbol)


def format_price(value):

    if value is None:
        return "-"

    if value < 1:
        return f"${value:.3f}"

    return f"${value:.2f}"


def format_volume(value):

    if value is None:
        return "-"

    if value >= 1_000_000:

        return f"{value/1_000_000:.2f}M"

    if value >= 1_000:

        return f"{value/1000:.1f}K"

    return str(value)


def format_market_cap(value):

    if value is None:
        return "-"

    if value >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"

    return f"${value/1_000_000:.1f}M"