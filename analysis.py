"""
MomentumHQ AI Analysis Engine
Version 2.5.1

Rule-based announcement analysis with explainable scoring.
"""

BASE_RULES = {
    "Major Contract": ("🟢", "Positive", "High", 18,
        "The company has announced a major contract that could increase future revenue.",
        "Large customer contracts are generally viewed positively by the market."),
    "Drill Results": ("🟢", "Positive", "Medium", 16,
        "The company has released exploration or drilling results.",
        "Positive exploration results can improve future resource potential."),
    "Resource Upgrade": ("🟢", "Positive", "High", 17,
        "The company's reported mineral resource has increased.",
        "Resource upgrades often improve company value."),
    "Quarterly": ("🟡", "Neutral", "Medium", 10,
        "Routine quarterly operational update.",
        "Further review is required to determine whether results exceeded expectations."),
    "Presentation": ("🔵", "Informational", "Low", 3,
        "Investor presentation released.",
        "Presentations normally summarise existing information."),
    "Capital Raising": ("🔴", "Negative", "Medium", 2,
        "The company is raising additional capital.",
        "Capital raisings may dilute existing shareholders."),
    "Trading Halt": ("🟡", "Neutral", "Low", 6,
        "Trading has been temporarily halted.",
        "A trading halt does not indicate whether future news will be positive or negative."),
    "Director Interest": ("🔵", "Informational", "Low", 4,
        "Director interest notice released.",
        "These announcements are usually regulatory."),
    "Other": ("⚪", "Unknown", "Low", 5,
        "No automated analysis available.",
        "Announcement type not yet recognised."),
}

CONFIDENCE_POINTS = {"High": 5, "Medium": 3, "Low": 1}
SENTIMENT_POINTS = {"Positive": 5, "Neutral": 2, "Informational": 1, "Negative": 0}

def analyse(category):
    icon, sentiment, confidence, base, summary, reason = BASE_RULES.get(
        category, BASE_RULES["Other"]
    )

    breakdown = {
        "Base": base,
        "Confidence": CONFIDENCE_POINTS[confidence],
        "Sentiment": SENTIMENT_POINTS[sentiment],
    }

    score = min(30, sum(breakdown.values()))

    return {
        "icon": icon,
        "sentiment": sentiment,
        "confidence": confidence,
        "score": score,
        "breakdown": breakdown,
        "summary": summary,
        "reason": reason,
    }

def get_announcement_score(category):
    return analyse(category)["score"]