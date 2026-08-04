"""
MomentumHQ Morning Brief Card
Version 3.1.0-dev

Compact opportunity card used by the Morning Brief.
"""

import streamlit as st


def render_morning_brief_card(analysis: dict) -> bool:
    """
    Render a compact Morning Brief opportunity card.

    Returns:
        True if the user selects "Research",
        otherwise False.
    """

    quote = analysis["quote"]

    ticker = quote["symbol"].replace(".AX", "")

    confidence = analysis["opportunity_score"]

    rating = analysis["rating"]

    summary = (
        analysis.get("brief", {}).get("summary")
        or analysis.get("summary")
        or "No analyst summary available."
    )

    with st.container(border=True):

        col1, col2 = st.columns([3, 1])

        with col1:

            st.subheader(ticker)

            st.caption(rating)

        with col2:

            st.metric(
                "Confidence",
                f"{confidence}",
            )

        st.write(summary)

        button_col1, button_col2 = st.columns(2)

        with button_col1:

            research = st.button(
                "🔎 Research",
                key=f"research_{ticker}",
                use_container_width=True,
            )

        with button_col2:

            if st.button(
                "➕ Opportunities",
                key=f"opportunity_{ticker}",
                use_container_width=True,
            ):
                st.info(
                    "Opportunity integration will be completed in the next capability."
                )

        return research