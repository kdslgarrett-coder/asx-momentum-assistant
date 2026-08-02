"""
MomentumHQ AI Analysis Engine
Version 2.5.2

Analysis engine driven by scoring_rules.py.
"""

from scoring_rules import (
    RULES,
    CONFIDENCE_POINTS,
    SENTIMENT_POINTS,
)


def analyse(category):
    rule = RULES.get(category, RULES["Other"])

    breakdown = {
        "Base": rule["base_score"],
        "Confidence": CONFIDENCE_POINTS.get(rule["confidence"], 0),
        "Sentiment": SENTIMENT_POINTS.get(rule["sentiment"], 0),
    }

    score = min(30, sum(breakdown.values()))

    return {
        "icon": rule["icon"],
        "sentiment": rule["sentiment"],
        "confidence": rule["confidence"],
        "score": score,
        "breakdown": breakdown,
        "summary": rule["summary"],
        "reason": rule["reason"],
    }


def get_announcement_score(category):
    return analyse(category)["score"]