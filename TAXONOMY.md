---
title: "Movement Taxonomy"
nav_order: 3
---

# Universe of Movement — Transport Taxonomy

> A living catalogue of every way a human being moves across the surface of the
> Earth (and off it), organised into modes, categories, and subcategories.

Every category gets its own research track with independent data collection,
AHV normalisation, and projections. The metric for each is its **contribution to
Aggregate Human Velocity** = (people in mode) × (their speed), sourced via the
flow lens (annual passenger-km ÷ hours per year) and cross-checked against the
snapshot lens where data allows.

**Counting rule:** we count the speed of *humans aboard or operating* —
passengers, crew, and operators. Cargo does not count (see the "Movement of
Stuff" sidebar campaign). Ambient movement (walking around a room) is out of
scope pending a future methodology.

---

## Mode 1: Road

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Cars — sedans | Private light-duty passenger sedans | ITF, IEA, national travel surveys |
| Cars — SUVs / crossovers | Light-duty SUVs | IEA Global EV/mobility, IHS |
| Cars — pickups / light trucks | Consumer pickups | IEA, BTS/NHTS |
| Motorcycles & two/three-wheelers | Mopeds, motorbikes, auto-rickshaws (huge in Asia/Africa) | IEA, national data |
| Buses & coaches | Urban transit + intercity coach | UITP, ITF |
| Taxi / ride-hail | Metered + app-based (Uber, Didi, Grab) | Company reports, city data |
| Trucking (driver only) | Freight drivers — crew count, not cargo | IRU, national freight surveys |
| Construction / agricultural equipment | Operators of slow off-road machinery | Industry estimates |

## Mode 2: Rail

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Metro / subway / light rail | Urban heavy & light rail | UITP, city operators |
| Commuter / regional rail | Suburban rail | UIC, national operators |
| Intercity conventional rail | Long-distance conventional | UIC, World Bank |
| High-speed rail | ≥250 km/h services (China, Japan, EU) | UIC, operators |
| Rail freight (crew only) | Freight train crews | UIC (crew count, not tonne-km) |

## Mode 3: Air

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Commercial — short-haul | Narrowbody / regional passenger flights | IATA, ICAO, OAG |
| Commercial — long-haul | Widebody intercontinental | IATA, ICAO |
| General & business aviation | Private jets, GA | GAMA, FAA |
| Helicopters | Rotorcraft (offshore, EMS, transit) | HAI, operators |
| Military aviation | Crew of military aircraft | SIPRI, defence data (est.) |

## Mode 4: Water

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Ferries | Scheduled passenger + Ro-Pax ferries | Interferry, national data |
| Cruise | Ocean & river cruise passengers ("institutional consumer") | CLIA |
| Recreational boating | Self-owned consumer craft | ICOMIA, NMMA |
| Cargo shipping (crew only) | Merchant seafarers — crew, not cargo | ICS, BIMCO, UNCTAD |
| Naval / military | Crew of naval vessels — surface / submarine / carrier | SIPRI, navy fleet data (est.) |
| Fishing | Fishing vessel crews | FAO |

## Mode 5: Active (Human-Powered)

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Walking (purposeful trips) | Trip-based walking (to work, transit, errands) | WHO, national travel surveys |
| Running / jogging | Recreational + commuting running | Survey estimates |
| Cycling | Bicycle trips | ECF, national travel surveys |

## Mode 6: Micromobility

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| E-bikes | Electric-assist bicycles | LEVA, industry reports |
| E-scooters | Shared + owned standing scooters | Operator data (Lime, Bird) |

## Mode 7: Vertical & Conveyed

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Elevators | Vertical movement in buildings | KONE/Otis estimates |
| Escalators | Inclined people-movers | Industry estimates |
| Moving walkways | Horizontal airport/transit belts | Industry estimates |

> **Note:** vertical/conveyed motion contributes negligibly to AHV (low speed,
> short distance) but is included for completeness — humans *do* move vertically.

## Mode 8: Off-Earth & Novel

| Subcategory | Description | Key Sources |
|-------------|-------------|-------------|
| Human spaceflight | Astronauts in orbit (ISS crew ~17,500 mph — the fastest humans alive) | NASA, Roscosmos, CSA |
| Suborbital tourism | Blue Origin / Virgin Galactic passengers | Operator data |

---

## Appendix: Involuntary Cosmic Motion (framing only — NOT in the Big Number)

Kept out of the canonical ground-frame AHV, documented for the "wow" narrative:

| Motion | Speed | Note |
|--------|-------|------|
| Earth's rotation (equator) | ~1,040 mph | Everyone standing still is "moving" this fast |
| Earth's orbit around the Sun | ~66,600 mph | ~18.5 km/s |
| Sun's orbit around galactic centre | ~447,000 mph | ~200 km/s |

---

## Double-Counting Rules

To avoid inflating AHV:

1. **Multi-modal trips**: A person who drives to an airport then flies is in
   exactly ONE mode at any instant (snapshot), and their pkm sum correctly across
   modes (flow). No double count.
2. **Crew vs. passengers**: Count each human once. A pilot is crew (air); a
   passenger is a passenger (air). Don't count the same seat twice.
3. **Cargo excluded**: Freight tonne-km never enters AHV — only the crew's own
   movement. Cargo movement is the separate "Movement of Stuff" campaign.
4. **Access/egress walking**: The short walk to/from a vehicle is walking pkm;
   the ride is the vehicle's pkm. Both count (different modes, different distance)
   — this is additive, not double-counting.
5. **Flow vs. snapshot**: Never sum a flow figure and a snapshot figure into the
   same total. Reconcile them; report one canonical AHV (flow-based in Run 1).

## Adding New Categories

When the Scout or Architect identifies a new mode:

1. Find the appropriate mode family (or propose a new one)
2. Add the category with description and key sources
3. Update this file via PR
4. The Architect designs a `METHODOLOGY.md` for the new category
