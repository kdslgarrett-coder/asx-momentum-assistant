"""
MomentumHQ Confirmation Engine
Version 2.7.0-dev

Determines whether the market is confirming a potential catalyst.

The Confirmation Engine does not know anything about announcements,
companies or sectors.

Its only responsibility is to evaluate whether current market
behaviour supports a potential opportunity.
"""

from typing import Any, Dict, List


def evaluate_confirmation(
    *,
    price_change: float,
    relative_volume: float,
    trend: str,
    above_vwap: bool,
    breakout: bool,
) -> Dict[str, Any]:
    """
    Evaluate market confirmation.

    Parameters
    ----------
    price_change
        Percentage price movement.

    relative_volume
        Relative Volume (RVOL).

    trend
        Bullish / Neutral / Bearish

    above_vwap
        True if price is above VWAP.

    breakout
        True if a breakout has been detected.

    Returns
    -------
    Dictionary containing confirmation analysis.
    """

    score = 0
    evidence: List[str] = []

    #
    # Price Confirmation
    #

    if price_change >= 5:
        score += 10
        evidence.append(f"Strong price movement (+{price_change:.1f}%)")

    elif price_change >= 2:
        score += 6
        evidence.append(f"Positive price movement (+{price_change:.1f}%)")

    elif price_change > 0:
        score += 2
        evidence.append(f"Price improving (+{price_change:.1f}%)")

    else:
        evidence.append(f"Weak price action ({price_change:.1f}%)")

    #
    # Volume Confirmation
    #

    if relative_volume >= 3:
        score += 10
        evidence.append(f"Exceptional volume ({relative_volume:.1f}×)")

    elif relative_volume >= 2:
        score += 7
        evidence.append(f"Strong volume ({relative_volume:.1f}×)")

    elif relative_volume >= 1.5:
        score += 4
        evidence.append(f"Above-average volume ({relative_volume:.1f}×)")

    else:
        evidence.append("Normal trading volume")

    #
    # Trend
    #

    if trend == "Bullish":
        score += 6
        evidence.append("Bullish trend")

    elif trend == "Neutral":
        score += 2
        evidence.append("Neutral trend")

    else:
        evidence.append("Bearish trend")

    #
    # VWAP
    #

    if above_vwap:
        score += 4
        evidence.append("Trading above VWAP")

    #
    # Breakout
    #

    if breakout:
        score += 4
        evidence.append("Breakout confirmed")

    #
    # Confirmation strength
    #

    if score >= 30:
        strength = "Strong"

    elif score >= 20:
        strength = "Moderate"

    elif score >= 10:
        strength = "Weak"

    else:
        strength = "None"

    confirmed = score >= 20

    #
    # Analyst narrative
    #

    if strength == "Strong":
        summary = (
            "The market is strongly validating the current move through "
            "price appreciation, healthy participation and positive trend."
        )

    elif strength == "Moderate":
        summary = (
            "The market is showing encouraging confirmation, although "
            "additional strength would improve confidence."
        )

    elif strength == "Weak":
        summary = (
            "Some confirmation exists, however the evidence is currently "
            "insufficient for a high-confidence opportunity."
        )

    else:
        summary = (
            "The market is not currently validating this opportunity."
        )

    return {
        "score": score,
        "strength": strength,
        "confirmed": confirmed,
        "summary": summary,
        "evidence": evidence,
    }