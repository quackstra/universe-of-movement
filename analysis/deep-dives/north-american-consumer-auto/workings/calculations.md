# North American Consumer Auto — Calculations

All figures ~2023. Conversion constants: 1 mile = 1.60934 km; 8,760 h/yr.

## 1. US personal light-duty vehicle-miles

FHWA Highway Statistics 2023, Table VM-1:
- Total motor-vehicle travel: **3,246,817 M vehicle-miles** (3.247T)
- Light-duty vehicles (cars + light trucks/SUV/van): **2,879,076 M** (2.879T)
- Motorcycles: ~20,000 M (~20B, NHTSA/FHWA)

Strip non-consumer light-duty:
- Government (publicly-owned): 4.67M / 284.6M registrations = **1.6%** → −0.046T
- Commercial/business light-duty (rental, corporate fleet, delivery vans,
  rideshare-as-business): assumed **~10%** of LDV VMT → −0.288T

US personal light-duty ≈ 2.879T − 0.046T − 0.288T ≈ **2.545T** → round **2.56T**
(includes ~20B motorcycle, nearly all personal).

## 2. Canada + Mexico

- **Canada**: Canadian Vehicle Survey light-vehicle VKT ≈ 330B km ≈ 205B
  vehicle-miles; personal share high. → **0.205T vehicle-miles**.
- **Mexico**: OECD/CEIC auto VKT 90.6B km (2007); fleet ~1.5–1.6× since →
  ~140B km ≈ 87B vehicle-miles. 🔴 → **0.087T vehicle-miles**.

**North America personal vehicle-miles = 2.560 + 0.205 + 0.087 = 2.852T.**

## 3. Vehicle-type split → passenger-miles

Shares from on-road fleet mix (light trucks ~61%, cars ~35%, motorcycles ~1%),
refined to body type using sales/registration composition. Passenger-miles =
VMT × occupancy (NHTS 2022 by type).

| Type | Share | VMT (B mi) | Occ | Pass-mi (B) |
|------|------:|-----------:|----:|------------:|
| SUV / Crossover | 40% | 1,140 | 1.7 | 1,938.0 |
| Sedan | 22% | 627 | 1.4 | 877.8 |
| Compact/subcompact | 15% | 428 | 1.4 | 599.2 |
| Pickup full-size | 11% | 314 | 1.5 | 471.0 |
| Minivan/Van | 7% | 200 | 2.1 | 420.0 |
| Pickup mid-size | 4% | 114 | 1.5 | 171.0 |
| Motorcycle | 1% | 29 | 1.1 | 31.9 |
| **Total** | 100% | **2,852** | — | **4,508.9** |

Blended occupancy = 4,508.9 / 2,852 = **1.581**.

## 4. AHV, v̄, and people-in-motion

```
annual_passenger_miles = 4.509e12
AHV [person-mph] = 4.509e12 / 8760            = 5.147e8  (515M person-mph)
annual_pkm       = 4.509e12 × 1.60934         = 7.256e12 passenger-km
v̄_NA (auto only) = 5.147e8 / 5.05e8 (NA pop)  = 1.019 mph
people_in_motion = 5.147e8 / 30 mph            = 1.716e7 (17.2M, ~3.4% of NA pop)
odometer (annual) = 4.509e12 passenger-miles
  → 4.509e12 / 1.86e8 (Sun round-trip mi) = 24,240 round-trips to the Sun / yr
```

## 5. Cross-check vs. global Road

NA consumer auto = 7.256T pkm. Global Road capsule = 37T pkm.
NA share of world road pkm = 7.256 / 37 = **19.6%** — from ~6% of world
population. Right order of magnitude; validates the global road residual and
North America's car-centricity.

## Assumptions (ranked by impact on the total)
1. **Commercial light-duty share (~10%)** — biggest lever on US personal VMT.
2. **Vehicle-type VMT shares** — modelled from fleet mix (no published VMT-by-body).
3. **Mexico VKT extrapolation** — 🔴 but only 3% of the NA total.
4. **Blended average speed 30 mph** — affects people-in-motion, not AHV/pkm.
