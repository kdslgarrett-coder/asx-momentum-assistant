"""
Momentum scoring engine for MomentumHQ
"""

from config import ANNOUNCEMENT_SCORES, TECHNICAL_SCORES


def score_announcement(event: str) -> int:
    """
    Return the score for a recognised announcement.

    Example:
        score_announcement("Major Contract")
    """

    return ANNOUNCEMENT_SCORES.get(event, 0)


def score_technical(signal: str) -> int:
    """
    Return the score for a recognised technical signal.
    """

    return TECHNICAL_SCORES.get(signal, 0)


def calculate_score(
    announcements=None,
    technicals=None,
):
    """
    Calculate the combined momentum score.

    Returns:

        {
            "announcement": 65,
            "technical": 30,
            "overall": 95,
            "recommendation": "BUY"
        }
    """

    if announcements is None:
        announcements = []

    if technicals is None:
        technicals = []

    announcement_score = sum(
        score_announcement(item)
        for item in announcements
    )

    technical_score = sum(
        score_technical(item)
        for item in technicals
    )

    overall = announcement_score + technical_score

    if overall >= 60:
        recommendation = "BUY"

    elif overall >= 30:
        recommendation = "WATCH"

    else:
        recommendation = "IGNORE"

    return {
        "announcement": announcement_score,
        "technical": technical_score,
        "overall": overall,
        "recommendation": recommendation,
    }


def demo_score():
    """
    Demonstration data until live feeds are connected.
    """

    announcements = [
        "Major Contract",
        "Broker Upgrade",
    ]

    technicals = [
        "Above EMA9",
        "EMA9 above EMA20",
        "High Volume Ratio",
    ]

    return calculate_score(
        announcements,
        technicals,
    )