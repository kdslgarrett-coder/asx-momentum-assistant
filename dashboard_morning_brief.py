"""
MomentumHQ Morning Brief
Version 3.5.0-dev

Presentation layer only.

Renders the Morning Brief using data supplied
by the Briefing Engine.
"""

import streamlit as st

from briefing import get_morning_brief
from components.morning_brief_card import render_morning_brief_card


def render() -> None:
    """
    Render the Morning Brief.
    """

    brief = get_morning_brief()

    st.subheader("🌅 Morning Brief")

    st.caption(
        "Your personalised daily briefing from the MomentumHQ Analyst."
    )

    st.divider()

    #
    # Scan Status
    #

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("### Last Market Scan")

        st.write(
            brief.generated_at.strftime("%A, %d %B %Y")
        )

        st.write(
            brief.generated_at.strftime("%H:%M")
        )

    with col2:

        st.markdown("### Status")

        if brief.status == "Complete":

            st.success("🟢 Complete")

        elif brief.status == "Scanning":

            st.warning("🟡 Scanning")

        else:

            st.error(f"🔴 {brief.status}")

    st.divider()

    #
    # Market Coverage
    #

    st.markdown("### Market Coverage")

    st.metric(
        "Companies Reviewed",
        brief.companies_reviewed,
    )

    st.divider()

    #
    # Analyst Summary
    #

    st.markdown("### Analyst Summary")

    st.info(
        brief.analyst_summary
    )

    st.divider()

    #
    # Opportunities
    #

    st.markdown("### Today's Opportunities")

    if not brief.opportunities:

        st.info(
            "No opportunities are currently available."
        )

    else:

        for opportunity in brief.opportunities:

            research_requested = render_morning_brief_card(
                opportunity.analysis
            )

            if research_requested:

                ticker = (
                    opportunity.analysis["quote"]["symbol"]
                    .replace(".AX", "")
                )

                st.session_state.ticker = ticker

                st.success(
                    f"{ticker} loaded into Research."
                )

                st.info(
                    "Research page integration will be completed in a future capability."
                )

    st.divider()

    st.caption(
        "Powered by the MomentumHQ Briefing Engine."
    )