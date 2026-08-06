"""
MomentumHQ Price Scout
Version 4.0.0-dev

Discovers significant daily price movement.

The Price Scout consumes the Market Provider and
converts factual market data into PriceSignal objects.

The Scout performs lightweight interpretation only.

It does not analyse opportunities or determine
investment merit.
"""

from __future__ import annotations

from market import get_quote
from price_signal import PriceSignal
from universe import companies


#
# Minimum daily movement required to
# generate a Price Signal.
#

PRICE_MOVE_THRESHOLD = 5.0


def scan() -> list[PriceSignal]:
    """
    Scan the investment universe for
    significant daily price movement.
    """

    signals: list[PriceSignal] = []

    for company in companies():

        quote = get_quote(company.symbol)

        if quote is None:
            continue

        change_percent = quote["change_percent"]

        if abs(change_percent) < PRICE_MOVE_THRESHOLD:
            continue

        signals.append(

            PriceSignal(

                symbol=company.symbol.replace(
                    ".AX",
                    "",
                ),

                company=company.name,

                current_price=quote["price"],

                previous_close=quote[
                    "previous_close"
                ],

                change=quote["change"],

                change_percent=change_percent,

                volume=quote["volume"],

                observed=quote[
                    "retrieved_at"
                ],

                source="Yahoo Finance",

            )

        )

    return signals


def latest_signals() -> list[PriceSignal]:
    """
    Return the latest Price Signals.
    """

    return scan()


def count() -> int:
    """
    Return the number of Price Signals.
    """

    return len(scan())