"""
MomentumHQ Scout Engine
Version 4.2.0-dev

Coordinates the MomentumHQ Scout Network.

The Scout Engine orchestrates all registered
Scouts, collects evidence, builds Candidate
objects and returns a prioritised list for the
MomentumHQ Analyst.

The Scout Engine does not analyse opportunities.

Its responsibility is to discover them.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import announcement_scout
import price_scout

from candidate import Candidate
from candidate_prioritiser import prioritise


#
# Registered Scouts.
#
# Every Scout exposes:
#
#     scan() -> list[Signal]
#
# New Scouts only need to be added to this list.
#

_REGISTERED_SCOUTS: list[Callable[[], list[Any]]] = [
    announcement_scout.scan,
    price_scout.scan,
]


def _collect_signals() -> list[Any]:
    """
    Execute all registered Scouts and
    return their combined evidence.
    """

    signals: list[Any] = []

    for scout in _REGISTERED_SCOUTS:
        signals.extend(scout())

    return signals


def scan() -> list[Candidate]:
    """
    Scan the investment universe.

    Returns
    -------
    list[Candidate]
        Prioritised Scout candidates.
    """

    return prioritise(_collect_signals())


def latest() -> list[Candidate]:
    """
    Return the latest Scout candidates.

    Alias for scan() while the Scout
    Engine remains stateless.
    """

    return scan()


def count() -> int:
    """
    Return the number of candidates
    produced by the Scout Engine.
    """

    return len(scan())


def signal_count() -> int:
    """
    Return the total number of Scout
    signals collected.
    """

    return len(_collect_signals())