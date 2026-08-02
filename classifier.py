"""
MomentumHQ Announcement Classifier
Version 2.5.2

Centralised announcement classification engine.
"""

from typing import Dict, List

_RULES = [
    ("Trading Halt", ["trading halt", "voluntary suspension"]),
    ("Major Contract", ["contract", "agreement", "award"]),
    ("Resource Upgrade", ["resource", "jorc", "ore reserve"]),
    ("Drill Results", ["drill", "drilling", "assay", "intercept"]),
    ("Capital Raising", ["capital raising", "placement", "entitlement offer", "share purchase plan"]),
    ("Quarterly", ["quarterly", "appendix 4c", "appendix 5b"]),
    ("Presentation", ["presentation", "investor presentation"]),
    ("Director Interest", ["director", "appendix 3x", "appendix 3y"]),
    ("Dividend", ["dividend"]),
    ("Acquisition", ["acquisition", "acquire", "scheme of arrangement"]),
    ("Profit Upgrade", ["profit upgrade", "guidance upgrade"]),
]


def classify(title: str) -> Dict:
    """Classify an announcement title."""

    text = (title or "").lower()
    matches: List[str] = []

    for category, keywords in _RULES:
        hit = [k for k in keywords if k in text]
        if hit:
            matches.extend(hit)
            confidence = "High" if len(hit) > 1 else "Medium"
            return {
                "category": category,
                "confidence": confidence,
                "matched_keywords": matches,
            }

    return {
        "category": "Other",
        "confidence": "Low",
        "matched_keywords": [],
    }


def classify_category(title: str) -> str:
    """Backward-compatible helper returning only the category."""
    return classify(title)["category"]