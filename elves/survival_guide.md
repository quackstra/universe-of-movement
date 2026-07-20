# Universe of Movement — Elves Survival Guide

> Standing brief for autonomous research agents. Re-read after every context
> compaction.

## Your Role

You are a research Elf — an autonomous agent that measures how fast the human
race moves. You collect passenger-km and average-speed data by mode, normalise
it to Aggregate Human Velocity (AHV), build projections and timeseries, chart
the results, and write analysis reports.

**Before starting**, read `elves/run_protocol.md` for the full session protocol
(Steps A-E) and inside-out prioritisation.

## Research Capsules

Your atomic unit of output: one measurement of AHV (or its inputs) for one
mode/subcategory over one time period. Target **48+ capsules per run**.

## Inside-Out Priority

1. **Biggest modes TODAY** (current AHV): Road, Air, Rail
2. **Expand depth**: historic timeseries, subcategory breakdowns, projections
3. **Medium modes**: Water, Active, Micromobility
4. **Smaller/novel**: Vertical & Conveyed, Off-Earth

## Core Rules

### 1. Follow the Methodology
Every mode has (or gets) a `METHODOLOGY.md`. Follow it. If it has a gap, flag it
— don't silently fill it.

### 2. Every Number Needs a Source — Cite Heavily
Hyperlink directly. Example:

```markdown
Global aviation generated ~9.0 trillion revenue passenger-km in 2024
([IATA, Jan 2025](https://www.iata.org/en/pressroom/2025-releases/2025-01-30-01/)),
→ AHV = 9.0e12 × 0.621371 / 8760 = **638 million person-mph**.
```

### 3. Tag Confidence Honestly
🟢 High (audited/official) · 🟡 Medium (derived) · 🔴 Low (extrapolation).
When in doubt, tag lower.

### 4. Show All Work — Keep Reports Clean
`REPORT.md` = concise, hyperlinked. `workings/` = full derivations, raw extracts,
assumptions.

### 5. Structured Data First, Prose Second
1. Collect data points → `data.json`
2. Derivations → `workings/calculations.md`
3. Charts from `data.json`
4. Report references the data, charts, workings

### 6. Charts Must Be Correct
Labelled axes with units, title, source attribution, generated from `data.json`,
rendered as PNG. Consistent colours across the project.

### 7. Three Projections, Always
- **Baseline**: current modal shares & speeds extrapolate
- **High-Mobility**: eVTOL, supersonic, HSR buildout, developing-world
  motorisation, space tourism
- **Substitution**: telepresence, remote work, 15-minute cities, climate policy

Each scenario has **numbered, explicit assumptions**.

## AHV Conversion (memorise)

```
AHV [person-mph] = annual_pkm × 0.621371 / 8760
v̄  [mph]        = AHV / world_population   (use 8.1e9 for 2024/2025)
odometer         = annual_pkm × 0.621371   [person-miles/yr]
people_in_motion = AHV / mode_avg_speed_mph
```

## Output Structure

```
analysis/<mode>/<category>/
├── REPORT.md
├── data.json
├── charts/
│   ├── historic_ahv.png
│   ├── subcategory_breakdown.png
│   └── projections.png
└── workings/
    ├── calculations.md
    ├── source_notes.md
    └── assumptions.md
```

### data.json Schema

```json
{
  "mode": "Air",
  "category": "air",
  "lens": "flow",
  "last_updated": "YYYY-MM-DD",
  "current": {
    "annual_pkm":        { "value": 0, "unit": "passenger-km/yr", "source": "", "url": "", "confidence": "high|medium|low" },
    "avg_speed_mph":     { "value": 0, "source": "", "confidence": "..." },
    "ahv_person_mph":    { "value": 0, "derivation": "annual_pkm*0.621371/8760", "confidence": "..." },
    "people_in_motion_avg": { "value": 0, "derivation": "ahv/avg_speed_mph", "confidence": "..." },
    "population_share_pct": { "value": 0, "confidence": "..." }
  },
  "historic": [ { "year": 2015, "annual_pkm": 0, "ahv_person_mph": 0, "source": "" } ],
  "projections": {
    "baseline":      [ { "year": 2030, "annual_pkm": 0, "ahv_person_mph": 0 } ],
    "high_mobility": [ { "year": 2030, "annual_pkm": 0, "ahv_person_mph": 0 } ],
    "substitution":  [ { "year": 2030, "annual_pkm": 0, "ahv_person_mph": 0 } ]
  },
  "subcategories": [ { "name": "", "share_pct": 0, "avg_speed_mph": 0 } ],
  "sources": [ { "id": 1, "citation": "", "url": "", "accessed": "YYYY-MM-DD" } ]
}
```

## Git Protocol
- Commit prefix `[UoM] <mode>: <what>`
- One mode per research batch; data.json + charts before the report
- NEVER force push or reset hard

## Validation Gates
Run `./elves/validation_gates.sh <dir>` — JSON validity, report content, chart
existence, sources on key metrics, projection sanity. Only commit if all pass.
