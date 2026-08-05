"""
MomentumHQ Candidate
Version 4.0.0-dev

Represents a company that has been shortlisted by the
Scout Network for further investigation.

A Candidate is not an investment recommendation.

It simply represents a company that has accumulated
sufficient evidence to justify analysis by the
MomentumHQ Analyst.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from universe import Company


@dataclass
class Candidate:
    """
    Represents a Scout candidate awaiting analysis.
    """

    #
    # Company
    #

    company: Company

    #
    # Scout evidence
    #

    signals: list[Any] = field(default_factory=list)

    #
    # Scout prioritisation
    #

    priority: int = 0

    #
    # Convenience properties
    #

    @property
    def symbol(self) -> str:
        """
        Return the ASX symbol.
        """

        return self.company.symbol

    @property
    def name(self) -> str:
        """
        Return the company name.
        """

        return self.company.name

    @property
    def sector(self) -> str:
        """
        Return the company sector.
        """

        return self.company.sector

    #
    # Evidence management
    #

    def add_signal(self, signal: Any) -> None:
        """
        Add a Scout signal.
        """

        self.signals.append(signal)

    @property
    def signal_count(self) -> int:
        """
        Return the number of attached signals.
        """

        return len(self.signals)

    #
    # Presentation
    #

    def summary(self) -> str:
        """
        Return a concise summary suitable for
        debugging or logging.
        """

        return (
            f"{self.symbol} | "
            f"{self.signal_count} signals | "
            f"Priority {self.priority}"
        )