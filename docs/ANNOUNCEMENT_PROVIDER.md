# MomentumHQ Announcement Provider

## Purpose

The Announcement Provider supplies raw ASX announcement data to the MomentumHQ Scout Network.

It is the single source of truth for announcement retrieval.

The provider retrieves factual information only.

It does not analyse announcements.

It does not score opportunities.

It does not determine importance.

---

# Responsibilities

The Announcement Provider is responsible for:

- Retrieving ASX announcements.
- Normalising announcement data.
- Caching results.
- Providing a simple public API.
- Hiding implementation details from the Scout.

The provider should never contain investment logic.

---

# Design Principle

The Announcement Provider answers one question.

> **What announcements exist?**

The Scout answers:

> **Which announcements deserve investigation?**

The Analyst answers:

> **Why do they matter?**

These responsibilities must remain separate.

---

# Public API

The provider exposes a small public interface.

```python
latest()

history()

refresh()

count()
```

The implementation may change without affecting callers.

---

# Announcement Model

Every announcement should expose a consistent structure.

```python
Announcement

symbol

title

released

url

category

source
```

Future versions may include:

- attachment_count
- announcement_id
- exchange
- language
- market_status

The public model should remain stable.

---

# Data Sources

The Announcement Provider should support multiple data sources.

Examples include:

- ASX
- RSS feeds
- Commercial APIs
- Historical datasets

The Scout should never know which source supplied the data.

---

# Caching

Announcements should be cached locally.

Example

```
data/

    announcements.json
```

Caching improves performance and reduces unnecessary network requests.

---

# Refresh Strategy

During development:

Manual refresh is acceptable.

Future versions may support:

- Startup refresh
- Scheduled refresh
- Incremental updates
- Background refresh

---

# Scheduling

The Announcement Provider retrieves announcements only when requested.

It does not determine when retrieval should occur.

Scheduling belongs to the service that consumes the provider.

Examples include:

- Scout Engine
- Morning Brief
- Future Background Scheduler

This separation allows the retrieval mechanism to remain independent of application workflows.

---

# Error Handling

If announcement retrieval fails:

- Return the most recent cached data.
- Log the failure.
- Never crash the application.

Reliability is more important than freshness.

---

# Consumers

The Announcement Provider is consumed by:

- Announcement Scout
- Historical Analysis
- Future Alert Engine
- Future Portfolio Monitor

Presentation layers should never access the provider directly.

---

# Future Capabilities

Future versions may provide:

- Category normalisation
- Duplicate detection
- Attachment retrieval
- Announcement classification
- Trading halt detection
- Capital raising detection
- Resource upgrade detection

These capabilities belong above the provider whenever possible.

---

# Engineering Principles

The Announcement Provider should:

- Return facts.
- Hide implementation details.
- Prefer deterministic behaviour.
- Remain independent of the Scout.
- Remain independent of the Analyst.

The provider supplies information.

It never interprets it.

---

# Long-Term Goal

The Announcement Provider becomes MomentumHQ's trusted source of market events.

Every Scout should obtain announcement information from the provider rather than directly from an external service.

This allows MomentumHQ to change data sources without changing business logic.

---

# Motto

**Retrieve. Normalise. Cache. Provide.**