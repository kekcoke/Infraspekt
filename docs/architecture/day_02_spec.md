# Day 02 Architecture Spec — Python Flask Backend

## Curriculum Position
Week 1 · Phase: Local Dev · Complexity Ceiling: Python Flask monolith, no external DB yet (SQLite dev, factory pattern).

## Context & Decision
Day 01 established a Node.js/Express backend at `backend/`. Day 02 introduces a **parallel Python/Flask** service at `python-backend/` — both coexist in the monorepo. This mirrors real polyglot architectures and avoids destructive changes to the Day 01 dependency surface.

## Deliverable
A production-structured Python 3.11 Flask application using the app-factory pattern, Flask Blueprints, dataclass models, and a `metrics` blueprint (assignment). Containerised, tested, and integrated into CI.

## Layer Changes

| Layer | Change | Scope |
|---|---|---|
| API | `GET /api/v1/health`, `GET /api/v1/servers`, `GET /api/v1/clusters` | New (python-backend) |
| API | `GET /api/v1/metrics/response-times`, `GET /api/v1/metrics/error-rates` | New (assignment) |
| Middleware | Request-duration logging on every request | New |
| Frontend | No change | — |
| Infrastructure | `python-backend/Dockerfile`, update root `docker-compose.yml` | New / Updated |
| Config | `python-backend/requirements*.txt`, `.env.example`, `pyproject`-style layout | New |
| CI | Add `python-backend` lint + test job to `.github/workflows/ci.yml` | Updated |

## Data Contracts

### `GET /api/v1/health` → 200
```json
{ "status": "healthy", "timestamp": "<ISO8601>", "version": "1.0.0", "service": "infrawatch-python-backend" }
```

### `GET /api/v1/servers` → 200
```json
{
  "servers": [
    {
      "id": "server-0",
      "hostname": "web-0.example.com",
      "ip_address": "10.0.1.10",
      "status": "healthy|warning|critical",
      "metrics": { "cpu_usage": 0.0, "memory_usage": 0.0, "disk_usage": 0.0 },
      "last_heartbeat": "<ISO8601>"
    }
  ],
  "total_count": 5,
  "timestamp": "<ISO8601>"
}
```

### `GET /api/v1/clusters` → 200
```json
{
  "cluster_name": "production-cluster",
  "total_servers": 3,
  "healthy_servers": 3,
  "servers": [ "<Server object>" ]
}
```

### `GET /api/v1/metrics/response-times` → 200
```json
{
  "endpoint_metrics": [
    { "endpoint": "/api/v1/health", "avg_ms": 12.4, "p95_ms": 28.1, "p99_ms": 45.0, "sample_count": 1000 }
  ],
  "timestamp": "<ISO8601>"
}
```

### `GET /api/v1/metrics/error-rates` → 200
```json
{
  "error_metrics": [
    { "endpoint": "/api/v1/servers", "total_requests": 5000, "errors": 12, "error_rate_pct": 0.24 }
  ],
  "window_minutes": 60,
  "timestamp": "<ISO8601>"
}
```

## Success Criteria
- [ ] All 5 endpoints return correct JSON with HTTP 200
- [ ] Request-duration middleware logs on every request
- [ ] `pytest --cov=app --cov-report=term-missing` ≥ 80% coverage
- [ ] `flake8 app/` exits 0
- [ ] Docker image builds and `docker run … curl /api/v1/health` returns healthy
- [ ] CI job passes on push

## Architectural Notes
- App factory (`create_app`) enables test isolation via `TestingConfig`.
- Blueprints map to bounded contexts — `health`, `infrastructure`, `metrics` — ready for microservice extraction.
- Mock data layer used intentionally; real DB introduced when the dependency map calls for it (est. Day 10–15).
- Python service runs on port **5001** to avoid collision with Node.js on 3001.
<END_OF_CONTENT>}}]