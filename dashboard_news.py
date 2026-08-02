"""
MomentumHQ Dashboard News
Version 2.5.1
"""

import streamlit as st

from announcements import get_announcements
from analysis import analyse


def show_card(item):
    ai = analyse(item["category"])

    with st.container(border=True):
        st.markdown(f"### {ai['icon']} {item['title']}")
        st.caption(item["published"])

        c1, c2, c3 = st.columns(3)
        c1.metric("Sentiment", ai["sentiment"])
        c2.metric("Confidence", ai["confidence"])
        c3.metric("Score", f"{ai['score']}/30")

        with st.expander("Analysis", expanded=True):
            st.markdown(f"**Summary**\n\n{ai['summary']}")
            st.markdown(f"**Reason**\n\n{ai['reason']}")

            if "breakdown" in ai:
                st.markdown("**Score Breakdown**")
                for key, value in ai["breakdown"].items():
                    st.write(f"- {key}: {value}")


def render(ticker):
    st.subheader("📢 Company Announcements")

    company = get_announcements(ticker, limit=5)

    if company:
        for item in company:
            show_card(item)
    else:
        st.info("No company announcements found.")

    st.divider()

    st.subheader("🔥 Market Announcements")

    market = get_announcements(limit=5)

    if market:
        for item in market:
            show_card(item)
    else:
        st.info("No market announcements available.")