"""
MomentumHQ Opportunity Engine
Version 3.0.0-dev

Central opportunity evaluation engine.
"""

from typing import Dict, List

from score import (
    calculate_confidence,
    calculate_opportunity_score,
    calculate_timing,
    get_rating,
)


def evaluate_opportunity(
    technical_score: int,
    announcement_score: int,
    volume_score: int = 0,
    risk_score: int = 0,
    confirmations: int = 3,
    minutes_since_signal: int = 30,
) -> Dict:
    """
    Evaluate a trading opportunity and return a standardised result.
    """

    score = calculate_opportunity_score(
        technical_score=technical_score,
        announcement_score=announcement_score,
        volume_score=volume_score,
        risk_score=risk_score,
    )

    strengths: List[str] = []
    risks: List[str] = []

    if technical_score >= 30:
        strengths.append("Strong technical trend")

    if announcement_score >= 20:
        strengths.append("Positive announcement")

    if volume_score >= 7:
        strengths.append("High relative volume")

    if risk_score <= 3:
        strengths.append("Low risk profile")
    else:
        risks.append("Elevated risk")

    #
    # Recommended investor action
    #

    if score >= 70:
        action = "Investigate Today"

    elif score >= 40:
        action = "Monitor"

    else:
        action = "Ignore"

    return {
        "score": score,
        "rating": get_rating(score),
        "technical_score": technical_score,
        "announcement_score": announcement_score,
        "volume_score": volume_score,
        "risk_score": risk_score,
        "confidence": calculate_confidence(confirmations),
        "timing": calculate_timing(minutes_since_signal),
        "strengths": strengths,
        "risks": risks,
        "action": action,
    }