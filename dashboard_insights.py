"""
MomentumHQ Dashboard Insights
Version 2.6.0-dev

Presentation layer only.

Business logic is provided by analysis_engine.py.
"""

import streamlit as st

from analysis_engine import analyse_stock


def render(ticker: str) -> None:
    """
    Render the Momentum Insights panel.

    All scoring and analysis is supplied by analysis_engine.
    """

    result = analyse_stock(ticker)

    if result is None:
        st.warning(f"No data available for {ticker}.")
        return

    st.subheader("💡 Momentum Insights")
    st.caption(f"Ticker: {ticker}")

    st.write(
        f"Latest Announcement Category: **{result['announcement_category']}**"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("Opportunity", f"{result['opportunity_score']}/100")
    c2.metric("Confidence", f"{result['confidence']}%")
    c3.metric("Timing", result["timing"])

    st.success(f"⭐ {result['rating']}")

    left, right = st.columns(2)

    with left:
        st.markdown("### Strengths")

        if result["strengths"]:
            for item in result["strengths"]:
                st.write(f"✅ {item}")
        else:
            st.write("No strengths identified yet.")

    with right:
        st.markdown("### Risks")

        if result["risks"]:
            for item in result["risks"]:
                st.write(f"⚠️ {item}")
        else:
            st.write("No significant risks identified.")

    st.markdown("### Suggested Action")
    st.info(result["action"])