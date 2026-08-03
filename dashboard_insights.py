"""
MomentumHQ Dashboard Insights
Version 2.5.3
"""

import streamlit as st
from opportunity_engine import evaluate_opportunity

def render(ticker: str):
    result = evaluate_opportunity(
        technical_score=0,
        announcement_score=0,
        volume_score=0,
        risk_score=0,
    )

    st.subheader("💡 Momentum Insights")
    st.caption(f"Ticker: {ticker}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Opportunity", f"{result['score']}/100")
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