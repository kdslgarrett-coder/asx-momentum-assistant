"""
MomentumHQ Opportunity Intelligence Engine
Version 2.5.0

The Opportunity Engine provides:

- Opportunity Score
- Rating
- Timing (future)
- Confidence (future)
- Explainability (future)
"""

from typing import Dict


def calculate_opportunity_score(
    technical_score: int,
    announcement_score: int,
    volume_score: int,
    risk_score: int,
) -> int:
    """
    Calculate the overall Opportunity Score.

    Weighting (Version 1)

    Technical     50%
    Announcements 30%
    Volume        10%
    Risk          10%
    """

    technical = (technical_score / 40) * 50
    announcements = (announcement_score / 30) * 30
    volume = (volume_score / 10) * 10
    risk = (risk_score / 10) * 10

    score = technical + announcements + volume + risk

    return round(max(0, min(score, 100)))


def get_rating(score: int) -> str:

    if score >= 85:
        return "Exceptional Opportunity"

    if score >= 70:
        return "Strong Opportunity"

    if score >= 55:
        return "Opportunity"

    if score >= 40:
        return "Watch"

    return "Avoid"


def calculate_timing(minutes: int) -> str:

    if minutes <= 30:
        return "Early"

    if minutes <= 90:
        return "Building"

    if minutes <= 240:
        return "Confirmed"

    if minutes <= 480:
        return "Mature"

    return "Passed"


def calculate_confidence(confirmations: int) -> int:

    confidence = confirmations * 20

    return max(0, min(confidence, 100))


def explain_score(
    technical_score: int,
    announcement_score: int,
    volume_score: int,
    risk_score: int,
) -> Dict:

    return {
        "Technical": technical_score,
        "Announcements": announcement_score,
        "Volume": volume_score,
        "Risk": risk_score,
        "Total": calculate_opportunity_score(
            technical_score,
            announcement_score,
            volume_score,
            risk_score,
        ),
    }