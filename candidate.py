"""
MomentumHQ Candidate
Version 4.1.0-dev

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

    @property
    def scouts(self) -> list[str]:
        """
        Return the unique Scout names that
        contributed evidence.
        """

        return sorted(
            {
                getattr(
                    signal,
                    "scout",
                    type(signal).__name__,
                )
                for signal in self.signals
            }
        )

    def evidence_summary(self) -> list[str]:
        """
        Return a concise summary of all
        attached Scout evidence.
        """

        summaries: list[str] = []

        for signal in self.signals:

            if hasattr(signal, "summary"):
                summaries.append(signal.summary())
            else:
                summaries.append(str(signal))

        return summaries

    #
    # Presentation
    #

    def summary(self) -> str:
        """
        Return a concise summary suitable for
        debugging or logging.
        """

        signal_text = (
            "signal"
            if self.signal_count == 1
            else "signals"
        )

        scout_text = (
            ", ".join(self.scouts)
            if self.scouts
            else "No Scouts"
        )

        return (
            f"{self.symbol} | "
            f"{self.signal_count} {signal_text} | "
            f"Priority {self.priority} | "
            f"{scout_text}"
        )

    def detailed_summary(self) -> str:
        """
        Return a detailed multi-line summary
        of the Candidate and its evidence.
        """

        lines = [

            f"{self.symbol} - {self.name}",

            f"Sector: {self.sector}",

            f"Priority: {self.priority}",

            f"Signals: {self.signal_count}",

            "",

            "Evidence:",
        ]

        if not self.signals:

            lines.append("  (none)")

        else:

            for summary in self.evidence_summary():
                lines.append(f"  • {summary}")

        return "\n".join(lines)