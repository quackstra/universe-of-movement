#!/usr/bin/env python3
"""Universe of Movement — granular auto rollup.

Reads the North American Consumer Auto granular tree and rolls
personal VMT / passenger-miles / AHV up the hierarchy
(model → make → company → type → total), then reconciles against the
US personal-driving target (~2.56T vehicle-miles) and reports coverage.

    personal_VMT(model) = VIO × personal_share × annual_miles
    passenger_miles     = personal_VMT × type_occupancy
    AHV [person-mph]    = passenger_miles / 8760
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
TREE = ROOT / "analysis/deep-dives/north-american-consumer-auto/granular/data.json"
HOURS = 8760.0


def main() -> None:
    d = json.loads(TREE.read_text())
    target = d["constants"]["us_personal_vmt_target"]

    rows = []
    by_company, by_type = {}, {}
    for t in d["types"]:
        occ = t["occupancy"]
        for oem in t["oems"]:
            for m in oem["models"]:
                vmt = m["vio_m"] * 1e6 * m["personal_share"] * m["annual_miles"]
                pm = vmt * occ
                ahv = pm / HOURS
                rows.append({
                    "type": t["type"], "company": oem["company"], "make": oem["make"],
                    "model": m["model"], "vio_m": m["vio_m"], "vmt": vmt, "ahv": ahv,
                    "conf": m.get("conf", "?"),
                })
                by_company[oem["company"]] = by_company.get(oem["company"], 0) + ahv
                by_type[t["type"]] = by_type.get(t["type"], 0) + ahv

    tot_vmt = sum(r["vmt"] for r in rows)
    tot_ahv = sum(r["ahv"] for r in rows)
    rows.sort(key=lambda r: r["ahv"], reverse=True)

    print("=" * 72)
    print("NA CONSUMER AUTO — GRANULAR ROLLUP  (US personal light vehicles)")
    print("=" * 72)
    print(f"\nModels in tree: {len(rows)}")
    print(f"Sum personal VMT (tree)  : {tot_vmt/1e12:6.3f} T vehicle-miles")
    print(f"US personal VMT (target) : {target/1e12:6.3f} T vehicle-miles")
    print(f"Coverage of US personal  : {100*tot_vmt/target:5.1f}%  (rest = the long tail of 300+ models)")
    print(f"Sum AHV (tree)           : {tot_ahv/1e6:6.1f} M person-mph")

    print("\nTop models by AHV contribution:")
    print(f"  {'#':>2} {'model':<22}{'VIO(M)':>8}{'VMT(B mi)':>11}{'AHV(M p-mph)':>14}  conf")
    for i, r in enumerate(rows[:12], 1):
        print(f"  {i:>2} {r['model']:<22}{r['vio_m']:>8.1f}{r['vmt']/1e9:>11.1f}{r['ahv']/1e6:>14.2f}  {r['conf']}")

    print("\nBy company (AHV, M person-mph):")
    for c, a in sorted(by_company.items(), key=lambda x: -x[1]):
        print(f"  {c:<16}{a/1e6:>8.1f}")

    print("\nBy type (AHV, M person-mph):")
    for t, a in sorted(by_type.items(), key=lambda x: -x[1]):
        print(f"  {t:<26}{a/1e6:>8.1f}")

    # F-150 model-year drill
    print("\n" + "-" * 72)
    print("DEEPEST DRILL — Ford F-150 by model-year cohort (full fleet)")
    print("-" * 72)
    f150 = next(m for t in d["types"] for o in t["oems"] for m in o["models"]
                if m["model"] == "F-150")
    fleet_vmt = 0.0
    for c in f150["model_years"]:
        v = c["vio_m"] * 1e6 * c["annual_miles"]
        fleet_vmt += v
        print(f"  MY {c['cohort']:<11} (age {c['age']:<6}) VIO {c['vio_m']:>4.1f}M × "
              f"{c['annual_miles']:>6,}mi = {v/1e9:6.1f} B vehicle-miles")
    fleet_ahv = fleet_vmt * 1.5 / HOURS
    pers_ahv = fleet_ahv * f150["personal_share"]
    print(f"  {'':<28}F-150 fleet VMT = {fleet_vmt/1e9:.0f} B vehicle-miles")
    print(f"  F-150 fleet AHV   : {fleet_ahv/1e6:5.1f} M person-mph  (ALL F-150s)")
    print(f"  F-150 consumer AHV: {pers_ahv/1e6:5.1f} M person-mph  (× {f150['personal_share']} personal)")
    print(f"  → one model = {100*pers_ahv/5.147e8:.1f}% of the whole NA consumer-auto AHV (515M)")


if __name__ == "__main__":
    main()
