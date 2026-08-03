"""
MomentumHQ AI Analysis Engine
Version 2.5.3

Analysis engine driven by scoring_rules.py.
"""

from typing import Any, Dict

from scoring_rules import (
    RULES,
    CONFIDENCE_POINTS,
    SENTIMENT_POINTS,
)

MAX_ANNOUNCEMENT_SCORE = 30


def analyse(category: str) -> Dict[str, Any]:
    """
    Analyse an announcement category and return the derived
    announcement scoring information.

    Unknown categories automatically fall back to the "Other" rule.
    """

    rule = RULES.get(category, RULES["Other"])

    breakdown = {
        "Base": rule["base_score"],
        "Confidence": CONFIDENCE_POINTS.get(rule["confidence"], 0),
        "Sentiment": SENTIMENT_POINTS.get(rule["sentiment"], 0),
    }

    score = min(MAX_ANNOUNCEMENT_SCORE, sum(breakdown.values()))

    return {
        "icon": rule["icon"],
        "sentiment": rule["sentiment"],
        "confidence": rule["confidence"],
        "score": score,
        "breakdown": breakdown,
        "summary": rule["summary"],
        "reason": rule["reason"],
    }


def get_announcement_score(category: str) -> int:
    """
    Return only the announcement score for a category.
    """

    return analyse(category)["score"]