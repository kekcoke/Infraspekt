# CURRENT STATE — PIPELINE HAND-OFF

> **Instructions for the AI:**
> - **Start of every session:** Read this file before doing anything else. Load `## Completed Days`, `## Active Dependency Map`, and `## Carry-Forward Items` into context.
> - **End of every task:** Append the day's entry to `## Completed Days`, update `## Active Dependency Map` with any new dependencies introduced, and clear resolved items from `## Carry-Forward Items`.
> - Never truncate or rewrite history. Append only.

---

## Project Overview

| Field | Value |
|---|---|
| Curriculum | 180-Day Progressive Platform Build |
| Current Day | 0 (not started) |
| Active Environment | Local Dev |
| Primary Services | User Service · Background Worker · Web App |
| Repo Root | `/` |

---

## Completed Days

<!-- APPEND new entries here after each task. Format shown below.
     Do NOT delete previous entries. -->

| Day | Title | Key Output | Notes | Assignment |
|---|---|---|---|---|
| 01 | InfraWatch Foundation | `docs/architecture/day_01_spec.md`, `backend/src/`, `frontend/public/index.html`, `docker-compose.yml`, `.github/workflows/ci.yml`, `ops/runbooks/day_01_runbook.md` | Assignment: disk endpoint + branch strategy implemented | ✅ `GET /api/infrastructure/disk` + branch strategy documented in runbook |

---

## Active Dependency Map

> Cross-day dependencies that future sessions MUST respect.
> When a day introduces a foundational resource (DB, queue, auth), record it here.
> When a later day consumes it, add a "consumed by" entry.

<!-- APPEND entries as dependencies are established. Format:

| Resource | Introduced On | Consumed By | Details |
|---|---|---|---|
| PostgreSQL (users DB) | Day 12 | Day 45, Day 67 | Connection string in `config/db.py`; schema in `docs/architecture/day_12_spec.md` |

-->

| Resource | Introduced On | Consumed By | Details |
|---|---|---|---|
| Express.js backend (Node 18) | Day 01 | — | `backend/src/server.js`; port 3001 (env: PORT) |
| Static frontend (nginx) | Day 01 | — | `frontend/public/index.html`; port 3000; polls backend every 30s |
| Docker Compose stack | Day 01 | — | `docker-compose.yml`; backend healthcheck gates frontend startup |

---

## Active Infrastructure Snapshot

> The current known state of the running system. Updated each day.

```
Services:   infrawatch-backend (Express, port 3001), infrawatch-frontend (nginx, port 3000)
Databases:  (none configured)
Queues:     (none configured)
Auth:       (none configured)
CI/CD:      GitHub Actions — lint + test + docker build on push to main/develop/feature/**
```

---

## Carry-Forward Items

> Unresolved items, deferred decisions, or explicit homework from previous days.
> Remove an item once it is resolved; note which day resolved it.

| Item | Raised On | Due / Blocking | Status |
|---|---|---|---|
| `/api/infrastructure/status` returns hardcoded uptime strings | Day 01 | When a data layer is introduced (est. Day 10–15) | Open — replace with real `os`/`systeminformation` metrics; schema frozen at `{ name, status, uptime }` |

---

## Architectural Decisions Log

> Record decisions that constrain future days (tech choices, schema freezes, API contracts).
> These are permanent — never delete.

| Decision | Made On | Rationale | Impact |
|---|---|---|---|
| — | — | — | — |

---

## Last Session Summary

**Date:** 2026-06-11
**Day Completed:** Day 01 — InfraWatch Foundation
**Handed Off To Next Session:**
- Backend is a plain Express app with no DB/auth yet; Day 02 should build on top of `backend/src/` without replacing it.
- Assignment branch strategy (feature/disk-monitoring → develop → main) is documented in runbook but not enforced via GitHub branch protection — add protection rules before Day 02 if using a real remote.
- Static service data in `/api/infrastructure/status` is hardcoded; replace with real system metrics when a data layer is introduced.

---
<!-- END OF FILE — append new Completed Days entries above the Last Session Summary block,
     and replace the Last Session Summary block entirely each time. -->
