# asx-momentum-assistant
# MomentumHQ

**A personal ASX market intelligence platform**

MomentumHQ combines live market data, technical analysis, company announcements and AI-assisted insights to help investors identify opportunities and make better-informed decisions.

---

## Current Release

**Version:** 2.4.0

**Status:** Stable

**Next Planned Release:** 2.5.0 – Momentum Score Engine

---

## Vision

MomentumHQ is designed to answer one simple question:

> **"What deserves my attention today?"**

Rather than making investors search multiple websites, MomentumHQ brings together:

- Live ASX market data
- Technical indicators
- Company announcements
- AI-assisted interpretation
- Watchlists
- Momentum scoring (coming soon)

into one application.

---

# Features

## Live Market Data

- Live ASX prices
- Company information
- Market capitalisation
- Volume
- Daily price statistics

## Technical Analysis

- Candlestick charts
- EMA 9
- EMA 20
- RSI
- VWAP
- Relative Volume (RVOL)
- Technical Score

## Announcements

- Company announcements
- Market announcements
- AI sentiment analysis
- Confidence ratings
- AI summaries

## Watchlists

- Custom watchlist
- Live pricing

---

# Project Structure

```text
MomentumHQ
│
├── app.py
├── dashboard.py
│
├── dashboard_home.py
├── dashboard_news.py
├── dashboard_watchlist.py
│
├── market.py
├── history.py
├── indicators.py
├── announcements.py
├── analysis.py
│
├── config.py
├── styles.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PRODUCT_VISION.md
│   ├── ROADMAP.md
│   ├── RELEASE_NOTES.md
│   └── CODING_STANDARDS.md
│
├── CHANGELOG.md
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd MomentumHQ
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# Documentation

Additional project documentation is available in the `docs` directory.

- ARCHITECTURE.md
- PRODUCT_VISION.md
- ROADMAP.md
- RELEASE_NOTES.md
- CODING_STANDARDS.md

---

# Development Workflow

MomentumHQ is developed using small, stable iterations.

Each release follows the same process:

1. Plan
2. Build
3. Test
4. Update version
5. Commit
6. Tag
7. Release

---

# Roadmap

### Completed

- Modular architecture
- Technical indicators
- Tabbed dashboard
- AI announcement analysis

### Coming Soon

- Momentum Score (/100)
- Ranked watchlists
- Smart alerts
- Portfolio tracking
- AI provider integration

---

# Technology Stack

- Python
- Streamlit
- Plotly
- Pandas
- yfinance
- Feedparser

---

# Contributing

MomentumHQ is currently under active development.

Suggestions and ideas are always welcome.

---

# License

License to be determined.
