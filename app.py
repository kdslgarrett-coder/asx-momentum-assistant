"""
MomentumHQ
Version 2.7.0-dev

Application entry point.
"""

import streamlit as st

from config import (
    APP_ICON,
    APP_NAME,
    PAGE_LAYOUT,
    SIDEBAR_STATE,
)
from dashboard import render
from styles import load_css


def main() -> None:
    """
    MomentumHQ application entry point.
    """

    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout=PAGE_LAYOUT,
        initial_sidebar_state=SIDEBAR_STATE,
    )

    load_css()

    render()


if __name__ == "__main__":
    main()