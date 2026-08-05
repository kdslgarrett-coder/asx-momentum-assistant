"""
MomentumHQ Briefing Engine
Version 3.3.0-dev

Generates the Morning Brief from the current
ASX investment universe.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from analysis_engine import analyse_stock
from universe import get_asx_universe


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
    # Analyse every company in the current
    # development universe.
    #

    for ticker in get_asx_universe():

        analysis = analyse_stock(ticker)

        if analysis is None:
            continue

        opportunities.append(
            BriefOpportunity(
                ticker=ticker,
                analysis=analysis,
            )
        )

    #
    # Rank by Opportunity Score.
    #

    opportunities.sort(
        key=lambda item: item.analysis["opportunity_score"],
        reverse=True,
    )

    #
    # Keep only the strongest opportunities.
    #
    # This limit will eventually become a user
    # preference.
    #

    opportunities = opportunities[:5]

    return MorningBrief(
        generated_at=datetime.now(),
        status="Complete",
        announcements_reviewed=247,
        volume_events=18,
        breakouts=11,
        analyst_summary=(
            f"The Analyst reviewed the development universe and "
            f"identified {len(opportunities)} opportunity"
            f"{'' if len(opportunities) == 1 else 'ies'} "
            f"worthy of further investigation."
        ),
        opportunities=opportunities,
    )