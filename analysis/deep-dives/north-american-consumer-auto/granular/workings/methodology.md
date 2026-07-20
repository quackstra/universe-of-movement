# Granular Auto — Methodology & Workings

## The core equation

Model-level VMT is not published. We model it:

```
personal_VMT(model) = VIO(model) × personal_share(model) × annual_miles(model)
passenger_miles     = personal_VMT × occupancy(type)
AHV [person-mph]    = passenger_miles / 8760
```

## Inputs and where each comes from

### VIO(model) — vehicles in operation
Grounded in **S&P Global Mobility DMV shares** (share of all US vehicles on the
road, Q2 2025) × **286M US VIO** (S&P, avg age 12.6 yr):

| Model | DMV share | VIO |
|-------|----------:|----:|
| Ford F-150 | 3.7% | 10.6M |
| Chevy Silverado 1500 | 2.7% | 7.7M |
| Toyota Camry | 2.3% | 6.6M |
| Honda Accord | 2.0% | 5.7M |
| Honda CR-V | 2.0% | 5.7M |

Models below the published top-5 use VIO estimated from sales history + segment
position (🟡→🔴).

### annual_miles(model) — the NHTS age–mileage curve
NHTS 2017 / ORNL best-mileage: 1–5 yr **>12,000** mi/yr; fleet average **~10,200**;
9+ yr **~7,800**. Trucks/SUVs run slightly higher (work + long-distance use),
older cars lower. Per-model values reflect the model's typical age mix and use.

### personal_share(model) — the crux below brand level
Fraction of the model in **private, non-commercial hands**:
- Passenger cars/SUVs (Camry, CR-V, Corolla): **0.90–0.95** (mostly personal).
- Full-size pickups (F-150, Silverado, Ram): **0.57–0.62** (heavy fleet/work use).
- Mid pickups (Tacoma): **0.80**.

This is the dominant modelling assumption below L3 and is **not** observable in
DMV counts — it needs registration-class data. At the aggregate deep dive we used
a single blended ~10% commercial factor; here every model needs its own.

### occupancy(type) — NHTS 2022
Car 1.4 · SUV/Crossover 1.7 · Van 2.1 · Pickup 1.5 · Motorcycle 1.1.

## F-150 model-year drill (survival curve)

VIO distributed across model-year cohorts using a scrappage/survival profile
(newer cohorts larger, tapering with age) and the age-mileage curve:

| MY | Age | VIO (M) | mi/yr | VMT (B) |
|----|-----|--------:|------:|--------:|
| 2021–2025 | 0–4 | 3.9 | 13,000 | 50.7 |
| 2016–2020 | 5–9 | 3.2 | 12,000 | 38.4 |
| 2011–2015 | 10–14 | 2.0 | 9,500 | 19.0 |
| 2006–2010 | 15–19 | 1.1 | 7,000 | 7.7 |
| ≤2005 | 20+ | 0.4 | 5,500 | 2.2 |
| Total | | 10.6 | | 118 |

Fleet AHV = 118e9 × 1.5 / 8760 = **20.2M person-mph**.
Consumer AHV = 20.2M × 0.57 = **11.5M person-mph**.

## Reconciliation

Sum of the 20-model tree = **0.699T personal vehicle-miles** = **27.3%** of the
2.56T US personal target. The residual 72.7% is the long tail of 300+ models.
This is a *coverage* check, not a claim of completeness — the tree is a method
demonstration. Full closure requires a paid model-by-model VIO dataset.

## Assumption sensitivity (ranked)
1. **personal_share** per model — biggest lever below brand level.
2. **VIO for tail models** — estimated, not measured.
3. **model-year survival curve** — generic, not model-specific.
4. **annual_miles per model** — from a national curve, not model telematics.
