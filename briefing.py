"""
MomentumHQ Briefing Engine
Version 3.5.0-dev

Generates the Morning Brief from the current
development investment universe.

This transitional implementation has been aligned
with the Version 4 architecture while remaining
independent of the Scout Engine.

Workflow

Universe
    ↓
Analysis
    ↓
Morning Brief
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from analysis_engine import analyse_stock
from universe import companies


# ---------------------------------------------------------------------
# Domain Objects
# ---------------------------------------------------------------------


@dataclass
class BriefOpportunity:
    """
    A single opportunity presented in the Morning Brief.
    """

    symbol: str

    analysis: dict[str, Any]


@dataclass
class MorningBrief:
    """
    Represents one generated Morning Brief.
    """

    generated_at: datetime

    status: str

    companies_reviewed: int

    analyst_summary: str

    opportunities: list[BriefOpportunity] = field(
        default_factory=list
    )


# ---------------------------------------------------------------------
# Business Service
# ---------------------------------------------------------------------


def get_morning_brief() -> MorningBrief:
    """
    Generate today's Morning Brief.

    This implementation analyses the current
    development universe directly.

    A future capability will replace the analysis
    source with the Scout Engine without changing
    the public interface.
    """

    opportunities: list[BriefOpportunity] = []

    universe = companies()

    for company in universe:

        analysis = analyse_stock(company.symbol)

        if analysis is None:
            continue

        opportunities.append(
            BriefOpportunity(
                symbol=company.symbol,
                analysis=analysis,
            )
        )

    #
    # Rank opportunities by Analyst score.
    #

    opportunities.sort(
        key=lambda item: item.analysis["opportunity_score"],
        reverse=True,
    )

    #
    # Display the five strongest opportunities.
    #

    opportunities = opportunities[:5]

    return MorningBrief(

        generated_at=datetime.now(),

        status="Complete",

        companies_reviewed=len(universe),

        analyst_summary=(
            f"The Analyst reviewed "
            f"{len(universe)} compan"
            f"{'y' if len(universe) == 1 else 'ies'} "
            f"and identified "
            f"{len(opportunities)} opportunit"
            f"{'y' if len(opportunities) == 1 else 'ies'} "
            "worthy of further investigation."
        ),

        opportunities=opportunities,

    )