# Universe of Movement — Project Brief

> Measure the unmeasured: a comprehensive, open-source census of how fast the
> human race is moving — the aggregate speed of every human on Earth, broken
> down by mode of transport, tracked over time.

## Mission

Build the definitive open dataset of humanity's collective velocity — historic,
current, and projected — across every mode of transport (road, rail, air, water,
active, and beyond). Published as transparent, reproducible research with full
source attribution.

## The Question We're Answering

**How fast is the human race moving, in aggregate, and how has that changed
over time?**

We answer it with three linked metrics derived from the same underlying data:

### 1. AHV — Aggregate Human Velocity (the Big Number)

> **AHV = Σ (people × their speed)**, measured in **person-mph** (person-miles
> per hour), i.e. the rate at which humanity as a whole covers distance.

This is the movement analogue of the Universe of Finance "Big Number" (global
TPS). Finance sums a *rate* (transactions/second); we sum a *rate*
(person-miles/hour). It is dominated by how many people are moving and how fast.

### 2. v̄ — Per-Capita Mean Speed (the intuitive companion)

> **v̄ = AHV ÷ world population**, in **mph**.

"The average human is moving at X mph right now." Because most humans are
stationary at any instant, and because it normalises for a growing population,
v̄ is the fairest way to compare across decades. (Spoiler: time-averaged, it is
well under 1 mph.)

### 3. The Odometer — Humanity's Total Distance (the hero number)

> **Odometer = ∫ AHV dt = total passenger-distance travelled**, in person-miles.

The integral of AHV over time. Annual odometer ties directly to the best-sourced
transport statistic in the world: **passenger-kilometres (pkm)**. AHV and pkm are
the same quantity viewed as a rate vs. an accumulation — which gives us a built-in
consistency check.

## Two Lenses (and why we need both)

The same aggregate can be measured two ways, and they must reconcile:

- **Flow lens** (our starting point): annual **passenger-kilometres by mode**.
  Best-sourced (IATA RPKs, ITF/OECD, UIC, IEA are gold-standard). AHV(flow) =
  annual pkm ÷ hours per year.
- **Snapshot lens**: at any instant, *how many humans are in each mode and at
  what speed*. Visceral, but needs occupancy + time-use data. AHV(snapshot)
  averaged over time must equal AHV(flow) — this is our double-counting / sanity
  gate, analogous to UoF's overlap matrix.

Interesting tension the two lenses expose: **road dominates the snapshot**
(hundreds of millions of people in cars) while **aviation dominates the flow**
(fewer people, but enormous distance). Different "winner" per lens is a headline
finding in itself.

## Scope (Run 1 decisions)

- **Whose speed counts?** Humans aboard/operating: **passengers + crew +
  operators** (a container ship's crew counts; its cargo does not — that is a
  separate "Movement of Stuff" campaign). **Active travel** (purposeful walking,
  running, cycling) counts — the traveller is the operator of their own body.
- **Ambient movement** (walking around a room, fidgeting) is **out of scope for
  now**, flagged as a future extension — it would dramatically raise v̄ and needs
  its own methodology.
- **Reference frame:** **Earth's surface (ground frame)** is canonical. A plane
  flying 500 mph east counts as 500 mph, not 500 + Earth's rotation. Cosmic
  motion (rotation ~1,040 mph, orbit ~67,000 mph) lives in an appendix so the
  headline stays interpretable.

## Core Principles

### 1. Measure, Don't Guess

Every number has a source. When exact data isn't available, we use bounded
estimates with explicit methodology, tagged by confidence:

- 🟢 **High** — direct measurement or audited/official report
- 🟡 **Medium** — derived from reliable partial data
- 🔴 **Low** — estimate based on limited data or extrapolation

### 2. Consistent Units

- **person-mph** — the primary AHV unit
- **passenger-km/year (pkm)** — the primary flow unit (converts to AHV)
- **mph** — for v̄ and modal average speeds
- **CAGR** — for growth over time

### 3. Modes, Not Brands

We measure "commercial aviation", not "Emirates". Operators are data points
within functional categories.

### 4. Transparent Methodology

Every output includes sources, collection method, assumptions, confidence, and
reproducibility instructions.

### 5. Multiple Futures

Three projection scenarios minimum:
- **Baseline** — current trends and modal shares extrapolate
- **High-Mobility** — eVTOL, supersonic revival, HSR buildout, developing-world
  motorisation, space tourism
- **Substitution** — telepresence, remote work, 15-minute cities and climate
  policy decouple human progress from physical motion

## Pipeline Architecture

```
Scout → Architect → Elves → Publish
```

- **Scout** — discovers and ranks data sources (ITF/OECD, IATA/ICAO, UIC, IEA,
  CLIA, IMO/ICS, national travel & time-use surveys, World Bank/UN population).
- **Architect** — writes a `METHODOLOGY.md` per mode: scope, sources,
  pkm→AHV normalisation, projection models, double-counting risks, known gaps.
- **Elves** — autonomous research agents that collect data, normalise to AHV,
  build timeseries and projections, chart, and write reports (48+ capsules/run).
- **Publish** — per-mode reports, master index, and the aggregate Big Number.

## The "Over Time" Arc (the real prize)

- **Pre-1800:** ~99% of human-distance at walking pace (~3 mph); horse/sail for
  the elite few. v̄ time-averaged ≈ 0.1–0.3 mph.
- **Rail (1830+), Auto (1900+), Jet (1950+):** each a step-change *up*. Aviation
  is the biggest jump because speed × distance both explode.
- **2020 (COVID):** a measurable **global deceleration** — humanity literally
  slowed down. A rare, cleanly datable inflection.
- **The open thesis:** Is v̄ still rising, or has **digital substitution** begun
  to decouple human progress from physical motion? We may be the first generation
  where the average human's speed plateaus even as the economy grows.

## Quality Gates

Before any research output publishes:

- [ ] All figures have cited sources
- [ ] Confidence levels assigned to every estimate
- [ ] pkm→AHV normalisation shown and reproducible
- [ ] Flow vs. snapshot reconciliation checked where both exist
- [ ] Double-counting risks (multi-modal trips) identified
- [ ] Charts render with labelled axes and units
- [ ] Projection assumptions explicitly stated
- [ ] Data structured in machine-readable JSON
