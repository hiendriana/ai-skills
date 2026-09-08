# Route-Idea Note Schema

Use this as a flexible content model, not as mandatory boilerplate. Remove sections that add no value and add activity-specific fields when needed.

## Individual Route Idea

```markdown
# Route Name

- **Status:** Idea
- **Activity:** Multipitch climbing / mountaineering / hiking / splitboarding
- **Location:** Area, region, country
- **Suggested by:** Person who recommended it
- **Inspiration:** [Publisher or post](URL)
- **Personal review:** Not reviewed / Promising / Not suitable, with a short reason if known

## Overview

One short paragraph explaining the route's character and why it entered the collection. Attribute subjective claims.

## Route Facts

| Field | Information |
| --- | --- |
| Difficulty | Published grade and grading system, or Unknown |
| Length | Pitches, distance, elevation gain, or Unknown |
| Time | Published estimate and scope, or Unknown |
| Exposure | Value and source, or Unknown |
| Protection | Published description, or Unknown |

## Topos

For climbing routes, list every useful topo newest first. If none is found, state that outcome and name the main sources checked.

| Date | Date basis | Topo | Format and scope | Notes |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Creation / publication / edition / upload / page or photo date | [Topo](URL) | Line topo / photo topo / overview / guidebook / on-site reference | Variants and important differences |

Do not imply that a webpage or photo date is the topo's creation date. Retain older useful versions and compare discrepancies in the line, grades, protection, variants, and descent. Prefer a current guidebook or route-author source for the primary comparison without discarding evidence of disagreement. Archive a downloadable topo in the route's Google Drive source folder only when lawful and useful for personal offline reference; otherwise keep the source page link.

## Logistics

| Field | Information |
| --- | --- |
| Route start | Exact trailhead, station, lift, hut, or access point |
| Route end | Same as start or distinct endpoint |
| By public transport | Useful connection and final access, or Unknown |
| By car | Access road, parking location, and relevant restrictions |
| Return logistics | Walk-back, shuttle, public transport, or vehicle positioning |
| Map | [Precisely labelled Google Maps point](URL), when verified and useful |

Summarize the approach and descent separately where route-finding detail is useful. Mark seasonal roads, lift operations, parking limits, reservations, and other time-sensitive constraints. A map link supports orientation and access; it does not replace an offline topographic map or route navigation.

## Navigation and Track

Include this section for route-based ideas. Omit it for a destination-only idea until a route exists.

- **Track source page:** [Page providing the route or download](URL), or Unknown
- **Source archive:** [Google Drive route folder or file](URL), or None
- **Navigation master:** [Komoot or Outdooractive route](URL), or Not prepared
- **Original GPX:** [Archived original file](URL), or None
- **Track status:** Unreviewed / Reviewed against map on YYYY-MM-DD / Personally verified on YYYY-MM-DD
- **Intended use:** Approach / Complete route / Descent / Specific stages
- **Downloaded:** YYYY-MM-DD, or Not applicable
- **Caveats:** Deviations, approximate sections, missing variants, age, or Unknown

The trip note is the canonical overview, Google Drive archives source files, one selected navigation service owns the editable working route, and Suunto or the watch receives the deployed copy. Preserve the original GPX unchanged and record its source before editing or route matching. Do not maintain duplicate working routes in Komoot and Outdooractive without a specific reason. A track is supporting navigation data, not proof that the route is correct, safe, or currently passable.

## Accommodation

Include this section for every multiday trip. Include it for a single-day trip only when an overnight materially affects access, an alpine start, transport, or route timing.

| Night or stage | Relevant location | Accommodation | Role in itinerary | Reservation or access note | Source |
| --- | --- | --- | --- | --- | --- |
| Night 1 | Area or stage endpoint | Hut, bivouac, camp, or necessary lodging | Enables the next stage | Booking, opening, or access status | [Official source](URL) |

List mountain huts, bivouacs, camps, staged trailheads, and necessary pre-route or post-route stays. Do not add generic valley hotels or broad lodging suggestions that do not influence the route plan. Use `Unknown` for a necessary overnight that has not been identified, and flag opening dates, reservation requirements, winter-room access, or other facts needing current confirmation.

## Equipment and Conditions

Route-specific equipment, suitable season, and condition dependencies. Do not turn incomplete source material into a complete packing list.

## Hazards and Uncertainties

Objective hazards, discrepancies between sources, ambiguous identification, and facts requiring current local verification.

## Sources

- [Descriptive source title](URL) — what it supports; accessed YYYY-MM-DD when time-sensitive
- [Original recommendation](URL) — inspiration or attributed experience
```

Keep `Suggested by` distinct from `Inspiration`: the recommender may have forwarded a post written by someone else.

## Recommendation Collection README

```markdown
# Route Suggestions from Person

These ideas were suggested by Person on YYYY-MM-DD. They remain candidates for review; the linked notes own the route detail.

| Route idea | Activity or character | Initial assessment |
| --- | --- | --- |
| [[Route Name]] | Multipitch climbing | Not reviewed |
```

Use one row per canonical route note. If several source posts describe one route or a natural combination, mention that merge in the individual note rather than creating duplicate entries.

## Lifecycle Rule

Keep every trip that has not happened yet in `Ideas/`, including detailed plans with dates, reservations, transport, route decisions, or equipment preparation. Add that preparation to the canonical idea note. After the outing happens, move it to `Completed/` and turn it into a completed-tour record through the repository's completed-tour workflow.
