"""
MomentumHQ Morning Brief
Version 3.0.0-dev

Presentation layer only.

This module renders the Morning Brief landing page.

Market scan and opportunity data will be integrated in
later capabilities.
"""

from datetime import datetime

import streamlit as st


def render() -> None:
    """
    Render the Morning Brief landing page.
    """

    st.subheader("🌅 Morning Brief")

    st.caption(
        "Your personalised daily briefing from the MomentumHQ Analyst."
    )

    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("### Last Market Scan")

        now = datetime.now()

        st.write(now.strftime("%A, %d %B %Y"))
        st.write(now.strftime("%H:%M"))

    with col2:

        st.markdown("### Status")

        st.success("🟢 Complete")

    st.markdown("---")

    st.markdown("### Market Coverage")

    coverage1, coverage2, coverage3 = st.columns(3)

    coverage1.metric(
        "Announcements",
        "247",
    )

    coverage2.metric(
        "Volume Events",
        "18",
    )

    coverage3.metric(
        "Breakouts",
        "11",
    )

    st.markdown("---")

    st.markdown("### Analyst Summary")

    st.info(
        """
The MomentumHQ Analyst reviewed the market and identified **5 opportunities**
that meet your investment criteria.

**High Confidence:** 2

**Monitor:** 2

**Speculative:** 1
"""
    )

    st.markdown("---")

    st.markdown("### Today's Opportunities")

    st.info(
        """
Opportunity Cards will appear here in the next capability.

Each opportunity will include:

- Confidence
- Why it matters
- Supporting evidence
- Analyst recommendation
- Add to Opportunities
"""
    )

    st.markdown("---")

    st.caption(
        "Automatic market scanning and live analyst updates will be introduced in a future capability."
    )