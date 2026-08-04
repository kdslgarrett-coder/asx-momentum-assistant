"""
MomentumHQ Confidence Badge
Version 3.0.0-dev

Reusable confidence badge displayed throughout MomentumHQ.
"""

import streamlit as st


def render_confidence_badge(analysis: dict) -> None:
    """
    Render the MomentumHQ confidence badge.
    """

    confidence = analysis["brief"]["confidence"]

    try:
        score = int(confidence)
    except (ValueError, TypeError):
        score = 0

    if score >= 80:
        icon = "🟢"
        label = "HIGH CONFIDENCE"
        message = "Strong market confirmation."

    elif score >= 65:
        icon = "🟡"
        label = "GOOD CONFIDENCE"
        message = "Positive confirmation with manageable risk."

    elif score >= 50:
        icon = "🟠"
        label = "MODERATE CONFIDENCE"
        message = "Further confirmation recommended."

    else:
        icon = "🔴"
        label = "LOW CONFIDENCE"
        message = "Insufficient supporting evidence."

    st.success(f"{icon} {label}")

    c1, c2 = st.columns([1, 3])

    with c1:
        st.metric("Confidence", f"{score}%")

    with c2:
        st.write(message)