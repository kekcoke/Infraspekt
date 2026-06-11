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
| 02 | Python Flask Backend | `docs/architecture/day_02_spec.md`, `python-backend/app/`, `python-backend/tests/` (15 tests, 100% cov), `python-backend/Dockerfile`, `ops/runbooks/day_02_runbook.md` | App factory, 3 blueprints, metrics assignment, request-duration middleware; PR #4 open against develop | ✅ All 5 endpoints + middleware + CI job added |

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
| Docker Compose stack | Day 01 | Day 02 | `docker-compose.yml`; backend healthcheck gates frontend startup |
| Python/Flask backend (Flask 2.3, Python 3.11) | Day 02 | — | `python-backend/app/`; port 5001 (gunicorn); app factory + 3 blueprints (health, infrastructure, metrics) |

---

## Active Infrastructure Snapshot

> The current known state of the running system. Updated each day.

```
Services:   infrawatch-backend (Express, port 3001), infrawatch-python-backend (Flask/gunicorn, port 5001), infrawatch-frontend (nginx, port 3000)
Databases:  (none configured)
Queues:     (none configured)
Auth:       (none configured)
CI/CD:      GitHub Actions — lint+test (Node 18) + lint+test (Python 3.11) + docker build on push to main/develop/feature/**
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
**Day Completed:** Day 02 — Python Flask Backend
**Handed Off To Next Session:**
- Python backend (`python-backend/`) runs on port 5001; Node backend (`backend/`) on 3001 — both coexist unchanged.
- PR #4 (feat/day02-python_backend → develop) is open at https://github.com/kekcoke/Infraspekt/pull/4 — merge manually (PAT lacks merge permission).
- All mock data in python-backend; real metrics/DB layer planned Day 10–15 per dependency map.

---
<!-- END OF FILE — append new Completed Days entries above the Last Session Summary block,
     and replace the Last Session Summary block entirely each time. -->
