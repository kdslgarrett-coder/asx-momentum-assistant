"""
MomentumHQ Candidate Prioritiser
Version 4.0.0-dev

Builds Candidate objects from Scout evidence.

The Candidate Prioritiser groups evidence by company,
creates Candidate objects, assigns an initial priority,
and returns candidates ranked by priority.

It does not analyse opportunities.

It does not generate recommendations.

It simply prepares candidates for the MomentumHQ Analyst.
"""

from __future__ import annotations

from typing import Any

from candidate import Candidate
from universe import company as get_company


def prioritise(signals: list[Any]) -> list[Candidate]:
    """
    Build and prioritise Scout candidates.

    Parameters
    ----------
    signals
        A collection of Scout evidence objects.

    Returns
    -------
    list[Candidate]
        Candidates sorted by descending priority.
    """

    candidates: dict[str, Candidate] = {}

    for signal in signals:

        symbol = signal.symbol

        if symbol not in candidates:

            company = get_company(symbol)

            if company is None:
                #
                # Ignore signals for companies that are
                # not part of the current universe.
                #
                continue

            candidates[symbol] = Candidate(
                company=company,
            )

        candidates[symbol].add_signal(signal)

    #
    # Initial prioritisation.
    #
    # Each independent signal contributes equally.
    # This will evolve as additional Scout types
    # are introduced.
    #

    for candidate in candidates.values():

        candidate.priority = candidate.signal_count * 10

    return sorted(
        candidates.values(),
        key=lambda candidate: (
            candidate.priority,
            candidate.symbol,
        ),
        reverse=True,
    )