"""
MomentumHQ Analyst Action
Version 3.1.0-dev

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

    st.markdown("## 🎯 Analyst Recommendation")

    #
    # Add to Opportunities
    #

    if recommendation == "Add to Watchlist":

        opportunities = get_watchlist()

        if ticker in opportunities:

            st.success(
                "✔ This opportunity is already being monitored."
            )

            return

        if st.button(
            f"➕ Add {ticker.replace('.AX', '')} to Opportunities",
            use_container_width=True,
        ):

            status, message = validate_and_add_ticker(ticker)

            if status == "success":

                st.success(
                    f"{ticker.replace('.AX', '')} has been added to your Opportunities."
                )

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
            "👁 Continue monitoring this opportunity for stronger confirmation."
        )

        return

    #
    # Ignore
    #

    if recommendation == "Ignore":

        st.warning(
            "No action is recommended at this time."
        )

        return

    #
    # Fallback
    #

    st.info(recommendation)