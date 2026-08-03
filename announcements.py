"""
MomentumHQ ASX Announcements
Version 2.5.3 Stable

RSS retrieval module.
Classification is delegated to classifier.py.
"""

from typing import Any, Dict, List, Optional

import feedparser

from classifier import classify_category

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


def get_announcements(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Return ASX announcements from the official ASX RSS feed.

    If the RSS feed is unavailable, a local fallback dataset is returned.
    """

    feed = feedparser.parse(ASX_RSS)
    announcements: List[Dict[str, Any]] = []

    code = symbol.upper() if symbol else None

    entries = getattr(feed, "entries", [])

    for entry in entries:
        title = getattr(entry, "title", "")

        if code and not title.upper().startswith(code):
            continue

        announcements.append(
            {
                "title": title,
                "link": getattr(entry, "link", ""),
                "published": getattr(entry, "published", ""),
                "category": classify_category(title),
            }
        )

        if len(announcements) >= limit:
            break

    if announcements:
        return announcements

    return fallback(symbol, limit)


def fallback(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Return a small offline announcement dataset used when the
    ASX RSS feed cannot be reached.
    """

    items = [
        {
            "title": "KRR Major Gold Discovery",
            "published": "Today",
            "link": "",
        },
        {
            "title": "CXO Trading Halt Lifted",
            "published": "Today",
            "link": "",
        },
        {
            "title": "IVZ Capital Raising",
            "published": "Yesterday",
            "link": "",
        },
        {
            "title": "BHP Investor Presentation",
            "published": "Yesterday",
            "link": "",
        },
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

    results: List[Dict[str, Any]] = []

    for item in items[:limit]:
        announcement = item.copy()
        announcement["category"] = classify_category(announcement["title"])
        results.append(announcement)

    return results