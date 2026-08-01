"""
MomentumHQ History Service
Version 2.2.0
"""

import streamlit as st
import yfinance as yf
import pandas as pd


@st.cache_data(ttl=300)
def get_history(symbol, period="6mo"):
    """
    Download historical price data for an ASX stock.
    """

    if not symbol.upper().endswith(".AX"):
        symbol = symbol.upper() + ".AX"

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

        # Flatten MultiIndex columns if returned by yfinance
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        return df

    except Exception as ex:

        st.error(f"History Error\n\n{ex}")

        return None