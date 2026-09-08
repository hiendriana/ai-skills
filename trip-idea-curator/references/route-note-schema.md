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

## Access and Descent

Concise approach, trailhead or transport context, descent, and access restrictions. Mark time-sensitive details.

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
