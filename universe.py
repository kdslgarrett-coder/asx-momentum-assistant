"""
MomentumHQ ASX Universe
Version 3.2.0-dev

Provides the investment universe used by the
Discovery Engine.

Future capabilities will replace the static list
with a dynamically maintained ASX universe.
"""

from typing import Final


#
# Development universe
#
# A small curated list keeps development fast while
# the Discovery Engine is being built.
#

DEVELOPMENT_UNIVERSE: Final[list[str]] = [
    "BHP.AX",
    "CBA.AX",
    "FMG.AX",
    "RIO.AX",
    "NST.AX",
    "KRR.AX",
    "PDN.AX",
    "LTR.AX",
    "CXO.AX",
    "MIN.AX",
]


def get_asx_universe() -> list[str]:
    """
    Return the investment universe.

    During development this is a curated subset
    of the ASX.

    Future versions will:
      - Download the latest ASX listings
      - Remove suspended securities
      - Exclude ETFs and warrants
      - Apply user preferences
      - Cache results
    """

    return DEVELOPMENT_UNIVERSE.copy()