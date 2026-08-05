"""
MomentumHQ Universe Provider
Version 4.0.0-dev

Provides the investment universe used by the
Scout Engine.

The Universe Provider is responsible only for
supplying companies that may be analysed.

It does not perform market analysis.
It does not generate signals.
It does not score opportunities.
"""

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Company:
    """
    Represents a company within the MomentumHQ
    investment universe.
    """

    symbol: str
    name: str
    sector: str


#
# Development universe
#
# A small curated universe keeps development
# fast while the Scout Engine is being built.
#

DEVELOPMENT_UNIVERSE: Final[list[Company]] = [

    Company(
        "BHP.AX",
        "BHP Group",
        "Materials",
    ),

    Company(
        "CBA.AX",
        "Commonwealth Bank",
        "Financials",
    ),

    Company(
        "FMG.AX",
        "Fortescue",
        "Materials",
    ),

    Company(
        "RIO.AX",
        "Rio Tinto",
        "Materials",
    ),

    Company(
        "NST.AX",
        "Northern Star Resources",
        "Gold",
    ),

    Company(
        "KRR.AX",
        "King River Resources",
        "Gold",
    ),

    Company(
        "PDN.AX",
        "Paladin Energy",
        "Uranium",
    ),

    Company(
        "LTR.AX",
        "Liontown Resources",
        "Lithium",
    ),

    Company(
        "CXO.AX",
        "Core Lithium",
        "Lithium",
    ),

    Company(
        "MIN.AX",
        "Mineral Resources",
        "Mining Services",
    ),
]


def companies() -> list[Company]:
    """
    Return the current investment universe.
    """

    return DEVELOPMENT_UNIVERSE.copy()


def symbols() -> list[str]:
    """
    Return all ASX symbols.
    """

    return [
        company.symbol
        for company in DEVELOPMENT_UNIVERSE
    ]


def company(symbol: str) -> Company | None:
    """
    Return company metadata.

    Returns None if the company
    does not exist.
    """

    symbol = symbol.upper()

    for item in DEVELOPMENT_UNIVERSE:

        if item.symbol == symbol:
            return item

    return None


def size() -> int:
    """
    Return the size of the universe.
    """

    return len(DEVELOPMENT_UNIVERSE)