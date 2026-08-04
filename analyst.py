"""
MomentumHQ Analyst
Version 2.7.0-dev

The Analyst coordinates all specialist engines and produces a
single structured review of an opportunity.

This module intentionally contains very little business logic.

Its responsibility is orchestration.
"""

from typing import Any, Dict

from classifier import classify
from confirmation_engine import evaluate_confirmation
from confidence_engine import evaluate_confidence


def review_opportunity(
    *,
    announcement_title: str,
    price_change: float,
    relative_volume: float,
    trend: str,
    above_vwap: bool,
    breakout: bool,
    technical_score: int,
    risk_score: int,
) -> Dict[str, Any]:
    """
    Review a potential opportunity.

    This function coordinates the specialist engines and returns
    a single structured assessment.
    """

    #
    # Step 1
    # Understand the catalyst.
    #

    catalyst = classify(announcement_title)

    #
    # Step 2
    # Determine whether the market is confirming it.
    #

    confirmation = evaluate_confirmation(
        price_change=price_change,
        relative_volume=relative_volume,
        trend=trend,
        above_vwap=above_vwap,
        breakout=breakout,
    )

    #
    # Step 3
    # Determine overall confidence.
    #

    confidence = evaluate_confidence(
        catalyst_impact=catalyst["impact"],
        confirmation_score=confirmation["score"],
        technical_score=technical_score,
        risk_score=risk_score,
    )

    #
    # Step 4
    # Return the Analyst's structured review.
    #

    return {
        "catalyst": catalyst,
        "confirmation": confirmation,
        "confidence": confidence,
    }