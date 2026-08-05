# MomentumHQ Coding Standards

Version: 2.0

---

# Philosophy

MomentumHQ is built through small, stable, incremental capabilities.

Every capability should leave the application in a fully working state.

The goal is continuous improvement through disciplined engineering rather than large, high-risk changes.

---

# Capability Workflow

Every capability follows the same workflow.

1. Define the investor problem.
2. Design the solution.
3. Implement one logical capability.
4. Test thoroughly.
5. Review architecture where appropriate.
6. Commit.
7. Update documentation.

---

# Coding Principles

- One responsibility per module.
- Prefer modular, reusable design.
- Keep functions focused.
- Avoid duplicate logic.
- Separate business logic from presentation.
- Components present data; they do not generate it.
- Prefer deterministic logic before introducing AI.
- Refactor names when the product evolves rather than carrying legacy terminology.
- Design modules to be replaceable without affecting other layers.

---

# Architecture Principles

MomentumHQ follows a layered architecture.

Business logic should never be implemented inside Streamlit views.

Application flow should be:

Presentation

↓

Business Services

↓

Analysis

↓

Market Data

Each layer should communicate only with the layer immediately below it.

---

# Documentation

Architectural changes should update:

- ARCHITECTURE.md
- ROADMAP.md (when priorities change)
- RELEASE_NOTES.md
- PRODUCT_VISION.md (when product direction changes)

Documentation should evolve alongside the software.

---

# Git Workflow

Every completed capability should have:

- A descriptive commit.
- A working application.
- Updated documentation where appropriate.

Tags should be created for significant releases.

Development should not continue from an uncommitted capability.

---

# ChatGPT Development Workflow

For this project:

- One capability at a time.
- One logical task at a time.
- Prefer complete file replacements over partial snippets.
- Test before moving on.
- Review before committing.
- Commit before starting the next capability.

Architectural improvements are encouraged when they simplify the design without changing behaviour.

---

# Design Philosophy

Every capability should answer one investor question or improve one investor workflow.

Examples include:

- What deserves my attention today?
- What do I need to know about this company?
- What should I continue monitoring?
- Why does this matter?
- What evidence supports this conclusion?

If a capability does not improve an investor's ability to make decisions, it should be reconsidered.

---

# Long-Term Goal

MomentumHQ should become a trusted ASX market intelligence platform that helps investors:

- Discover opportunities.
- Understand significance.
- Verify evidence.
- Monitor developments.
- Make better-informed investment decisions.