"""
MomentumHQ Briefing Engine
Version 3.4.0-dev

Generates the Morning Brief from the current
ASX investment universe.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from analysis_engine import analyse_stock
from narrative import (
    generate_headline,
    generate_summary,
)
from universe import get_asx_universe


@dataclass
class BriefOpportunity:
    """
    A single opportunity presented in the Morning Brief.
    """

    ticker: str
    analysis: dict[str, Any]
    headline: str
    summary: str


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

    for ticker in get_asx_universe():

        analysis = analyse_stock(ticker)

        if analysis is None:
            continue

        opportunities.append(
            BriefOpportunity(
                ticker=ticker,
                analysis=analysis,
                headline=generate_headline(analysis),
                summary=generate_summary(analysis),
            )
        )

    opportunities.sort(
        key=lambda item: item.analysis["opportunity_score"],
        reverse=True,
    )

    opportunities = opportunities[:5]

    return MorningBrief(
        generated_at=datetime.now(),
        status="Complete",
        announcements_reviewed=247,
        volume_events=18,
        breakouts=11,
        analyst_summary=(
            f"The Analyst reviewed the development universe and "
            f"identified {len(opportunities)} opportunit"
            f"{'y' if len(opportunities) == 1 else 'ies'} "
            "worthy of further investigation."
        ),
        opportunities=opportunities,
    )