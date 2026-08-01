"""
MomentumHQ Styling
Version 2.0.0
"""

import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        h1 {
            color: #00C853;
            font-weight: 700;
        }

        h2 {
            color: #1976D2;
            margin-top: 1rem;
        }

        div[data-testid="stMetric"] {
            border: 1px solid #E0E0E0;
            border-radius: 12px;
            padding: 15px;
            background-color: #FAFAFA;
        }

        div[data-testid="stMetricValue"] {
            font-size: 30px;
            font-weight: bold;
        }

        div[data-testid="stMetricLabel"] {
            font-size: 15px;
            color: #666666;
        }

        .stButton>button {
            width: 100%;
            border-radius: 10px;
            font-weight: bold;
            height: 42px;
        }

        .watchlist-header {
            font-size: 20px;
            font-weight: bold;
            color: #1976D2;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .footer {
            text-align: center;
            color: grey;
            font-size: 13px;
            margin-top: 40px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )