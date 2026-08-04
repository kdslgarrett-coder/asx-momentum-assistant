"""
MomentumHQ Opportunities
Version 3.0.0-dev

Presentation layer only.

Opportunity data is provided by watchlist.py.
Analysis data is provided by analysis_engine.py.
"""

import streamlit as st

from analysis_engine import analyse_stock
from market import format_price
from watchlist import (
    get_watchlist,
    remove_ticker,
    validate_and_add_ticker,
)


def render() -> None:
    """
    Render the user's Opportunities workspace.
    """

    st.subheader("📈 Opportunities")

    st.caption(
        "MomentumHQ continuously monitors the opportunities you've chosen from the Morning Brief."
    )

    st.markdown("### Add Opportunity")

    col1, col2 = st.columns([3, 1])

    with col1:
        ticker = st.text_input(
            "ASX Code",
            placeholder="e.g. KRR",
            label_visibility="collapsed",
        )

    with col2:
        add_clicked = st.button(
            "➕ Add to Opportunities",
            use_container_width=True,
        )

    if add_clicked:

        status, message = validate_and_add_ticker(ticker)

        if status == "success":
            st.success(message)
            st.rerun()

        elif status == "warning":
            st.warning(message)

        else:
            st.error(message)

    st.divider()

    st.markdown("### Active Opportunities")

    symbols = get_watchlist()

    if not symbols:

        st.info(
            """
### 📈 No Active Opportunities

You haven't accepted any opportunities yet.

### Your daily workflow

🌅 Read the Morning Brief

🧠 Review the Analyst's recommendations

➕ Add the opportunities that interest you

📈 MomentumHQ will then continuously monitor them and notify you when something meaningful changes.

You can also manually add an ASX ticker above if you'd like to analyse a specific company.
"""
        )

        return

    header = st.columns([1.2, 0.8, 1.2, 1.0, 1.0, 1.5, 0.8])

    header[0].markdown("**Ticker**")
    header[1].markdown("**Score**")
    header[2].markdown("**Rating**")
    header[3].markdown("**Price**")
    header[4].markdown("**Change**")
    header[5].markdown("**Announcement**")
    header[6].markdown("**Action**")

    st.divider()

    watchlist = []

    for symbol in symbols:

        analysis = analyse_stock(symbol)

        if analysis is None:
            continue

        quote = analysis["quote"]

        watchlist.append(
            {
                "symbol": symbol,
                "ticker": symbol.replace(".AX", ""),
                "score": analysis["opportunity_score"],
                "rating": analysis["rating"],
                "price": format_price(quote["price"]),
                "change": quote["percent"],
                "announcement": analysis["announcement_category"],
            }
        )

    watchlist.sort(
        key=lambda row: row["score"],
        reverse=True,
    )

    for row in watchlist:

        cols = st.columns([1.2, 0.8, 1.2, 1.0, 1.0, 1.5, 0.8])

        cols[0].write(row["ticker"])
        cols[1].write(row["score"])
        cols[2].write(row["rating"])
        cols[3].write(row["price"])
        cols[4].write(row["change"])
        cols[5].write(row["announcement"])

        if cols[6].button(
            "🗑",
            key=f"remove_{row['symbol']}",
            help=f"Stop monitoring {row['ticker']}",
        ):
            remove_ticker(row["symbol"])

            st.success(
                f"MomentumHQ has stopped monitoring {row['ticker']}."
            )

            st.rerun()