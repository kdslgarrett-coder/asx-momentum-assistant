"""
MomentumHQ History Service
Version 2.2.0
"""

from typing import Optional

import pandas as pd
import streamlit as st
import yfinance as yf


@st.cache_data(ttl=300)
def get_history(symbol: str, period: str = "6mo") -> Optional[pd.DataFrame]:
    """
    Download historical price data for an ASX stock.

    Args:
        symbol: ASX ticker with or without the .AX suffix.
        period: Valid yfinance period (e.g. "1mo", "6mo", "1y").

    Returns:
        A pandas DataFrame containing historical OHLCV data, or None if
        no data is available or the download fails.
    """

    symbol = symbol.upper()

    if not symbol.endswith(".AX"):
        symbol += ".AX"

    try:
        df = yf.download(
            symbol,
            period=period,
            progress=False,
            auto_adjust=True,
            group_by="column",
        )

        if df.empty:
            return None

        # Flatten MultiIndex columns if returned by yfinance.
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        return df

    except Exception as ex:
        st.error(f"History Error\n\n{ex}")
        return None