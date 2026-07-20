# Last Session Notes — 2026-07-20 (Run 4)

## Focus: PRECISION — triangulate custom annual miles per model

Replaced Run 3's flat per-model mileage with a multiplicative **factor model** that
estimates each vehicle's miles from **WHERE × HOW × WHO × NEW/USED × AGE**.

## What was built
- **`factors.json`** — base-by-type mileage (HOW) + per-model WHERE/WHO profiles
  (geo, income, driver-age) + cohort curves (age decay × new/used).
- **`tools/mileage_model.py`** — computes `custom_miles = base_by_type ×
  normalize(geo×income×driverage)`, mean-normalized (VIO-weighted) so factors
  REDISTRIBUTE without inflating the total; F-150 model-year drill with new/used.
- **PRECISION_MODEL.md** + methodology workings (ecological inference, collinearity,
  normalization); charts (mileage_revision, f150_cohort_miles); dashboard section.

## Sourced factor anchors
- HOW: car ~12,400 / SUV ~11,600 / pickup ~13,900 / motorcycle ~2,259 mi/yr (NHTS/iSeeCars)
- WHERE: WY 21,588 vs DC 6,695 mi/driver; pickups rural/mountain, EVs urban-coastal
- WHO income: HH >$70k ~2× HH <$10k; F-150 = #1 vehicle for >$200k earners
- WHO age: 35–54 peak 15,291; 65+ 7,646 (FHWA)
- NEW/USED: new-buyer HH ~$80k vs used ~$48k

## Key findings
- **Pickups revise up hard**: F-150 +39%, Sierra +37%, Ram +34%, Tacoma +32%
  (rural + high-income + utility use). Motorcycles −16/−24%, compacts −5/−8%.
- **F-150 AHV 12.4 → 17.3M person-mph**; a **new F-150 (~20,000 mi/yr) ≈ 2.5× a
  20-yr-old one** (age × new/used compound).
- **Distribution-shape insight**: top-20 models average 11,717 mi/yr but the whole
  fleet averages ~10,160 → the **long tail is driven LESS** than the popular models.
  Granularity changed the *shape*, not just the level.

## Honest limits (documented)
- Ecological inference: combining marginals assumes conditional independence
  (model↔income↔geo). A structured prior, not measurement.
- Collinearity: income/new-used/geo overlap → income full weight, new/used small
  residual, geo capped; elasticity knobs in factors.json.
- Per-model profiles are analyst-set (🟡); true fix = telematics/registration (L6).

## Big Number unchanged
- AHV ≈ 3.859B person-mph. All granular/precision work is a Road subset, excluded.

## Deferred / next (Ferg's stated next phase)
- Return to refining aggregates BY REGION (the precision engine is reusable there).
- Buy a VIO-by-model dataset to convert L4–L5 to 🟢 and fit factor profiles.
- Historic reconstruction + snapshot lens still outstanding from Runs 1–2.
