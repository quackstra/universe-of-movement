#!/usr/bin/env python3
"""Universe of Movement — Scout.

Reads scout/config.yaml, scores mode categories by inside-out priority
(biggest AHV contribution today first), and writes a ranked backlog.yaml.
"""
from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
CONFIG = HERE / "config.yaml"
BACKLOG = HERE / "backlog.yaml"


def main() -> None:
    config = yaml.safe_load(CONFIG.read_text())
    rows = []
    for sector, cats in config.get("categories", {}).items():
        for cat in cats:
            rows.append(
                {
                    "slug": cat["slug"],
                    "name": cat["name"],
                    "sector": sector,
                    "priority": cat.get("priority", 5),
                    "estimated_scale": cat.get("estimated_scale", ""),
                    "status": "pending",
                }
            )
    # Lower priority number = research sooner (inside-out core first).
    rows.sort(key=lambda r: (r["priority"], r["slug"]))
    BACKLOG.write_text(
        yaml.safe_dump(
            {"generated_from": "config.yaml", "categories": rows},
            sort_keys=False,
        )
    )
    print(f"Scout: wrote {len(rows)} categories to {BACKLOG.name}")
    for r in rows:
        print(f"  [{r['priority']}] {r['slug']:16s} {r['name']}")


if __name__ == "__main__":
    main()
