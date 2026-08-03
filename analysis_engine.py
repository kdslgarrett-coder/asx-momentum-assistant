"""
MomentumHQ Analysis Engine
Version 2.6.0-dev

Shared analysis engine for dashboard modules.

Task 11A:
- Extract the existing technical scoring logic from dashboard_home.py.
- Preserve existing behaviour.
"""

from typing import Any, Dict, Optional

from history import get_history
from indicators import calculate_indicators
from market import search_quote
from score import calculate_opportunity_score, get_rating


def analyse_stock(ticker: str) -> Optional[Dict[str, Any]]:
    """
    Analyse a stock and return all information required by the dashboard.

    This implementation intentionally preserves the existing behaviour
    from dashboard_home.py. Only the location of the technical scoring
    logic has changed.
    """

    quote = search_quote(ticker)

    if quote is None:
        return None

    history = get_history(ticker)

    indicators = calculate_indicators(history)

    if indicators:
        history = indicators["history"]

    technical_score = 0

    if indicators:
        if indicators["trend"] == "Bullish":
            technical_score += 10

        if quote["price"] > indicators["ema20"]:
            technical_score += 10

        if quote["price"] > indicators["vwap"]:
            technical_score += 5

        if 50 <= indicators["rsi"] <= 70:
            technical_score += 5

        if indicators["rvol"] >= 1.5:
            technical_score += 10

    opportunity_score = calculate_opportunity_score(
        technical_score=technical_score,
        announcement_score=0,
        volume_score=0,
        risk_score=0,
    )

    return {
        "quote": quote,
        "history": history,
        "indicators": indicators,
        "technical_score": technical_score,
        "announcement_score": 0,
        "volume_score": 0,
        "risk_score": 0,
        "opportunity_score": opportunity_score,
        "rating": get_rating(opportunity_score),
    }