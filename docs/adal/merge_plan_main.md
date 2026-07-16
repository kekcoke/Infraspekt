# Merge Plan: Develop to Main (Release Synchronization)

**Date:** 2026-06-11
**POC:** Master Orchestrator
**Complexity:** High (Divergent History)

## 1. Objective
Synchronize the `main` branch with `develop` to establish a production-ready baseline for Day 01–04, while preparing the environment for the Day 05 Database integration.

## 2. Risk Assessment
- **State Bottleneck:** `.ai/current_state.md` is likely to conflict due to parallel updates.
- **Service Collision:** The transition from the old static frontend (`frontend/`) to the new React dashboard (`ecommerce-frontend/`) needs careful path handling.
- **CI/CD Alignment:** Ensure the modern Node 20 environment is preserved in `main`.

## 3. Execution Strategy (Isolated Merge)
To prevent polluting `main` or `develop` with failed merge attempts, we will use a temporary sync branch.

1. **Checkout Main:** `git checkout main && git pull origin main`
2. **Create Sync Branch:** `git checkout -b release/sync-develop-to-main`
3. **Merge Develop:** `git merge develop`
4. **Resolve Conflicts:** Apply the guidelines in Section 4.
5. **Verify:** Run `docker compose config` and CI gates.
6. **Finalize:** Merge `release/sync-develop-to-main` into `main` via PR.

## 4. Conflict Resolution Guidelines

### A. State Files (`.ai/current_state.md`, `changelog/`)
- **Action:** Manual Union.
- **Guideline:** Keep the structured "Pipeline Hand-off" template from `develop`. Ensure the "Completed Days" table includes all entries from 01 to 04. Replace the "Last Session Summary" with the latest state from `develop`.

### B. Infrastructure (`docker-compose.yml`, `.env`)
- **Action:** Accept `develop` (Theirs).
- **Guideline:** `develop` contains the multi-service network and healthcheck logic required for the full stack to function. `main` version is likely deprecated.

### C. Backend/Frontend Assets
- **Action:** Preserve the new directory structure.
- **Guideline:** Ensure `ecommerce-frontend/` is the primary frontend. If `frontend/` (legacy) exists in `main`, it should be marked for deletion or archiving.

### D. CI/CD Workflows (`.github/workflows/ci.yml`)
- **Action:** Accept `develop` (Theirs).
- **Guideline:** Use the version with Node 20/24 alignment and multi-service quality gates to prevent regressions on `main`.

## 5. Post-Merge Checklist
- [ ] `docker-compose ps` shows all 4 services (Backend, Python-Backend, Frontend, Postgres).
- [ ] `.ai/current_state.md` correctly lists Day 04 as complete.
- [ ] `git branch -d release/sync-develop-to-main` after successful PR merge.
