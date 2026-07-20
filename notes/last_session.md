# Last Session Notes — 2026-07-20 (Run 2)

## Capsules Produced (Run 2): 1 deep dive + 1 mode capsule + dashboard

- **Deep Dive — North American Consumer Auto** (star deliverable)
- **Off-Earth** mode capsule (astronauts)
- **index.html** interactive dashboard (GitHub Pages)

## Key Findings (Run 2)
- **NA Consumer Auto**: ~2.85T personal vehicle-miles/yr (US+CA+MX, non-commercial/
  non-government) → ~4.51T passenger-miles (occ 1.58) → **AHV ~515M person-mph** —
  nearly equal to ALL of global commercial aviation (638M).
- Vehicle-type split (by VMT): **SUV/Crossover 40%** (now the largest), sedan 22%,
  compact 15%, full pickup 11%, van 7%, mid pickup 4%, motorcycle 1%.
- Occupancy reshuffles ranking in passenger-miles: vans (2.1) and SUVs (1.7) gain;
  cars (1.4) lose. US = 90% of NA personal driving.
- NA personal cars = ~19.6% of ALL global road pkm from ~6% of world population —
  validates the global road residual and North America's car-centricity.
- **Off-Earth**: ~10 humans in orbit at ~17,150 mph = fastest humans alive, but
  AHV ~0.17M person-mph (0.004%) — the inverse of "ubiquity beats speed".

## Big Number (unchanged, deep dive excluded to avoid double-count)
- **AHV ≈ 3.859B person-mph** · v̄ ≈ 0.476 mph · odometer ≈ 33.8T person-mi/yr.
- Off-Earth added as mode #6 (negligible). Deep dive is a Road subset — hyphenated
  slug keeps it out of tools/ahv.py total.

## Data anchored (Run 2)
- FHWA VM-1 2023 (total VMT 3.247T; light-duty 2.879T), MV-1 (284.6M regs, 4.67M
  government), NHTS 2022 occupancy (1.5 blended; car 1.4/SUV 1.7/van 2.1), AFDC
  fleet mix, NHTSA motorcycle 2023 (~20B mi), StatCan Canadian Vehicle Survey,
  CEIC Mexico VKT.

## Unfinished / deferred
- Snapshot lens still not built.
- Historic reconstruction (pre-rail → jet age) not started.
- Micromobility, vertical/conveyed modes not yet measured (double-count care needed
  for e-bikes vs road two-wheelers).
- Road global capsule confidence not yet formally upgraded (deep dive gives the
  method; apply US/CA/MX + extend to other regions in Run 3).
