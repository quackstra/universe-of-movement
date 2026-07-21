---
title: "Recruiter Overview"
parent: SLE Profiles
grand_parent: Explore
nav_order: 100
---

# Intergalactic Recruiter — Soul Less Employee Framework (Movement)

> "The right question, asked by the right mind, with the right odometer."

## What This Is

The Intergalactic Recruiter maintains a roster of **Soul Less Employees (SLEs)** —
expert personas grounded in real job descriptions from the world's transport,
mobility-data, and demographic organizations. When an Elf researches a mode or
a cross-cutting question for the Universe of Movement, it consults this framework
to decide **which expert(s) would best answer it**, then adopts their perspective.

Each SLE brings a different definition of "movement," a different authoritative
data source, and a documented bias to check against. Movement's two measurement
lenses — the **flow lens** (annual pkm ÷ hours) and the **snapshot lens**
(occupancy × speed) — must reconcile, and different SLEs own different lenses.
The recruiter's core job is to pair them.

## The Roster

| # | Slug | Role Title | Pillar | Primary Coverage | Lens |
|---|------|-----------|--------|------------------|------|
| 1 | `transport-economist` | Transport Economist & pkm Statistician | Gov / Academia | Road, Rail, aggregate modal split | Flow |
| 2 | `aviation-network-analyst` | Aviation Network & Air Traffic Analyst | Industry | Air (all subcategories) | Both |
| 3 | `maritime-mobility-analyst` | Maritime & Waterborne Mobility Analyst | Gov / Industry | Water (ferry, cruise, crew) | Both |
| 4 | `active-mobility-scientist` | Active Mobility & Urban Travel Researcher | Academia / NGO | Active (walk, cycle), micromobility | Flow |
| 5 | `human-mobility-data-scientist` | Human Mobility Data Scientist | Academia / Industry | Speed distributions, in-motion fraction | Snapshot |
| 6 | `time-use-demographer` | Time-Use Demographer | Gov / Academia | Time-averaged v̄, fraction-in-motion | Snapshot |

**Pillar balance (by design):** the roster spans academia, government, and
industry so that every mode is triangulated by sources with different incentives
and blind spots.

## Dispatch Matrix

### Mode → SLE Routing

| Mode / Question | Primary SLE | Secondary SLE(s) |
|-----------------|-------------|-------------------|
| **Road** (cars, 2/3-wheelers, buses, taxi/ride-hail) | `transport-economist` | `human-mobility-data-scientist` |
| **Rail** (metro, commuter, intercity, HSR) | `transport-economist` | `time-use-demographer` |
| **Air** (short/long-haul, GA, helicopter, military) | `aviation-network-analyst` | `transport-economist` |
| **Water** (ferry, cruise, recreational, crew) | `maritime-mobility-analyst` | `transport-economist` |
| **Active** (walking, cycling, micromobility) | `active-mobility-scientist` | `human-mobility-data-scientist`, `time-use-demographer` |
| **Off-Earth** (astronauts) | `aviation-network-analyst` | — *(stretch; add `astrodynamics-analyst` when the category matures)* |

### Cross-Cutting / Lens SLEs

| Trigger | Lead SLE | Role When Deployed |
|---------|----------|--------------------|
| "What's the instantaneous speed *distribution*?" | `human-mobility-data-scientist` | Derives per-capita speed distribution and in-motion fraction from device traces |
| "What's the time-averaged v̄?" / "How many are moving *now*?" | `time-use-demographer` | Converts travel-time budgets to v̄ and fraction-in-motion; applies the Marchetti ~1 hr/day anchor |
| "Does the flow total reconcile with the snapshot?" | `transport-economist` (arbiter) | Runs the two-lens sanity gate below |
| "What's the historic arc / acceleration curve?" | `transport-economist` | Reconstructs v̄ back through jet/auto/rail/pre-industrial eras from fuel, fleet, fare data |

### Question-Type Routing

| Question Archetype | Lead SLE | Supporting SLE(s) |
|-------------------|----------|-------------------|
| "What is the pkm for mode X?" | Mode primary (above) | Mode secondary |
| "What speed should I use for X?" | Mode primary | `human-mobility-data-scientist` |
| "What's the occupancy / load factor?" | Mode primary | `transport-economist` |
| "How many people are in motion right now?" | `time-use-demographer` | `human-mobility-data-scientist` |
| "How has this grown over time?" | `transport-economist` | Mode primary |
| "Is this survey number representative?" | `time-use-demographer` | `human-mobility-data-scientist` |
| "Is this device number biased?" | `human-mobility-data-scientist` | `time-use-demographer` |

## The Two-Lens Reconciliation Panel

Movement's headline sanity gate: the **flow lens** and the **snapshot lens** must
land on the same AHV. When they diverge >20% for a mode, convene the panel.

1. **`transport-economist` states the flow estimate** — annual pkm ÷ hours/yr,
   with the modal ledger and occupancy assumptions explicit.
2. **`human-mobility-data-scientist` states the snapshot estimate** — headcount
   in motion × speed distribution at an instant, reweighted for panel bias.
3. **`time-use-demographer` arbitrates the gap** — checks both against the
   travel-time budget (~1 hr/day) and the fraction-in-motion; a mode that
   violates the time budget is over-counted somewhere.

**Output:** a reconciliation note — which lens is trusted, the revised AHV, and
the confidence tag (🟢/🟡/🔴). A mode publishes only when both lenses agree or
the disagreement is explicitly explained.

## Multi-SLE Protocol

1. **Mode primary frames the estimate** — defines the counting point (crew-only?
   passengers-only?), the authoritative source, and the expected range.
2. **Secondary SLE(s) challenge** — contribute an independent method or speed anchor.
3. **A lens SLE reconciles** — the snapshot/time-use experts stress-test the flow
   number against the instantaneous picture.
4. **Blind spots are cross-checked** — each SLE's documented bias is reviewed
   against the finding (e.g., the data scientist's device-panel skew vs. the
   demographer's rich-country survey coverage).

## When to Add a New SLE

- A new mode enters TAXONOMY.md with no natural home (e.g., **Off-Earth** →
  add `astrodynamics-analyst`; **vertical & conveyed** — elevators/escalators →
  consider a `built-environment-flow-analyst`)
- An existing SLE holds >4 primary modes and its blind spots start to dominate
- A mode's confidence stays 🔴 after two runs and the current SLE's data sources
  are exhausted (Active and Water are the current watch-list)
- A major new data stream appears that needs specialist interpretation (e.g.,
  connected-vehicle telematics, universal AIS from satellite constellations)

## Integration with Elf Pipeline

```
Scout → Architect → [RECRUITER dispatch] → Elf (with SLE persona) → Two-Lens Gate → Publish
                           ↓
                    Read SOUL.md for:
                    - Activation phrase (prepend to research prompt)
                    - Data sources (prioritized lookup order)
                    - Mental models (analytical lens)
                    - Blind spots (explicit bias check)
```

The Elf adopts the mode primary's perspective, pulls a lens SLE for the snapshot
cross-check, and uses each SLE's "Blind Spots" section as a built-in adversarial
check before a capsule passes the two-lens gate.
