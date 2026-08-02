"""
MomentumHQ Dashboard Home
Version 2.5.3
"""

import streamlit as st
import plotly.graph_objects as go
from market import search_quote, format_price, format_volume, format_market_cap
from history import get_history
from indicators import calculate_indicators
from analysis import get_announcement_score
from opportunity_engine import evaluate_opportunity

def render(ticker):
    quote = search_quote(ticker)
    if quote is None:
        st.error("Unable to retrieve market data.")
        return
    history = get_history(ticker)
    indicators = calculate_indicators(history)
    if indicators:
        history = indicators["history"]
    st.subheader(quote["company"])
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Price",format_price(quote["price"]))
    c2.metric("Change",quote["percent"])
    c3.metric("Volume",format_volume(quote["volume"]))
    c4.metric("Previous Close",format_price(quote["previous_close"]))
    c1,c2,c3=st.columns(3)
    c1.metric("Day High",format_price(quote["high"]))
    c2.metric("Day Low",format_price(quote["low"]))
    c3.metric("Market Cap",format_market_cap(quote["market_cap"]))
    st.divider()
    if history is not None:
        fig=go.Figure()
        fig.add_trace(go.Candlestick(x=history.index,open=history["Open"],high=history["High"],low=history["Low"],close=history["Close"],name="Price"))
        fig.add_trace(go.Scatter(x=history.index,y=history["EMA9"],name="EMA 9"))
        fig.add_trace(go.Scatter(x=history.index,y=history["EMA20"],name="EMA 20"))
        fig.update_layout(height=650,xaxis_rangeslider_visible=False)
        st.plotly_chart(fig,use_container_width=True)
    if not indicators:
        return
    technical_score=0
    if indicators["trend"]=="Bullish": technical_score+=10
    if quote["price"]>indicators["ema20"]: technical_score+=10
    if quote["price"]>indicators["vwap"]: technical_score+=5
    if 50<=indicators["rsi"]<=70: technical_score+=5
    if indicators["rvol"]>=1.5: technical_score+=10
    result=evaluate_opportunity(technical_score,get_announcement_score("Other"))
    st.metric("Opportunity Score",f'{result["score"]}/100')
    st.success(f'⭐ {result["rating"]}')