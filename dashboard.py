import streamlit as st
from config import APP_NAME, VERSION, DEFAULT_WATCHLIST
from market import search_quote, format_price, format_volume
from momentum import demo_score

def render():
    st.title(APP_NAME)
    st.caption(f"Version {VERSION}")

    if "quote" not in st.session_state:
        st.session_state.quote = None

    col1, col2 = st.columns([3,1])
    with col1:
        ticker = st.text_input("ASX Code", value="BHP").upper()
    with col2:
        st.write("")
        if st.button("Get Quote", use_container_width=True):
            st.session_state.quote = search_quote(ticker)

    quote = st.session_state.quote
    if quote:
        st.subheader(quote.get("symbol",""))
        a,b,c,d = st.columns(4)
        a.metric("Price", format_price(quote.get("price")))
        b.metric("Change", f"{quote.get('change_percent','0')}%")
        c.metric("Volume", format_volume(quote.get("volume")))
        d.metric("Previous Close", format_price(quote.get("previous_close")))

    st.divider()
    st.subheader("Momentum")
    score = demo_score()
    st.progress(score["overall"]/100)
    l,r = st.columns(2)
    with l:
        st.metric("Announcement", score["announcement"])
        st.metric("Technical", score["technical"])
    with r:
        st.metric("Overall", score["overall"])
        st.success(score["recommendation"])

    st.divider()
    st.subheader("Latest Announcements")
    st.info("Coming soon")

    st.divider()
    st.subheader("Watchlist")
    for code in DEFAULT_WATCHLIST:
        st.write(f"• {code}")

    st.caption("MomentumHQ")
