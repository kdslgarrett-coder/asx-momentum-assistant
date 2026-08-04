"""
MomentumHQ Confidence Engine
Version 2.7.0-dev

Combines evidence from the Analyst's engines into a single
confidence assessment.
"""

from typing import Any, Dict


def evaluate_confidence(
    *,
    catalyst_impact: str,
    confirmation_score: int,
    technical_score: int,
    risk_score: int,
) -> Dict[str, Any]:
    """
    Evaluate the overall confidence in an opportunity.
    """

    confidence = 0

    #
    # Catalyst
    #

    if catalyst_impact == "High":
        confidence += 30

    elif catalyst_impact == "Medium":
        confidence += 20

    else:
        confidence += 10

    #
    # Market Confirmation
    #

    confidence += min(confirmation_score, 35)

    #
    # Technical Health
    #

    confidence += min(technical_score, 20)

    #
    # Risk
    #

    confidence -= min(risk_score, 15)

    confidence = max(0, min(confidence, 100))

    #
    # Rating
    #

    if confidence >= 90:
        rating = "Exceptional"

    elif confidence >= 80:
        rating = "High"

    elif confidence >= 65:
        rating = "Good"

    elif confidence >= 50:
        rating = "Watch"

    else:
        rating = "Ignore"

    #
    # Analyst recommendation
    #

    if confidence >= 90:
        recommendation = "Investigate immediately."

    elif confidence >= 80:
        recommendation = (
            "High-priority opportunity requiring further analysis."
        )

    elif confidence >= 65:
        recommendation = (
            "Worth monitoring closely."
        )

    elif confidence >= 50:
        recommendation = (
            "Await stronger confirmation."
        )

    else:
        recommendation = (
            "Insufficient evidence at this time."
        )

    return {
        "confidence": confidence,
        "rating": rating,
        "recommendation": recommendation,
    }