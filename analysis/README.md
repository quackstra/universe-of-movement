---
title: "Research Index"
nav_order: 2
---

# Universe of Movement — Research Index

> Master index of all research capsules. Run 1 (2026-07-20): flow lens, top modes.

## The Big Number

### **AHV ≈ 3.86 billion person-mph** · v̄ ≈ 0.48 mph · odometer ≈ 33.8T person-mi/yr

See the full [**Big Number report**](aggregate/BIG_NUMBER.md).

![AHV by mode](aggregate/charts/leaderboard.png)

## Modal Leaderboard

| # | Mode | AHV (M person-mph) | Share | Annual pkm | Confidence | Capsule |
|---|------|--------------------|-------|-----------|------------|---------|
| 1 | Road | 2,625 | 68.0% | ~37T | 🟡 | [road](road/road/REPORT.md) |
| 2 | Air | 638 | 16.5% | 9.0T | 🟢 | [air](air/air/REPORT.md) |
| 3 | Active | 312 | 8.1% | ~4.4T | 🔴 | [active](active/active/REPORT.md) |
| 4 | Rail | 270 | 7.0% | 3.8T | 🟡 | [rail](rail/rail/REPORT.md) |
| 5 | Water | 14 | 0.4% | ~0.2T | 🔴 | [water](water/water/REPORT.md) |
| 6 | Off-Earth | 0.17 | 0.004% | 2.4B | 🟡 | [offearth](offearth/offearth/REPORT.md) |
| | **Total (flow lens)** | **3,859** | **100%** | **~54.4T** | | |

## Deep Dives

- **[North American Consumer Auto](deep-dives/north-american-consumer-auto/REPORT.md)** —
  non-commercial/non-government miles driven in US+CA+MX, split by vehicle type
  (SUV/sedan/compact/pickup/van/motorcycle). ~2.85T vehicle-miles → ~4.51T
  passenger-miles → **AHV ~515M person-mph** (≈ all of global aviation). *Subset
  of Road — excluded from the Big Number total.*
  - [**Granular Decomposition**](deep-dives/north-american-consumer-auto/granular/REPORT.md)
    — type → company → make → model → model-year; top models by AHV, Ford F-150
    model-year drill (`tools/granular_rollup.py`).
  - [**The Granularity Frontier**](deep-dives/north-american-consumer-auto/GRANULARITY_FRONTIER.md)
    — meta-analysis: how deep public data reaches (L1–L6), the paid/proprietary
    wall, and the new research capabilities & needs this unveils.

## Capsules by Mode

- **[Road](road/road/REPORT.md)** — dominant mode; cars/2-wheelers/buses; residual sourcing (Run-2 upgrade target)
- **[Air](air/air/REPORT.md)** — best-sourced (IATA RPK); extreme flow-vs-snapshot split
- **[Rail](rail/rail/REPORT.md)** — an Asia story; HSR punches above its share
- **[Water](water/water/REPORT.md)** — tiny AHV, dominant freight; the "Movement of Stuff" sidebar
- **[Active](active/active/REPORT.md)** — ubiquity beats speed; the ambient-movement boundary

## Method

- **Metric:** AHV = Σ(people × speed), person-mph. See [BRIEF](../BRIEF.md).
- **Lens:** flow (annual pkm ÷ hours/yr). Snapshot reconciliation planned.
- **Scope:** passengers + crew + operators; ground reference frame; ambient
  movement deferred.
- **Tooling:** `python3 tools/ahv.py` (Big Number), `python3 tools/charts.py`.

## Run Log

| Run | Date | Focus | Output |
|-----|------|-------|--------|
| 1 | 2026-07-20 | Flow lens, top 5 modes | First Big Number (AHV ≈ 3.86B person-mph) |
| 2 | 2026-07-20 | NA Consumer Auto deep dive + Off-Earth + dashboard | Deep dive (~515M p-mph), GitHub Pages site |
| 3 | 2026-07-20 | Granularity experiment (auto: type→company→make→model→year) | VIO×mileage-curve engine, granular tree (27.3% coverage), Granularity Frontier report |
