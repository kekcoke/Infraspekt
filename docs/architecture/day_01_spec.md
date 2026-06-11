# Day 01 Architecture Spec — InfraWatch Foundation

## Curriculum Position
Week 1 · Phase: Local Dev · Complexity Ceiling: monorepo scaffold, no external services yet.

## Deliverable
Bootstrap the `infrawatch` monorepo with a production-grade project structure, a minimal Express.js backend (health + status endpoints), a static HTML dashboard frontend, Docker containerization, and a branch-strategy implementation (assignment addendum).

## Layer Changes
| Layer | Change | Scope |
|---|---|---|
| API | `GET /health`, `GET /api/infrastructure/status`, `GET /api/infrastructure/disk` | New |
| Frontend | Static HTML dashboard polling backend every 30s | New |
| Infrastructure | `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml` | New |
| Config | `.gitignore`, `backend/package.json`, env var `PORT` | New |

## Data Contracts

### `GET /health` → 200
```json
{ "status": "healthy", "timestamp": "<ISO8601>", "service": "infrawatch-backend" }
```

### `GET /api/infrastructure/status` → 200
```json
{
  "services": [
    { "name": "string", "status": "running|degraded|down", "uptime": "string" }
  ],
  "timestamp": "<ISO8601>"
}
```

### `GET /api/infrastructure/disk` → 200 (Assignment)
```json
{
  "filesystem": "string",
  "size": "string",
  "used": "string",
  "available": "string",
  "use_percent": "string",
  "mount": "string",
  "timestamp": "<ISO8601>"
}
```

## Component Boundaries
- Backend owns all data. Frontend is read-only consumer.
- No database yet — all data is static/computed.
- Backend port: `3001` (env: `PORT`). Frontend port: `3000`.

## Success Checklist
- [ ] `docker-compose up --build` starts both services with no errors
- [ ] `GET /health` returns `200` with `status: healthy`
- [ ] `GET /api/infrastructure/status` returns 3 service entries
- [ ] `GET /api/infrastructure/disk` returns disk metrics for root mount
- [ ] Frontend dashboard loads and renders all status cards
- [ ] All Jest tests pass (`npm test` in `backend/`)
- [ ] GitHub Actions CI workflow runs lint + test on push
- [ ] Assignment: `feature/disk-monitoring` branch merged to `develop` via PR conventions
