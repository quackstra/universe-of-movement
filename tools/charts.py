#!/usr/bin/env python3
"""Universe of Movement — chart suite.

Generates, from capsule data.json files:
  - per-mode historic AHV line charts (analysis/<mode>/<mode>/charts/historic_ahv.png)
  - aggregate AHV leaderboard (analysis/aggregate/charts/leaderboard.png)
  - aggregate v̄ history (analysis/aggregate/charts/vbar_history.png)

Consistent modal colour map, labelled axes with units, source attribution.
"""
from __future__ import annotations

import json
import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

MI_PER_KM = 0.621371
HOURS_PER_YEAR = 8760.0
WORLD_POP = 8.1e9

ROOT = pathlib.Path(__file__).resolve().parents[1]
ANALYSIS = ROOT / "analysis"

# Accessible, consistent categorical palette (colour-blind safe-ish)
COLORS = {
    "Road": "#4C78A8",
    "Air": "#F58518",
    "Rail": "#54A24B",
    "Active": "#B279A2",
    "Water": "#72B7B2",
}
BG = "#12141a"
FG = "#e6e8ee"


def _style(ax, title, xlabel, ylabel, source):
    ax.set_title(title, color=FG, fontsize=12, pad=12)
    ax.set_xlabel(xlabel, color=FG)
    ax.set_ylabel(ylabel, color=FG)
    ax.tick_params(colors=FG)
    for s in ax.spines.values():
        s.set_color("#39404d")
    ax.grid(True, color="#262b34", linewidth=0.6)
    ax.figure.text(0.99, 0.01, source, ha="right", va="bottom",
                   color="#8a92a3", fontsize=7)


def load():
    caps = {}
    for p in sorted(ANALYSIS.rglob("data.json")):
        d = json.loads(p.read_text())
        if "-" in d.get("category", ""):
            continue
        caps[d["mode"]] = (d, p.parent)
    return caps


def per_mode_historic(caps):
    for mode, (d, folder) in caps.items():
        hist = d.get("historic", [])
        if not hist:
            continue
        yrs = [h["year"] for h in hist]
        ahv = [h.get("ahv_person_mph", 0) / 1e6 for h in hist]
        fig, ax = plt.subplots(figsize=(7, 4), facecolor=BG)
        ax.set_facecolor(BG)
        ax.plot(yrs, ahv, marker="o", color=COLORS.get(mode, "#cccccc"), linewidth=2)
        _style(ax, f"{mode} — Historic AHV", "Year",
               "AHV (million person-mph)", "Universe of Movement · flow lens")
        out = folder / "charts" / "historic_ahv.png"
        fig.tight_layout()
        fig.savefig(out, dpi=120, facecolor=BG)
        plt.close(fig)
        print(f"  wrote {out.relative_to(ROOT)}")


def aggregate(caps):
    (ANALYSIS / "aggregate" / "charts").mkdir(parents=True, exist_ok=True)
    # Leaderboard
    items = sorted(((m, d["current"]["ahv_person_mph"]["value"] / 1e6)
                    for m, (d, _) in caps.items()), key=lambda x: x[1])
    fig, ax = plt.subplots(figsize=(7, 4), facecolor=BG)
    ax.set_facecolor(BG)
    ax.barh([m for m, _ in items], [v for _, v in items],
            color=[COLORS.get(m, "#ccc") for m, _ in items])
    _style(ax, "Aggregate Human Velocity by Mode (2024)", "AHV (million person-mph)",
           "", "Universe of Movement · flow lens")
    fig.tight_layout()
    fig.savefig(ANALYSIS / "aggregate" / "charts" / "leaderboard.png", dpi=120, facecolor=BG)
    plt.close(fig)

    # v̄ history (sum modal historic AHV by year / population)
    years = {}
    for m, (d, _) in caps.items():
        for h in d.get("historic", []):
            years.setdefault(h["year"], 0.0)
            years[h["year"]] += h.get("ahv_person_mph", 0)
    yrs = sorted(years)
    vbar = [years[y] / WORLD_POP for y in yrs]
    fig, ax = plt.subplots(figsize=(7, 4), facecolor=BG)
    ax.set_facecolor(BG)
    ax.plot(yrs, vbar, marker="o", color="#F58518", linewidth=2)
    ax.annotate("COVID", xy=(2020, vbar[yrs.index(2020)]),
                xytext=(2020, max(vbar)), color=FG, fontsize=9,
                arrowprops=dict(color=FG, arrowstyle="->"))
    _style(ax, "Per-Capita Mean Speed v̄ (all modes, time-averaged)", "Year",
           "v̄ (mph)", "Universe of Movement · flow lens")
    fig.tight_layout()
    fig.savefig(ANALYSIS / "aggregate" / "charts" / "vbar_history.png", dpi=120, facecolor=BG)
    plt.close(fig)
    print("  wrote aggregate/charts/leaderboard.png, vbar_history.png")


def main():
    caps = load()
    per_mode_historic(caps)
    aggregate(caps)


if __name__ == "__main__":
    main()
