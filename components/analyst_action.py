"""
MomentumHQ Analyst Action
Version 3.0.0-dev

Displays the Analyst's recommended next action.
"""

import streamlit as st

from watchlist import (
    get_watchlist,
    validate_and_add_ticker,
)


def render_analyst_action(analysis: dict) -> None:
    """
    Render the Analyst Action component.
    """

    ticker = analysis["quote"]["symbol"]

    recommendation = (
        analysis.get("action")
        or analysis.get("brief", {}).get("recommendation", "")
    )

    st.markdown("## 🎯 Recommended Action")

    #
    # Add to Watchlist
    #

    if recommendation == "Add to Watchlist":

        watchlist = get_watchlist()

        if ticker in watchlist:

            st.success("✔ Already in your watchlist")

            return

        if st.button(
            f"➕ Add {ticker.replace('.AX', '')} to Watchlist",
            use_container_width=True,
        ):

            status, message = validate_and_add_ticker(ticker)

            if status == "success":
                st.success(message)
                st.rerun()

            elif status == "warning":
                st.warning(message)

            else:
                st.error(message)

        return

    #
    # Monitor
    #

    if recommendation == "Monitor":

        st.info(
            "👁 Monitor this opportunity for further confirmation."
        )

        return

    #
    # Ignore
    #

    if recommendation == "Ignore":

        st.warning(
            "No action recommended at this stage."
        )

        return

    #
    # Fallback
    #

    st.info(recommendation)