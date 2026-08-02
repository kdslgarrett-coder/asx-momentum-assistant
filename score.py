"""
MomentumHQ Opportunity Intelligence Engine
Version 2.5.1
"""

from typing import Dict

TECHNICAL_MAX = 40
ANNOUNCEMENT_MAX = 30
VOLUME_MAX = 10
RISK_MAX = 10

WEIGHTS = {
    "technical": 50,
    "announcement": 30,
    "volume": 10,
    "risk": 10,
}


def _clamp(value: int, maximum: int) -> int:
    return max(0, min(value, maximum))


def calculate_opportunity_score(
    technical_score: int,
    announcement_score: int,
    volume_score: int,
    risk_score: int,
) -> int:
    technical_score = _clamp(technical_score, TECHNICAL_MAX)
    announcement_score = _clamp(announcement_score, ANNOUNCEMENT_MAX)
    volume_score = _clamp(volume_score, VOLUME_MAX)
    risk_score = _clamp(risk_score, RISK_MAX)

    score = (
        (technical_score / TECHNICAL_MAX) * WEIGHTS["technical"]
        + (announcement_score / ANNOUNCEMENT_MAX) * WEIGHTS["announcement"]
        + (volume_score / VOLUME_MAX) * WEIGHTS["volume"]
        + (risk_score / RISK_MAX) * WEIGHTS["risk"]
    )

    return round(score)


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
    return _clamp(confirmations * 20, 100)


def explain_score(
    technical_score: int,
    announcement_score: int,
    volume_score: int,
    risk_score: int,
) -> Dict:
    return {
        "Technical": _clamp(technical_score, TECHNICAL_MAX),
        "Announcements": _clamp(announcement_score, ANNOUNCEMENT_MAX),
        "Volume": _clamp(volume_score, VOLUME_MAX),
        "Risk": _clamp(risk_score, RISK_MAX),
        "Weights": WEIGHTS.copy(),
        "Total": calculate_opportunity_score(
            technical_score,
            announcement_score,
            volume_score,
            risk_score,
        ),
    }