# MomentumHQ Development Standards

## Philosophy

MomentumHQ is built through small, stable iterations.

Every release should leave the application in a working state.

---

## Release Process

Every version follows the same workflow.

1. Plan
2. Implement
3. Test
4. Update VERSION in config.py
5. Commit
6. Tag
7. Update RELEASE_NOTES.md

---

## Coding Principles

- One responsibility per file.
- Prefer modular design.
- Avoid duplicate logic.
- Keep functions focused.
- Separate business logic from presentation.
- Design modules to be replaceable.

---

## Documentation

Every significant feature should update:

- RELEASE_NOTES.md
- ROADMAP.md (if appropriate)
- ARCHITECTURE.md (if architecture changes)

---

## Git

Every stable version should have:

- Commit
- Tag
- Push

No work should continue from an uncommitted state.

---

## ChatGPT Workflow

For this project:

- One feature at a time.
- One module at a time.
- Complete files only.
- Test before moving on.
- Commit before the next feature.

Large files should be generated as downloadable files when appropriate.

---

## Long-Term Goal

MomentumHQ should become a professional ASX market intelligence platform rather than simply a market viewer.