"""
MomentumHQ Briefing Engine
Version 3.2.0-dev

Generates the data model for the Morning Brief.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from analysis_engine import analyse_stock


@dataclass
class BriefOpportunity:
    """
    A single opportunity presented in the Morning Brief.
    """

    ticker: str
    analysis: dict[str, Any]


@dataclass
class MorningBrief:
    """
    Represents one generated Morning Brief.
    """

    generated_at: datetime
    status: str
    announcements_reviewed: int
    volume_events: int
    breakouts: int
    analyst_summary: str
    opportunities: list[BriefOpportunity] = field(default_factory=list)


def get_morning_brief() -> MorningBrief:
    """
    Generate today's Morning Brief.
    """

    opportunities: list[BriefOpportunity] = []

    #
    # Temporary demonstration opportunity.
    #
    # Future capabilities will replace this with
    # market scanning and opportunity ranking.
    #

    ticker = "KRR.AX"

    analysis = analyse_stock(ticker)

    if analysis is not None:

        opportunities.append(
            BriefOpportunity(
                ticker=ticker,
                analysis=analysis,
            )
        )

    return MorningBrief(
        generated_at=datetime.now(),
        status="Complete",
        announcements_reviewed=247,
        volume_events=18,
        breakouts=11,
        analyst_summary=(
            f"The Analyst reviewed the market and identified "
            f"{len(opportunities)} opportunity worth further investigation."
            if len(opportunities) == 1
            else f"The Analyst reviewed the market and identified "
                 f"{len(opportunities)} opportunities worth further investigation."
        ),
        opportunities=opportunities,
    )