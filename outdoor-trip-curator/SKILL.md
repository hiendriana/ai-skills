---
name: outdoor-trip-curator
description: Research and organize outdoor route and trip ideas in repositories that define their own trip policy, schema, templates, lifecycle, and indexes. Use for climbing, mountaineering, hiking, splitboarding, and related suggestions where source verification, duplicate detection, provenance, uncertainty, and current research matter.
---

# Outdoor Trip Curator

Turn links, captions, messages, rough route names, and recommendation collections into reviewable trip-idea notes while preserving provenance, uncertainty, and the difference between inspiration and current safety information.

## Establish Repository Context

1. Read applicable `AGENTS.md`, README files, and repository-defined trip templates or schemas.
2. Identify the repository-defined canonical owner, lifecycle, naming rules, structured properties, indexes, and templates.
3. Inspect existing notes for the route, destination, spelling variants, and source links before creating anything.
4. Preserve unrelated changes. Do not commit unless explicitly asked.
5. If no durable trip owner or schema is defined, research and propose a note shape but do not invent a permanent repository hierarchy or lifecycle.

If the input is an active inbox capture, use the repository's generic curation workflow when available. This skill owns trip-specific research and note content; it does not independently manage generic inbox lifecycle.

## Research and Assess

1. Identify the route or destination precisely and keep ambiguity explicit.
2. Research repository-defined structured properties when they are relevant and can be established reliably, plus location, activity, difficulty, length or elevation, approach, descent, protection or equipment, season, access restrictions, objective hazards, and useful logistics when relevant.
3. For climbing routes, search for available topos and compare useful versions.
4. Prefer official route databases, guidebook publishers, land managers, huts, rescue or avalanche services, and other first-party sources. Use trip reports for attributed experience, not universal facts.
5. Distinguish verified facts, attributed source claims, the user's personal assessment, and unresolved or time-sensitive information.
6. Treat historical posts, condition reports, grades, protection descriptions, and access details as planning context. State what requires current local verification.
7. Never infer suitability, safety, or equipment requirements from sparse social-media material.
8. For skiing or splitboarding ideas adapted from ski itineraries, label the adaptation and leave terrain suitability, transitions, exit options, and current avalanche conditions as explicit review items unless verified.

Browse whenever conditions, restrictions, route details, transport, accommodation, or recommendations could have changed. Link useful sources and include checked dates for time-sensitive information.

## Review Candidate Findings Before Writing

Before adding interpretation-sensitive external research to canonical knowledge,
prepare candidate findings and run the independent evidence review in
[the research review guide](guides/research-review.md). This is a write gate, not
part of final output validation: canonical knowledge must not receive a candidate
until the review returns `PASS`, or until a `REVISE` result has been corrected and
then passes a second review. After one failed correction, preserve the unresolved
uncertainty or use `ESCALATE` rather than retrying or inventing a resolution.

Use a fresh reviewer context when the runtime supports one. Otherwise perform the
guide's distinct adversarial verification pass and report that it was not
context-independent. Simple directly sourced metadata may use proportionate
checking; consequential interpretations, classifications, conversions, route
identity, and safety-relevant findings require the full review.

## Write or Update the Trip Note

Follow the target repository's trip policy and template rather than a skill-owned schema.

- Use repository-defined structured properties exactly as documented.
- Keep one canonical detailed owner for each trip when required; link from indexes instead of duplicating detail.
- Prefer updating an existing canonical note over creating a near-duplicate.
- Preserve `Suggested by`, inspiration/source attribution, and personal review as distinct concepts when supported by the repository model.
- Preserve original links and attribution.
- Record stable research once and distinguish information that must be re-verified before the trip.
- Keep relevant unknowns explicit, but omit clearly irrelevant sections or rows instead of filling the note with boilerplate.
- Do not add task lists unless requested or required by repository policy.

### Logistics and accommodation

Record useful start and end points, approach and descent, parking or public-transport constraints, return or shuttle needs, and time-sensitive restrictions. Include direct map links only to verified useful points.

For time-sensitive access, transport, lift, hut, road, or restriction information, preserve the last known information with the date checked and clearly flag it for re-verification before the trip.

For multiday trips, record accommodation that shapes the itinerary. For single-day trips, include accommodation only when it materially affects access, an alpine start, transport, or timing.

### Navigation and tracks

For route-based ideas, record navigation and track information when repository policy supports it. Preserve the source and intended scope of original tracks, distinguish source archives from editable navigation masters, and keep caveats visible. A track is supporting navigation data, not proof that a route is correct, safe, or currently passable.

### Topos

For climbing routes, retain multiple useful topo versions when they add information. Record the date and what it represents, a separate format and scope (for example line topo, photo topo, overview, guidebook page, or on-site reference), and meaningful differences in line, grades, protection, variants, and descent. Do not present a webpage or photo date as the topo's creation date. If no useful topo is found, state that and name the principal sources checked.

## Collections and Provenance

When recommendations share meaningful provenance, follow the repository's collection convention if one exists. Keep one canonical route note per distinct route or natural combination, merge duplicate suggestions, and retain useful source and recommender attribution.

## Transition to Completed Trips

If repository policy moves ideas into a completed-tour lifecycle, preserve useful research and planning decisions while adding what actually happened. Replace predictions with observed outcomes where possible, retain useful differences between expected and actual conditions or timing, and remove obsolete planning detail.

Do not perform the lifecycle transition unless repository policy and the user request authorize it.

## Validate

Update only repository-defined indexes or views necessary for the change. Before finishing, inspect the diff and working-tree status, verify links and paths, confirm canonical ownership, and check that externally researched facts added to the note are supported by the sources actually recorded there. A broadly related source does not count as support for a specific route fact it does not establish. Check visible uncertainty, confirm time-sensitive facts have checked dates and re-verification warnings where appropriate, and check that no private values, credentials, duplicated detail, or placeholder pages were introduced. Report what changed and what remains uncertain. Do not claim a validation passed unless it was actually performed.
