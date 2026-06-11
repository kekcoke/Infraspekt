# Operational Runbook: Day 05 — Database & Cache

## 1. Overview
This runbook covers the management of the PostgreSQL (log storage) and Redis (cache) services introduced in Day 05.

## 2. Service Management
### 2.1 Start Services
```bash
docker compose --profile dev up -d postgres redis
```

### 2.2 Check Health
```bash
docker compose ps
# Or manual check
docker exec log_processor_db pg_isready -U devuser
docker exec log_processor_cache redis-cli ping
```

## 3. Database Maintenance
### 3.1 Partitioning
Log entries are partitioned by `timestamp`. The `log_entries_default` partition handles logs from 2024 to 2026. Future partitions should be created monthly.

### 3.2 Backup
```bash
docker exec log_processor_db pg_dump -U devuser log_processor > backup.sql
```

## 4. Redis Maintenance
### 4.1 Eviction Policy
Redis is configured with `allkeys-lru` and a `256mb` limit. Monitor memory usage via:
```bash
docker exec log_processor_cache redis-cli info memory
```
