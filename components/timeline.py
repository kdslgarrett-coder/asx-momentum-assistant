"""
MomentumHQ Timeline
Version 3.0.0-dev

Displays the chronology behind an opportunity.

Version 1 establishes the reusable component.
Future versions will display richer market events as
additional timestamp data becomes available.
"""

import streamlit as st


def render_timeline(analysis: dict) -> None:
    """
    Render the MomentumHQ Timeline.
    """

    announcement = analysis.get("announcement", {})

    published = (
        announcement.get("published_datetime")
        or announcement.get("published")
        or "Unknown"
    )

    recommendation = (
        analysis.get("brief", {})
        .get("recommendation", "No recommendation")
    )

    st.markdown("## 📅 Timeline")

    timeline = [
        ("📰", "Announcement Released", str(published)),
        ("🧠", "Analyst Review", "Opportunity analysed"),
        ("⭐", "Recommendation", recommendation),
    ]

    for icon, title, detail in timeline:
        st.markdown(f"**{icon} {title}**")
        st.caption(detail)