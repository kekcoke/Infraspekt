# 180 Days of Infraspekt Ops-First Engineering: Autonomous Pipeline

## Overview
This repository also contains an autonomous, multi-agent AI pipeline designed to execute a 180-day production-grade software engineering curriculum. Instead of acting as a monolithic code generator, this system simulates a high-performing engineering team: a **Platform Architect**, a **Backend Developer**, a **QA/SDET**, and a **DevOps/SRE**.

The core philosophy of this pipeline is **"Ops-mindset baked in"**: no code is generated without accompanying CI/CD pipelines, automated tests, infrastructure-as-code, and operational runbooks.

## Architecture: Agents & Skills
The pipeline decouples **Agents** (decision-makers) from **Skills** (execution templates). This ensures modularity and allows the system to scale in complexity over the 6-month arc.

### Directory Structure
```text
project_root/
├── .ai/                    # AI Context & State Management
│   ├── current_state.md    # Rolling memory of previous days
│   └── entrypoint.md       # The kickstart prompt
├── templates/
│   ├── agents/             # Persona definitions
│   │   ├── agent_platform_architect.md
│   │   ├── agent_backend_dev.md
│   │   ├── agent_qa_sdet.md
│   │   └── agent_devops_sre.md
│   └── skills/             # Abstracted capabilities
│       ├── skill_requirements_parser.md
│       ├── skill_code_generation.md
│       ├── skill_cicd_infrastructure.md
│       └── skill_ops_runbook.md
├── src/                    # Generated application code
├── ops/                    # Generated Docker, CI, IaC
└── tests/                  # Generated test suites

COMMAND: Acknowledge these instructions, adopt the Orchestrator persona, and begin executing Phase 1 through Phase 5 for the payload provided above. Use Markdown code blocks for all generated files and prefix each block with its intended filepath.