"""
MomentumHQ Analysis Engine
Version 2.6.0-dev

Shared analysis engine for dashboard modules.

Task 14A:
- Centralise technical, opportunity and announcement analysis.
- Preserve existing behaviour.
- Dashboard modules consume this module only.
"""

from typing import Any, Dict, Optional

from analysis import analyse, get_announcement_score
from announcements import get_announcements
from history import get_history
from indicators import calculate_indicators
from market import search_quote
from opportunity_engine import evaluate_opportunity


def analyse_announcement(category: str) -> Dict[str, Any]:
    """
    Return the standard announcement analysis for a category.

    Dashboard modules should use this helper instead of importing
    analysis.py directly.
    """
    return analyse(category)


def analyse_stock(ticker: str) -> Optional[Dict[str, Any]]:
    """
    Analyse a stock and return all information required by dashboard modules.

    This module is the single source of truth for:
    - Technical analysis
    - Announcement scoring
    - Opportunity evaluation

    Dashboard modules should render these results only.
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

    announcements = get_announcements(ticker, limit=1)

    if announcements:
        category = announcements[0]["category"]
    else:
        category = "Other"

    announcement_score = get_announcement_score(category)

    opportunity = evaluate_opportunity(
        technical_score=technical_score,
        announcement_score=announcement_score,
        volume_score=0,
        risk_score=0,
    )

    return {
        "quote": quote,
        "history": history,
        "indicators": indicators,
        "technical_score": technical_score,
        "announcement_category": category,
        "announcement_score": announcement_score,
        "volume_score": 0,
        "risk_score": 0,
        "opportunity_score": opportunity["score"],
        "rating": opportunity["rating"],
        "confidence": opportunity["confidence"],
        "timing": opportunity["timing"],
        "strengths": opportunity["strengths"],
        "risks": opportunity["risks"],
        "action": opportunity["action"],
    }