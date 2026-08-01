"""
MomentumHQ Dashboard
Version 2.1.0
"""

import streamlit as st
import plotly.graph_objects as go

from config import (
    APP_NAME,
    VERSION,
    DEFAULT_TICKER,
    DEFAULT_WATCHLIST,
)

from market import (
    search_quote,
    get_history,
    format_price,
    format_volume,
    format_market_cap,
)


def render():

    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    st.divider()

    # -----------------------------
    # Search
    # -----------------------------

    if "ticker" not in st.session_state:
        st.session_state.ticker = DEFAULT_TICKER

    ticker = st.text_input(
        "ASX Code",
        value=st.session_state.ticker,
    ).upper()

    if ticker != st.session_state.ticker:
        st.session_state.ticker = ticker

    quote = search_quote(st.session_state.ticker)

    if quote is None:
        st.error("Unable to retrieve market data.")
        return

    # -----------------------------
    # Quote
    # -----------------------------

    st.subheader(quote["company"])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Price",
        format_price(quote["price"]),
    )

    c2.metric(
        "Change",
        quote["percent"],
    )

    c3.metric(
        "Volume",
        format_volume(quote["volume"]),
    )

    c4.metric(
        "Previous Close",
        format_price(
            quote["previous_close"]
        ),
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Day High",
        format_price(
            quote["high"]
        ),
    )

    c2.metric(
        "Day Low",
        format_price(
            quote["low"]
        ),
    )

    c3.metric(
        "Market Cap",
        format_market_cap(
            quote["market_cap"]
        ),
    )

    st.divider()

    # -----------------------------
    # Chart
    # -----------------------------

    st.subheader("Price Chart")

    history = get_history(st.session_state.ticker)

    if history is not None:

        fig = go.Figure()

        fig.add_trace(
            go.Candlestick(
                x=history.index,
                open=history["Open"],
                high=history["High"],
                low=history["Low"],
                close=history["Close"],
                name="Price",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=history.index,
                y=history["EMA9"],
                name="EMA 9",
                line=dict(width=2),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=history.index,
                y=history["EMA20"],
                name="EMA 20",
                line=dict(width=2),
            )
        )

        fig.update_layout(
            height=650,
            xaxis_rangeslider_visible=False,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20,
            ),
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.divider()

    # -----------------------------
    # Watchlist
    # -----------------------------

    st.subheader("Watchlist")

    rows = []

    for symbol in DEFAULT_WATCHLIST:

        q = search_quote(symbol)

        if q:

            rows.append(
                {
                    "Ticker": symbol.replace(".AX", ""),
                    "Price": format_price(
                        q["price"]
                    ),
                    "Change": q["percent"],
                    "Volume": format_volume(
                        q["volume"]
                    ),
                }
            )

    st.dataframe(
        rows,
        hide_index=True,
        use_container_width=True,
    )

    st.divider()

    st.caption(
        f"{APP_NAME} • Version {VERSION}"
    )