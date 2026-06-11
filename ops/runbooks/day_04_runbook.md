# Day 04 Runbook — Quality Enforcement

## Overview
This runbook details the quality gates and local validation steps introduced in Day 04 to ensure production-grade code.

## Local Validation
Before pushing any changes, developers should run:

### 1. Backend Checks
```bash
cd backend
black .
flake8 .
mypy src/
pytest
```

### 2. Frontend Checks
```bash
cd ecommerce-frontend
npx tsc --noEmit
```

### 3. Pre-commit
If pre-commit is installed:
```bash
pre-commit run --all-files
```

## Troubleshooting
- **Mypy Errors:** Ensure all function arguments and return types are annotated.
- **Linting Failures:** Run `black .` to automatically format Python code.
- **CI Failures:** Check the GitHub Actions logs. Most failures are due to missing type annotations or formatting mismatches.
