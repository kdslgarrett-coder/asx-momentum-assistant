"""
MomentumHQ Announcement Signal
Version 4.1.0-dev

Represents a factual announcement detected by the
Announcement Scout.

Announcement Signals are observations only.

They do not contain opinions, recommendations,
or confidence scores.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class AnnouncementSignal:
    """
    Represents an ASX announcement discovered by
    the Announcement Scout.
    """

    #
    # Company
    #

    symbol: str

    #
    # Company name is optional.
    #
    # The Announcement Provider supplies factual
    # announcement data only. A future Company
    # Registry may enrich signals with company
    # metadata without requiring additional
    # network requests during discovery.
    #

    company: str = ""

    #
    # Announcement
    #

    title: str = ""

    category: str = ""

    released: datetime | None = None

    url: str = ""

    #
    # Evidence
    #

    source: str = "ASX RSS"

    scout: str = "Announcement Scout"

    def summary(self) -> str:
        """
        Return a concise description suitable for
        logging or debugging.
        """

        return (
            f"{self.symbol}: "
            f"{self.category} - "
            f"{self.title}"
        )