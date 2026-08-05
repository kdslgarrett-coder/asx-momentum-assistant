"""
MomentumHQ Monitor Service
Version 4.0.0-dev

Persistent monitored opportunity service.

This module is the single source of truth for monitored
ASX opportunities.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Tuple

import streamlit as st

from market import search_quote

MONITOR_FILE = Path("monitor.json")

SESSION_KEY = "monitored_opportunities"


#
# Persistence
#


def _save(symbols: List[str]) -> None:
    """
    Persist monitored symbols.
    """

    MONITOR_FILE.write_text(
        json.dumps(sorted(symbols), indent=4),
        encoding="utf-8",
    )


def _load() -> List[str]:
    """
    Load monitored symbols.
    """

    if not MONITOR_FILE.exists():
        _save([])

    try:

        symbols = json.loads(
            MONITOR_FILE.read_text(encoding="utf-8")
        )

        return sorted(
            list(
                dict.fromkeys(
                    symbol.upper()
                    for symbol in symbols
                )
            )
        )

    except Exception:

        _save([])

        return []


#
# Session cache
#


def _get_store() -> dict:
    """
    Return the session analysis cache.
    """

    if SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = {}

    return st.session_state[SESSION_KEY]


#
# Public API
#


def monitored_symbols() -> List[str]:
    """
    Return monitored ASX symbols.
    """

    return _load()


def add(analysis: dict) -> bool:
    """
    Add an analysed opportunity.

    Returns True if added.
    """

    symbol = analysis["quote"]["symbol"].upper()

    symbols = _load()

    if symbol in symbols:
        return False

    symbols.append(symbol)

    _save(symbols)

    _get_store()[symbol] = analysis

    return True


def validate_and_add(symbol: str) -> Tuple[str, str]:
    """
    Validate a ticker before monitoring.
    """

    symbol = symbol.strip().upper()

    if not symbol:

        return (
            "error",
            "Please enter an ASX ticker.",
        )

    if not symbol.endswith(".AX"):
        symbol = f"{symbol}.AX"

    symbols = _load()

    if symbol in symbols:

        return (
            "warning",
            f"{symbol.replace('.AX','')} is already being monitored.",
        )

    quote = search_quote(symbol)

    if quote is None:

        return (
            "error",
            f"{symbol.replace('.AX','')} is not a valid ASX ticker.",
        )

    symbols.append(symbol)

    _save(symbols)

    return (
        "success",
        f"{symbol.replace('.AX','')} is now being monitored.",
    )


def remove(symbol: str) -> bool:
    """
    Stop monitoring a company.
    """

    symbol = symbol.upper()

    if not symbol.endswith(".AX"):
        symbol = f"{symbol}.AX"

    symbols = _load()

    if symbol not in symbols:
        return False

    symbols.remove(symbol)

    _save(symbols)

    _get_store().pop(symbol, None)

    return True


def is_monitored(symbol: str) -> bool:
    """
    Determine whether a company is monitored.
    """

    symbol = symbol.upper()

    if not symbol.endswith(".AX"):
        symbol = f"{symbol}.AX"

    return symbol in _load()


def get_analysis(symbol: str):
    """
    Return cached analysis if available.
    """

    symbol = symbol.upper()

    if not symbol.endswith(".AX"):
        symbol = f"{symbol}.AX"

    return _get_store().get(symbol)


def clear() -> None:
    """
    Remove every monitored opportunity.
    """

    _save([])

    st.session_state[SESSION_KEY] = {}