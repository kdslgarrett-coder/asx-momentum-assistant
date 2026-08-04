"""
MomentumHQ Catalyst Intelligence
Version 2.7.0-dev

Provides catalyst classification and intelligence for ASX announcements.
"""

from typing import Dict, List, Sequence, Tuple

Rule = Tuple[str, Sequence[str]]

_RULES: List[Rule] = [
    ("Trading Halt", ["trading halt", "voluntary suspension"]),
    ("Major Contract", ["contract", "agreement", "award"]),
    ("Resource Upgrade", ["resource", "jorc", "ore reserve"]),
    ("Drill Results", ["drill", "drilling", "assay", "intercept"]),
    (
        "Capital Raising",
        [
            "capital raising",
            "placement",
            "entitlement offer",
            "share purchase plan",
        ],
    ),
    ("Quarterly", ["quarterly", "appendix 4c", "appendix 5b"]),
    ("Presentation", ["presentation", "investor presentation"]),
    ("Director Interest", ["director", "appendix 3x", "appendix 3y"]),
    ("Dividend", ["dividend"]),
    ("Acquisition", ["acquisition", "acquire", "scheme of arrangement"]),
    ("Profit Upgrade", ["profit upgrade", "guidance upgrade"]),
]

CATALYST_LIBRARY = {
    "Trading Halt": {
        "impact": "High",
        "market_reaction": "Variable",
        "holding_period": "1–5 days",
        "requires_confirmation": True,
        "historical_reliability": 75,
        "reason": (
            "Trading halts often precede significant announcements. "
            "The market reaction determines whether the opportunity develops."
        ),
    },
    "Major Contract": {
        "impact": "High",
        "market_reaction": "Often Bullish",
        "holding_period": "2–10 days",
        "requires_confirmation": True,
        "historical_reliability": 82,
        "reason": (
            "Major contracts can materially improve revenue outlook "
            "and often attract institutional buying."
        ),
    },
    "Resource Upgrade": {
        "impact": "High",
        "market_reaction": "Often Bullish",
        "holding_period": "3–15 days",
        "requires_confirmation": True,
        "historical_reliability": 86,
        "reason": (
            "Resource upgrades can materially improve project value "
            "when supported by strong buying."
        ),
    },
    "Drill Results": {
        "impact": "High",
        "market_reaction": "Often Bullish",
        "holding_period": "2–10 days",
        "requires_confirmation": True,
        "historical_reliability": 80,
        "reason": (
            "High-grade drill results frequently generate momentum, "
            "provided the market validates the results."
        ),
    },
    "Capital Raising": {
        "impact": "Medium",
        "market_reaction": "Often Bearish",
        "holding_period": "1–5 days",
        "requires_confirmation": True,
        "historical_reliability": 72,
        "reason": (
            "Capital raisings can dilute shareholders, although market "
            "reaction depends on purpose and pricing."
        ),
    },
    "Quarterly": {
        "impact": "Medium",
        "market_reaction": "Variable",
        "holding_period": "1–3 days",
        "requires_confirmation": True,
        "historical_reliability": 55,
        "reason": (
            "Quarterly reports provide operational updates, but only "
            "meaningful surprises tend to create momentum."
        ),
    },
    "Presentation": {
        "impact": "Low",
        "market_reaction": "Usually Neutral",
        "holding_period": "Same Day",
        "requires_confirmation": False,
        "historical_reliability": 20,
        "reason": (
            "Investor presentations rarely create new momentum without "
            "additional market-moving information."
        ),
    },
    "Director Interest": {
        "impact": "Low",
        "market_reaction": "Usually Neutral",
        "holding_period": "Same Day",
        "requires_confirmation": False,
        "historical_reliability": 10,
        "reason": (
            "Director interest notices are generally administrative and "
            "rarely influence price action."
        ),
    },
    "Dividend": {
        "impact": "Medium",
        "market_reaction": "Variable",
        "holding_period": "1–5 days",
        "requires_confirmation": True,
        "historical_reliability": 60,
        "reason": (
            "Dividend announcements may influence investor demand "
            "depending on expectations."
        ),
    },
    "Acquisition": {
        "impact": "High",
        "market_reaction": "Variable",
        "holding_period": "3–10 days",
        "requires_confirmation": True,
        "historical_reliability": 78,
        "reason": (
            "Acquisitions can significantly alter future growth prospects "
            "if the market supports the strategy."
        ),
    },
    "Profit Upgrade": {
        "impact": "High",
        "market_reaction": "Often Bullish",
        "holding_period": "2–10 days",
        "requires_confirmation": True,
        "historical_reliability": 88,
        "reason": (
            "Profit upgrades are among the strongest earnings-related "
            "catalysts when confirmed by buying."
        ),
    },
    "Other": {
        "impact": "Low",
        "market_reaction": "Unknown",
        "holding_period": "Unknown",
        "requires_confirmation": True,
        "historical_reliability": 25,
        "reason": (
            "The announcement does not match a recognised catalyst and "
            "requires further assessment."
        ),
    },
}


def classify(title: str) -> Dict:
    """
    Classify an ASX announcement and return catalyst intelligence.
    """

    text = (title or "").lower()

    for category, keywords in _RULES:
        matched_keywords = [k for k in keywords if k in text]

        if matched_keywords:
            result = {
                "category": category,
                "confidence": (
                    "High" if len(matched_keywords) > 1 else "Medium"
                ),
                "matched_keywords": matched_keywords,
            }

            result.update(CATALYST_LIBRARY[category])
            return result

    result = {
        "category": "Other",
        "confidence": "Low",
        "matched_keywords": [],
    }

    result.update(CATALYST_LIBRARY["Other"])
    return result


def classify_category(title: str) -> str:
    """
    Backwards-compatible helper returning only the category.
    """

    return classify(title)["category"]