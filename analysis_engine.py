"""
MomentumHQ Analysis Engine
Version 2.7.0-dev

Compatibility layer between the legacy dashboard and the
MomentumHQ Analyst architecture.

Existing dashboard modules continue to work unchanged while
new functionality is exposed through the Analyst.
"""

from typing import Any, Dict, Optional

from analysis import analyse, get_announcement_score
from announcements import get_announcements
from history import get_history
from indicators import calculate_indicators
from market import search_quote
from opportunity_engine import evaluate_opportunity

from analyst import review_opportunity
from story_engine import build_brief


def analyse_announcement(category: str) -> Dict[str, Any]:
    """
    Legacy announcement analysis.
    """

    return analyse(category)


def analyse_stock(ticker: str) -> Optional[Dict[str, Any]]:
    """
    Analyse a stock.

    Returns the complete legacy structure together with the new
    MomentumHQ Analyst outputs.
    """

    quote = search_quote(ticker)

    if quote is None:
        return None

    history = get_history(ticker)

    indicators = calculate_indicators(history)

    if indicators:
        history = indicators["history"]

    #
    # Legacy technical scoring
    #

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

    announcements = get_announcements(
        ticker,
        limit=1,
    )

    if announcements:
        announcement = announcements[0]
        category = announcement["category"]
        title = announcement["title"]
    else:
        category = "Other"
        title = "No recent announcements"

    announcement_score = get_announcement_score(category)

    #
    # Legacy opportunity model
    #

    opportunity = evaluate_opportunity(
        technical_score=technical_score,
        announcement_score=announcement_score,
        volume_score=0,
        risk_score=0,
    )

    #
    # New Analyst
    #

    analyst_review = review_opportunity(
        announcement_title=title,
        price_change=float(
            str(quote["percent"]).replace("%", "")
        ),
        relative_volume=(
            indicators["rvol"] if indicators else 1.0
        ),
        trend=(
            indicators["trend"] if indicators else "Neutral"
        ),
        above_vwap=(
            quote["price"] > indicators["vwap"]
            if indicators
            else False
        ),
        breakout=(
            quote["price"] > indicators["ema20"]
            if indicators
            else False
        ),
        technical_score=technical_score,
        risk_score=0,
    )

    analyst_brief = build_brief(
        analyst_review
    )

    #
    # Backwards-compatible return structure
    #

    return {
        # Existing dashboard data
        "quote": quote,
        "history": history,
        "indicators": indicators,

        # Existing scoring
        "technical_score": technical_score,
        "announcement_category": category,
        "announcement_score": announcement_score,
        "volume_score": 0,
        "risk_score": 0,

        # Existing Opportunity Engine outputs
        "opportunity_score": opportunity["score"],
        "rating": opportunity["rating"],
        "confidence": opportunity["confidence"],
        "timing": opportunity["timing"],
        "strengths": opportunity["strengths"],
        "risks": opportunity["risks"],
        "action": opportunity["action"],

        # New Analyst
        "analyst": analyst_review,
        "brief": analyst_brief,
    }