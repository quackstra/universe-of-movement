# Universe of Movement — Standard Elf Run Protocol

> This document defines the standard structure for a single autonomous research
> run. Every Elf session follows steps A through E in order. Re-read this after
> every context compaction.

## Inside-Out Prioritisation

Research expands outward from the centre like ripples:

```
                         ┌─ Future (projections)
                    ┌────┤
               ┌────┤    └─ Past (historic timeseries)
          ┌────┤    │
     ┌────┤    │    └─ Smaller modes / subcategories
     │    │    └─ Medium modes
     │    └─ Biggest modes TODAY (current AHV contribution)
     └─ THE CENTRE: largest passenger-km volumes right now
```

**Start with the modes that contribute the most AHV today** (Road, Air, Rail).
Measure the present first, via the **flow lens** (annual pkm ÷ hours/year). Then
expand:
- **Outward by scale**: biggest modes → progressively smaller ones
- **Outward in time**: present → historic timeseries → future projections
- **Outward in detail**: headline modal AHV → subcategory breakdowns
- **Outward by lens**: flow (Run 1) → snapshot reconciliation (later runs)

The top 3 modes (road + air + rail) give ~95% of mechanised AHV — establish
those first, then refine.

## Research Capsules

A **research capsule** is the atomic unit of output:

> One measurement of AHV (or its inputs: pkm, average speed, people-in-motion)
> for one mode/subcategory over one time period, plus accompanying analysis.

Examples:
- "Air — 2024 current AHV estimate (flow lens)"
- "Road — car subcategory breakdown (sedan/SUV/pickup)"
- "Rail — 2015-2024 historic pkm timeseries"
- "Water — naval subcategory (carrier/submarine/surface crew)"

Each capsule has: a **finding** (number/dataset), **sources** (hyperlinked),
**methodology** (how AHV was derived), a **confidence** tag (🟢/🟡/🔴), and
**calculations** shown in full (in `workings/` if complex). A capsule is complete
when it passes validation and is committed.

## Standard Run Steps

### Step A: Session Start — Review & Orient
1. Read `notes/last_session.md` — pick up where the last run left off
2. Read `notes/research_agenda.md` — the planned queue for this run
3. Run `./run.sh scout` — refresh the backlog
4. Check `analysis/README.md` — see what's done
5. Plan the session — select capsules by inside-out priority

### Step B: Research — Produce Capsules (target: 48+)
For each mode in priority order:
1. If no methodology exists, design one (Architect step)
2. Collect pkm + average-speed data; cite sources; compute AHV
3. Write `REPORT.md` + `data.json` + `workings/`
4. Generate charts
5. Run `./elves/validation_gates.sh <dir>`
6. Commit the capsule (`[UoM] <mode>: <what>`)

Track capsule count; continue until at least **48 capsules** this session
(throughput floor, not ceiling). Cross-pollinate sources as you go.

### Step C: Taxonomy Review — Assess Coverage
After the 48 floor, assess whether `TAXONOMY.md` needs new modes, categories,
splits, or merges. Update and document rationale in `notes/taxonomy_changes.md`.

### Step D: Retrospective — Review Prior Research
Check for stale data, cross-mode conflicts (does the aggregate still sum?),
confidence upgrades, double-counting (multi-modal trips), and flow-vs-snapshot
discrepancies. Fix quick wins; queue larger revisions.

### Step E: Session End — Prepare Notes
Write `notes/last_session.md` and `notes/research_agenda.md` for the next run.
Recompute the Big Number (`python3 tools/ahv.py`). Commit with prefix
`[UoM] session-notes:`.

## File Organisation

```
analysis/<mode>/<category>/
├── REPORT.md              # Clean, reader-facing analysis (hyperlinked sources)
├── data.json              # Structured data (AHV inputs, projections, sources)
├── charts/                # Visualisations
└── workings/              # Full calculations, source notes, assumptions
```

## AHV Normalisation (the core conversion)

```
AHV [person-mph] = annual_pkm [passenger-km/yr] × 0.621371 [mi/km] ÷ 8760 [h/yr]
v̄  [mph]        = AHV ÷ world_population
odometer [person-miles/yr] = annual_pkm × 0.621371
people_in_motion_avg       = AHV ÷ mode_average_speed_mph
```

Show this conversion in every capsule's `workings/calculations.md`.

## Citation Standards

Every number links to its source. Prefer primary (ITF, IATA, UIC, IEA, CLIA,
ICS) over secondary; recent over old; official over estimated. When sources
disagree, report the range and explain. In `data.json`, every data point carries
`source`, `url`, `confidence`, `accessed`.
