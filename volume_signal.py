"""
MomentumHQ Volume Signal
Version 4.0.0-dev

Represents unusual trading volume detected by the
Volume Scout.

Volume Signals are observations only.

They do not contain opinions, recommendations,
or confidence scores.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class VolumeSignal:
    """
    Represents unusual trading volume discovered
    by the Volume Scout.
    """

    #
    # Company
    #

    symbol: str

    company: str = ""

    #
    # Volume data
    #

    volume: int = 0

    average_volume: int = 0

    volume_ratio: float = 0.0

    #
    # Evidence
    #

    observed: datetime | None = None

    source: str = "Yahoo Finance"

    scout: str = "Volume Scout"

    def summary(self) -> str:
        """
        Return a concise description suitable for
        logging or debugging.
        """

        return (
            f"{self.symbol}: "
            f"{self.volume_ratio:.2f}x "
            f"average volume"
        )