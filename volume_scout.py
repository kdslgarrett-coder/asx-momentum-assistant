"""
MomentumHQ Volume Scout
Version 4.0.0-dev

Discovers unusual trading volume.

The Volume Scout consumes the Market Provider and
converts factual market data into VolumeSignal objects.

The Scout performs lightweight interpretation only.

It does not analyse opportunities or determine
investment merit.
"""

from __future__ import annotations

from market import get_quote
from universe import companies
from volume_signal import VolumeSignal


#
# Minimum multiple of average volume required
# before a Volume Signal is generated.
#

VOLUME_RATIO_THRESHOLD = 2.0


def scan() -> list[VolumeSignal]:
    """
    Scan the investment universe for
    unusual trading volume.
    """

    signals: list[VolumeSignal] = []

    for company in companies():

        quote = get_quote(company.symbol)

        if quote is None:
            continue

        volume_ratio = quote["volume_ratio"]

        if volume_ratio < VOLUME_RATIO_THRESHOLD:
            continue

        signals.append(

            VolumeSignal(

                symbol=company.symbol.replace(
                    ".AX",
                    "",
                ),

                company=company.name,

                volume=quote["volume"],

                average_volume=quote[
                    "average_volume"
                ],

                volume_ratio=volume_ratio,

                observed=quote[
                    "retrieved_at"
                ],

                source="Yahoo Finance",

            )

        )

    return signals


def latest_signals() -> list[VolumeSignal]:
    """
    Return the latest Volume Signals.
    """

    return scan()


def count() -> int:
    """
    Return the number of Volume Signals.
    """

    return len(scan())