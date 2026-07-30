"""
Market data functions for MomentumHQ
"""

import requests
import streamlit as st

from config import get_api_key


BASE_URL = "https://www.alphavantage.co/query"


@st.cache_data(ttl=300)
def get_quote(symbol: str):
    """
    Returns a live quote for a stock.

    Example:
        BHP.AX
        CBA.AX
        FMG.AX
    """

    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": get_api_key(),
    }

    try:

        response = requests.get(BASE_URL, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        quote = data.get("Global Quote", {})

        if not quote:
            return None

        return {
            "symbol": quote.get("01. symbol"),
            "price": float(quote.get("05. price", 0)),
            "change": float(quote.get("09. change", 0)),
            "percent": quote.get("10. change percent"),
            "volume": int(float(quote.get("06. volume", 0))),
            "previous_close": float(quote.get("08. previous close", 0)),
        }

    except Exception as ex:

        st.error(f"Unable to retrieve market data.\n\n{ex}")

        return None


@st.cache_data(ttl=300)
def search_quote(symbol):
    """
    Convenience wrapper.
    """

    if not symbol.endswith(".AX"):
        symbol = symbol.upper() + ".AX"

    return get_quote(symbol)


def format_price(value):

    if value is None:
        return "-"

    return f"${value:,.2f}"


def format_volume(value):

    if value is None:
        return "-"

    if value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"

    if value >= 1000:
        return f"{value/1000:.1f}K"

    return str(value)