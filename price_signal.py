"""
MomentumHQ Price Signal
Version 4.0.0-dev

Represents a factual price movement detected by the
Price Scout.

Price Signals are observations only.

They do not contain opinions, recommendations,
or confidence scores.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class PriceSignal:
    """
    Represents a price movement discovered by
    the Price Scout.
    """

    #
    # Company
    #

    symbol: str

    company: str = ""

    #
    # Price data
    #

    current_price: float = 0.0

    previous_close: float = 0.0

    change: float = 0.0

    change_percent: float = 0.0

    volume: int = 0

    #
    # Evidence
    #

    observed: datetime | None = None

    source: str = "Yahoo Finance"

    scout: str = "Price Scout"

    def summary(self) -> str:
        """
        Return a concise description suitable for
        logging or debugging.
        """

        return (
            f"{self.symbol}: "
            f"{self.change_percent:+.2f}% "
            f"(${self.current_price:.2f})"
        )