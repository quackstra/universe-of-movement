# Custom-Mileage Triangulation — Methodology & Workings

## Model form

Multiplicative (log-linear) factor model with mean-normalization:

```
raw(model)     = geo(model) × income(model) × driverage(model)
norm(model)    = raw(model) / VIO_weighted_mean( raw )
custom(model)  = base_by_type[type] × norm(model)

cohort_f(my)   = age_curve[my] × newused[my]
cohort_norm    = cohort_f(my) / VIO_weighted_mean_within_model( cohort_f )
custom(model,my) = custom(model) × cohort_norm(my)
```

Weight for all VIO-weighted means = **personal VIO** = `vio × personal_share`.

## Why mean-normalize?

Without normalization, multiplying five factors > 1 would inflate total distance —
we'd invent miles. Normalizing the WHO/WHERE product to a VIO-weighted mean of 1.0
guarantees the factors **only redistribute** the level set by `base_by_type`.
`base_by_type` itself is anchored to published type mileage (NHTS/iSeeCars), so the
level is empirical, not free.

## Factor derivation

### HOW — base_by_type (the level)
Direct from published averages: pickup 13,900 · van 12,500 · sedan 12,000 · SUV
11,800 · compact 11,000 · motorcycle 2,600 mi/yr.

### WHERE — geo(model)
Ownership-skew × local mileage. Range set from state VMT/driver (WY 21,588 → DC
6,695, national ~13,500/driver). Pickups (rural/mountain concentration) → 1.10–1.15;
EVs (urban-coastal, affluent) → 0.85; urban compacts → 0.95; mainstream → 1.00.
Kept modest to avoid double-counting the type base (pickups are already high-mileage).

### WHO — income(model)
Owner median income → mileage, **dampened**: household mileage rises ~2× across the
income range, but high-income households own *more* vehicles, so miles *per vehicle*
rise less. We compress the ~2× household effect to ~±12% per-vehicle. F-150 1.08
(high-income truck owners), Tesla 1.10–1.12, economy compacts 0.94–0.96.

### WHO — driverage(model)
Owner age-mix × FHWA age-mileage curve (35–54 peak 15,291; 65+ 7,646). Family
vehicles (Explorer, minivans) skew peak-age → 1.05; older-skewing sedans → 0.98;
recreational motorcycles → 0.95. The most orthogonal WHO factor.

### NEW/USED + AGE — cohort curves
- `age_curve` = NHTS vehicle-age mileage decay (0–4: 1.28 … 20+: 0.55).
- `newused` = residual buyer-channel tilt (new cohorts bought new by ~$80k-income
  buyers → 1.03; old cohorts bought used by ~$48k-income buyers → 0.97).
- Applied only at cohort level and normalized within the model, so they reshape a
  model's mileage across model-years without changing its overall average.

## Collinearity handling

income ↔ new/used ↔ homeownership ↔ geography are correlated. Mitigations:
1. income at full weight (primary SES lever);
2. new/used demoted to a small cohort-level residual (±3%), NOT a full model factor;
3. geo deviations capped (±15%);
4. driverage kept because it is comparatively independent.
Residual double-count risk is acknowledged, not eliminated. `factor_elasticity`
knobs in `factors.json` allow damping any factor toward 1.0.

## Ecological inference (the core caveat)

We observe **marginals** (P(income | model), P(miles | income)) and multiply them,
which assumes **P(miles | model) ≈ Σ P(miles | income)·P(income | model)** — i.e.
conditional independence of miles and model given income (and likewise for geo,
age). Real joint distributions violate this. The output is therefore a **structured
prior**, defensible and transparent, but not a substitute for per-model telematics.

## Reconciliation checks
- VIO-weighted fleet custom miles = 11,717 mi/yr (top-20 skew high vs national
  ~10,160 — implies a lower-mileage long tail; documented as an insight).
- F-150 cohort VMT sums to F-150 model VMT (custom 16,692 × personal VIO) by the
  within-model normalization — verified in `tools/mileage_model.py` output.
