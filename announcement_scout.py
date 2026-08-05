"""
MomentumHQ Announcement Scout
Version 4.1.0-dev

Discovers ASX announcement evidence.

The Announcement Scout consumes the Announcement
Provider and converts factual announcement data into
AnnouncementSignal objects.

The Scout performs lightweight interpretation only.

It does not analyse announcements or determine
investment merit.
"""

from __future__ import annotations

import re

from announcements import latest
from announcement_signal import AnnouncementSignal


#
# Typical ASX ticker format.
#
# Examples:
#   BHP
#   FMG
#   KRR
#   CXO
#

_SYMBOL_PATTERN = re.compile(r"^([A-Z]{2,5})\b")


def _extract_symbol(title: str) -> str:
    """
    Extract an ASX ticker from the beginning of an
    announcement title.

    Returns an empty string if no valid ticker is
    detected.
    """

    match = _SYMBOL_PATTERN.match(title.strip().upper())

    if match:
        return match.group(1)

    return ""


def scan(limit: int = 100) -> list[AnnouncementSignal]:
    """
    Scan for announcement signals.

    Parameters
    ----------
    limit
        Maximum announcements to retrieve.

    Returns
    -------
    list[AnnouncementSignal]
    """

    signals: list[AnnouncementSignal] = []

    for announcement in latest(limit=limit):

        symbol = _extract_symbol(
            announcement["title"]
        )

        #
        # Ignore announcements that cannot be
        # confidently associated with a company.
        #

        if not symbol:
            continue

        signals.append(

            AnnouncementSignal(

                symbol=symbol,

                title=announcement["title"],

                category=announcement["category"],

                released=announcement[
                    "published_datetime"
                ],

                url=announcement["link"],

                source=announcement.get(
                    "source",
                    "ASX RSS",
                ),

            )

        )

    return signals


def latest_signals(
    limit: int = 100,
) -> list[AnnouncementSignal]:
    """
    Return the latest announcement signals.
    """

    return scan(limit)


def count() -> int:
    """
    Return the number of announcement signals.
    """

    return len(scan())