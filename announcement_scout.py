"""
MomentumHQ Announcement Scout
Version 4.0.0-dev

Placeholder implementation.

The Announcement Scout will discover ASX announcements
once the Announcement Provider has been implemented.

Until then, the Scout returns no signals.
"""

from __future__ import annotations

from announcement_signal import AnnouncementSignal


def scan() -> list[AnnouncementSignal]:
    """
    Scan for announcement signals.

    Returns an empty list until the Announcement
    Provider has been implemented.
    """

    return []


def latest() -> list[AnnouncementSignal]:
    """
    Return the latest announcement signals.
    """

    return scan()


def count() -> int:
    """
    Return the number of announcement signals.
    """

    return 0