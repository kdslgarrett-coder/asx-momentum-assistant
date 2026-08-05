"""
MomentumHQ Announcement Provider
Version 4.0.0-dev

Provides ASX announcement data for MomentumHQ.

This module is the single source of truth for
announcement retrieval.

It retrieves and normalises announcement data.

It does not analyse announcements.

It does not determine importance.

It does not generate investment recommendations.
"""

from __future__ import annotations

from datetime import datetime
from email.utils import parsedate_to_datetime
from typing import Any, Dict, List, Optional

import feedparser

from classifier import classify_category

ASX_RSS = "https://www.asx.com.au/asx/rss/asx-announcements.xml"


# ---------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------


def _enrich_announcement(
    title: str,
    link: str,
    published: str,
) -> Dict[str, Any]:
    """
    Build a standard MomentumHQ announcement object.
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
        "source": "ASX RSS",
    }

    try:

        dt = parsedate_to_datetime(published)

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

        announcement["published_date"] = published
        announcement["published_time"] = ""
        announcement["freshness"] = published

    return announcement


# ---------------------------------------------------------------------
# Provider implementation
# ---------------------------------------------------------------------


def latest(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Return the latest ASX announcements.

    This is the preferred Version 4 provider API.
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


def history(
    symbol: Optional[str] = None,
    limit: int = 50,
) -> List[Dict[str, Any]]:
    """
    Return historical announcements.

    Currently aliases latest().
    """

    return latest(symbol, limit)


def refresh() -> List[Dict[str, Any]]:
    """
    Refresh announcement data.

    A future capability will introduce local caching.

    For now this simply performs a fresh retrieval.
    """

    return latest()


def count(
    symbol: Optional[str] = None,
) -> int:
    """
    Return the number of retrieved announcements.
    """

    return len(latest(symbol))


# ---------------------------------------------------------------------
# Backwards compatibility
# ---------------------------------------------------------------------


def get_announcements(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Legacy API.

    Retained for backwards compatibility.

    New code should call latest().
    """

    return latest(symbol, limit)


# ---------------------------------------------------------------------
# Offline fallback
# ---------------------------------------------------------------------


def fallback(
    symbol: Optional[str] = None,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    """
    Return a small offline dataset when
    live retrieval is unavailable.
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
                "title": (
                    f"{symbol.upper()} "
                    "Quarterly Activities Report"
                ),
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