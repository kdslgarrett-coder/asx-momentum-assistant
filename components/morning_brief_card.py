"""
MomentumHQ Morning Brief Card
Version 3.3.0-dev

Compact opportunity card used by the Morning Brief.
"""

import streamlit as st

import monitor

from narrative import (
    generate_headline,
    generate_summary,
)


def render_morning_brief_card(analysis: dict) -> bool:
    """
    Render a Morning Brief opportunity card.

    Returns:
        True if the user selects Open Research,
        otherwise False.
    """

    quote = analysis["quote"]

    ticker = quote["symbol"].replace(".AX", "")

    confidence = analysis["opportunity_score"]

    rating = analysis["rating"]

    headline = generate_headline(analysis)

    summary = generate_summary(analysis)

    #
    # Confidence presentation
    #

    if confidence >= 80:
        confidence_label = "Very High"

    elif confidence >= 65:
        confidence_label = "High"

    elif confidence >= 50:
        confidence_label = "Moderate"

    else:
        confidence_label = "Low"

    #
    # Recommendation presentation
    #

    if rating == "Strong Buy":
        recommendation = "🟢 STRONG BUY"

    elif rating == "Watch":
        recommendation = "🟡 WATCH"

    elif rating == "Avoid":
        recommendation = "🔴 AVOID"

    else:
        recommendation = rating.upper()

    with st.container(border=True):

        left, right = st.columns([3, 1])

        with left:

            st.subheader(ticker)

            st.markdown(f"**{recommendation}**")

            st.caption(headline)

        with right:

            st.metric(
                "Confidence",
                f"{confidence}%",
                confidence_label,
            )

        st.write(summary)

        button_left, button_right = st.columns(2)

        with button_left:

            research = st.button(
                "🔎 Open Research",
                key=f"research_{ticker}",
                use_container_width=True,
            )

        with button_right:

            if st.button(
                "👁 Monitor",
                key=f"monitor_{ticker}",
                use_container_width=True,
            ):

                if monitor.add(analysis):

                    st.success(
                        f"{ticker} added to Opportunities."
                    )

                else:

                    st.info(
                        f"{ticker} is already being monitored."
                    )

        return research