#!/usr/bin/env bash
# Universe of Movement Runner — orchestrates Scout → Architect → Analyze
#
# Usage:
#   ./run.sh                      # Full pipeline: scout + architect + analyze
#   ./run.sh scout                # Scout only (refresh backlog)
#   ./run.sh elf-run              # Full autonomous elf run (Steps A-E, 48+ capsules)
#   ./run.sh bignumber            # Recompute the aggregate AHV Big Number
set -euo pipefail

UOM_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="${UOM_DIR}/logs"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
mkdir -p "$LOG_DIR"

log() { echo "[$(date '+%H:%M:%S')] $*" | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"; }

run_scout() {
    log "=== SCOUT: ranking transport modes ==="
    cd "${UOM_DIR}/scout" && python3 scout.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
}

run_bignumber() {
    log "=== BIG NUMBER: aggregating AHV across capsules ==="
    cd "${UOM_DIR}" && python3 tools/ahv.py 2>&1 | tee -a "${LOG_DIR}/run_${TIMESTAMP}.log"
}

run_elf_run() {
    log "=== ELF RUN: full autonomous research session (Steps A-E) ==="
    local elf_prompt
    elf_prompt="$(cat <<'PROMPT'
You are a Universe of Movement research Elf executing a full autonomous run.
Follow elves/run_protocol.md exactly.

Step A: Read notes/last_session.md, notes/research_agenda.md, analysis/README.md,
        TAXONOMY.md, elves/survival_guide.md.
Step B: Produce 48+ capsules, inside-out (Road, Air, Rail first). For each mode:
        collect pkm + average speed, cite sources, compute AHV
        (annual_pkm*0.621371/8760), write REPORT.md + data.json + workings/,
        chart, run elves/validation_gates.sh, commit ([UoM] <mode>: ...).
Step C: Review TAXONOMY.md for new modes/splits/merges.
Step D: Retrospective — stale data, cross-mode conflicts, double-counting,
        flow-vs-snapshot reconciliation.
Step E: Recompute python3 tools/ahv.py; write notes/last_session.md and
        notes/research_agenda.md; commit ([UoM] session-notes:).

Rules: CITE HEAVILY (hyperlinks), SHOW ALL MATH (workings/), CONFIDENCE TAG every
number, inside-out priority.
PROMPT
)"
    cd "${UOM_DIR}" && claude -p "$elf_prompt" 2>&1 | tee -a "${LOG_DIR}/elf_run_${TIMESTAMP}.log"
}

main() {
    local mode="${1:-all}"
    log "Universe of Movement Runner — mode: ${mode}"
    case "$mode" in
        scout)     run_scout ;;
        bignumber) run_bignumber ;;
        elf-run)   run_elf_run ;;
        all)       run_scout; run_bignumber ;;
        *) echo "Usage: $0 [scout|elf-run|bignumber|all]"; exit 1 ;;
    esac
    log "Runner complete."
}

main "$@"
