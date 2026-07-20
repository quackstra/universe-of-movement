#!/usr/bin/env python3
"""Universe of Movement — custom-mileage triangulation model.

Replaces Run 3's flat per-model annual_miles with a multiplicative factor model:

    custom_miles(model) = base_by_type[type] × norm( geo × income × driverage )

The WHO/WHERE multipliers are VIO-weighted mean-normalized to 1.0, so they
REDISTRIBUTE miles across models without inflating the fleet total (base_by_type
sets the level). Model-year cohorts get a second normalized factor
(age_curve × new/used). See workings/mileage_model_methodology.md for the
ecological-inference and collinearity caveats.
"""
from __future__ import annotations

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis/deep-dives/north-american-consumer-auto/granular"
TREE = json.loads((BASE / "data.json").read_text())
FAC = json.loads((BASE / "factors.json").read_text())
HOURS = 8760.0


def wmean(pairs):
    num = sum(v * w for v, w in pairs)
    den = sum(w for _, w in pairs)
    return num / den if den else 1.0


def main() -> None:
    base_type = FAC["base_by_type_miles"]
    per_model = FAC["per_model"]

    models = []
    for t in TREE["types"]:
        occ = t["occupancy"]
        for oem in t["oems"]:
            for m in oem["models"]:
                p = per_model.get(m["model"], {"geo": 1, "income": 1, "driverage": 1})
                raw = p["geo"] * p["income"] * p["driverage"]
                models.append({
                    "model": m["model"], "type": t["type"], "company": oem["company"],
                    "occ": occ, "vio": m["vio_m"] * 1e6, "pshare": m["personal_share"],
                    "orig_miles": m["annual_miles"], "raw": raw,
                    "pvio": m["vio_m"] * 1e6 * m["personal_share"],
                })

    # Normalize WHO/WHERE product to personal-VIO-weighted mean 1.0
    wm = wmean([(m["raw"], m["pvio"]) for m in models])
    for m in models:
        m["norm"] = m["raw"] / wm
        m["custom_miles"] = base_type[m["type"]] * m["norm"]
        m["old_vmt"] = m["pvio"] * m["orig_miles"]
        m["new_vmt"] = m["pvio"] * m["custom_miles"]
        m["old_ahv"] = m["old_vmt"] * m["occ"] / HOURS
        m["new_ahv"] = m["new_vmt"] * m["occ"] / HOURS

    fleet_custom = wmean([(m["custom_miles"], m["pvio"]) for m in models])
    old_tot_vmt = sum(m["old_vmt"] for m in models)
    new_tot_vmt = sum(m["new_vmt"] for m in models)

    print("=" * 78)
    print("CUSTOM-MILEAGE TRIANGULATION  (WHERE × HOW × WHO × NEW/USED × AGE)")
    print("=" * 78)
    print(f"\nVIO-weighted custom miles (fleet) : {fleet_custom:8,.0f} mi/yr")
    print(f"Tree personal VMT — Run 3 (flat)  : {old_tot_vmt/1e12:6.3f} T")
    print(f"Tree personal VMT — triangulated  : {new_tot_vmt/1e12:6.3f} T "
          f"({100*(new_tot_vmt/old_tot_vmt-1):+.1f}% level shift from base-by-type)")

    print("\nPer-model: Run 3 flat vs triangulated custom miles, and AHV")
    print(f"  {'model':<22}{'flat mi':>9}{'custom mi':>11}{'Δmi%':>7}"
          f"{'AHV old':>9}{'AHV new':>9}{'ΔAHV%':>7}")
    for m in sorted(models, key=lambda x: -x["new_ahv"]):
        dmi = 100 * (m["custom_miles"] / m["orig_miles"] - 1)
        dahv = 100 * (m["new_ahv"] / m["old_ahv"] - 1)
        print(f"  {m['model']:<22}{m['orig_miles']:>9,.0f}{m['custom_miles']:>11,.0f}"
              f"{dmi:>+7.0f}{m['old_ahv']/1e6:>9.2f}{m['new_ahv']/1e6:>9.2f}{dahv:>+7.0f}")

    # Biggest movers
    movers = sorted(models, key=lambda m: m["custom_miles"] / m["orig_miles"])
    print("\nBiggest downward revisions:", ", ".join(
        f"{m['model']} ({100*(m['custom_miles']/m['orig_miles']-1):+.0f}%)" for m in movers[:3]))
    print("Biggest upward revisions:  ", ", ".join(
        f"{m['model']} ({100*(m['custom_miles']/m['orig_miles']-1):+.0f}%)" for m in movers[-3:][::-1]))

    # F-150 cohort drill with age × new/used
    print("\n" + "-" * 78)
    print("F-150 model-year cohorts — age × new/used, normalized within model")
    print("-" * 78)
    f150 = next(m for m in models if m["model"] == "F-150")
    tree_f = next(x for t in TREE["types"] for o in t["oems"] for x in o["models"]
                  if x["model"] == "F-150")
    ac, nu = FAC["cohort_curves"]["age_curve"], FAC["cohort_curves"]["newused"]
    cohorts = [{"c": c["cohort"], "vio": c["vio_m"] * 1e6,
                "f": ac[c["cohort"]] * nu[c["cohort"]]} for c in tree_f["model_years"]]
    cwm = wmean([(c["f"], c["vio"]) for c in cohorts])
    print(f"  {'cohort':<14}{'VIO(M)':>8}{'age×NU':>9}{'custom mi':>11}{'VMT(B)':>9}")
    tot = 0.0
    for c in cohorts:
        cmiles = f150["custom_miles"] * c["f"] / cwm
        vmt = c["vio"] * cmiles
        tot += vmt
        print(f"  {c['c']:<14}{c['vio']/1e6:>8.1f}{c['f']:>9.2f}{cmiles:>11,.0f}{vmt/1e9:>9.1f}")
    print(f"  {'':<14}{'':>8}{'':>9}{'fleet VMT':>11}{tot/1e9:>9.1f}  "
          f"(reconciles to F-150 custom {f150['custom_miles']:,.0f} mi × VIO)")


if __name__ == "__main__":
    main()
