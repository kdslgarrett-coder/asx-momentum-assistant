# MomentumHQ Architecture

Version: 2.0

---

# Purpose

MomentumHQ follows a layered architecture that separates presentation,
business services, analysis and market data.

Each layer has a single responsibility and communicates only with the
layer immediately below it.

```
Presentation Layer
────────────────────────────────────

dashboard.py

🌅 Morning Brief
🔎 Research
📈 Opportunities
💡 Insights
📢 Announcements

        │
        ▼

Components
────────────────────────────────────

Morning Brief Card
Opportunity Card
Evidence Pack
Timeline
Confidence Badge
Analyst Action

        │
        ▼

Business Services
────────────────────────────────────

Briefing Engine
Narrative Engine
Universe

        │
        ▼

Analysis Layer
────────────────────────────────────

Analysis Engine
Scoring Engine
Classification Engine
Confidence Engine

        │
        ▼

Market Data
────────────────────────────────────

ASX announcements
Market prices
Historical data
Technical indicators
```

---

# Layer Responsibilities

## Presentation Layer

Responsible for user interaction only.

Responsibilities:

- Render Streamlit workspaces.
- Collect user input.
- Display business results.
- Never contain business logic.

---

## Components

Reusable UI elements shared across multiple workspaces.

Examples include:

- Morning Brief Card
- Opportunity Card
- Timeline
- Evidence Pack
- Confidence Badge
- Analyst Action

Components present information only.

They should never perform analysis or business decisions.

---

## Business Services

Coordinate MomentumHQ workflows.

Examples include:

- Briefing Engine
- Narrative Engine
- Universe

Responsibilities include:

- Orchestrating workflows.
- Combining analysis results.
- Preparing presentation models.
- Never rendering user interface elements.

---

## Analysis Layer

Transforms raw market data into structured intelligence.

Responsibilities include:

- Technical analysis
- Opportunity scoring
- Classification
- Confidence assessment

The Analysis Layer should never contain presentation logic.

---

## Market Data

Provides the raw information used by the Analysis Layer.

Examples include:

- ASX announcements
- Market prices
- Historical data
- Technical indicators

This layer should remain independent of business logic.

---

# Design Principles

MomentumHQ follows these architectural principles.

- One responsibility per module.
- One logical capability per commit.
- Business logic never belongs in Streamlit views.
- Components present information; they do not generate it.
- Business services coordinate workflows.
- Prefer deterministic logic before introducing AI.
- Each capability should answer an investor question.
- Refactor names when the product evolves rather than preserving legacy terminology.
- Extend existing layers before introducing new ones.

---

# Architecture Philosophy

MomentumHQ transforms raw market information into investor-ready intelligence.

The application follows this flow:

Market Data

↓

Analysis

↓

Business Services

↓

Presentation

↓

Investor Decision

Every capability should strengthen this flow rather than bypass it.