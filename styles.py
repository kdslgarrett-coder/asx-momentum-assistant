"""
Custom CSS styling for MomentumHQ
"""

import streamlit as st


def load_css():
    st.markdown(
        """
        <style>

        /* -------------------------------------------------
           Main App
        -------------------------------------------------- */

        .stApp {
            background-color: #0E1117;
            color: #FAFAFA;
        }

        /* -------------------------------------------------
           Header
        -------------------------------------------------- */

        .main-title {
            font-size: 42px;
            font-weight: 700;
            color: #00C853;
            margin-bottom: 0px;
        }

        .sub-title {
            font-size: 18px;
            color: #BBBBBB;
            margin-top: -10px;
            margin-bottom: 25px;
        }

        /* -------------------------------------------------
           Cards
        -------------------------------------------------- */

        .metric-card {
            background-color: #161B22;
            border: 1px solid #30363D;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 15px;
        }

        /* -------------------------------------------------
           Section Headers
        -------------------------------------------------- */

        .section-header {
            font-size: 24px;
            font-weight: 600;
            color: white;
            padding-top: 10px;
            padding-bottom: 10px;
        }

        /* -------------------------------------------------
           Buy / Watch / Ignore Badges
        -------------------------------------------------- */

        .buy {
            color: #00E676;
            font-weight: bold;
        }

        .watch {
            color: #FFD54F;
            font-weight: bold;
        }

        .ignore {
            color: #FF5252;
            font-weight: bold;
        }

        /* -------------------------------------------------
           DataFrames
        -------------------------------------------------- */

        div[data-testid="stDataFrame"] {
            border: 1px solid #30363D;
            border-radius: 10px;
            overflow: hidden;
        }

        /* -------------------------------------------------
           Buttons
        -------------------------------------------------- */

        .stButton > button {
            background-color: #00C853;
            color: white;
            border-radius: 8px;
            border: none;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #00A844;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )