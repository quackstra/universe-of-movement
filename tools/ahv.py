#!/usr/bin/env python3
"""Universe of Movement — Aggregate Human Velocity (AHV) calculator.

Scans analysis/**/data.json for flow-lens capsules and computes the Big Number:

    AHV   = Σ (people × speed)        [person-mph]   ← the headline
    v̄     = AHV / world_population     [mph]          ← the intuitive companion
    Odometer = Σ annual_pkm × MI_PER_KM [person-miles/yr] ← humanity's distance

Each capsule contributes via current.ahv_person_mph (preferred) or, if absent,
is derived from current.annual_pkm.value using annual_pkm * MI_PER_KM / HOURS_YR.
"""
from __future__ import annotations

import json
import pathlib

MI_PER_KM = 0.621371
HOURS_PER_YEAR = 8760.0
WORLD_POPULATION = 8.1e9  # 2024/2025, UN
SUN_ROUND_TRIP_MI = 1.86e8  # ~93M mi each way

ROOT = pathlib.Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"


def _num(x):
    return x.get("value") if isinstance(x, dict) else x


def load_capsules():
    caps = []
    for path in sorted(ANALYSIS.rglob("data.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            print(f"  ⚠️  skipping malformed {path.relative_to(ROOT)}")
            continue
        if data.get("lens") and data["lens"] != "flow":
            continue  # Run 1 aggregates the flow lens only
        cur = data.get("current", {})
        ahv = _num(cur.get("ahv_person_mph"))
        pkm = _num(cur.get("annual_pkm"))
        if ahv is None and pkm is not None:
            ahv = pkm * MI_PER_KM / HOURS_PER_YEAR
        if ahv is None:
            continue
        caps.append(
            {
                "mode": data.get("mode", path.parent.name),
                "slug": data.get("category", path.parent.name),
                "ahv": float(ahv),
                "pkm": float(pkm) if pkm is not None else None,
                "conf": (cur.get("ahv_person_mph") or {}).get("confidence")
                if isinstance(cur.get("ahv_person_mph"), dict)
                else None,
            }
        )
    return caps


def main() -> None:
    caps = load_capsules()
    if not caps:
        print("No flow-lens capsules found under analysis/.")
        return

    # De-duplicate: prefer aggregate 'road'/'air'/... over their subcategory
    # splits so we don't double-count. Convention: a capsule whose slug has no
    # hyphen is a mode total and supersedes its 'mode-*' children.
    totals = {c["slug"]: c for c in caps if "-" not in c["slug"]}
    counted = [c for c in caps if "-" not in c["slug"]] or caps

    ahv = sum(c["ahv"] for c in counted)
    pkm = sum(c["pkm"] for c in counted if c["pkm"] is not None)
    vbar = ahv / WORLD_POPULATION
    odometer = pkm * MI_PER_KM
    sun_trips = odometer / SUN_ROUND_TRIP_MI

    counted.sort(key=lambda c: c["ahv"], reverse=True)

    print("=" * 64)
    print("UNIVERSE OF MOVEMENT — THE BIG NUMBER (flow lens)")
    print("=" * 64)
    print(f"\n  AHV (Aggregate Human Velocity) : {ahv/1e9:8.3f} billion person-mph")
    print(f"  v̄  (per-capita mean speed)     : {vbar:8.3f} mph")
    print(f"  Annual odometer                : {odometer/1e12:8.2f} trillion person-miles/yr")
    print(f"  ...equivalent to               : {sun_trips:,.0f} round-trips to the Sun / yr")
    print(f"  World population (assumed)     : {WORLD_POPULATION:,.0f}")
    print(f"\n  Modes counted (deduped): {len(counted)}")
    print("\n  Leaderboard (AHV contribution):")
    print(f"  {'#':>2}  {'mode':<18}{'AHV (M p-mph)':>14}{'share':>8}")
    for i, c in enumerate(counted, 1):
        share = 100 * c["ahv"] / ahv if ahv else 0
        print(f"  {i:>2}  {c['mode']:<18}{c['ahv']/1e6:>14.1f}{share:>7.1f}%")
    if len(totals) < len(set(c['slug'] for c in caps)):
        print("\n  (subcategory-split capsules excluded from the total to avoid double-count)")


if __name__ == "__main__":
    main()
