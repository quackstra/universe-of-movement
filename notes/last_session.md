# Last Session Notes — 2026-07-20 (Run 3)

## Focus: granularity experiment — how deep can we go in NA consumer auto?

Deliberate depth test (per Ferg): drill the North American consumer-auto deep dive
down the full hierarchy **type → company → make → model → model-year → (trim/VIN)**
to unveil new research capabilities and data needs for the Universe of Research.

## What was built
- **Granular tree** (`analysis/.../granular/data.json`) — 20 models across 7 types,
  grounded in **S&P DMV VIO shares** (F-150 3.7%, Silverado 2.7%, Camry 2.3%,
  Accord/CR-V 2.0%) × 286M US VIO.
- **New capability — VIO × mileage-age-curve engine** (`tools/granular_rollup.py`):
  personal_VMT = VIO × personal_share × annual_miles; rolls up model→make→company→
  type→total and reconciles to the deep-dive target.
- **F-150 model-year drill** (survival curve × age-mileage curve).
- **GRANULARITY_FRONTIER.md** — the meta-deliverable: L1–L6 levels, data source +
  confidence + cost per level, the public-data wall at L5/L6, new capabilities/needs.
- Charts: top models by AHV, F-150 by model-year, the granularity pyramid.
- Dashboard: added a granularity section (top-models chart + pyramid + frontier link).

## Key findings
- **Long tail dominates**: top-20 models = only **27.3%** of US personal VMT (300+
  tail models are the rest). Granularity has steep diminishing returns for the
  aggregate, but is essential for per-model questions.
- **Occupancy reshuffles ranking**: by AHV, **CR-V & RAV4 outrank Camry & Silverado**
  (SUV occupancy 1.7 > sedan 1.4). Biggest-by-sales ≠ biggest-by-human-velocity.
- **Personal/commercial split becomes decisive at model level**: F-150 fleet AHV
  ~20.2M vs consumer ~11.5M (43% haircut) — invisible in DMV counts.
- **One model ≈ 2.2%** of the whole NA consumer-auto AHV (F-150).
- **Brand ≠ volume for velocity**: Toyota+Honda lead consumer AHV vs GM+Ford leading
  sales (truck vs passenger skew). [tree is partial — GM/Ford understated.]

## The frontier (new needs unveiled)
- First hard **paywall**: L4–L5 need a paid VIO dataset (S&P/Experian/Polk).
- **Telematics/connected-car** is the only path to true per-model/per-trim VMT.
- **Per-model personal-vs-commercial splits** = dominant error below brand level.
- **Model-level Canada/Mexico** data too thin — granular tree is US-only.
- Reusable pattern for Universe of Research: map the public-data ceiling + price
  the datasets that lower it; state precisely what can't be known.

## Big Number unchanged
- AHV ≈ 3.859B person-mph. Granular tree (hyphenated slug) excluded from total.

## Deferred / next
- Buy/ingest a VIO-by-model dataset to convert L4–L5 to 🟢 and close the 73% tail.
- Extend granular method to another region (validate reusability).
- Return to refining aggregates by region (Ferg's stated next phase).
- Historic reconstruction + snapshot lens still outstanding from Run 1–2.
