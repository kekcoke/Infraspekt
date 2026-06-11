# Day 02 Runbook — Python Flask Backend (infrawatch-python-backend)

## Service Overview
| Field | Value |
|---|---|
| Service | infrawatch-python-backend |
| Language | Python 3.11 / Flask 2.3 |
| Port | 5001 |
| Path | `python-backend/` |
| Start command | `gunicorn --bind 0.0.0.0:5001 --workers 4 run:app` |
| Health endpoint | `GET /api/v1/health` |

## Local Development

```bash
cd python-backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python run.py          # dev server on :5001
```

## Docker

```bash
# Build + run standalone
docker build -t infrawatch-python-backend ./python-backend
docker run -p 5001:5001 infrawatch-python-backend

# Full stack (Node backend + Python backend + frontend)
docker compose up --build
```

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | /api/v1/health | Liveness probe |
| GET | /api/v1/servers | All monitored servers (mock) |
| GET | /api/v1/clusters | Cluster overview (mock) |
| GET | /api/v1/metrics/response-times | P95/P99 per endpoint (mock) |
| GET | /api/v1/metrics/error-rates | Error rate per endpoint (mock) |

## Middleware
Every request emits a structured log line:
```
method=GET path=/api/v1/health status=200 duration_ms=1.23
```
The `X-Response-Time-Ms` header is set on every response.

## Running Tests

```bash
cd python-backend && source venv/bin/activate
pytest tests/ --cov=app --cov-report=term-missing
# Expected: 15 passed, 100% coverage
```

## Lint

```bash
flake8 app/ --max-line-length=120
```

## Carry-Forward / Known Limitations
- All data is mock/simulated. Real metrics collection planned for Day 10–15 when DB is introduced.
- No auth/rate-limiting yet — both are on the Day 10+ roadmap.
- SQLite configured but not actively used; schema migrations will be introduced with SQLAlchemy on Day 10+.

## Port Map (full stack)
| Service | Port |
|---|---|
| infrawatch-frontend (nginx) | 3000 |
| infrawatch-backend (Node/Express) | 3001 |
| infrawatch-python-backend (Flask/gunicorn) | 5001 |
