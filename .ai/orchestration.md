# Infraspekt — Orchestration Loop

> **How to start a session:**
> Paste the following prompt into your AI assistant (Claude, GPT-4, etc.):
>
> ```
> Read .ai/entrypoint.md in full and adopt the Master Orchestrator persona.
> Acknowledge these instructions, then execute Phase 0 through Phase 5 for today's task.
> Current day article: ./templates/articles/day_{{NUMBER}}.txt
> ```
> Replace `{{NUMBER}}` with today's day (e.g. `day_02`). That's it — the pipeline runs itself.

---

## Overview

Infraspekt uses a fully automated, gated pipeline to process a 180-day curriculum into production-ready code, tests, infrastructure, and merge records. Each day runs as a single orchestration loop driven by the `entrypoint.md` contract, managed by four virtual personas, and closed with a verified PR merge and changelog entry.

```
User prompt → Orchestrator reads state → Architect → Developer+QA → DevOps → Review+Merge → State update
```

---

## Personas

| Persona | Responsibility | Key Output |
|---|---|---|
| **Platform Architect** | Scope, boundaries, data contracts | `docs/architecture/day_XX_spec.md` |
| **Backend Developer** | Business logic, per-task commits | Source files + Commit Log table |
| **QA / SDET** | Tests written alongside each task | Test files (paired with Developer) |
| **DevOps / SRE** | Containerization, CI/CD, runbook | Dockerfile, `ci.yml`, runbook |
| **Reviewer / Auditor** | Audit all outputs, gate the PR | Review Report + merged PR |

---

## Prerequisites

Before Phase 4b (push + PR + merge) can execute, verify:

```bash
git remote get-url origin   # must return a valid GitHub URL
gh auth status              # must return authenticated
```

If either fails, all phases before 4b still run — only the push/merge step halts.

---

## Pipeline Phases

### Phase 0 — State Initialization
Reads `.ai/current_state.md` in full. Loads:
- `## Completed Days` — what has already been built
- `## Active Dependency Map` — cross-day dependencies that must not be broken
- `## Carry-Forward Items` — open blockers from prior sessions

**Gate:** Confirms today's task does not conflict with any existing dependency before proceeding.

---

### Phase 0b — Branch Bootstrap *(first session only)*
Runs only when the repo has no commits yet.

```bash
git checkout -b main
git add .ai/ templates/ scripts/ .gitignore README.md
git commit -m "chore: initialize repo scaffolding and orchestration templates"
git checkout -b develop
git push origin main develop
```

Skipped permanently after the first session. `develop` is the permanent integration branch.

---

### Phase 1 — Architecture *(Platform Architect)*
Reads the day's article and produces a scoped specification:

- Layer changes (which service is affected)
- Data contracts (request/response schemas)
- Success checklist (explicit pass/fail criteria)

**Output:** `docs/architecture/day_XX_spec.md`

---

### Phase 2 — Implementation + Validation *(Developer + QA paired)*
Developer and QA work in lockstep — one task at a time:

```
for each task in Architect spec:
  1. Developer implements (scoped change only)
  2. QA writes tests for that task
  3. Run lint → if fail: HALT, fix, retry
  4. Run tests → if fail or coverage drops: HALT, fix, retry
  5. git commit (only on double-green) with SHA, coverage %, lint status
```

Branch is checked out from `develop` before any code is written:
```
feature/day-XX-<slug>
```

**Output:** Source files + test files + `## Commit Log` table (SHA · lint · tests · coverage per task)

---

### Phase 4 — Delivery & Operations *(DevOps / SRE)*
Wraps the day's code in production-grade infrastructure:

- `backend/Dockerfile` — multi-stage, non-root
- `docker-compose.yml` — healthcheck gating
- `.github/workflows/ci.yml` — lint + test + docker build
- `ops/runbooks/day_XX_runbook.md` — deploy, rollback, incident triage

---

