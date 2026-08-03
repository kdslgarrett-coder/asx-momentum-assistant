"""
MomentumHQ Announcement Classifier
Version 2.5.3

Centralised announcement classification engine.
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


def classify(title: str) -> Dict:
    """
    Classify an ASX announcement title.

    Returns:
        {
            "category": str,
            "confidence": str,
            "matched_keywords": list[str],
        }
    """

    text = (title or "").lower()

    for category, keywords in _RULES:
        matched_keywords = [keyword for keyword in keywords if keyword in text]

        if matched_keywords:
            return {
                "category": category,
                "confidence": (
                    "High" if len(matched_keywords) > 1 else "Medium"
                ),
                "matched_keywords": matched_keywords,
            }

    return {
        "category": "Other",
        "confidence": "Low",
        "matched_keywords": [],
    }


def classify_category(title: str) -> str:
    """
    Backwards-compatible helper returning only the category.
    """

    return classify(title)["category"]