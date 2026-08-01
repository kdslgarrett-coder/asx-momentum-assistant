# MomentumHQ Architecture

Version: 2.4.0

---

# Vision

MomentumHQ is a personal ASX market intelligence platform.

The objective is not simply to display market data, but to assist investors by combining:

- Live market information
- Technical analysis
- Company announcements
- AI-assisted interpretation
- Momentum scoring

into a single application.

---

# Design Principles

The application follows these principles.

## 1. Single Responsibility

Every module performs one job.

Example:

history.py

Downloads historical prices.

indicators.py

Calculates indicators.

dashboard_news.py

Displays announcements.

analysis.py

Provides AI or rule-based analysis.

---

## 2. Loose Coupling

Display code should never perform calculations.

Dashboard modules display information.

Service modules calculate information.

---

## 3. Replaceable Components

Modules should be replaceable.

Example:

analysis.py currently uses a rule engine.

Future versions may use:

- OpenAI
- Claude
- Gemini
- Ollama

without changing the dashboard.

---

## 4. Stability First

Every release should be:

- Complete
- Tested
- Committed
- Tagged

before new work begins.

---

# Current Architecture

app.py

↓

dashboard.py

↓

├── dashboard_home.py

├── dashboard_news.py

└── dashboard_watchlist.py

These modules consume:

market.py

history.py

indicators.py

announcements.py

analysis.py

config.py

styles.py

---

# Data Flow

User enters ticker

↓

Market Data

↓

Historical Prices

↓

Technical Indicators

↓

Dashboard

↓

User

Announcements follow a similar path.

RSS Feed

↓

announcements.py

↓

analysis.py

↓

dashboard_news.py

↓

User

---

# Development Workflow

Every feature follows the same process.

1. Design

2. Build

3. Test

4. Commit

5. Tag

6. Release

---

# Coding Standards

Small files are preferred.

Each file should have one responsibility.

Avoid duplicate logic.

Functions should be descriptive.

Complex logic belongs in service modules.

---

# Long-Term Roadmap

Future capabilities include:

- AI announcement summaries
- Momentum Score (/100)
- Portfolio tracking
- Smart watchlists
- Alert engine
- AI trading assistant
- Mobile optimisation
- Dark mode

---

# Project Goal

MomentumHQ should become a daily decision-support platform for ASX investors.

The application should answer:

"What deserves my attention today?"

rather than simply displaying market information.