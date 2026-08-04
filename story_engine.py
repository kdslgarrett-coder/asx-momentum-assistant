"""
MomentumHQ Analyst Brief Engine
Version 2.7.0-dev

Converts the Analyst's structured reasoning into an
investor-friendly briefing.

The Brief Engine never performs analysis.

Its responsibility is to communicate the Analyst's opinion
clearly and consistently.
"""

from typing import Any, Dict


def build_brief(review: Dict[str, Any]) -> Dict[str, str]:
    """
    Convert an Analyst review into a structured briefing.
    """

    catalyst = review["catalyst"]
    confirmation = review["confirmation"]
    confidence = review["confidence"]

    #
    # What happened?
    #

    what_happened = (
        f"A {catalyst['category'].lower()} has been identified."
    )

    #
    # Why it matters
    #

    why_it_matters = catalyst["reason"]

    #
    # Market confirmation
    #

    market_confirmation = confirmation["summary"]

    #
    # Risks
    #

    if confirmation["confirmed"]:
        risks = (
            "The opportunity appears well supported, however "
            "continued market confirmation should be monitored."
        )
    else:
        risks = (
            "The catalyst has not yet been confirmed by the market. "
            "Additional buying strength would improve confidence."
        )

    #
    # Recommendation
    #

    recommendation = confidence["recommendation"]

    return {
        "headline": catalyst["category"],
        "confidence": str(confidence["confidence"]),
        "rating": confidence["rating"],
        "what_happened": what_happened,
        "why_it_matters": why_it_matters,
        "market_confirmation": market_confirmation,
        "risks": risks,
        "recommendation": recommendation,
    }