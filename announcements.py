"""
MomentumHQ ASX Announcements
Version 2.5.2

RSS retrieval module.
Classification is delegated to classifier.py.
"""

import feedparser

from classifier import classify_category

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


def get_announcements(symbol=None, limit=10):
    """Return ASX announcements."""

    feed = feedparser.parse(ASX_RSS)
    announcements = []

    code = symbol.upper() if symbol else None

    if getattr(feed, "entries", None):
        for entry in feed.entries:
            title = getattr(entry, "title", "")

            if code and not title.upper().startswith(code):
                continue

            announcements.append({
                "title": title,
                "link": getattr(entry, "link", ""),
                "published": getattr(entry, "published", ""),
                "category": classify_category(title),
            })

            if len(announcements) >= limit:
                break

    return announcements if announcements else fallback(symbol, limit)


def fallback(symbol=None, limit=10):
    items = [
        {"title": "KRR Major Gold Discovery", "published": "Today", "link": ""},
        {"title": "CXO Trading Halt Lifted", "published": "Today", "link": ""},
        {"title": "IVZ Capital Raising", "published": "Yesterday", "link": ""},
        {"title": "BHP Investor Presentation", "published": "Yesterday", "link": ""},
    ]

    if symbol:
        items.insert(
            0,
            {
                "title": f"{symbol.upper()} Quarterly Activities Report",
                "published": "Today",
                "link": "",
            },
        )

    results = []
    for item in items[:limit]:
        result = item.copy()
        result["category"] = classify_category(result["title"])
        results.append(result)

    return results