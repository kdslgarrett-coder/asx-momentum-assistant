"""
Configuration settings for MomentumHQ
"""

import streamlit as st

# ----------------------------------------------------
# Application
# ----------------------------------------------------

APP_NAME = "MomentumHQ"
VERSION = "1.0.0"

# ----------------------------------------------------
# Alpha Vantage
# ----------------------------------------------------

def get_api_key():
    """
    Returns the Alpha Vantage API key.

    Uses Streamlit Secrets if available.
    Falls back to a hard-coded key for local development.
    """

    try:
        return st.secrets["ALPHA_VANTAGE_API_KEY"]
    except Exception:
        return "AWYQGRWXJY6KG3RU"

# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

DEFAULT_WATCHLIST = [
    "BHP.AX",
    "CBA.AX",
    "FMG.AX",
    "RIO.AX",
    "WDS.AX",
]

REFRESH_INTERVAL = 300  # seconds

# ----------------------------------------------------
# Momentum Scoring
# ----------------------------------------------------

ANNOUNCEMENT_SCORES = {
    "Trading Halt Lifted": 40,
    "Major Acquisition": 35,
    "Major Contract": 35,
    "Resource Upgrade": 30,
    "Drill Results": 30,
    "Quarterly": 20,
    "Broker Upgrade": 15,
    "Capital Raising": -30,
    "Director Selling": -20,
    "Suspension": -40,
}

TECHNICAL_SCORES = {
    "Above EMA9": 10,
    "EMA9 Above EMA20": 10,
    "Above VWAP": 10,
    "High Volume": 10,
    "Turnover": 10,
}