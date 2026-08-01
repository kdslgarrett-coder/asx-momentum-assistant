"""
MomentumHQ AI Analysis Engine
Version 2.4.0

This module currently uses a rule engine.

In future versions this can be replaced by:

- OpenAI
- Claude
- Gemini
- Ollama

without changing the dashboard.
"""

RULES = {

    "Major Contract": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "summary": (
            "The company has announced a major contract "
            "that could increase future revenue."
        ),
        "reason": (
            "Large customer contracts are generally viewed "
            "positively by the market."
        ),
    },

    "Drill Results": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "Medium",
        "summary": (
            "The company has released exploration or "
            "drilling results."
        ),
        "reason": (
            "Positive exploration results can improve "
            "future resource potential."
        ),
    },

    "Resource Upgrade": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "summary": (
            "The company's reported mineral resource "
            "has increased."
        ),
        "reason": (
            "Resource upgrades often improve company value."
        ),
    },

    "Quarterly": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Medium",
        "summary": (
            "Routine quarterly operational update."
        ),
        "reason": (
            "Further review is required to determine "
            "whether the operational results exceeded "
            "market expectations."
        ),
    },

    "Presentation": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "summary": (
            "Investor presentation released."
        ),
        "reason": (
            "Presentations normally summarise existing "
            "information rather than announce new events."
        ),
    },

    "Capital Raising": {
        "icon": "🔴",
        "sentiment": "Negative",
        "confidence": "Medium",
        "summary": (
            "The company is raising additional capital."
        ),
        "reason": (
            "Capital raisings may dilute existing "
            "shareholders."
        ),
    },

    "Trading Halt": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Low",
        "summary": (
            "Trading has been temporarily halted."
        ),
        "reason": (
            "A trading halt does not indicate whether "
            "future news will be positive or negative."
        ),
    },

    "Director Interest": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "summary": (
            "Director interest notice released."
        ),
        "reason": (
            "These announcements are usually regulatory."
        ),
    },

    "Other": {
        "icon": "⚪",
        "sentiment": "Unknown",
        "confidence": "Low",
        "summary": (
            "No automated analysis available."
        ),
        "reason": (
            "Announcement type not yet recognised."
        ),
    },

}


def analyse(category):
    """
    Returns analysis for an announcement category.
    """

    return RULES.get(
        category,
        RULES["Other"],
    )