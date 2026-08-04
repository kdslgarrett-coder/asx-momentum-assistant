"""
MomentumHQ Opportunity Card
Version 3.0.0-dev

Reusable Analyst Opportunity Card.

This component presents the Analyst's conclusion in a concise,
investor-focused format and will be reused throughout
MomentumHQ.
"""

import streamlit as st


def render_opportunity_card(analysis: dict) -> None:
    """
    Render the MomentumHQ Opportunity Card.
    """

    brief = analysis["brief"]

    confidence = analysis["analyst"]["confidence"]

    confidence_rating = confidence["rating"]

    recommendation = confidence["recommendation"]

    if confidence_rating == "High":
        badge = "🟢 High Confidence"

    elif confidence_rating == "Good":
        badge = "🟡 Good Confidence"

    elif confidence_rating == "Medium":
        badge = "🟠 Medium Confidence"

    else:
        badge = "🔴 Low Confidence"

    st.markdown("## 🧠 The Analyst")

    st.success(badge)

    st.markdown("### ⭐ Action")

    st.write(recommendation)

    st.markdown("---")

    st.markdown("### 📰 What happened?")

    st.write(brief["what_happened"])

    st.markdown("### 📈 Why it matters")

    st.write(brief["why_it_matters"])

    st.markdown("### 📊 Market confirmation")

    st.write(brief["market_confirmation"])

    st.markdown("### ⚠️ Risks")

    st.write(brief["risks"])