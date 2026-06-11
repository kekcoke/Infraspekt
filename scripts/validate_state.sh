#!/usr/bin/env bash
# Usage: ./scripts/validate_state.sh <DAY_NUMBER>
# Validates .ai/current_state.md structure after a Phase 5 update.
set -euo pipefail

STATE=".ai/current_state.md"
DAY="${1:-}"

if [[ -z "$DAY" ]]; then
  echo "Usage: $0 <day_number>" >&2
  exit 1
fi

ERRORS=0

check_section() {
  local section="$1"
  if ! grep -q "^## ${section}" "$STATE"; then
    echo "❌ Missing section: ## ${section}" >&2
    ERRORS=$((ERRORS + 1))
  else
    echo "✅ Section present: ## ${section}"
  fi
}

# 1. Required sections
check_section "Completed Days"
check_section "Active Dependency Map"
check_section "Active Infrastructure Snapshot"
check_section "Carry-Forward Items"
check_section "Architectural Decisions Log"
check_section "Last Session Summary"

# 2. Today's day appears in Completed Days
PADDED=$(printf "%02d" "$DAY")
if grep -q "| ${DAY} \|| 0*${DAY} " "$STATE" 2>/dev/null || grep -Eq "^\| 0*${PADDED} \|" "$STATE"; then
  echo "✅ Day ${DAY} found in Completed Days"
else
  echo "❌ Day ${DAY} NOT found in Completed Days table" >&2
  ERRORS=$((ERRORS + 1))
fi

# 3. Last Session Summary references today's day
if grep -q "Day ${DAY}" "$STATE"; then
  echo "✅ Last Session Summary references Day ${DAY}"
else
  echo "❌ Last Session Summary does not reference Day ${DAY}" >&2
  ERRORS=$((ERRORS + 1))
fi

if [[ $ERRORS -gt 0 ]]; then
  echo ""
  echo "validate_state: $ERRORS error(s) found. Fix before proceeding." >&2
  exit 1
else
  echo ""
  echo "validate_state: all checks passed for Day ${DAY} ✅"
fi
