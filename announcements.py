"""
Announcement functions for MomentumHQ
"""

import feedparser

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


def get_announcements(limit=10):
    """
    Returns the latest ASX announcements.

    Returns:
        [
            {
                "title": "...",
                "link": "...",
                "published": "...",
                "category": "Major Contract"
            }
        ]
    """

    feed = feedparser.parse(ASX_RSS)

    announcements = []

    for entry in feed.entries[:limit]:

        title = entry.title

        announcements.append(
            {
                "title": title,
                "link": entry.link,
                "published": getattr(entry, "published", ""),
                "category": classify(title),
            }
        )

    return announcements


def classify(title):
    """
    Classify an announcement for momentum scoring.
    """

    t = title.lower()

    if "trading halt" in t:
        return "Trading Halt"

    if "contract" in t:
        return "Major Contract"

    if "quarterly" in t:
        return "Quarterly"

    if "appendix 4c" in t:
        return "Quarterly"

    if "resource" in t:
        return "Resource Upgrade"

    if "drill" in t:
        return "Drill Results"

    if "capital raising" in t:
        return "Capital Raising"

    if "placement" in t:
        return "Capital Raising"

    if "director" in t:
        return "Director Selling"

    return "Other"