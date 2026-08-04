"""
MomentumHQ ASX Announcements
Version 2.7.0-dev

RSS retrieval module.

Classification is delegated to classifier.py.

This version enriches announcement metadata with parsed
date/time fields and freshness while remaining backwards
compatible.
"""

from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Any, Dict, List, Optional

import feedparser

from classifier import classify_category

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


def _enrich_announcement(
    title: str,
    link: str,
    published: str,
) -> Dict[str, Any]:
    """
    Build a standard MomentumHQ announcement object.

    Existing fields are preserved while additional metadata
    is added for dashboards and the Analyst.
    """

    announcement: Dict[str, Any] = {
        "title": title,
        "link": link,
        "published": published,
        "category": classify_category(title),
        "published_date": "",
        "published_time": "",
        "published_datetime": None,
        "freshness": "",
    }

    try:
        dt = parsedate_to_datetime(published)

        # Convert timezone-aware values to local time if possible
        if dt.tzinfo is not None:
            dt = dt.astimezone()

        announcement["published_datetime"] = dt
        announcement["published_date"] = dt.strftime("%d %b %Y")
        announcement["published_time"] = dt.strftime("%H:%M")

        today = datetime.now(dt.tzinfo).date()

        if dt.date() == today:
            announcement["freshness"] = "Today"

        elif (today - dt.date()).days == 1:
            announcement["freshness"] = "Yesterday"

        else:
            announcement["freshness"] = dt.strftime("%d %b %Y")

    except Exception:
        #
        # Fallback data (or unexpected formats)
        #

        announcement["published_date"] = published
        announcement["published_time"] = ""
        announcement["freshness"] = published

    return announcement


def get_announcements(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Return ASX announcements from the official ASX RSS feed.

    If the RSS feed is unavailable, a local fallback dataset
    is returned.
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
            _enrich_announcement(
                title=title,
                link=getattr(entry, "link", ""),
                published=getattr(entry, "published", ""),
            )
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
        results.append(
            _enrich_announcement(
                title=item["title"],
                link=item["link"],
                published=item["published"],
            )
        )

    return results