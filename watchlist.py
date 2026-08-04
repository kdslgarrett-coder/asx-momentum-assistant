"""
MomentumHQ Watchlist
Version 2.7.0-dev

Persistent watchlist storage.

This module is the single source of truth for the user's watchlist.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple

from config import DEFAULT_WATCHLIST
from market import search_quote

WATCHLIST_FILE = Path("watchlist.json")


def _save(items: List[str]) -> None:
    """Save the watchlist to disk."""

    WATCHLIST_FILE.write_text(
        json.dumps(sorted(items), indent=4),
        encoding="utf-8",
    )


def get_watchlist() -> List[str]:
    """
    Return the current watchlist.

    If the watchlist file does not exist it is automatically
    created from DEFAULT_WATCHLIST.
    """

    if not WATCHLIST_FILE.exists():
        _save(DEFAULT_WATCHLIST)

    try:
        items = json.loads(
            WATCHLIST_FILE.read_text(encoding="utf-8")
        )

        return sorted(
            list(dict.fromkeys(symbol.upper() for symbol in items))
        )

    except Exception:
        _save(DEFAULT_WATCHLIST)
        return DEFAULT_WATCHLIST.copy()


def add_ticker(symbol: str) -> None:
    """Add a ticker to the watchlist."""

    symbol = symbol.strip().upper()

    if not symbol:
        return

    items = get_watchlist()

    if symbol not in items:
        items.append(symbol)
        _save(items)


def remove_ticker(symbol: str) -> None:
    """Remove a ticker from the watchlist."""

    symbol = symbol.strip().upper()

    items = get_watchlist()

    if symbol in items:
        items.remove(symbol)
        _save(items)


def validate_and_add_ticker(symbol: str) -> Tuple[str, str]:
    """
    Validate a ticker before adding it to the watchlist.

    Returns:
        ("success", message)
        ("warning", message)
        ("error", message)
    """

    symbol = symbol.strip().upper()

    if not symbol:
        return (
            "error",
            "Please enter an ASX ticker.",
        )

    if not symbol.endswith(".AX"):
        symbol = f"{symbol}.AX"

    items = get_watchlist()

    if symbol in items:
        return (
            "warning",
            f"{symbol.replace('.AX', '')} is already in your watchlist.",
        )

    quote = search_quote(symbol)

    if quote is None:
        return (
            "error",
            f"{symbol.replace('.AX', '')} is not a valid ASX ticker.",
        )

    add_ticker(symbol)

    return (
        "success",
        f"Added {symbol.replace('.AX', '')} to your watchlist.",
    )