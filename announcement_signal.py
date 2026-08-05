"""
MomentumHQ Announcement Signal
Version 4.0.0-dev

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

    company: str

    #
    # Announcement
    #

    title: str

    category: str

    released: datetime

    url: str

    #
    # Evidence
    #

    source: str = "ASX"

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