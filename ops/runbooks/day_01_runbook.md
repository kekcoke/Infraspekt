# Day 01 Runbook — InfraWatch Foundation

## Health & Observability Contract

| Endpoint | Expected Response | Alerting Threshold |
|---|---|---|
| `GET /health` | `200 { status: "healthy" }` | Any non-200 → PagerDuty P2 |
| `GET /api/infrastructure/status` | `200` with `services[]` | Any non-200 → PagerDuty P2 |
| `GET /api/infrastructure/disk` | `200` with disk fields | `use_percent > 85%` → alert |

**Log format:** stdout JSON (Node.js default). Collect with `docker logs infrawatch-backend-1`.

**Key metrics to watch:**
- Container restart count (threshold: >2 in 5 min → investigate)
- Disk `use_percent` on host (threshold: >85% → alert, >95% → critical)
- Backend response time (threshold: p99 > 500ms → alert)

---

## Deployment Playbook

### Prerequisites
- Docker ≥ 24.x, Docker Compose ≥ 2.x
- Node.js 18 (for local dev only)
- Port 3001 and 3000 free on host

### Steps
```bash
# 1. Clone and enter repo
git clone <repo-url> && cd infrawatch

# 2. Install backend deps (local dev only)
cd backend && npm ci && cd ..

# 3. Build and start all services
docker-compose up --build -d

# 4. Verify health
curl -s http://localhost:3001/health | jq .
curl -s http://localhost:3001/api/infrastructure/status | jq .
curl -s http://localhost:3001/api/infrastructure/disk | jq .

# 5. Open dashboard
open http://localhost:3000
```

### Verification Checklist
- [ ] Both containers show `healthy` in `docker-compose ps`
- [ ] `/health` returns `{ "status": "healthy" }`
- [ ] `/api/infrastructure/status` returns 3 services
- [ ] `/api/infrastructure/disk` returns real disk metrics
- [ ] Dashboard renders all cards without console errors

---

## Rollback Playbook

```bash
# Stop services
docker-compose down

# Roll back to previous image (if tagged)
docker tag infrawatch-backend:previous infrawatch-backend:latest
docker-compose up -d

# Or revert Git commit and rebuild
git revert HEAD --no-edit
docker-compose up --build -d
```

---

## Branch Strategy (Assignment)

```
main          ← production-only, protected
develop       ← integration branch, requires PR + 1 review
feature/*     ← short-lived feature branches off develop
```

**Conventional commit format:**
```
<type>(<scope>): <description>

Types: feat | fix | chore | docs | test | refactor | ci
Example: feat(api): add disk usage monitoring endpoint
```

**PR merge strategy:** Squash merge into `develop`. Rebase merge into `main` from `develop`.

---

## Incident Triage Template

```
Incident: 
Date/Time: 
Severity: P1 | P2 | P3
Detected by: 

## Timeline
- HH:MM — symptom observed
- HH:MM — investigation started
- HH:MM — root cause identified
- HH:MM — fix deployed
- HH:MM — resolved

## Root Cause

## Fix Applied

## Prevention
```