### Phase 4b — Review & Merge *(Reviewer / Auditor)*
Collects all upstream outputs and applies two skills in sequence:

**`skill_reviewer_auditor`:**
- Architectural adherence (implementation matches spec layers)
- Test coverage completeness (all deliverables mapped to tests)
- Assignment/homework check

**Gate:** Any Fail → blockers routed back to responsible agent. PR not opened.

**`skill_pr_writer`** *(all-Pass only)*:
```bash
git push origin feature/day-XX-<slug>
gh pr create --base develop --title "feat(day-XX): ..." --body-file pr_body.md
gh pr checks --watch --interval 30   # waits for CI
gh pr merge --squash --delete-branch
```

**Output:** `docs/Day_XX_Review_Report.md` · PR URL · merged SHA

---

### Phase 5 — State Update & Changelog
Six writes to `.ai/current_state.md` (append-only except where noted):

| Write | Target Section | Mode |
|---|---|---|
| Day row + assignment status | `## Completed Days` | Append |
| New cross-day resources | `## Active Dependency Map` | Append |
| Live service/DB/queue snapshot | `## Active Infrastructure Snapshot` | Replace |
| New deferred items / resolved items | `## Carry-Forward Items` | Append / Remove |
| Tech choices, API freezes | `## Architectural Decisions Log` | Append |
| 3-bullet hand-off note | `## Last Session Summary` | Replace |

Plus one write to `changelog/YYYY-MM-DD.md`:

```markdown
## Day XX — Deliverable Title
**MR:** [feat(day-XX): title](PR_URL) · merged `SHA`

### Changed
- <what shipped>

### Deferred
- <new carry-forwards, or "None">

### Fixed
- <resolved carry-forwards, or "None">
```

**Validation gate:** `./scripts/validate_state.sh XX` must exit 0 before the session closes.

---

## Commit Convention

```
<type>(<scope>): <description>

Day XX — task N of M
Coverage: <n>%
Lint: clean
```

Types: `feat` · `fix` · `chore` · `docs` · `test` · `refactor` · `ci`

---

## Branch Strategy

```
main        ← production; receives releases from develop
develop     ← integration; all PRs merge here (squash)
feature/*   ← day branches; format: feature/day-XX-<slug>
```

PR labels: `day-01`, `day-02`, … (zero-padded, no special characters).

---

## Key Files

| File | Purpose |
|---|---|
| `.ai/entrypoint.md` | Master orchestration contract (authoritative source) |
| `.ai/current_state.md` | Live session hand-off — read at start, updated at end |
| `templates/agents/` | Agent persona definitions with injected skills |
| `templates/skills/` | Reusable skill modules imported by agents |
| `scripts/validate_state.sh` | Post-Phase-5 integrity check |
| `changelog/YYYY-MM-DD.md` | Date-indexed merge records with MR references |
| `docs/architecture/day_XX_spec.md` | Per-day architectural spec and success checklist |
| `ops/runbooks/day_XX_runbook.md` | Per-day operational runbook |

---

## Skill Inventory

| Skill | Used By | Purpose |
|---|---|---|
| `skill_requirements_parser` | Platform Architect | Extract deliverables and tech stack from raw article |
| `skill_system_design` | Platform Architect | Translate requirements into directory/schema/contract design |
| `skill_implementation_coder` | Developer | Scaffold and implement per-spec |
| `skill_sequential_commit` | Developer | Branch checkout + per-task lint/test gate + commit loop |
| `skill_tester_qa` | QA Engineer | Test strategy, functional scenarios, failure-state validation |
| `skill_cicd_infrastructure` | DevOps / SRE | Dockerfiles, GitHub Actions, IaC |
| `skill_ops_runbook` | DevOps / SRE | Health checks, observability, deployment/rollback playbook |
| `skill_reviewer_auditor` | Reviewer | Architectural adherence + QA coverage audit |
| `skill_pr_writer` | Reviewer | Push branch, open PR, wait for CI, squash-merge |
