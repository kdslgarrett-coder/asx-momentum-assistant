"""
MomentumHQ
Version 2.6.0-dev

Application entry point.

Task 16:
- Initialise Streamlit.
- Load global styling.
- Delegate application rendering to dashboard.py.
"""

import streamlit as st

from config import APP_NAME
from dashboard import render
from styles import load_css


def main() -> None:
    """
    MomentumHQ application entry point.
    """

    st.set_page_config(
        page_title=APP_NAME,
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    load_css()

    render()


if __name__ == "__main__":
    main()