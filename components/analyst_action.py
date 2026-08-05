"""
MomentumHQ Analyst Action
Version 3.3.0-dev

Displays the Analyst's recommended next action.
"""

import streamlit as st

import monitor


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
    # Monitor Opportunity
    #

    if recommendation == "Monitor":

        if monitor.is_monitored(ticker):

            st.success(
                "✔ This opportunity is already being monitored."
            )

            return

        if st.button(
            f"👁 Monitor {ticker.replace('.AX', '')}",
            use_container_width=True,
        ):

            status, message = monitor.validate_and_add(ticker)

            if status == "success":

                st.success(message)

                st.rerun()

            elif status == "warning":

                st.warning(message)

            else:

                st.error(message)

        return

    #
    # Investigate Today
    #

    if recommendation == "Investigate Today":

        st.success(
            "🔎 The Analyst recommends immediate investigation."
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