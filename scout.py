"""
MomentumHQ Scout Engine
Version 4.0.0-dev

Coordinates the MomentumHQ Scout Network.

The Scout Engine orchestrates individual Scouts,
collects evidence, builds Candidate objects and
returns a prioritised list for the MomentumHQ Analyst.

The Scout Engine does not analyse opportunities.

Its responsibility is to discover them.
"""

from __future__ import annotations

from candidate import Candidate
from candidate_prioritiser import prioritise

import announcement_scout


def scan() -> list[Candidate]:
    """
    Scan the investment universe.

    Returns
    -------
    list[Candidate]
        Prioritised Scout candidates.
    """

    signals = []

    #
    # Announcement Scout
    #

    signals.extend(
        announcement_scout.scan()
    )

    #
    # Future Scouts
    #
    # signals.extend(price_scout.scan())
    # signals.extend(volume_scout.scan())
    # signals.extend(breakout_scout.scan())
    # signals.extend(sector_scout.scan())
    #

    return prioritise(signals)


def latest() -> list[Candidate]:
    """
    Return the latest Scout candidates.

    Alias for scan() while the Scout
    remains stateless.
    """

    return scan()


def count() -> int:
    """
    Return the number of candidates
    produced by the Scout Engine.
    """

    return len(scan())