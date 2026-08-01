"""
MomentumHQ Dashboard News
Version 2.3.0
"""

import streamlit as st

from announcements import get_announcements


def render(ticker):

    st.subheader("📢 Latest Company Announcements")

    company = get_announcements(
        ticker,
        limit=5,
    )

    if company:

        for item in company:

            st.markdown(
                f"""
**{item['title']}**

{item['published']}

{item['category']}

---
"""
            )

    else:

        st.info(
            "No company announcements found."
        )

    st.subheader("🔥 Latest Market Announcements")

    market = get_announcements(
        limit=5,
    )

    if market:

        for item in market:

            st.markdown(
                f"""
**{item['title']}**

{item['published']}

{item['category']}

---
"""
            )

    else:

        st.info(
            "No market announcements available."
        )