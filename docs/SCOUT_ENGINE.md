# MomentumHQ Scout Engine

Version: 1.0

---

# Purpose

The Scout Engine continuously scans the Australian Securities Exchange (ASX) to identify companies that deserve further investigation.

The Scout does not analyse opportunities.

The Scout discovers them.

Its role is to rapidly eliminate the majority of the market while identifying companies that exhibit unusual or significant behaviour.

The output of the Scout Engine is a prioritised list of candidate opportunities for the MomentumHQ Analyst.

---

# Mission

Answer one question:

> **What changed today that deserves an investor's attention?**

The Scout should find opportunities before investors begin searching for them.

---

# Philosophy

The Scout is an observer.

It does not make investment decisions.

It does not score opportunities.

It does not generate recommendations.

Instead, it identifies evidence that suggests a company deserves further investigation.

The Analyst is responsible for determining whether the evidence represents a genuine opportunity.

---

# Responsibilities

The Scout Engine should:

- Scan the entire ASX universe.
- Detect unusual market activity.
- Detect significant corporate events.
- Prioritise candidates.
- Provide supporting evidence.
- Deliver candidates to the Analyst.

The Scout should never attempt to replace the Analyst.

---

# Scout Workflow

```
ASX Universe
      │
      ▼
Fast Market Scan
      │
      ▼
Signal Detection
      │
      ▼
Candidate Prioritisation
      │
      ▼
MomentumHQ Analyst
      │
      ▼
Morning Brief
```

---

# Scout Signals

Signals represent observations rather than conclusions.

Multiple signals increase the likelihood that a company deserves further investigation.

Examples include:

## Announcement Signals

- New ASX announcement
- Trading halt
- Trading halt lifted
- Quarterly report
- Resource upgrade
- Major contract
- Earnings release
- Acquisition
- Capital raising
- Regulatory approval

---

## Market Signals

- Significant price movement
- Relative volume spike
- Turnover expansion
- Gap opening
- New 52-week high
- New 52-week low
- Increased volatility

---

## Technical Signals

Examples may include:

- Breakout
- Trend change
- EMA alignment
- Relative strength improvement
- Momentum acceleration

The Scout records these observations only.

Interpretation belongs to the Analyst.

---

## Sector Signals

Examples:

- Gold strength
- Lithium weakness
- Uranium momentum
- Banking leadership
- Energy rotation

Sector behaviour may increase the importance of company-specific signals.

---

# Candidate Evidence

Every shortlisted company should include the reasons it was selected.

Example:

```
KRR

Signals

✓ ASX announcement
✓ Price +8.4%
✓ Relative Volume 3.6x
✓ Gold sector strength
```

The Scout explains what changed.

The Analyst explains why it matters.

---

# Prioritisation

Candidates should be ranked according to the quantity and quality of supporting signals.

The Scout does not generate investment recommendations.

It simply determines which companies deserve to be analysed first.

---

# Performance Goals

The Scout must be significantly faster than the Analyst.

Target performance:

- Load ASX universe in under 2 seconds.
- Complete market scan in under 10 seconds.
- Produce candidate list in under 15 seconds.
- Analyse only shortlisted companies.

The Scout should eliminate the majority of companies before expensive analysis begins.

---

# Relationship with the Analyst

The Scout discovers opportunities.

The Analyst evaluates opportunities.

The Reporter explains opportunities.

The Monitor tracks opportunities.

Each subsystem has one responsibility.

---

# Design Principles

## Fast

Speed is more important than detail.

---

## Objective

Record observations rather than opinions.

---

## Evidence-Based

Every shortlisted company should include supporting signals.

---

## Modular

Individual Scouts should operate independently.

Examples include:

- Announcement Scout
- Price Scout
- Volume Scout
- Breakout Scout
- Sector Scout
- Trading Halt Scout

New Scouts should be able to be added without changing existing Scouts.

---

## Deterministic

The Scout should rely on deterministic rules rather than AI interpretation.

Artificial Intelligence belongs in the Analyst.

---

# Long-Term Vision

Over time the Scout Engine should evolve into a network of specialised Scouts that continuously observe different aspects of the market.

Each Scout contributes evidence.

The Scout Engine combines that evidence into a prioritised opportunity pipeline.

The Analyst then determines which opportunities deserve investor attention.

---

# Success Criteria

The Scout succeeds when it:

- Finds important opportunities quickly.
- Ignores market noise.
- Produces a manageable shortlist.
- Supplies useful evidence to the Analyst.
- Reduces the amount of analysis required.

---

# Golden Rule

The Scout should never attempt to explain opportunities.

Its responsibility ends when it can answer:

> **"Something important happened here."**

The Analyst answers:

> **"Here's why it matters."**

---

# Motto

**Observe. Filter. Prioritise.**