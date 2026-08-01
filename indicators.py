"""
MomentumHQ Technical Indicators
Version 2.2.0
"""

import pandas as pd
import numpy as np


def calculate_indicators(df):
    """
    Calculate technical indicators from historical data.
    """

    if df is None or df.empty:
        return None

    data = df.copy()

    # EMA
    data["EMA9"] = (
        data["Close"]
        .ewm(span=9, adjust=False)
        .mean()
    )

    data["EMA20"] = (
        data["Close"]
        .ewm(span=20, adjust=False)
        .mean()
    )

    # RSI (14)

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()

    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)

    data["RSI"] = 100 - (
        100 / (1 + rs)
    )

    # VWAP

    typical_price = (
        data["High"]
        + data["Low"]
        + data["Close"]
    ) / 3

    data["VWAP"] = (
        (typical_price * data["Volume"]).cumsum()
        / data["Volume"].cumsum()
    )

    # Relative Volume

    data["AVG_VOL20"] = (
        data["Volume"]
        .rolling(20)
        .mean()
    )

    data["RVOL"] = (
        data["Volume"]
        / data["AVG_VOL20"]
    )

    latest = data.iloc[-1]

    trend = (
        "Bullish"
        if latest["EMA9"] > latest["EMA20"]
        else "Bearish"
    )

    return {

        "history": data,

        "ema9": float(
            latest["EMA9"]
        ),

        "ema20": float(
            latest["EMA20"]
        ),

        "rsi": float(
            latest["RSI"]
        ),

        "vwap": float(
            latest["VWAP"]
        ),

        "rvol": float(
            latest["RVOL"]
        ),

        "trend": trend,

    }