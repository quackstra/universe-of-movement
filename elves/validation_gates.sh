#!/usr/bin/env bash
# Universe of Movement — Research Validation Gates
#
# Usage: ./elves/validation_gates.sh <category-dir>
# Example: ./elves/validation_gates.sh analysis/air/air
#
# Gates:
#   1. data.json exists and is valid JSON
#   2. REPORT.md exists and has content
#   3. All charts referenced in REPORT.md exist
#   4. Every key metric in data.json.current has a source
#   5. AHV / projection sanity checks pass

set -euo pipefail

CATEGORY_DIR="${1:?Usage: $0 <category-dir>}"
PASS=0
FAIL=0

gate() {
    local name="$1"; shift
    if "$@"; then
        echo "  ✅ PASS: ${name}"; PASS=$((PASS + 1))
    else
        echo "  ❌ FAIL: ${name}"; FAIL=$((FAIL + 1))
    fi
}

echo "=== Validation Gates: ${CATEGORY_DIR} ==="
echo ""

check_json() {
    local f="${CATEGORY_DIR}/data.json"
    [ -f "$f" ] && python3 -c "import json; json.load(open('${f}'))" 2>/dev/null
}
gate "data.json is valid JSON" check_json

check_report() {
    local r="${CATEGORY_DIR}/REPORT.md"
    [ -f "$r" ] && [ "$(wc -l < "$r")" -gt 10 ]
}
gate "REPORT.md exists with content" check_report

check_charts() {
    local r="${CATEGORY_DIR}/REPORT.md"
    [ -f "$r" ] || return 1
    local missing=0
    while IFS= read -r img; do
        local path
        path=$(echo "$img" | sed -n 's/.*(\([^)]*\)).*/\1/p')
        if [ -n "$path" ] && [[ "$path" != http* ]]; then
            [ -f "${CATEGORY_DIR}/${path}" ] || { echo "    Missing chart: ${path}"; missing=1; }
        fi
    done < <(grep -o '!\[.*\](.*\.png)' "$r" 2>/dev/null || true)
    return "$missing"
}
gate "All referenced charts exist" check_charts

check_sources() {
    local f="${CATEGORY_DIR}/data.json"
    [ -f "$f" ] || return 1
    python3 -c "
import json, sys
data = json.load(open('${f}'))
current = data.get('current', {})
missing = [k for k, v in current.items() if isinstance(v, dict) and not v.get('source') and not v.get('derivation')]
if missing:
    print(f'    Missing sources for: {missing}'); sys.exit(1)
"
}
gate "Key metrics have sources or derivations" check_sources

check_projections() {
    local f="${CATEGORY_DIR}/data.json"
    [ -f "$f" ] || return 1
    python3 -c "
import json, sys
data = json.load(open('${f}'))
issues = []
for scenario, pts in data.get('projections', {}).items():
    for p in pts:
        ahv = p.get('ahv_person_mph', 0)
        if ahv is not None and ahv < 0:
            issues.append(f'{scenario} {p.get(\"year\")}: negative AHV ({ahv})')
    if len(pts) >= 2:
        a, b = pts[0].get('ahv_person_mph', 1), pts[-1].get('ahv_person_mph', 1)
        yrs = pts[-1].get('year', 2035) - pts[0].get('year', 2025)
        if a and a > 0 and yrs > 0:
            cagr = (b / a) ** (1 / yrs) - 1
            if cagr > 1.0:
                issues.append(f'{scenario}: AHV CAGR {cagr:.0%} exceeds 100%')
if issues:
    for i in issues: print(f'    ⚠️  {i}')
    sys.exit(1)
"
}
gate "AHV / projection sanity checks" check_projections

echo ""
echo "Results: ${PASS} passed, ${FAIL} failed"
if [ "$FAIL" -gt 0 ]; then
    echo "❌ VALIDATION FAILED — fix issues before committing"; exit 1
else
    echo "✅ ALL GATES PASSED — safe to commit"; exit 0
fi
