"""
MomentumHQ Scoring Rules
Version 2.5.2

Central scoring configuration for announcement analysis.
"""

RULES = {
    "Major Contract": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "base_score": 18,
        "summary": "The company has announced a significant customer or commercial contract.",
        "reason": "Large contracts can materially improve future revenue and earnings."
    },
    "Drill Results": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "Medium",
        "base_score": 16,
        "summary": "Exploration or drilling results have been released.",
        "reason": "Strong exploration results may increase project value."
    },
    "Resource Upgrade": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "base_score": 17,
        "summary": "Mineral resource or reserve has increased.",
        "reason": "Resource growth generally improves long-term project economics."
    },
    "Capital Raising": {
        "icon": "🔴",
        "sentiment": "Negative",
        "confidence": "Medium",
        "base_score": 2,
        "summary": "The company is raising additional capital.",
        "reason": "New equity may dilute existing shareholders."
    },
    "Trading Halt": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Low",
        "base_score": 6,
        "summary": "Trading has been halted pending an announcement.",
        "reason": "A halt alone is neither positive nor negative."
    },
    "Quarterly": {
        "icon": "🟡",
        "sentiment": "Neutral",
        "confidence": "Medium",
        "base_score": 10,
        "summary": "Routine quarterly operational or cashflow report.",
        "reason": "Further review is required to assess performance."
    },
    "Presentation": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "base_score": 3,
        "summary": "Investor presentation released.",
        "reason": "Usually summarises previously announced information."
    },
    "Director Interest": {
        "icon": "🔵",
        "sentiment": "Informational",
        "confidence": "Low",
        "base_score": 4,
        "summary": "Director interest notice lodged.",
        "reason": "Primarily a regulatory disclosure."
    },
    "Dividend": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "Medium",
        "base_score": 14,
        "summary": "Dividend announcement released.",
        "reason": "Dividends can indicate financial strength."
    },
    "Acquisition": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "Medium",
        "base_score": 15,
        "summary": "Acquisition or merger announced.",
        "reason": "Strategic acquisitions may enhance future growth."
    },
    "Profit Upgrade": {
        "icon": "🟢",
        "sentiment": "Positive",
        "confidence": "High",
        "base_score": 20,
        "summary": "Company has upgraded earnings guidance.",
        "reason": "Profit upgrades are often well received by the market."
    },
    "Other": {
        "icon": "⚪",
        "sentiment": "Unknown",
        "confidence": "Low",
        "base_score": 5,
        "summary": "No specific rule available.",
        "reason": "Announcement type is not yet recognised."
    },
}

CONFIDENCE_POINTS = {
    "High": 5,
    "Medium": 3,
    "Low": 1,
}

SENTIMENT_POINTS = {
    "Positive": 5,
    "Neutral": 2,
    "Informational": 1,
    "Negative": 0,
    "Unknown": 0,
}