"""
MomentumHQ AI Analysis Engine
Version 2.5.1

Rule-based announcement analysis with announcement scoring.
"""

RULES = {
    "Major Contract": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "score": 28,
        "summary": "The company has announced a major contract that could increase future revenue.",
        "reason": "Large customer contracts are generally viewed positively by the market.",
    },
    "Drill Results": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "Medium",
        "score": 26,
        "summary": "The company has released exploration or drilling results.",
        "reason": "Positive exploration results can improve future resource potential.",
    },
    "Resource Upgrade": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "score": 24,
        "summary": "The company's reported mineral resource has increased.",
        "reason": "Resource upgrades often improve company value.",
    },
    "Quarterly": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Medium",
        "score": 15,
        "summary": "Routine quarterly operational update.",
        "reason": "Further review is required to determine whether results exceeded expectations.",
    },
    "Presentation": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "score": 5,
        "summary": "Investor presentation released.",
        "reason": "Presentations normally summarise existing information.",
    },
    "Capital Raising": {
        "icon": "🔴",
        "sentiment": "Negative",
        "confidence": "Medium",
        "score": 4,
        "summary": "The company is raising additional capital.",
        "reason": "Capital raisings may dilute existing shareholders.",
    },
    "Trading Halt": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Low",
        "score": 10,
        "summary": "Trading has been temporarily halted.",
        "reason": "A trading halt does not indicate whether future news will be positive or negative.",
    },
    "Director Interest": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "score": 8,
        "summary": "Director interest notice released.",
        "reason": "These announcements are usually regulatory.",
    },
    "Other": {
        "icon": "⚪",
        "sentiment": "Unknown",
        "confidence": "Low",
        "score": 10,
        "summary": "No automated analysis available.",
        "reason": "Announcement type not yet recognised.",
    },
}

def analyse(category):
    """
    Returns analysis for an announcement category.
    """
    return RULES.get(category, RULES["Other"])

def get_announcement_score(category):
    """
    Returns the announcement score (0-30).
    """
    return analyse(category)["score"]