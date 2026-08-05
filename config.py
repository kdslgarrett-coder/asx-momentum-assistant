"""
MomentumHQ Configuration
Version 3.0.0-dev

Application-wide configuration and branding.
"""

# -----------------------------------------------------------------------------
# Branding
# -----------------------------------------------------------------------------

APP_NAME = "MomentumHQ"

APP_TAGLINE = "Opportunity Intelligence for ASX Investors"

APP_DESCRIPTION = (
    "MomentumHQ helps investors identify high-potential ASX "
    "opportunities using technical analysis, announcement "
    "intelligence and market context."
)

APP_ICON = "📈"

VERSION = "3.0.0-dev"

COPYRIGHT = "© 2026 MomentumHQ"

FOOTER = f"{APP_NAME} • Version {VERSION}"

# -----------------------------------------------------------------------------
# Defaults
# -----------------------------------------------------------------------------

DEFAULT_TICKER = "BHP"

DEFAULT_MONITORED_OPPORTUNITIES = [
    "BHP.AX",
    "CBA.AX",
    "FMG.AX",
    "RIO.AX",
    "WDS.AX",
]

# -----------------------------------------------------------------------------
# Market
# -----------------------------------------------------------------------------

MARKET_NAME = "Australian Securities Exchange"

MARKET_CODE = "ASX"

MARKET_TIMEZONE = "Australia/Sydney"

# -----------------------------------------------------------------------------
# Application
# -----------------------------------------------------------------------------

PAGE_LAYOUT = "wide"

SIDEBAR_STATE = "collapsed"